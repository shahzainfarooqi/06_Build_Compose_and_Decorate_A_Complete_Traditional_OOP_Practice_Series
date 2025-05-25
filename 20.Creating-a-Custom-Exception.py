class InvalidAgeError(Exception):
    def __init__(self, message="Age must be at least 18."):
        super().__init__(message)


def check_age(age):
    if age < 18:
        raise InvalidAgeError(f"Invalid age: {age}. Must be at least 18.")
    else:
        print("Age is valid.")


try:
    check_age(16)
except InvalidAgeError as e:
    print("Caught an exception:", e)
