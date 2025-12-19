from datetime import date
import re


class DataLancamento:
    def __init__(self, value):
        if isinstance(value, str):
            # Valida formato YYYY-MM-DD
            if not re.match(r'^\d{4}-\d{2}-\d{2}$', value):
                raise ValueError("Data de Lançamento inválida")
            self.value = value
        elif isinstance(value, date):
            self.value = value.isoformat()
        else:
            raise ValueError("Data de Lançamento inválida")
