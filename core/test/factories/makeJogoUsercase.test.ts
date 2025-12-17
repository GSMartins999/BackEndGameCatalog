import { makeJogoUseCase } from '@/core/factories/makeJogo';
import { MockJogoRepository } from '@/core/infra/mocks/MockJogoRepository';

describe('makeJogoUseCase Factory', () => {
  it('deve garantir que todos os casos de uso compartilham o mesmo repositório singleton', () => {
    const { registerJogo, editJogo, removeJogo } = makeJogoUseCase();

    const repo1 = (registerJogo as any).jogoRepository;
    const repo2 = (editJogo as any).jogoRepository;
    const repo3 = (removeJogo as any).jogoRepository;

    expect(repo1).toBe(repo2);
    expect(repo2).toBe(repo3);
    expect(repo1).toBeInstanceOf(MockJogoRepository);
  });
});
