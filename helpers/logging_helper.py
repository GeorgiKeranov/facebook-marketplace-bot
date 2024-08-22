import logging

def log(exception):
    # Configure logging to write to a file
    logging.basicConfig(filename='log.txt', level=logging.DEBUG,
                        format='%(asctime)s - %(levelname)s - %(message)s')
    
    logging.exception(exception)
