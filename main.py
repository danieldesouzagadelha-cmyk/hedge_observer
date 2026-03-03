from model_engine import calculate_probability
from regime_filter import valid_regime

def evaluate(momentum_3m,
             momentum_5m,
             momentum_15m,
             order_imbalance,
             volatility,
             market_prob_5m,
             market_prob_15m):

    prob_5m, prob_15m = calculate_probability(
        momentum_3m,
        momentum_5m,
        momentum_15m,
        order_imbalance,
        volatility
    )

    edge_5m = prob_5m - market_prob_5m
    edge_15m = prob_15m - market_prob_15m

    if edge_5m > 0.06 and edge_15m > 0.04:
        return "SIGNAL"

    return "NO TRADE"
