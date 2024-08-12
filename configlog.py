import logging

def setup_logging(log_file='app.log'):
    logging.basicConfig(
        filename=log_file,                  
        level=logging.DEBUG,                
        format='%(asctime)s - %(levelname)s - %(message)s',
        filemode='w'                        
    )

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console.setFormatter(formatter)
    logging.getLogger().addHandler(console)
