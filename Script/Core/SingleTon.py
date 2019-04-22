class SingleTon():
    __instance = None

    @classmethod
    def get(cls, *args):
        if cls.__instance is None:
            if args:
                cls.__instance = cls(*args)
            else:
                cls.__instance = cls()

        return cls.__instance