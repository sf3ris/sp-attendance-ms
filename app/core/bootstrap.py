from .database import Database

class Bootstrap():

    __database : Database = None

    def __init__(self) -> None:

        self.__database = Database().connect()