from photonmap import UniformSampler
import random

def test_random_sampler():
    sampler = UniformSampler()
    rng1 = sampler.getNext1D()
    rng2 = sampler.getNext1D()
    try:
        assert (rng1 != rng2)
    except AssertionError:
        print("[Assertion ERROR] UniformSampler with default seed: "
              + str(rng1) + " is " + str(rng2))

    print("UniformSampler with default seed: "
          + str(rng1) + " is not " + str(rng2))
    sampler = UniformSampler(random.randint(1, 10000000))

    rng1 = sampler.getNext1D()
    rng2 = sampler.getNext1D()
    try:
        assert (rng1 != rng2)
    except AssertionError:
        print("[Assertion ERROR] UniformSampler with default seed: "
              + str(rng1) + " is " + str(rng2))
    print("UniformSampler with random seed (randint python function): "
          + str(rng1) + " is not " + str(rng2))
