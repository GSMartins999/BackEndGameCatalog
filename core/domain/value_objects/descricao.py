class Descricao:
    def __init__(self, value: str):
        if not value or not value.strip():
            raise ValueError("A descrição é obrigatória.")

        value = value.strip()

        if len(value) < 10:
            raise ValueError("A descrição deve ter no mínimo 10 caracteres.")

        if len(value) > 500:
            raise ValueError("A descrição deve ter no máximo 500 caracteres.")

        self.value = value
