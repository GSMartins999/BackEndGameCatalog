import { EditJogo } from '../../../domain/use-cases/EditJogo';
import { MockJogoRepository } from '../../../infra/mocks/MockJogoRepository';
import { Jogo } from '../../../domain/entities/Jogo';
import { NomeDoJogo } from '../../../domain/value-objects/NomeDoJogo';
import { Descricao } from '../../../domain/value-objects/Descricao';
import { URL } from '../../../domain/value-objects/URL';
import { DataLancamento } from '../../../domain/value-objects/DataLancamento';

interface EditJogoParams {
    IDJogo: number;
    NomeDoJogo?: string; 
    Descricao?: string;
    URL?: string; 
    DataLancamento?: Date; 
}

describe('EditJogo Use Case', () => {
    let editJogo: EditJogo;
    let jogoRepository: MockJogoRepository;
    const jogoId = 10;

    beforeEach(async () => {
        jogoRepository = MockJogoRepository.getInstance();
        jogoRepository.reset();
        
        const initialJogo = Jogo.create(
            jogoId,
            NomeDoJogo.create('Jogo Antigo'),
            Descricao.create('Descricao inicial.'),
            URL.create('https://antiga.com/img.jpg'),
            DataLancamento.create(new Date('2000-01-01'))
        );
        await jogoRepository.save(initialJogo);

        editJogo = new EditJogo(jogoRepository);
    });

    it('deve editar o nome e a descrição do jogo com sucesso', async () => {
        const novoNome = 'Novo Jogo Incrível';
        const novaDescricao = 'Esta é a nova descrição atualizada.';
        
        const params: EditJogoParams = {
            IDJogo: jogoId,
            NomeDoJogo: novoNome,
            Descricao: novaDescricao,
        };

        await editJogo.execute(params);

        const updatedJogo = await jogoRepository.findById(jogoId);

        expect(updatedJogo).not.toBeNull();
        expect(updatedJogo?.NomeDoJogo.value).toBe(novoNome);
        expect(updatedJogo?.Descricao.value).toBe(novaDescricao);
    });

    it('deve lançar um erro se o ID do jogo não for encontrado', async () => {
        const params: EditJogoParams = {
            IDJogo: 999,
            NomeDoJogo: 'Nome',
            Descricao: 'Desc',
            URL: 'https://url.com',
            DataLancamento: new Date()
        };

        await expect(
            editJogo.execute(params)
        ).rejects.toThrow('Jogo não encontrado para edição.');
    });
});