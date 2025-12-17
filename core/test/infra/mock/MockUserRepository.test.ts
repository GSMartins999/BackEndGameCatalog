import { MockUserRepository } from '../../../infra/mocks/MockUserRepository';
import { User } from '../../../domain/entities/User';
import { Email } from '../../../domain/value-objects/Email';
import { Password } from '../../../domain/value-objects/Password';

describe('MockUserRepository', () => {
  let repository: MockUserRepository;
  
  const mockUser1 = User.create('u-1', Email.create('user1@test.com'), Password.create('Password123!'));
  const mockUser2 = User.create('u-2', Email.create('user2@test.com'), Password.create('Password123!'));

  beforeEach(async () => {
    repository = MockUserRepository.getInstance();
    repository.reset(); 
    await repository.save(mockUser1); 
    await repository.save(mockUser2); 
  });

  it('deve ser um singleton, retornando sempre a mesma instância', () => {
    const instance2 = MockUserRepository.getInstance();
    expect(repository).toBe(instance2);
  });

  it('deve encontrar um usuário pelo ID com findById', async () => {
    const user = await repository.findById('u-1');
    expect(user).toEqual(mockUser1);
  });

  it('deve retornar null para ID de usuário inexistente', async () => {
    const user = await repository.findById('u-99');
    expect(user).toBeNull();
  });

  it('deve encontrar um usuário pelo Email com findByEmail', async () => {
    const user = await repository.findByEmail('user2@test.com');
    expect(user).toEqual(mockUser2);
  });

  it('deve retornar null para Email inexistente', async () => {
    const user = await repository.findByEmail('inexistente@test.com');
    expect(user).toBeNull();
  });

  it('deve salvar um novo usuário', async () => {
    const newUser = User.create('u-3', Email.create('user3@test.com'), Password.create('OutraSenha456!'));
    await repository.save(newUser);

    const user = await repository.findById('u-3');
    expect(user).toEqual(newUser);
  });

  it('deve atualizar um usuário existente', async () => {
    const newEmailValue = 'user1.novo@test.com';
    const updatedUser = User.create('u-1', Email.create(newEmailValue), mockUser1.password); 

    await repository.update(updatedUser);

    const user = await repository.findById('u-1');
    expect(user?.email.value).toBe(newEmailValue);
  });

  it('deve deletar um usuário pelo ID', async () => {
    await repository.delete('u-2');
    
    const user = await repository.findById('u-2');
    expect(user).toBeNull();
  });

  it('deve limpar o repositório com reset', async () => {
    repository.reset();
    const user = await repository.findById('u-1');
    expect(user).toBeNull();
  });
});