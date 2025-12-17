import { URL } from '../../../domain/value-objects/URL';

describe('URL Value Object', () => {

  const urlValida = 'https://www.meusite.com/imagem.png';
  const urlInvalida = 'www.linksemprotocolo.com';
  const urlInvalidaFormat = 'htt://linkerrado';

  it('deve criar uma URL válida com protocolo HTTPS', () => {
    const url = URL.create(urlValida);
    expect(url).toBeInstanceOf(URL);
    expect(url.value).toBe(urlValida);
  });

  it('deve lançar um erro se a URL for vazia', () => {
    expect(() => {
      URL.create('');
    }).toThrow('A URL é obrigatória.');
  });

  it('deve lançar um erro se a URL não tiver um protocolo válido (http/https)', () => {
    expect(() => {
      URL.create(urlInvalida);
    }).toThrow('O formato da URL é inválido. Deve começar com http:// ou https://'); 
  });

  it('deve lançar um erro se o formato geral da URL estiver incorreto', () => {
    expect(() => {
      URL.create(urlInvalidaFormat);
    }).toThrow('O formato da URL é inválido. Deve começar com http:// ou https://');
  });
});