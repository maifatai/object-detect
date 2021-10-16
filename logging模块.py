import logging
def test():
    logging.warning('warning')# 信息会被输出到控制台
    logging.info('running')#不会打印任何信息，因为warning的优先级比info高
def test1():
    logging.basicConfig(level=logging.INFO, format=
    '%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    '''
    logging.basicConfig函数各参数：
    filename：指定日志文件名；
    filemode：和file函数意义相同，指定日志文件的打开模式，'w'或者'a'；
    format：指定输出的格式和内容，format可以输出很多有用的信息，
            %(levelno)s：打印日志级别的数值
            %(levelname)s：打印日志级别的名称
            %(pathname)s：打印当前执行程序的路径，其实就是sys.argv[0]
            %(filename)s：打印当前执行程序名
            %(funcName)s：打印日志的当前函数
            %(lineno)d：打印日志的当前行号
            %(asctime)s：打印日志的时间
            %(thread)d：打印线程ID
            %(threadName)s：打印线程名称
            %(process)d：打印进程ID
            %(message)s：打印日志信息
    datefmt：指定时间格式，同time.strftime()；
    level：设置日志级别，默认为logging.WARNNING；
    stream：指定将日志的输出流，可以指定输出到sys.stderr，sys.stdout或者文件，
            默认输出到sys.stderr，当stream和filename同时指定时，stream被忽略；
    '''

    logger = logging.getLogger(__name__)
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")
def test2():
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logger = logging.getLogger(__name__)
    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")
def test3():
    #将日志写入文件中
    #设置logging，创建一个FileHandler，并对输出消息的格式进行设置，
    #将其添加到logger，然后将日志写入到指定的文件中，
    logging.basicConfig(filename='log.txt',level=logging.INFO,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    #可以替代下面的
    logger = logging.getLogger(__name__)
    # logger.setLevel(level=logging.INFO)
    # handler = logging.FileHandler("log.txt")
    # handler.setLevel(logging.INFO)
    # formatter = logging.Formatter('%(asctime)s -
    # %(name)s - %(levelname)s - %(message)s')
    # handler.setFormatter(formatter)
    # logger.addHandler(handler)

    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")
def test4():
    #将日志同时输出到屏幕和日志文件
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler("log.txt")#流向的最终日志文件
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    #Logger对象默认不包含handler对象，但是可用通过addHandler()方法添加
    logger.addHandler(handler)
    logger.addHandler(console)

    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")
def test5():
    #记录变量信息
    #通过格式化字符串的方式可以将想要保存的描述信息以及变量方便的保存下来
    logging.warning('%s before you %s', 'Look', 'leap!')
def test6():
    #日志回滚
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    # 定义一个RotatingFileHandler，最多备份3个日志文件，每个日志文件最大1K
    rHandler = logging.handlers.RotatingFileHandler("log.txt", maxBytes=1 * 1024, backupCount=3)
    rHandler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    rHandler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)
    console.setFormatter(formatter)

    logger.addHandler(rHandler)
    logger.addHandler(console)

    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    logger.info("Finish")
def test7():
    #跟踪异常
    logger = logging.getLogger(__name__)
    logger.setLevel(level=logging.INFO)
    handler = logging.FileHandler("log.txt")
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    console = logging.StreamHandler()
    console.setLevel(logging.INFO)

    logger.addHandler(handler)
    logger.addHandler(console)

    logger.info("Start print log")
    logger.debug("Do something")
    logger.warning("Something maybe fail.")
    try:
        open("sklearn.txt", "rb")
    except (SystemExit, KeyboardInterrupt):
        raise
    except Exception:
        logger.error("Faild to open sklearn.txt from logger.error", exc_info=True)
    logger.info("Finish")
if __name__=='__main__':
    test7()