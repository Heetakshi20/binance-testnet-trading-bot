from binance.client import Client
from binance.exceptions import BinanceAPIException, BinanceRequestException
from bot.logger import setup_logger
import time

logger = setup_logger()

class BinanceTestnetClient:
    def __init__(self, api_key: str, api_secret: str):
        self.client = Client(api_key, api_secret, testnet=True)

        # Sync time
        self._sync_time()

        logger.info("Initialized Binance Futures Testnet Client")

    def _sync_time(self):
        """Synchronize local time with Binance server."""
        try:
            server_time = self.client.futures_time()['serverTime']
            local_time = int(time.time() * 1000)
            self.client.TIME_OFFSET = server_time - local_time

            logger.info(f"Time synced with Binance. Offset: {self.client.TIME_OFFSET} ms")

        except Exception as e:
            logger.error(f"Time sync failed: {e}")

    def get_current_price(self, symbol: str):
        """Fetch current market price"""
        ticker = self.client.futures_symbol_ticker(symbol=symbol.upper())
        return float(ticker['price'])

    def place_futures_order(self, symbol: str, side: str, order_type: str, quantity: float, price: float = None):
        """Send futures order"""
        params = {
            "symbol": symbol.upper(),
            "side": side.upper(),
            "type": order_type.upper(),
            "quantity": quantity
        }

        if order_type.upper() == 'LIMIT':
            params['price'] = price
            params['timeInForce'] = 'GTC'

        logger.info(f"Sending API Request: {params}")

        # Retry logic
        for attempt in range(2):
            try:
                response = self.client.futures_create_order(**params)
                logger.info("Order executed successfully")
                return response

            except BinanceAPIException as e:
                if "Timestamp" in str(e) and attempt == 0:
                    logger.warning("Timestamp issue detected. Resyncing time...")
                    self._sync_time()
                    continue

                logger.error(f"Binance API Error: {e.status_code} - {e.message}")
                raise

            except BinanceRequestException as e:
                logger.error(f"Network Error: {e}")
                raise

            except Exception as e:
                logger.error(f"Unexpected Error: {e}")
                raise