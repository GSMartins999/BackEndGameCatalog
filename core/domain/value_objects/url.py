from urllib.parse import urlparse


class URL:
    def __init__(self, value: str):
        if not value or not value.strip():
            raise ValueError("Invalid photo URL")

        if not value.startswith(("http://", "https://")):
            raise ValueError("Invalid photo URL")

        parsed = urlparse(value)
        if not parsed.scheme or not parsed.netloc:
            raise ValueError("Invalid photo URL")

        self.value = value
        self.url = value
