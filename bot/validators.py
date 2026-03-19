from bot.exceptions import ValidationError

def validate_order_params(symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    """Validates input before sending to the API."""
    if quantity <= 0:
        raise ValidationError("Quantity must be greater than zero.")
        
    if order_type.upper() == "LIMIT":
        if price is None or price <= 0:
            raise ValidationError("A valid price (>0) is required for LIMIT orders.")
            
    if order_type.upper() == "MARKET" and price is not None:
        # Just a warning, we can ignore the price for market orders
        pass

    return True