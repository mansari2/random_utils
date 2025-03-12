import logging
import os

# Create a logs directory if it doesn't exist
LOG_DIR = "logs"
os.makedirs(LOG_DIR, exist_ok=True)
LOG_FILE = os.path.join(LOG_DIR, "app.log")

# Configure logging settings
logging.basicConfig(
    level=logging.DEBUG,  # Set logging level
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler(LOG_FILE),  # Save logs to a file
        logging.StreamHandler()  # Print logs to console
    ]
)

# Create a logger instance
logger = logging.getLogger("MyApp")

# Logging at different levels
def log_messages():
    logger.debug("This is a debug message")
    logger.info("This is an info message")
    logger.warning("This is a warning message")
    logger.error("This is an error message")
    logger.critical("This is a critical message")

# Example usage
if __name__ == "__main__":
    log_messages()
    print(f"Logs have been saved to {LOG_FILE}")
