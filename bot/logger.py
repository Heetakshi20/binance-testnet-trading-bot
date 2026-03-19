import logging
import os

def setup_logger():
    # Ensure logs directory exists
    os.makedirs('logs', exist_ok=True)
    
    logger = logging.getLogger('TradingBot')
    logger.setLevel(logging.INFO)
    
    # Avoid adding multiple handlers if logger is imported multiple times
    if not logger.handlers:
        # File Handler
        file_handler = logging.FileHandler('logs/bot.log')
        file_handler.setLevel(logging.INFO)
        
        # Console Handler
        console_handler = logging.StreamHandler()
        console_handler.setLevel(logging.INFO)
        
        # Format
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        file_handler.setFormatter(formatter)
        console_handler.setFormatter(formatter)
        
        logger.addHandler(file_handler)
        logger.addHandler(console_handler)
        
    return logger