import { User } from "../../../domain/entities/User";
import { Email } from '../../../domain/value-objects/Email';
import { Password } from '../../../domain/value-objects/Password';

describe('User', () => {
  it('deve criar uma instância de User válida', () => {
    const mockId = 'user-123';
    const mockEmail = 'john.doe@example.com';
    const mockPassword = 'SenhaSegura123!';

    const user = User.create(
      mockId,
      Email.create(mockEmail),
      Password.create(mockPassword),
    );

    expect(user).toBeInstanceOf(User);

    expect(user.id).toBe(mockId);
    expect(user.email.value).toBe(mockEmail);
    expect(user.password.value).toBe(mockPassword);
  });

  it('deve lançar um erro ao tentar criar um Email inválido', () => {
    const emailInvalido = 'email-invalido-sem-arroba.com';

    expect(() => {
      User.create(
        '2',
        Email.create(emailInvalido), 
        Password.create('P@ssword1'),
      );
    }).toThrow('Invalid email');
  });
});