from datetime import date


class DataLancamento:
    def __init__(self, value: date):
        if not isinstance(value, date):
            raise ValueError("Data de lançamento é obrigatória e deve ser válida.")

        self.value = value
