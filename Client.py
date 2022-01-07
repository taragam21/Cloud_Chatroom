class Client:

    # Constructeur
    def __init__(self, nom, password):
        self.__name = nom
        self.__password = password

    # getter
    def getName(self):
        return self.__name

    def getPassword(self):
        return self.__password

    # setter
    def setName(self, nom):
        self.__name = nom

    def setPassword(self, password):
        self.__password = password

    def equal(self, client):
        return  self.__name == client.__name and self.__password == client.__password        
