from core.domain.entities import Jogo
from core.domain.value_objects import nome_jogo, descricao, url, data_lancamento


def test_should_create_a_valid_jogo():
    jogo = Jogo(
        id_jogo=1,
        nome_do_jogo=nome_jogo("Need for Speed"),
        descricao=descricao("Jogo de corrida"),
        url=url("http://example.com/photo.jpg"),
        data_lancamento=data_lancamento(2025),
    )

    assert jogo.id_jogo == 1
    assert jogo.nome_do_jogo.value == "Need for Speed"
    assert jogo.descricao.value == "Jogo de corrida"
    assert jogo.url.value == "http://example.com/photo.jpg"
    assert jogo.data_lancamento == 2025
