import { RegisterJogo } from '@/core/domain/use-cases/RegisterJogo';
import { Jogo } from '@/core/domain/entities/Jogo';

class MockJogoRepository {
  public jogos: Jogo[] = [];

  async save(jogo: Jogo): Promise<void> {
    this.jogos.push(jogo);
  }
}

describe('RegisterJogo Use Case', () => {
  let registerJogo: RegisterJogo;
  let repo: MockJogoRepository;

  beforeEach(() => {
    repo = new MockJogoRepository();
    registerJogo = new RegisterJogo(repo as any);
  });

  it('deve registrar um jogo válido', async () => {
    const jogo = await registerJogo.execute({
      NomeDoJogo: 'Super Mario',
      Descricao: 'Um jogo clássico da Nintendo com descrição válida.',
      URL: 'https://example.com/mario.jpg',
      DataLancamento: new Date('1985-09-13'),
    });

    expect(jogo).toBeInstanceOf(Jogo);
    expect(jogo.NomeDoJogo.value).toBe('Super Mario');
    expect(repo.jogos).toHaveLength(1);
  });

  it('deve lançar erro se a descrição for muito curta', async () => {
    await expect(
      registerJogo.execute({
        NomeDoJogo: 'Zelda',
        Descricao: 'Curto', // inválido
        URL: 'https://example.com/zelda.jpg',
        DataLancamento: new Date('1998-11-21'),
      })
    ).rejects.toThrow('A descrição deve ter no mínimo 10 caracteres.');
  });
});
