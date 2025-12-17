class NomeDoJogo:
    def __init__(self, value: str):
        if not value or not value.strip():
            raise ValueError("O nome do jogo é obrigatório.")

        value = value.strip()

        if len(value) < 2:
            raise ValueError("O nome do jogo deve ter pelo menos 2 caracteres.")

        if len(value) > 150:
            raise ValueError("O nome do jogo deve ter no máximo 150 caracteres.")

        self.value = value
