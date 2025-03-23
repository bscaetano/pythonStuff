import datetime

# Dicionários para armazenar clientes e contas
clientes = {}
contas = {}

# Log das transações
LOG_FILE = "transacoes.log"

# Função para registrar logs
def registrar_log(mensagem):
    with open(LOG_FILE, "a") as log:
        log.write(f"{datetime.datetime.now()} - {mensagem}\n")

# Menu principal
def menu():
    return """\n
    [1] Cadastrar Cliente
    [2] Criar Conta
    [3] Depositar
    [4] Sacar
    [5] Extrato
    [6] Sair
    => """

# Cadastro de cliente
def cadastrar_cliente():
    cpf = input("Digite o CPF (somente números): ")
    
    if cpf in clientes:
        print("CPF já cadastrado.")
        return
    
    nome = input("Nome completo: ")
    data_nascimento = input("Data de nascimento (DD/MM/AAAA): ")
    endereco = input("Endereço (Rua, Número, Bairro, Cidade - Estado): ")
    
    clientes[cpf] = {"nome": nome, "data_nascimento": data_nascimento, "endereco": endereco}
    print("Cliente cadastrado com sucesso!")
    registrar_log(f"Novo cliente cadastrado: {cpf} - {nome}")

# Criação de conta
def criar_conta():
    cpf = input("Digite o CPF do titular: ")
    
    if cpf not in clientes:
        print("Cliente não encontrado! Cadastre primeiro.")
        return
    
    numero_conta = len(contas) + 1
    contas[numero_conta] = {"cpf": cpf, "saldo": 0, "limite": 500, "saques_realizados": 0, "extrato": ""}
    print(f"Conta criada com sucesso! Número da conta: {numero_conta}")
    registrar_log(f"Conta {numero_conta} criada para CPF {cpf}")

# Depósito
def depositar():
    conta = int(input("Digite o número da conta: "))
    
    if conta not in contas:
        print("Conta não encontrada!")
        return
    
    valor = float(input("Informe o valor do depósito: "))

    if valor > 0:
        contas[conta]["saldo"] += valor
        contas[conta]["extrato"] += f"Depósito: R$ {valor:.2f}\n"
        print("Depósito realizado com sucesso!")
        registrar_log(f"Depósito de R$ {valor:.2f} na conta {conta}")
    else:
        print("Valor inválido!")

# Saque
def sacar():
    conta = int(input("Digite o número da conta: "))

    if conta not in contas:
        print("Conta não encontrada!")
        return

    valor = float(input("Informe o valor do saque: "))
    saldo = contas[conta]["saldo"]
    limite = contas[conta]["limite"]
    saques_realizados = contas[conta]["saques_realizados"]

    if valor > saldo:
        print("Saldo insuficiente!")
    elif valor > limite:
        print("Saque excede o limite!")
    elif saques_realizados >= 3:
        print("Número máximo de saques diários atingido!")
    elif valor > 0:
        contas[conta]["saldo"] -= valor
        contas[conta]["saques_realizados"] += 1
        contas[conta]["extrato"] += f"Saque: R$ {valor:.2f}\n"
        print("Saque realizado com sucesso!")
        registrar_log(f"Saque de R$ {valor:.2f} na conta {conta}")
    else:
        print("Valor inválido!")

# Extrato
def exibir_extrato():
    conta = int(input("Digite o número da conta: "))

    if conta not in contas:
        print("Conta não encontrada!")
        return

    extrato = contas[conta]["extrato"]
    saldo = contas[conta]["saldo"]
    
    print("\n================ EXTRATO ================")
    print("Sem movimentações." if not extrato else extrato)
    print(f"\nSaldo atual: R$ {saldo:.2f}")
    print("==========================================")

# Loop principal
while True:
    opcao = input(menu())

    if opcao == "1":
        cadastrar_cliente()
    elif opcao == "2":
        criar_conta()
    elif opcao == "3":
        depositar()
    elif opcao == "4":
        sacar()
    elif opcao == "5":
        exibir_extrato()
    elif opcao == "6":
        print("Obrigado por usar nosso banco!")
        break
    else:
        print("Opção inválida, tente novamente.")