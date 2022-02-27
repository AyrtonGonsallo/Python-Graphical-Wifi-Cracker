class Singleton(object):
    _instances = {}

    def __new__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(Singleton, cls).__new__(cls, *args, **kwargs)
        return cls._instances[cls]


class MyClass(Singleton):
    results = ""
    isOver = False

    def __init__(self):
        self.results = ""

    def getResults(self):
        return self.results

    def setResults(self,res):
        self.results = res

    def addResults(self,res):
        self.results += res

    def setIsOver(self,io):
        self.isOver = io

    def getIsOver(self):
        return self.isOver

    pass



