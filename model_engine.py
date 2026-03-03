import math

def logistic(x):
    return 1 / (1 + math.exp(-x))

def calculate_probability(momentum_3m,
                          momentum_5m,
                          momentum_15m,
                          order_imbalance,
                          volatility):

    score_5m = (
        0.35 * momentum_3m +
        0.30 * momentum_5m +
        0.20 * order_imbalance +
        0.15 * volatility
    )

    score_15m = (
        0.40 * momentum_5m +
        0.30 * momentum_15m +
        0.20 * order_imbalance +
        0.10 * volatility
    )

    prob_5m = logistic(score_5m)
    prob_15m = logistic(score_15m)

    return prob_5m, prob_15m
