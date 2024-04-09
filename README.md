# Enviador de E-mails

Este é um script Python para enviar e-mails utilizando a biblioteca `smtplib`. Ele é útil para enviar mensagens personalizadas com anexos para múltiplos destinatários de uma lista.

## Funcionalidades

- **Envio de E-mails Personalizados:** O script permite enviar e-mails com mensagens personalizadas em HTML para destinatários específicos.
- **Anexos:** É possível adicionar anexos aos e-mails, como documentos PDF.
- **Imagem de Assinatura:** Adiciona uma imagem de assinatura ao e-mail.
- **Leitura de Lista de E-mails:** O script lê uma lista de e-mails de um arquivo de texto para enviar e-mails para múltiplos destinatários.

## Requisitos

- Python 3.x

## Bibliotecas Utilizadas

- `smtplib`: Para enviar e-mails através do protocolo SMTP.
- `os`: Para interagir com o sistema operacional e gerenciar arquivos.
- `email.mime`: Para construir as partes da mensagem de e-mail.
- `email.encoders`: Para codificar os anexos em base64.

## Como Usar

1. Certifique-se de ter Python instalado em seu sistema.
2. Edite o script e insira as informações necessárias, como assunto, remetente, senha, corpo do e-mail e caminho do arquivo de lista de e-mails.
3. Execute o script.
4. Aguarde o envio dos e-mails para os destinatários.

## Como Contribuir

Se você deseja contribuir para este script, sinta-se à vontade para fazer um fork do repositório, fazer suas modificações e enviar um pull request.

## Autor

Este script foi desenvolvido por Ageu Felipe Nunes Moraes. Para dúvidas ou sugestões, entre em contato pelo e-mail [ageumoraes67@gmail.com](mailto:ageumoraes67@gmail.com).

## Aviso Legal

Este script é apenas para fins educacionais e não possui afiliação com serviços de e-mail ou outras empresas mencionadas.
