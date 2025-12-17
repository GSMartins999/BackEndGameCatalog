import { Descricao } from '../../../domain/value-objects/Descricao';

describe('Descricao Value Object', () => {

  const descricaoValida = 'Esta é uma descrição curta, mas válida.';
  const descricaoMuitoCurta = 'curta';
  const descricaoMuitoLonga = 'a'.repeat(501);

  it('deve criar uma descrição válida', () => {
    const descricao = Descricao.create(descricaoValida);
    expect(descricao).toBeInstanceOf(Descricao);
    expect(descricao.value).toBe(descricaoValida);
  });

  it('deve lançar um erro se a descrição for vazia', () => {
    expect(() => {
      Descricao.create('');
    }).toThrow('A descrição é obrigatória.');
  });

  it('deve lançar um erro se a descrição for muito curta', () => {
    expect(() => {
      Descricao.create(descricaoMuitoCurta);
    }).toThrow('A descrição deve ter no mínimo 10 caracteres.');
  });

  it('deve lançar um erro se a descrição for muito longa', () => {
    expect(() => {
      Descricao.create(descricaoMuitoLonga);
    }).toThrow('A descrição deve ter no máximo 500 caracteres.');
  });
});