"""Questão prática 1 - POO: Sistema de gerenciamento de uma escola.

Relações:
- Escola -> SalaDeAula: COMPOSIÇÃO
- Escola <-> Professor: ASSOCIAÇÃO
- Aluno -> Endereco: AGREGAÇÃO
"""


# --- CLASSES FOLHA (sem dependência) ---

class Endereco:
    def __init__(self, logradouro, cidade, estado, cep):
        self.logradouro = logradouro
        self.cidade = cidade
        self.estado = estado
        self.cep = cep

    def formatar_endereco(self):
        return f"{self.logradouro}, {self.cidade}/{self.estado} - {self.cep}"

class SalaDeAula:
    def __init__(self, numero, capacidade):
        self.numero = numero
        self.capacidade = capacidade

    def exibir_info(self):
        print(f"Sala {self.numero} - Capacidade: {self.capacidade}")

class Professor:
    def __init__(self, nome, matricula, especialidade):
        self.nome = nome
        self.matricula = matricula
        self.especialidade = especialidade
        self.escolas = []  # Associação

    def vincular_escola(self, escola):
        self.escolas.append(escola)

# --- CLASSES TODO ---

class Escola:
    def __init__(self, nome, codigo):
        self.nome = nome
        self.codigo = codigo
        self.salas = []  # COMPOSIÇÃO: Escola cria e controla as salas
        self.professores = [] # ASSOCIAÇÃO

    # COMPOSIÇÃO: A Escola é responsável por criar a sala
    def criar_sala(self, numero, capacidade):
        nova_sala = SalaDeAula(numero, capacidade)
        self.salas.append(nova_sala)
        return nova_sala

    # ASSOCIAÇÃO: Só vincula, não cria
    def adicionar_professor(self, professor: Professor):
        self.professores.append(professor)
        professor.vincular_escola(self)

    def listar_salas(self):
        for sala in self.salas:
            sala.exibir_info()

class Aluno:
    def __init__(self, nome, matricula, endereco: Endereco):
        self.nome = nome
        self.matricula = matricula
        # AGREGAÇÃO: Recebe um objeto Endereco já existente
        self.endereco = endereco

# --- TESTANDO ---

# 1. Agregação: Endereço existe independente
end1 = Endereco("Rua Piauí, 100", "Bom Princípio", "PI", "64225-000")

# 2. Aluno agrega o endereço
aluno1 = Aluno("João Silva", "2026A001", end1)
print(aluno1.endereco.formatar_endereco())

# 3. Composição: Escola cria suas próprias salas
escola1 = Escola("Escola Modelo", "ESC001")
escola1.criar_sala("101A", 40)
escola1.criar_sala("102B", 35)

# 4. Associação: Professor existe independente da escola
prof1 = Professor("Maria Souza", "PROF01", "Coding POO")
escola1.adicionar_professor(prof1)

print(f"\nEscola: {escola1.nome}")
escola1.listar_salas()
print(f"Professor {prof1.nome} leciona em {len(prof1.escolas)} escola(s)")

# Se a escola for deletada, as salas somem junto (Composição)
# Mas o endereço e o professor continuam existindo (Agregação e Associação)