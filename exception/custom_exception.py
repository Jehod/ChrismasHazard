class CustomException(BaseException):

    def __init__(self, str) -> None:
        super().__init__()
        self.str = str

    def __str__(self) -> str:
        return f"!!! {self.str} {super().__str__()}"
