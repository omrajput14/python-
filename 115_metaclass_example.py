# Metaclass Example
class SingletonMeta(type):
    _instances = {}
    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super().__call__(*args, **kwargs)
        return cls._instances[cls]

class DatabaseConnection(metaclass=SingletonMeta):
    def __init__(self):
        print("Initializing database connection...")
        self.connected = True

if __name__ == "__main__":
    db1 = DatabaseConnection()
    db2 = DatabaseConnection()
    print("Same instance?", db1 is db2)
