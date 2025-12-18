import pytest
from core.domain.value_objects import Descricao


def test_should_create_a_valid_descricao():
    descricao = Descricao("Jogo legal")
    assert descricao.value == "Jogo legal"


def test_should_raise_error_for_empty_descricao():
    with pytest.raises(ValueError, match="Descrição não pode ser vazia"):
        Descricao("")


def test_should_raise_error_for_invalid_descricao():
    with pytest.raises(ValueError, match="Descrição invalida"):
        Descricao("invalid description")
