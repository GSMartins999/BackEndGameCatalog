import { UpdateUser } from '../../../domain/use-cases/UpdateUser';
import { MockUserRepository } from '../../../infra/mocks/MockUserRepository';
import { User } from '../../../domain/entities/User';
import { Email } from '../../../domain/value-objects/Email';
import { Password } from '../../../domain/value-objects/Password';

interface UpdateUserParams {
    id: string;
    password: string; 
}

describe('Update Use Case (UpdateUser)', () => {
    let updateUser: UpdateUser;
    let userRepository: MockUserRepository;
    const userId = 'u-edit';
    const oldPassword = 'SenhaAntiga1!';
    const newPassword = 'NovaSenhaForte2@';

    beforeEach(async () => {
        userRepository = MockUserRepository.getInstance();
        userRepository.reset();

        const user = User.create(userId, Email.create('edit@user.com'), Password.create(oldPassword));
        await userRepository.save(user);

        updateUser = new UpdateUser(userRepository);
    });

    it('deve atualizar a senha do usuário com sucesso', async () => {
        const params: UpdateUserParams = { id: userId, password: newPassword };
        await updateUser.execute(params);

        const updatedUser = await userRepository.findById(userId);

        expect(updatedUser).not.toBeNull();
        expect(updatedUser?.password.value).toBe(newPassword);
    });

    it('deve lançar um erro se o ID do usuário não for encontrado', async () => {
        const params: UpdateUserParams = { id: 'id-nao-existe', password: newPassword };
        await expect(
            updateUser.execute(params)
        ).rejects.toThrow('Usuário não encontrado.');
    });
});