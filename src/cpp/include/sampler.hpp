#ifndef SAMPLER_H
#define SAMPLER_H

#include <cstdint>
#include <limits>
#include <memory>

#include "core.hpp"
#include <boost/algorithm/clamp.hpp>
#include <boost/make_unique.hpp>

// *Really* minimal PCG32 code / (c) 2014 M.E. O'Neill / pcg-random.org
// Licensed under Apache License 2.0 (NO WARRANTY, etc. see website)
typedef struct {
    uint64_t state;
    uint64_t inc;
} pcg32_random_t;

inline uint32_t pcg32_random_r(pcg32_random_t *rng) {
    uint64_t oldstate = rng->state;
    // Advance internal state
    rng->state = oldstate * 6364136223846793005ULL + (rng->inc | 1);
    // Calculate output function (XSH RR), uses old state for max ILP
    uint32_t xorshifted = ((oldstate >> 18u) ^ oldstate) >> 27u;
    uint32_t rot = oldstate >> 59u;
    return (xorshifted >> rot) | (xorshifted << ((-rot) & 31));
}

constexpr static float divider =
        1.0f / (float) std::numeric_limits<uint32_t>::max();

// random number generator
class RNG {
private:
    pcg32_random_t state;

public:
    RNG() {
        state.state = 1;
        state.inc = 1;
    }

    explicit RNG(uint64_t seed) {
        state.state = seed;
        state.inc = 1;
    }

    uint64_t getSeed() const { return state.state; }

    void setSeed(uint64_t seed) { state.state = seed; }

    float getNext() { return pcg32_random_r(&state) * divider; }
};


/**
 * @brief Abstract class of a sampler interface.
 * @class Sampler.
 */
class Sampler {
protected:
    RNG rng;

public:
    Sampler() = default;

    virtual ~Sampler() = default;

    explicit Sampler(uint64_t seed) : rng(seed) {}

    uint64_t getSeed() { return rng.getSeed(); }

    void setSeed(uint64_t seed) { rng.setSeed(seed); }

    virtual std::unique_ptr<Sampler> clone() = 0;

    virtual float getNext1D() = 0;

    virtual Vec2f getNext2D() = 0;
};

/**
 * @brief Uniform distribution sampler
 * @class UniformSampler.
 */
class UniformSampler : public Sampler {
public:
    UniformSampler() : Sampler() {}

    explicit UniformSampler(uint64_t seed) : Sampler(seed) {}

    std::unique_ptr<Sampler> clone() override {
        return boost::make_unique<UniformSampler>();
    }

    float getNext1D() override { return rng.getNext(); }

    Vec2f getNext2D() override { return {rng.getNext(), rng.getNext()}; }
};

// sample direction in the hemisphere
// its pdf is proportional to cosine
inline Vec3f sampleCosineHemisphere(Vec2f uv, float &pdf) {
    float theta = 0.5f * std::acos(boost::algorithm::clamp(1.0f - 2.0f * uv[0],
                                                           -1.0f, 1.0f));
    float phi = PI_MUL_2 * uv[1];
    float cosTheta = std::cos(theta);
    pdf = PI_INV * cosTheta;
    Vec3f cart = sphericalToCartesian(theta, phi);
    return cart;
}

#endif
