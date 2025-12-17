import { DeleteUser } from '../../../domain/use-cases/DeleteUser';
import { MockUserRepository } from '../../../infra/mocks/MockUserRepository';
import { User } from '../../../domain/entities/User';
import { Email } from '../../../domain/value-objects/Email';
import { Password } from '../../../domain/value-objects/Password';

describe('Delete Use Case (DeleteUser)', () => {
    let deleteUser: DeleteUser;
    let userRepository: MockUserRepository;
    const userIdToDelete = 'u-delete';

    beforeEach(async () => {
        userRepository = MockUserRepository.getInstance();
        userRepository.reset();

        const userToDelete = User.create(userIdToDelete, Email.create('delete@user.com'), Password.create('SenhaDelete1!'));
        await userRepository.save(userToDelete);

        deleteUser = new DeleteUser(userRepository);
    });

    it('deve deletar o usuário com sucesso', async () => {
        expect(await userRepository.findById(userIdToDelete)).not.toBeNull();

        await deleteUser.execute({ id: userIdToDelete });

        expect(await userRepository.findById(userIdToDelete)).toBeNull();
    });

    it('não deve lançar erro ao tentar deletar um ID que não existe', async () => {
        await expect(
            deleteUser.execute({ id: 'id-inexistente' })
        ).resolves.not.toThrow();
    });
});