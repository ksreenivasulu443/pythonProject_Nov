import logging

import pandas as pd
logging.basicConfig(level='INFO',filename='automation.log',filemode='a',
                    format='%(asctime)s:%(levelname)s:%(message)s:%(lineno)d-%(filename)s-%(funcName)s')

#Default level set is Warning( 30 )

# 1. CRITICAL==>50==>Represents a very serious problem that needs high attention
# 2. ERROR===>40===>Represents a serious error
# 3. WARNING==>30==>Represents a warning message, some caution needed. It is alert to
# the programmer
# 4. INFO===>20===>Represents a message with some important information
# 5. DEBUG===>10==>Represents a message with debugging information
# 6. NOTSET==>0==>Rrepresents that the level is not set.


# %(asctime)s: The timestamp of the log message in the format specified by the datefmt parameter (if provided).
# %(levelname)s: The log level (e.g., DEBUG, INFO, WARNING, ERROR, CRITICAL).
# %(message)s: The log message itself.
# %(name)s: The name of the logger.
# %(filename)s: The name of the file containing the logging call.
# %(lineno)d: The line number where the logging call occurred.
# %(funcName)s: The name of the function/method where the logging call occurred.



def read(file_type, path):
    if file_type =='csv':
        #print("file has been read successfully " +path)
        logging.info("file has been read successfully "+path)
        count=0
        if count == 0:
            logging.warning("file has been read successfully but count 0 " + path)
    else:
        #print("pls provide correct file type to process" + path )
        logging.critical("file type was received incorrect so no further executions will be performed")


read("csv", 'path')



print("This is logging class")
logging.debug("This is debug logger")
logging.info("This is info logger")
logging.warning("This is warning logger")
logging.error("This is error logger")
logging.critical("This is critical logger")
logging.info("This is info2 logger")
logging.error("This is error2 logger")