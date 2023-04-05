class ConnectionDB:
    """
    class for make connection with database
    """
    __instance = None

    def __init__(self, __private: bool = False) -> None:
        self.DB_host = '0.0.0.0:9200'
        self.__instance = self

        if not __private:
            raise ("Can't be instantiated through the constructor,"
                   " Use .instance() instead")

    @classmethod
    def instance(cls) -> 'ConnectionDB':
        if cls.__instance is None:
            cls.__instance = cls(True)
        return cls.__instance


if __name__ == '__main__':
    # incorrect called
    incorrect_called = ConnectionDB()
    # correct called
    correct_call = ConnectionDB.instance()
