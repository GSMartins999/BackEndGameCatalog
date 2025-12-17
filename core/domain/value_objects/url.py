from urllib.parse import urlparse


class URL:
    def __init__(self, value: str):
        if not value or not value.strip():
            raise ValueError("A URL é obrigatória.")

        if not value.startswith(("http://", "https://")):
            raise ValueError(
                "O formato da URL é inválido. Deve começar com http:// ou https://"
            )

        parsed = urlparse(value)
        if not parsed.scheme or not parsed.netloc:
            raise ValueError(
                "O formato da URL é inválido. Deve começar com http:// ou https://"
            )

        self.value = value
