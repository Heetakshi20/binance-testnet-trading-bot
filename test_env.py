import os
from dotenv import load_dotenv

load_dotenv()
key = os.getenv('BINANCE_TESTNET_API_KEY')

print("\n--- FORENSIC CHECK ---")
print(f"EXACTLY what Python sees: >{key}<")
print(f"Length: {len(str(key))} characters")
print("----------------------\n")