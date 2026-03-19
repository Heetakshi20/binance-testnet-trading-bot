import argparse
import os
import sys
from dotenv import load_dotenv
from bot.orders import execute_order

def main():
    load_dotenv()
    
    api_key = os.getenv('BINANCE_TESTNET_API_KEY')
    api_secret = os.getenv('BINANCE_TESTNET_API_SECRET')
    
    if not api_key or not api_secret:
        print("Error: API Keys not found. Check your .env file.")
        sys.exit(1)

    parser = argparse.ArgumentParser(description="Binance Futures Testnet Trading Bot")
    
    parser.add_argument("--symbol", type=str, required=True)
    parser.add_argument("--side", type=str, choices=['BUY', 'SELL'], required=True)
    parser.add_argument("--type", type=str, choices=['MARKET', 'LIMIT'], required=True)
    parser.add_argument("--qty", type=float, required=True)
    parser.add_argument("--price", type=float, default=None)
    
    args = parser.parse_args()
    
    execute_order(
        api_key,
        api_secret,
        args.symbol,
        args.side,
        args.type,
        args.qty,
        args.price
    )

if __name__ == "__main__":
    main()