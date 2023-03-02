# Importa a biblioteca pandas e a renomeia como pd
import pandas as pd

# Importa a biblioteca twilio
import twilio as tw

# Importa a classe Client da biblioteca twilio.rest
from twilio.rest import Client

# Define as credenciais da conta do Twilio
# Your Account SID from twilio.com/console
account_sid = "AC55751ee362872314447aa44cd156f524"
# Your Auth Token from twilio.com/console
auth_token  = "665e9a50bfc97f685ee1af3e5368d5d8"

# Cria um objeto Client com as credenciais do Twilio
client = Client(account_sid, auth_token)

# Cria uma lista com os nomes dos meses
lista_meses = ['janeiro', 'fevereiro', 'março', 'abril', 'maio', 'junho']

# Percorre a lista de meses
for mes in lista_meses: 
    # Lê o arquivo Excel correspondente ao mês atual
    tabela_vendas = pd.read_excel(f'{mes}.xlsx')
    
    # Verifica se há alguma venda acima de 55000
    if (tabela_vendas['Vendas'] > 55000).any():
        # Obtém o nome e a quantidade de vendas do vendedor que fez a venda acima de 55000
        pessoa = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0]
        numero_vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0]
        
        # Envia uma mensagem SMS com as informações da venda acima de 55000
        message = client.messages.create(
            to="+5551994565446", 
            from_="+13155992967",
            body=f"No mes de {mes} eu achei alguem com mais de 55000, essa pessoa é {pessoa} e ela fez um total de R${numero_vendas}"
        )
        
        # Imprime o ID da mensagem enviada
        print(message.sid)