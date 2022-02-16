import logging
import time

from interface.rootview import RootViewController as Root


logger = logging.getLogger()
logger.setLevel(logging.DEBUG) #NOTE: minimum logging level - set this to whatever suits your needs

#config logging
stream_handler = logging.StreamHandler() 
formatter = logging.Formatter('%(asctime)s %(levelname)s :: %(message)s')
stream_handler.setFormatter(formatter)
stream_handler.setLevel(logging.INFO) 
file_handler = logging.FileHandler('info.log')
file_handler.setFormatter(formatter)
file_handler.setLevel(logging.DEBUG) 
logger.addHandler(stream_handler)
logger.addHandler(file_handler)


if __name__ == '__main__':
    root = Root()
    root.mainloop()