import { LoginUser } from '../../../domain/use-cases/LoginUser';
import { MockUserRepository } from '../../../infra/mocks/MockUserRepository';
import { User } from '../../../domain/entities/User';
import { Email } from '../../../domain/value-objects/Email';
import { Password } from '../../../domain/value-objects/Password';

interface LoginParams {
    email: string;
    password: string;
}

describe('Login Use Case (LoginUser)', () => {
    let loginUser: LoginUser;
    let userRepository: MockUserRepository;
    const mockEmail = 'teste@login.com';
    const mockPassword = 'SenhaCorreta1!';

    beforeEach(async () => {
        userRepository = MockUserRepository.getInstance();
        userRepository.reset();

        const userToSave = User.create('u-1', Email.create(mockEmail), Password.create(mockPassword));
        await userRepository.save(userToSave);

        loginUser = new LoginUser(userRepository);
    });

    it('deve logar o usuário com credenciais válidas', async () => {
        const user = await loginUser.execute({ email: mockEmail, password: mockPassword } as LoginParams);

        expect(user).toBeInstanceOf(User);
        expect(user.email.value).toBe(mockEmail);
    });

    it('deve lançar um erro se o e-mail não for encontrado', async () => {
        await expect(
            loginUser.execute({ email: 'naoencontrado@email.com', password: mockPassword } as LoginParams)
        ).rejects.toThrow('Credenciais inválidas.');
    });

    it('deve lançar um erro se a senha estiver incorreta', async () => {
        await expect(
            loginUser.execute({ email: mockEmail, password: 'SenhaIncorreta0!' } as LoginParams)
        ).rejects.toThrow('Credenciais inválidas.');
    });
});