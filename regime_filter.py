def valid_regime(volatility, atr):

    if volatility < 0.002:
        return False  # mercado morto

    if volatility > 0.02:
        return False  # mercado caótico

    return True
