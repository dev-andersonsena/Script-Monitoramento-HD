import psutil
from twilio.rest import Client

# Configurações do Twilio
account_sid = 'sua_account_sid'
auth_token = 'seu_auth_token'
twilio_number = 'seu_numero_twilio'
to_number = 'numero_para_envio'

# Função para verificar o uso do HD
def verificar_uso_hd():
    uso_hd = psutil.disk_usage('/')
    return uso_hd.percent

# Função para enviar alerta via WhatsApp
def enviar_alerta(mensagem):
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body=mensagem,
        from_='whatsapp:' + twilio_number,
        to='whatsapp:' + to_number
    )
    print(f"Mensagem enviada: {message.sid}")

# Função principal
def monitorar_hd():
    uso_atual = verificar_uso_hd()
    print(f"Uso atual do HD: {uso_atual}%")
    if uso_atual > 80:
        mensagem = f"Alerta! Uso do HD está em {uso_atual}%"
        enviar_alerta(mensagem)

# Executa a função de monitoramento
if __name__ == '__main__':
    monitorar_hd()
