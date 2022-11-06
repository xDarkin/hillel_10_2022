data = [1, 2, 3, 4, 5, 1, 43, 5, 6, 2, 4, 1, 34, 45, 12, 4, 2]


class User:
    def __init__(self, username: str, age: int) -> None:
        self.username: str = username
        self.age: int = age

    def __repr__(self) -> str:
        return f"{self.username=}, {self.age}"


john = User(username="John", age=22)
marry = User(username="Marry", age=8)
max_ = User(username="Max", age=23)

users = [john, marry, max_]

only_adults = (user for user in users if user.age > 18)


print(list(only_adults))
