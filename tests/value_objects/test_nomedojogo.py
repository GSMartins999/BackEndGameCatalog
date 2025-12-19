import pytest
from core.domain.value_objects import NomeDoJogo


def test_should_create_a_valid_nomejogo():
    nomejogo = NomeDoJogo("Mario Kart")
    assert nomejogo.value == "Mario Kart"


def test_should_raise_error_for_invalid_nomejogo():
    # Test with very short name (less than 3 characters)
    with pytest.raises(ValueError, match="Nome Inválido"):
        NomeDoJogo("ZZ")


def test_should_raise_error_for_empty_nomejogo():
    with pytest.raises(ValueError, match="Nome Inválido"):
        NomeDoJogo("")
