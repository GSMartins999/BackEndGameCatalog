import { DataLancamento } from '../../../domain/value-objects/DataLancamento';

describe('DataLancamento Value Object', () => {

  const dataValida = new Date('2020-01-01');
  const dataFutura = new Date('2099-01-01');

  it('deve criar uma instância válida se a data for no passado ou presente', () => {
    const data = DataLancamento.create(dataValida);
    expect(data).toBeInstanceOf(DataLancamento);
    expect(data.value.getFullYear()).toBe(2020);
  });

  it('deve lançar um erro se a data de lançamento for no futuro', () => {
    expect(() => {
      DataLancamento.create(dataFutura);
    }).toThrow('A data de lançamento não pode ser no futuro.'); 
  });

  it('deve lançar um erro se for fornecida uma data inválida (ex: null)', () => {
    expect(() => {
      // @ts-ignore
      DataLancamento.create(null); 
    }).toThrow('Data de lançamento é obrigatória e deve ser válida.');
  });
});