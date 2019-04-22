class SingleTon():
    __instancde = None

    @classmethod
    def get(cls):
        if cls.__instancde is None:
            cls.__instancde = cls()

        return cls.__instancde