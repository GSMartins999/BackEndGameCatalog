import { RemoveJogo } from '../../../domain/use-cases/RemoveJogo'; 
import { MockJogoRepository } from '../../../infra/mocks/MockJogoRepository';
import { Jogo } from '../../../domain/entities/Jogo';
import { NomeDoJogo } from '../../../domain/value-objects/NomeDoJogo';
import { Descricao } from '../../../domain/value-objects/Descricao';
import { URL } from '../../../domain/value-objects/URL';
import { DataLancamento } from '../../../domain/value-objects/DataLancamento';

describe('Remove Use Case (RemoveJogo)', () => {
  let removeJogo: RemoveJogo;
  let jogoRepository: MockJogoRepository;
  const jogoIdToRemove = 20;

  beforeEach(async () => {
    jogoRepository = MockJogoRepository.getInstance();
    jogoRepository.reset();
    
    const jogoToRemove = Jogo.create(
      jogoIdToRemove,
      NomeDoJogo.create('Jogo a Remover'),
      Descricao.create('Descricao.'),
      URL.create('https://remover.com/img.jpg'),
      DataLancamento.create(new Date('2010-01-01'))
    );
    await jogoRepository.save(jogoToRemove);

    removeJogo = new RemoveJogo(jogoRepository);
  });

  it('deve remover o jogo com sucesso', async () => {
    expect(await jogoRepository.findById(jogoIdToRemove)).not.toBeNull();

    await removeJogo.execute(jogoIdToRemove);

    expect(await jogoRepository.findById(jogoIdToRemove)).toBeNull();
  });

  it('não deve lançar erro ao tentar remover um jogo que não existe', async () => {
    await expect(
      removeJogo.execute(999)
    ).resolves.not.toThrow();
  });
});