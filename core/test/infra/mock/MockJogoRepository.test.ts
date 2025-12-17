import { MockJogoRepository } from '../../../infra/mocks/MockJogoRepository';
import { Jogo } from '../../../domain/entities/Jogo';
import { NomeDoJogo } from '../../../domain/value-objects/NomeDoJogo';
import { Descricao } from '../../../domain/value-objects/Descricao';
import { URL } from '../../../domain/value-objects/URL';
import { DataLancamento } from '../../../domain/value-objects/DataLancamento';

describe('MockJogoRepository', () => {
  let repository: MockJogoRepository;
  
  const mockJogo1 = Jogo.create(
    1,
    NomeDoJogo.create('The Witcher 3'),
    Descricao.create('RPG de fantasia sombria.'),
    URL.create('https://thewitcher.com/img.jpg'),
    DataLancamento.create(new Date('2015-05-19T00:00:00Z'))
  );

  const mockJogo2 = Jogo.create(
    2,
    NomeDoJogo.create('Doom Eternal'),
    Descricao.create('Tiro em primeira pessoa acelerado.'),
    URL.create('https://doom.com/img.jpg'),
    DataLancamento.create(new Date('2020-03-20T00:00:00Z'))
  );
  
  beforeEach(async () => {
    repository = MockJogoRepository.getInstance();
    repository.reset();
    await repository.save(mockJogo1); 
    await repository.save(mockJogo2); 
  });

  it('deve retornar todos os jogos com findAll', async () => {
    const jogos = await repository.findAll();
    expect(jogos).toHaveLength(2);
    expect(jogos[0].NomeDoJogo.value).toBe('The Witcher 3');
  });

  it('deve encontrar um jogo pelo ID com findById', async () => {
    const jogo = await repository.findById(1);
    expect(jogo).toEqual(mockJogo1);
  });

  it('deve retornar null para um ID inexistente com findById', async () => {
    const jogo = await repository.findById(99);
    expect(jogo).toBeNull();
  });

  it('deve salvar um novo jogo', async () => {
    const newJogo = Jogo.create(
        3, 
        NomeDoJogo.create('Hades'), 
        Descricao.create('Roguelite com narrativa.'),
        URL.create('https://hades.com/img.jpg'),
        DataLancamento.create(new Date('2020-09-17T00:00:00Z'))
    );
    await repository.save(newJogo);

    const savedJogo = await repository.findById(3);
    expect(savedJogo).toEqual(newJogo);
  });

  it('deve atualizar um jogo existente', async () => {
    const novoNome = 'The Witcher 3: Wild Hunt (GOTY)';
    const updatedJogo = Jogo.create(
        1, 
        NomeDoJogo.create(novoNome),
        mockJogo1.Descricao,
        mockJogo1.URL,
        mockJogo1.DataLancamento
    );

    await repository.update(updatedJogo);

    const jogo = await repository.findById(1);
    expect(jogo?.NomeDoJogo.value).toBe(novoNome);
  });

  it('deve deletar um jogo pelo ID', async () => {
    await repository.delete(2);
    
    const jogo = await repository.findById(2);
    expect(jogo).toBeNull();
  });

  it('deve encontrar jogos pelo nome com findByJogoName (busca parcial)', async () => {
    const jogos = await repository.findByJogoName('witcher');
    expect(jogos).toHaveLength(1);
    expect(jogos[0].IDJogo).toBe(1);
  });
  
  it('deve encontrar um jogo pela data de lançamento com findByDataLancamento', async () => {
    const dataBusca = new Date('2020-03-20'); 
    const jogo = await repository.findByDataLancamento(dataBusca);
    expect(jogo).toEqual(mockJogo2);
  });
});