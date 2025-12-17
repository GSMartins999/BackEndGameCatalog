import { NomeDoJogo } from '../../../domain/value-objects/NomeDoJogo';

describe('NomeDoJogo Value Object', () => {

  const nomeValido = 'Final Fantasy VII Remake';
  const nomeVazio = '  ';
  const nomeMuitoLongo = 'N'.repeat(151);

  it('deve criar um NomeDoJogo válido', () => {
    const nome = NomeDoJogo.create(nomeValido);
    expect(nome).toBeInstanceOf(NomeDoJogo);
    expect(nome.value).toBe(nomeValido);
  });

  it('deve limpar espaços em branco no início/fim', () => {
    const nomeComEspacos = '  Super Mario Bros  ';
    const nome = NomeDoJogo.create(nomeComEspacos);
    expect(nome.value).toBe('Super Mario Bros');
  });

  it('deve lançar um erro se o nome for nulo ou apenas espaços', () => {
    expect(() => {
      NomeDoJogo.create(nomeVazio);
    }).toThrow('O nome do jogo é obrigatório.');
  });

  it('deve lançar um erro se o nome for muito longo', () => {
    expect(() => {
      NomeDoJogo.create(nomeMuitoLongo);
    }).toThrow('O nome do jogo deve ter no máximo 150 caracteres.');
  });
});