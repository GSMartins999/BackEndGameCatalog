import { RegisterJogo } from '../../../domain/use-cases/RegisterJogo';
import { MockJogoRepository } from '../../../infra/mocks/MockJogoRepository';

interface RegisterJogoParams {
    NomeDoJogo: string;
    Descricao: string;
    URL: string;
    DataLancamento: Date;
}

describe('RegisterJogo Use Case', () => {
    let registerJogo: RegisterJogo;
    let jogoRepository: MockJogoRepository;

    beforeEach(() => {
        jogoRepository = MockJogoRepository.getInstance();
        jogoRepository.reset();
        registerJogo = new RegisterJogo(jogoRepository);
    });

    it('deve registrar um novo jogo com sucesso', async () => {
        const nome = 'The Sims 4';
        const descricao = 'Jogo de simulação de vida.';
        const url = 'https://sims.com/photo.jpg';
        const dataLancamento = new Date('2014-09-02');

        const params: RegisterJogoParams = {
            NomeDoJogo: nome,
            Descricao: descricao,
            URL: url,
            DataLancamento: dataLancamento
        };
        const jogo = await registerJogo.execute(params);

        expect(jogo.IDJogo).toBeDefined();
        expect(jogo.NomeDoJogo.value).toBe(nome);

        const savedJogos = await jogoRepository.findAll();
        expect(savedJogos.length).toBe(1);
    });

    it('deve lançar um erro se a URL for inválida', async () => {
        const params = {
            NomeDoJogo: 'Zelda',
            Descricao: 'Descrição válida com mais de 10 caracteres.', // ✅ descrição válida
            URL: 'ftp://invalid-url', // ❌ inválida
            DataLancamento: new Date('1998-11-21'),
        };

        await expect(registerJogo.execute(params))
            .rejects
            .toThrow('O formato da URL é inválido. Deve começar com http:// ou https://');
    });
});