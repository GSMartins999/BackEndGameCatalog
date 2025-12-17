import re


class Email:
    def __init__(self, value: str):
        if not self._validate(value):
            raise ValueError("E-mail inválido")

        self.value = value

    @staticmethod
    def _validate(email: str) -> bool:
        email_regex = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"
        return re.match(email_regex, email) is not None
