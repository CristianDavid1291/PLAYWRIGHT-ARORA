import logging
import os

class Logger:

    @staticmethod
    def log():
        """
        This method sets up the logging configuration for the application.
        It logs messages to a file named 'automation.log' in the 'logs' directory.
        """
        # Create logs directory if it doesn't exist
        if not os.path.exists("logs"):
            os.makedirs("logs")
        
        # Get or create logger
        logger = logging.getLogger("automation")
        
        # Only configure if not already configured
        if not logger.handlers:
            logger.setLevel(logging.INFO)
            
            # File handler
            file_handler = logging.FileHandler("logs/automation.log")
            file_handler.setLevel(logging.INFO)
            
            # Formatter
            formatter = logging.Formatter(
                '%(asctime)s: %(levelname)s: %(message)s',
                datefmt='%m/%d/%Y %I:%M:%S %p'
            )
            
            file_handler.setFormatter(formatter)
            logger.addHandler(file_handler)
        
        return logger

