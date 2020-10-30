class CustomerInformation:
    def __init__(self):
        self.__customerId = None # int value
        self.__name = None # string value
        self.__amountPayable = None # float value
        self.__creditLimit = None # float value

    # getters settesr
    def setCustomerId(self, id):
        self.__customerId = id
    def getCustomerId(self):
        return self.__customerId

    def setName(self, name):
        self.__name = name
    def getName(self):
        return self.__name

    def setAmountPayable(self, amount):
        self.__amountPayable = amount
    def getAmountPayable(self):
        return self.__amountPayable

    def setCreditLimit(self, limit):
        self.__creditLimit = limit
    def getCreditLimit(self):
        return self.__creditLimit