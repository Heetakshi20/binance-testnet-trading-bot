class TradingBotException(Exception):
    """Base exception for the trading bot."""
    pass

class ValidationError(TradingBotException):
    """Raised when user input fails validation."""
    pass