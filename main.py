import time
listinvest = []
listvalorinvest = []
listgastos = []
listvalorgasto = []
programexe = input("Deseja iniciar o programa? (s/n): ")
if programexe == "s":
    print("Iniciando o programa...")
    time.sleep(1)
    print("Ok! Vamos começar!")
    valor = float(input("Digite a funcionalidade. \n(1) Investimento, \n(2) Gastos, \n(3) Compras, \n(4) Sair: "))
    if valor == 1:
        invest = input("Deseja adicionar apelido ao investimento? (s/n):")
        if invest == "s":
            apelido = input("Como deseja chamar o investimento? ")
            valor = str(input(f"Digite o valor de {apelido}: "))
            print(f"Você adicionou o investimento {apelido} no valor de R${valor} na lista de investimentos.")
            listinvest.append((apelido))
            listvalorinvest.append((valor))
            while True:
                moreinvest = input("Deseja adicionar mais investimentos? (s/n): ")
                if moreinvest == "s":
                    apelido = input("Como deseja chamar o investimento? ")
                    valor = str(input(f"Digite o valor de {apelido}: "))
                    print(f"Você adicionou o investimento {apelido} no valor de R${valor} na lista de investimentos.")
                    listinvest.append((apelido))
                    listvalorinvest.append((valor))
                elif moreinvest == "n":
                    print("Ok! Obrigado!")
                    break
                else: 
                    print("ERRO! Digite apenas 's' ou 'n'.")
            print("Lista de investimentos:", listinvest)
            print("Lista de Valores: ", listvalorinvest)
        if invest == "n":
            print(valor)
    if valor == 2:
        analisegastos = str(input("Ok! Vamos analisar seus gastos! O que deseja fazer? \n(1) Adicionar gastos, \n(2) Ver lista de gastos, \n(3) Sair: "))
        if analisegastos == "1":
            namegasto = str(input("Deseja apelidar o gasto? (s/n): "))
            if namegasto =="s":
                apelidogasto = str(input("Como deseja chamar o gasto? "))
                valor = str(input(f"Digite o valor de {apelidogasto}: "))
                print(f"Você adicionou o gasto {apelidogasto} no valor de R${valor} na lista de gastos.")
                listgastos.append((apelidogasto))
                listvalorgasto.append((valor))
                while True:
                    moregasto = input("Deseja adicionar mais gastos? (s/n): ")
                    if moregasto == "s":
                        apelidogasto = str(input("Como deseja chamar o gasto? "))
                        valor = str(input(f"Digite o valor de {apelidogasto}: "))
                        print(f"Você adicionou o gasto {apelidogasto} no valor de R${valor} na lista de gastos.")
                        listgastos.append((apelidogasto))
                        listvalorgasto.append((valor))
                    elif moregasto == "n":
                        print("Ok! Obrigado!")
                        break
                    else: 
                        print("ERRO! Digite apenas 's' ou 'n'.")
