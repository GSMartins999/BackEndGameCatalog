import { RegisterUser } from '../../../domain/use-cases/RegisterUser';
import { MockUserRepository } from '../../../infra/mocks/MockUserRepository';

interface RegisterParams {
    email: string;
    password: string;
}

describe('RegisterUser Use Case', () => {
    let registerUser: RegisterUser;
    let userRepository: MockUserRepository;

    beforeEach(() => {
        userRepository = MockUserRepository.getInstance();
        userRepository.reset();
        registerUser = new RegisterUser(userRepository);
    });

    it('deve registrar um novo usuário com sucesso', async () => {
        const emailString = 'novo@teste.com';
        const passwordString = 'NovaSenha123!';

        const params: RegisterParams = { email: emailString, password: passwordString };
        const result = await registerUser.execute(params);

        expect(result.id).toBeDefined();
        expect(result.email.value).toBe(emailString);

        const savedUser = await userRepository.findByEmail(emailString);
        expect(savedUser).not.toBeNull();
    });

    it('deve lançar um erro se o e-mail já estiver em uso', async () => {
        const existingEmail = 'existente@teste.com';
        const passwordString = 'Senha123!';

        const params: RegisterParams = { email: existingEmail, password: passwordString };

        await registerUser.execute(params);

        await expect(
            registerUser.execute(params)
        ).rejects.toThrow('Usuário já existe.');
    });
});