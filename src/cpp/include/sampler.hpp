#ifndef SAMPLER_H
#define SAMPLER_H

#include <stdlib.h>
#include <cstdint>
#include <limits>
#include <memory>
#include <cmath>

#include "core.hpp"
#include <boost/algorithm/clamp.hpp>
#include <boost/make_unique.hpp>




// *Really* minimal PCG32 code / (c) 2014 M.E. O'Neill / pcg-random.org
// Licensed under Apache License 2.0 (NO WARRANTY, etc. see website)
typedef struct {
    uint64_t state;
    uint64_t inc;
} pcg32_random_t;

//SplitMix
inline uint64_t nextSplitMix(pcg32_random_t *rng)
{
    uint64_t oldstate = rng->state;
    rng->state = oldstate + UINT64_C(0x9E3779B97F4A7C15);
    uint64_t z = rng->state;
    z = (z ^ (z >> 30)) * UINT64_C(0xBF58476D1CE4E5B9);
    z = (z ^ (z >> 27)) * UINT64_C(0x94D049BB133111EB);
    return z ^ (z >> 31);
}

inline uint64_t nextXoroshiro(uint64_t* seed1, uint64_t* seed2)
{
    uint64_t s1 = seed1[0];
    uint64_t s0 = seed2[0];
    uint64_t result = s0 + s1;
    seed1[0] = s0;
    s1 ^= s1 << 23;
    seed2[0] = s1 ^ s0 ^ (s1 >> 18) ^ (s0 >> 5);
    return result;
}

//PCG
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
constexpr static double divider64 =
        1.0f / (double) std::numeric_limits<uint64_t>::max();

// random number generator
class RNG {
private:
    pcg32_random_t state;
    unsigned int seedRand;
    uint64_t seed1;
    uint64_t seed2;
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

    void setSeed(uint64_t seed) { state.state = seed; seedRand = seed; seed1 = rand_r(&seedRand); seed2 = rand_r(&seedRand); }

    float getNext() { 
        return pcg32_random_r(&state) * divider; 
        //return nextSplitMix(&state) * divider64; 
        //return rand_r(&seedRand) / static_cast<float>(RAND_MAX);
        //return nextXoroshiro(&seed1, &seed2) * divider64; 
    }
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
    
    // float e = std::sqrt(uv[0]);
    // cart = Vec3f(e * std::cos(phi), std::sqrt(1 - uv[0]), e * std::sin(phi));

    return normalize(cart);
}

inline Vec3f sampleSphere(Vec2f uv, float &pdf) {

    float angle = PI_MUL_2 * uv[1];
    pdf = PI_INV / 4;

    float y = -1 + 2 * uv[0];
    float r = std::sqrt(1.0 - y*y);
    float x = r * std::sin(angle);
    float z = r * std::cos(angle);
    Vec3f cart = Vec3f(x, y, z);

    return normalize(cart);
}

#endif
