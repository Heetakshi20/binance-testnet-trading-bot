# 🤖 Binance Trading Bot - Futures Testnet

A modular Python command-line application built to execute **MARKET** and **LIMIT** orders on the **Binance Futures Testnet (USDT-M)**. This project demonstrates clean architecture, robust error handling, and secure API integration for automated trading simulations.

## 🚀 Key Features

* **⚡ Automated Order Execution:** Place real-time Market and Limit orders directly from your terminal with high precision.
* **🛡️ Parameter Validation:** Pre-execution checks ensure all required fields (like price for Limit orders) are present and valid before hitting the API.
* **📝 Comprehensive Logging:** Dual-stream logging that records every API request, response, and error to both the console and a persistent `logs/bot.log` file.
* **🔒 Secure Credential Management:** Fully integrated with `python-dotenv` to keep sensitive API keys protected via environment variables.
* **🛠️ Clean Architecture:** Decoupled structure separating the CLI, business logic, and API layers for maximum maintainability and reusability.

## 🛠️ Tech Stack

* **Language:** Python 3.12+
* **API Wrapper:** `python-binance` (Official-compliant SDK)
* **Environment:** `python-dotenv` (Security)
* **CLI Engine:** `argparse` (Native Python)
* **Logging:** `logging` (Structured execution tracking)

## 📂 Project Structure

```text
binance_trading_bot/
├── bot/                    # Core Logic Package
│   ├── client.py           # Binance API wrapper & authentication
│   ├── orders.py           # Order orchestration & flow logic
│   ├── validators.py       # Input & parameter validation
│   ├── logger.py           # Centralized logging configuration
│   └── exceptions.py       # Custom error classes for handling
├── logs/                   # Execution history folder
│   └── bot.log             # Generated log file (git-ignored)
├── cli.py                  # CLI Entry Point
├── .env                    # Secret API Keys (git-ignored)
├── .env.example            # Template for local environment setup
├── README.md               # Project documentation
└── requirements.txt        # Project dependencies
