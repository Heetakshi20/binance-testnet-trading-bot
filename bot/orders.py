from bot.client import BinanceTestnetClient
from bot.validators import validate_order_params
from bot.exceptions import TradingBotException
from bot.logger import setup_logger

logger = setup_logger()

def execute_order(api_key: str, api_secret: str, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
    logger.info("--- New Order Request ---")
    logger.info(f"Summary: {side} {quantity} {symbol} | Type: {order_type} | Price: {price}")
    
    try:
        # 1. Validate basic input
        validate_order_params(symbol, side, order_type, quantity, price)
        
        # 2. Initialize client
        bot_client = BinanceTestnetClient(api_key, api_secret)
        
        # 3. Get current price
        current_price = bot_client.get_current_price(symbol)
        logger.info(f"Current Market Price: {current_price}")
        
        # 4. Validate LIMIT price range
        if order_type.upper() == "LIMIT":
            if side.upper() == "SELL" and price < current_price * 0.9:
                raise TradingBotException(
                    f"Price too low. Market price is ~{current_price}"
                )

            if side.upper() == "BUY" and price > current_price * 1.1:
                raise TradingBotException(
                    f"Price too high. Market price is ~{current_price}"
                )
        
        # 5. Execute order
        response = bot_client.place_futures_order(symbol, side, order_type, quantity, price)
        
        # 6. Display result
        print("\n✅ ORDER SUCCESSFUL ✅")
        print("-" * 25)
        print(f"Order ID   : {response.get('orderId')}")
        print(f"Status     : {response.get('status')}")
        print(f"Symbol     : {response.get('symbol')}")
        print(f"Exec Qty   : {response.get('executedQty')}")
        print(f"Avg Price  : {response.get('avgPrice')}")
        print("-" * 25)
        
        logger.info(f"Order Success Response: {response}")
        
    except TradingBotException as e:
        print(f"\n❌ VALIDATION ERROR: {e}")
        logger.error(f"Validation Failed: {e}")

    except Exception as e:
        print(f"\n❌ ORDER FAILED: Please check logs for details.")