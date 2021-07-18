import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "ACxxxx"
# Your Auth Token from twilio.com/console
auth_token  = "5dbxxxxx"
client = Client(account_sid, auth_token)

# Passo a passo da solução

# Abrir os arquivos em xls

lista_meses = ['janeiro', 'fevereiro','março', 'abril', 'maio', 'junho'] #toda lista fica em colchetes

# Procurar valores > 55k em cada arquivo na coluna VENDAS
for mes in lista_meses:
    tabela_vendas = pd.read_excel (f'{mes}.xlsx') #f{},valor entre chaves fica dinamico
    if (tabela_vendas['Vendas'] > 55000).any(): #tabela[coluna] > 55.000.algumvalor():
        vendedor = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendedor'].values[0] #linhacoluna
        vendas = tabela_vendas.loc[tabela_vendas['Vendas'] > 55000, 'Vendas'].values[0] #.values[0] sinaliza o valor direto
        print(f'No mês {mes}, foi localizado um vendedor! Vendedor: {vendedor}, com o total de vendas: {vendas}')
        message = client.messages.create(
            to="+55119xxxxx",
            from_="+12xxxxxx",
            body=f'No mês {mes}, foi localizado um vendedor! Vendedor: {vendedor}, com o total de vendas: {vendas}')

        print(message.sid)
# Se maior que 55k> sms para número: com nome/mês e vendasmes









