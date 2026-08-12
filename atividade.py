import os

class Consulta:
    def __init__(self, data, paciente, medico):
        self.data = data
        self.paciente = paciente
        self.medico = medico
        self.diagnostico = None

    def registrar_diagnostico(self, texto):
        self.diagnostico = texto

    def exibir_consulta(self):
        print("\n--- Consulta ---")
        print(f"Data: {self.data}")
        print(f"Paciente: {self.paciente.exibir_info()}")
        print(f"Médico: {self.medico.exibir_info()} - Esp: {self.medico.especialidade}")
        if self.diagnostico:
            print(f"Diagnóstico: {self.diagnostico}")
        else:
            print("Diagnóstico: [a definir]")
        print("----------------\n")

class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def exibir_info(self, texto):
        self.diagnostico = texto

    def exibir_consulta(self):
        print("\n--- Pessoa ---")
        print(f"Data: {self.data}")
        print(f"Paciente: {self.paciente.exibir_info()}")
        print(f"Médico: {self.medico.exibir_info()} - Esp: {self.medico.especialidade}")
        if self.diagnostico:
            print(f"Diagnóstico: {self.diagnostico}")
        else:
            print("Diagnóstico: [a definir]")
        print("----------------\n")

class Medico:
    def __init__(self, data, paciente, medico):
        self.data = data
        self.paciente = paciente
        self.medico = medico
        self.diagnostico = None

    def registrar_diagnostico(self, texto):
        self.diagnostico = texto

    def exibir_consulta(self):
        print("\n--- Pessoa ---")
        print(f"Data: {self.data}")
        print(f"Paciente: {self.paciente.exibir_info()}")
        print(f"Médico: {self.medico.exibir_info()} - Esp: {self.medico.especialidade}")
        if self.diagnostico:
            print(f"Diagnóstico: {self.diagnostico}")
        else:
            print("Diagnóstico: [a definir]")
        print("----------------\n")
# ============================
# Menu de Linha de Comando
# ============================

medicos = []
pacientes = []
consultas = []


while True:

    print("===== Sistema da Clínica =====")
    print("1 - Cadastrar Médico")
    print("2 - Cadastrar Paciente")
    print("3 - Listar Médicos")
    print("4 - Listar Pacientes")
    print("5 - Marcar Consulta")
    print("6 - Listar Consultas")
    print("7 - Registrar Diagnóstico")
    print("0 - Sair")

    opcao = input("Escolha: ")
    os.system("clear")

    # Cadastrar Médico
    if opcao == "1":
        ####### CRIE O CÓDIGO PARA CADASTRAR MÉDICO
        print("Médico cadastrado com sucesso!\n")

    # Cadastrar Paciente
    elif opcao == "2":
        ####### CRIE O CÓDICO PARA CADASTRAR PACIENTE
        print("Paciente cadastrado com sucesso!\n")

    # Listar Médicos
    elif opcao == "3":
        for i, m in enumerate(medicos):
            print(f"{i} - {m.exibir_info()} | Esp: {m.especialidade}")
        print()

    # Listar Pacientes
    elif opcao == "4":
        ####### CRIE O CÓDIGO PARA LISTAR PACIENTES
        print()

    # Marcar Consulta
    elif opcao == "5":
        if not medicos or not pacientes:
            print("Cadastre médicos e pacientes primeiro!\n")
            continue
        for i, p in enumerate(pacientes):
            print(f"{i} - {p.exibir_info()}")
        idx_p = int(input("Escolha o paciente: "))
        paciente = pacientes[idx_p]

        for i, m in enumerate(medicos):
            print(f"{i} - {m.exibir_info()} | Esp: {m.especialidade}")
        idx_m = int(input("Escolha o médico: "))
        medico = medicos[idx_m]

        data = input("Data da consulta (dd/mm/aaaa): ")
        consulta = paciente.marcar_consulta(medico, data)
        consultas.append(consulta)
        print("Consulta marcada com sucesso!\n")

    # Listar Consultas
    elif opcao == "6":
        ###### CRIE O CÓDIGO PARA LISTAR AS CONSULTAS
        print()

    # Registrar Diagnóstico
    elif opcao == "7":
        for i, c in enumerate(consultas):
            print(f"{i} - {c.data} | Paciente: {c.paciente.nome} | Médico: {c.medico.nome}")
        idx_c = int(input("Escolha a consulta: "))
        diag = input("Digite o diagnóstico: ")
        consultas[idx_c].registrar_diagnostico(diag)
        print("Diagnóstico registrado!\n")

    # Sair
    elif opcao == "0":
        print("Saindo...")
        break

    else:
        print("Opção inválida!\n")
