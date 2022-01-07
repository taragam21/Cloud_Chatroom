from Client import Client
from datetime import datetime

class Message:

    # Constructeur
    def __init__(self, client, message):  # heure, client de type Client
        self.__client = client
        self.__date = datetime.now().strftime("%H:%M:%S ")
        self.__message = message

	#getter
    def getClient(self):
        return self.__client

    def getDate(self):
        return self.__date

    def getMessage(self):
        return self.__message

    def getHeader(self):
       return self.__client.getName() + "" " ( " + self.__date + " ) " + ":" + "  " + self.__message   
    
