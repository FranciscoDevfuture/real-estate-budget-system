
#import os
#Vou importar a biblioteca csv
import csv
#função para mostrar o título da aplicação
def mostrar_titulo():
    print('Sistema de simulação de Orçamento Imobiliário versao 1.0')
    print('#'*8,'R.M IMOBILIÁRIA - LTDA','#'*8)
    
#função para calcular o valor do aluguel
def calcular_aluguel(tipo,quartos=1,garagem=False,vagas_estudio=0,tem_criancas=True):
    #valores da proposta se a escolha for apartamento
    if tipo == 'apartamento':
        valor = 700
        if quartos == 2:
            #se quarto for 2 então acrescenta valor de 200
            valor += 200
        if not tem_criancas: # 5% se nao tiver crianças
            valor *= 0.95
        if garagem:
            valor += 300

        #se escolha for casa
    elif tipo =='casa':
            valor = 900
            if quartos == 2:
                valor += 250
            if garagem:
                valor += 300
        #se escolha for Estudio
    elif tipo == 'estudio':
        valor = 1200
        if vagas_estudio >= 2: #primeira opção de 2 vagas = 250
            valor += 250
            if vagas_estudio > 2: #para vagas adicionais = 60 reais
                valor += (vagas_estudio- 2) * 60
            #se considera que até 2 duas vagas custam 250
            #se pedir mais que duas, calcular o valor extra.
            #se ele pediu 4 (4-2=2> ou seja duas vagas adicionais)
            #cada vaga extra custa 60, entao se multiplica por 60
            #2*60=120
            #O Operador += signifca somoar o valor atual de vagas.
            #ele ja tinha 250 pelas duas primeiras vagas, agora entao teve acrescimo de 120 extras 
            #250+120=370
    else:
        raise ValueError('o tipo de imóvel é inválido!')
        
    return valor
    
#função que gera um orçamento e salvar em CSV
def gerar_orcamento(tipo,quartos=1,garagem=False,vagas_estudio=0,tem_criancas=True):
    aluguel = calcular_aluguel(tipo,quartos,garagem,vagas_estudio,tem_criancas)
   
   
  #valor do contrato que pode ser parcelado em até 5 vezes  
    valor_contrato = 2000
    valor_parcelamento = valor_contrato/5
    #valor mensal total(aluguel+parcela do contrato)
    valor_mensal = aluguel + valor_parcelamento
    
    
    print(f'Tipo de contrato: {tipo}')
    print(f'Valor do aluguel: R$ {aluguel:.2f}')
    print(f'Parcela do contrato: {valor_parcelamento}')
    print(f'Valor Mensal: R$ {valor_mensal:.2f}')
    
# Aqui vou pedir pra gerar o arquivo CSV com 12 parcelas mensais

    with open('Orcamento.csv','w',newline='') as arquivo:
        escrever = csv.writer(arquivo)
        escrever.writerow(['Mês','Valor Mensal'])
        for mes in range(1,13):
            escrever.writerow([mes,round(valor_mensal,2)])
            
    print('O orçamento foi gerado com sucesso!')
    

#gerar_orcamento(tipo='estudio',vagas_estudio=2)
                
def menu():
    while True:
    #def limpar_tela():
       # os.system('cls' if os.name == 'nt' else 'clear')
        mostrar_titulo()
        #limpar_tela()
        print("""Escolha o Tipo de Imóvel:
        1 - Apartamento
        2 - Casa
        3 - Estudio
        0 - Sair
    """)
        opcao= input('Escolha a opção desejada:')
        if opcao == '1':
            tipo = 'apartamento'
            quartos = int(input('Quantos quartos deseja: (1 ou 2):'))
            garagem = input('Vagas de garagem (s/n)?:').lower()=='s'
            tem_criancas = input('Têm crianças (s/n)?:').lower()=='s'
            gerar_orcamento(tipo,quartos,garagem,tem_criancas=tem_criancas)
        
        elif opcao == '2':
            tipo = 'casa'
            quartos = int(input('Quantos quartos deseja: (1 ou 2):'))
            garagem = input('Vagas de garagem (s/n)?:').lower()=='s'
            tem_criancas = input('Têm crianças (s/n)?:').lower()=='s'
            gerar_orcamento(tipo,quartos,garagem,tem_criancas=tem_criancas)
        
        elif opcao == "3": 
             tipo = "estudio" 
             vagas = int(input("Quantas vagas de estacionamento? ")) 
             gerar_orcamento(tipo, vagas_estudio=vagas) 
        elif opcao == "0": 
            print('Encerrando o programa. Obrigado por usar a R.M Imobiliária!')
            break
        else:
            print('Opçao inválida! Tente Novamente.\n')
            
          
menu()
