import pandas as pd
from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC60c7d0706d03803df5b8792b59f275f8"
# Your Auth Token from twilio.com/console
auth_token  = "5dbc4bf10ccb3b11b229b211b422cefe"
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
            to="+5511958689330",
            from_="+12132933323",
            body=f'No mês {mes}, foi localizado um vendedor! Vendedor: {vendedor}, com o total de vendas: {vendas}')

        print(message.sid)
# Se maior que 55k> sms para número: com nome/mês e vendasmes









