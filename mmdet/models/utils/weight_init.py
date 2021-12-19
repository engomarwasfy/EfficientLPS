import numpy as np


def bias_init_with_prob(prior_prob):
    """ initialize conv/fc bias value according to giving probablity"""
    return float(-np.log((1 - prior_prob) / prior_prob))
