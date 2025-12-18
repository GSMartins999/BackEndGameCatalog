import pytest
from core.domain.value_objects import DataLancamento


def test_should_create_a_valid_datalancamento():
    datalancamento = DataLancamento("2023-05-05")
    assert datalancamento.value == "2023-05-05"


def test_should_raise_error_for_invalid_datalancamento():
    with pytest.raises(ValueError, match="Data de Lançamento inválida"):
        DataLancamento("05-05-2023")


def test_should_raise_error_for_empty_datalancamento():
    with pytest.raises(ValueError, match="Data de Lançamento inválida"):
        DataLancamento("")
