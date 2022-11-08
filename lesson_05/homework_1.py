class Colorized:
    """A context manager that colorizes your text.
    Available colors are pink, blue, grey, yellow, green,
    red and bright_blue."""

    color: dict = {
        "pink": "\033[95m",
        "blue": "\033[94m",
        "grey": "\033[90m",
        "yellow": "\033[93m",
        "green": "\033[92m",
        "red": "\033[91m",
        "bright_blue": "\033[96m",
        "end": "\033[0m",
    }

    def __init__(self, color: str):
        print(Colorized.color[color])

    def __enter__(self):
        print("Now your text is colored\n")

    def __exit__(self, type_, value, traceback):
        print(self.color["end"])
        print("Now your text color will be default")


if __name__ == "__main__":
    with Colorized("yellow"):
        print("test text")
