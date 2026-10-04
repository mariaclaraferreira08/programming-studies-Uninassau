from datetime import date

# --- COMPOSIÇÃO 1: Veiculo -> Manutencao ---

class Manutencao:
    def __init__(self, data, tipo_servico, custo):
        self.data = data
        self.tipo_servico = tipo_servico
        self.custo = custo
    
    def exibir(self):
        print(f"Manutenção em {self.data}: {self.tipo_servico} - R$ {self.custo}")

class Veiculo:
    def __init__(self, placa, modelo, ano, valor_diaria):
        self.placa = placa
        self.modelo = modelo
        self.ano = ano
        self.valor_diaria = valor_diaria
        self.manutencoes = [] # Composição: Veículo CONTÉM manutenções
        self.status = "disponivel"

    # O Veículo é responsável por CRIAR a manutenção
    def adicionar_manutencao(self, data, tipo_servico, custo):
        nova_manut = Manutencao(data, tipo_servico, custo)
        self.manutencoes.append(nova_manut)
        return nova_manut
    
    def calcular_custo_manutencoes(self):
        return sum(m.custo for m in self.manutencoes)

# --- COMPOSIÇÃO 2: Contrato -> Condutor ---

class Condutor:
    def __init__(self, nome, numero_cnh):
        self.nome = nome
        self.numero_cnh = numero_cnh
    
    def validar_cnh(self):
        return len(self.numero_cnh) == 11

class ContratoLocacao:
    def __init__(self, cliente, veiculo, data_inicio, data_fim):
        self.cliente = cliente  # Associação
        self.veiculo = veiculo  # Associação
        self.data_inicio = data_inicio
        self.data_fim = data_fim
        self.status = "ativo"
        self.condutor = None # Será criado via composição

    # Composição: Contrato CRIA o condutor, condutor não existe fora
    def definir_condutor(self, nome, numero_cnh):
        self.condutor = Condutor(nome, numero_cnh)
        return self.condutor

    def finalizar(self):
        self.status = "finalizado"
        self.veiculo.status = "disponivel"

# --- TESTE ---
veiculo1 = Veiculo("PIA2J28", "Honda CG 160", 2023, 50.0)
veiculo1.adicionar_manutencao(date(2026, 9, 10), "Troca de óleo", 80.0)
veiculo1.adicionar_manutencao(date(2026, 9, 20), "Freio", 120.0)

print(f"Veículo {veiculo1.modelo} tem {len(veiculo1.manutencoes)} manutenções")
print(f"Custo total: R$ {veiculo1.calcular_custo_manutencoes()}")

contrato = ContratoLocacao("João Silva", veiculo1, date(2026, 9, 28), date(2026, 9, 30))
contrato.definir_condutor("João Silva", "12345678901")
print(f"\nContrato criado para {contrato.cliente} com condutor {contrato.condutor.nome}")
# Se deletar o contrato, o condutor some junto -> Composição