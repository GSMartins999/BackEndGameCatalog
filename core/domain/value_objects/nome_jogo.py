class NomeDoJogo:
    def __init__(self, value: str):
        if not value or not value.strip():
            raise ValueError("Nome Inválido")

        value = value.strip()

        if len(value) < 3:
            raise ValueError("Nome Inválido")

        if len(value) > 150:
            raise ValueError("Nome Inválido")

        self.value = value
