# Custom Exception Example
class ValueTooHighError(Exception):
    def __init__(self, value, message="Value is too high"):
        self.value = value
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f'{self.value} -> {self.message}'

def check_value(x):
    if x > 100:
        raise ValueTooHighError(x)
    return True

if __name__ == "__main__":
    try:
        check_value(150)
    except ValueTooHighError as e:
        print(f"Caught custom exception: {e}")
