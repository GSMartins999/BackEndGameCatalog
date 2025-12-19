class Descricao:
    def __init__(self, value: str):
        if not value or not value.strip():
            raise ValueError("Descrição não pode ser vazia")

        value = value.strip()

        if len(value) < 10:
            raise ValueError("Descrição invalida")

        if len(value) > 500:
            raise ValueError("Descrição invalida")

        self.value = value
