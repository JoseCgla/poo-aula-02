import os


# ============================
# Classes (Arquitetura e Herança)
# ============================

class Pessoa:
    def __init__(self, nome, idade, email):
        self.nome = nome
        self.idade = idade
        self.email = email

    def exibir_info(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, E-mail: {self.email}"


class Medico(Pessoa):
    def __init__(self, nome, idade, email, especialidade):
        super().__init__(nome, idade, email)
        self.especialidade = especialidade

    def atender(self):
        print(f"O médico {self.nome} está atendendo.")


class Paciente(Pessoa):
    def __init__(self, nome, idade, email, historico):
        super().__init__(nome, idade, email)
        self.historico = historico

    def marcar_consulta(self, medico, data):
        return Consulta(data, self, medico)


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


# ============================
# Funções Auxiliares (DRY)
# ============================

def coletar_dados_pessoa():
    """Função para evitar repetição de código na coleta de dados básicos."""
    nome = input("Nome: ")
    idade = input("Idade: ")
    email = input("E-mail: ")
    return nome, idade, email


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
    # Correção aplicada: Limpa a tela no Windows (nt) e em sistemas Unix (posix)
    os.system('cls' if os.name == 'nt' else 'clear')

    # 1 - Cadastrar Médico
    if opcao == "1":
        print("--- Cadastrar Médico ---")
        nome, idade, email = coletar_dados_pessoa()
        especialidade = input("Especialidade: ")
        novo_medico = Medico(nome, idade, email, especialidade)
        medicos.append(novo_medico)
        print("Médico cadastrado com sucesso!\n")

    # 2 - Cadastrar Paciente
    elif opcao == "2":
        print("--- Cadastrar Paciente ---")
        nome, idade, email = coletar_dados_pessoa()
        historico = input("Histórico médico: ")
        novo_paciente = Paciente(nome, idade, email, historico)
        pacientes.append(novo_paciente)
        print("Paciente cadastrado com sucesso!\n")

    # 3 - Listar Médicos
    elif opcao == "3":
        print("--- Lista de Médicos ---")
        if not medicos:
            print("Nenhum médico cadastrado.")
        else:
            for i, m in enumerate(medicos):
                print(f"{i} - {m.exibir_info()} | Esp: {m.especialidade}")
        print()

    # 4 - Listar Pacientes
    elif opcao == "4":
        print("--- Lista de Pacientes ---")
        if not pacientes:
            print("Nenhum paciente cadastrado.")
        else:
            for i, p in enumerate(pacientes):
                print(f"{i} - {p.exibir_info()} | Histórico: {p.historico}")
        print()

    # 5 - Marcar Consulta
    elif opcao == "5":
        print("--- Marcar Consulta ---")
        if not medicos or not pacientes:
            print("Cadastre médicos e pacientes primeiro!\n")
            continue

        print("Pacientes disponíveis:")
        for i, p in enumerate(pacientes):
            print(f"{i} - {p.exibir_info()}")
        idx_p = int(input("Escolha o paciente pelo número: "))
        paciente = pacientes[idx_p]

        print("\nMédicos disponíveis:")
        for i, m in enumerate(medicos):
            print(f"{i} - {m.exibir_info()} | Esp: {m.especialidade}")
        idx_m = int(input("Escolha o médico pelo número: "))
        medico = medicos[idx_m]

        data = input("Data da consulta (dd/mm/aaaa): ")
        consulta = paciente.marcar_consulta(medico, data)
        consultas.append(consulta)
        print("Consulta marcada com sucesso!\n")

    # 6 - Listar Consultas
    elif opcao == "6":
        print("--- Lista de Consultas ---")
        if not consultas:
            print("Nenhuma consulta agendada.")
        else:
            for c in consultas:
                c.exibir_consulta()
        print()

    # 7 - Registrar Diagnóstico
    elif opcao == "7":
        print("--- Registrar Diagnóstico ---")
        if not consultas:
            print("Nenhuma consulta disponível para registrar diagnóstico.\n")
            continue

        for i, c in enumerate(consultas):
            print(f"{i} - {c.data} | Paciente: {c.paciente.nome} | Médico: {c.medico.nome}")
        idx_c = int(input("Escolha a consulta pelo número: "))
        diag = input("Digite o diagnóstico: ")
        consultas[idx_c].registrar_diagnostico(diag)
        print("Diagnóstico registrado!\n")

    # 0 - Sair
    elif opcao == "0":
        print("Saindo do sistema...")
        break

    else:
        print("Opção inválida!\n")
