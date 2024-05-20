
import smtplib  # Envio de e-mails
import os  # Interação com o sistema operacional
from email.mime.multipart import MIMEMultipart  # Mensagens multipartes
from email.mime.text import MIMEText  # Partes de texto em MIME
from email.mime.base import MIMEBase  # Partes MIME com conteúdo base
from email import encoders  # Codificação MIME


#Função para enviar emails
def enviar_email(enviar_para):
    #Escrever texto usando a linguagem HTML
    corpo_email = """
    <p>Cumprimento</p> 
    <p>Mensagem a ser passada</p>
    <p><b>Atenciosamente, </b></p>
    <img src="cid:assinatura"> <!-- Referência à imagem de assinatura -->
    """

    # Configuração da mensagem
    msg = MIMEMultipart()
    msg['Subject'] = ' Assunto' #Assunto da mensagem de e-mail
    msg['From'] = 'Email do emissor' #Quem está enviando o e-mail
    msg['To'] = enviar_para #Para quem o e-mail será enviado
    password = 'Senha' #Senha(obs: senha aleátoria gerada pelo gmail para a segurança)
    msg.add_header('Content-Type', 'text/html') #Define o tipo do texto(html)
    msg.attach(MIMEText(corpo_email, 'html')) #Traz html para o corpo

    # Adiciona anexo
    caminho_atual = os.path.abspath(os.path.dirname(__file__)) #Caça o caminho arquivo no sistema
    caminho_relativo_anexo = os.path.join(caminho_atual, "NomeArquivo") #O nome se junta com o caminho
    attachment = open(caminho_relativo_anexo, 'rb') #Transforma o arquivo em leitura binária
    att = MIMEBase('application', 'pdf') #Cria um objeto MIMEBase com o tipo de conteúdo(Mude a extensão para o seu tipo)
    att.set_payload(attachment.read()) #Define o conteúdo do anexo como os dados lidos do arquivo
    encoders.encode_base64(att) #Codifica o conteúdo do anexo em base64
    nome_anexo = os.path.basename(caminho_relativo_anexo) #Nome do arquivo
    #Adiciona um cabeçalho à parte do anexo indicando o nome do arquivo
    att.add_header('Content-Disposition', 'attachment', filename=('UTF-8', '', nome_anexo))
    attachment.close()#Fecha o arquivo anexo
    msg.attach(att)#Anexa o arquivo à mensagem

    # Anexar imagem de assinatura
    caminho_relativo_assinatura = os.path.join(caminho_atual, "nomeAssinatura") #Junta o nome e o caminho do arquivo
    with open(caminho_relativo_assinatura, 'rb') as img: #Abre a imagem tornando ela em leitura binária
        imagem_anexada = MIMEBase('image', 'jpeg', filename="nomeAssinatura") #Cria um objeto MIMEBase com o tipo de conteúdo
        imagem_anexada.set_payload(img.read()) #Define o conteúdo do anexo como os dados lidos do arquivo
        encoders.encode_base64(imagem_anexada) #Codifica o conteúdo do anexo em base64
        imagem_anexada.add_header('Content-ID', '<assinatura>') #Adiciona um cabeçalho à parte do anexo indicando o nome do arquivo
        msg.attach(imagem_anexada) #Anexa o arquivo à mensagem

    # Envio do e-mail
    s = smtplib.SMTP('smtp.gmail.com:587') #Cria um objeto para se conectar ao servidor do Gmail
    s.starttls() #Inicia a conexão para criptografar a comunicação com o servidor SMTP
    s.login(msg['From'], password) #Realiza o login no servidor
    s.sendmail(msg['From'], [msg['To']], msg.as_string().encode('utf-8')) #Envia o e-mail
    print(f'Email enviado para {enviar_para}...') #Exibe mensagem de para quem foi enviado

# Caminho do arquivo de e-mails
caminho_atual = os.path.abspath(os.path.dirname(__file__)) #Caça o caminho arquivo no sistema
caminho_relativo_emails = os.path.join(caminho_atual, "listaDeEmails.txt") #O nome se junta com o caminho

# Envio para cada e-mail da lista
with open(caminho_relativo_emails) as file: #Abre o arquivo de texto contendo a lista de e-mails
    while line := file.readline(): #Itera sobre cada linha do arquivo
        enviar_email(line.rstrip()) #Remove quaisquer espaços em branco no final da linha e chama a funçaõ "enviar_email"

# Confirmação de envio conluída
print("Envios concluídos com sucesso!")
