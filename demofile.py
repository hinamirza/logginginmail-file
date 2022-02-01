import logging
import logging.handlers

# Create or get the logger
logger = logging.getLogger(__name__)  
logger.setLevel(logging.INFO)
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(lineno)d : %(filename)s : %(funcName)s : %(message)s')

# Setup File Handeler (for file i.e. log.txt)
fh = logging.FileHandler('log.txt','w')
fh.setFormatter(formatter)
logger.addHandler(fh)

#Setup Stream Handler (i.e. console)
sh = logging.StreamHandler()
sh.setFormatter(formatter)
sh.setLevel(logging.INFO)
logger.addHandler(sh)

# Adding SMTP Handeler (for mail)
smtp_handler = logging.handlers.SMTPHandler(mailhost=('smtp.gmail.com', 587),
                                            fromaddr='hinamirza886@gmail.com',
                                            toaddrs=['hinamirza886@gmail.com'],
                                            subject='Error',
                                            credentials= ('hinamirza886@gmail.com','gumhsgqzbsbmmlvj'),
                                            secure=())
logger.addHandler(smtp_handler)


def divide(x, y):
    try:
        out = x / y
    except ZeroDivisionError:
        logger.exception("Division by zero problem")
    else:
        return out

# Logs
logger.error("Divide {x} / {y} = {c}".format(x=10, y=0, c=divide(10,0)))