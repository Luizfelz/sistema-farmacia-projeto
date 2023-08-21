from biblioteca.laboratorio import Laboratorio

class Medicamento:

    def __init__(self, nome: str, principal_composto: str, laboratorio: Laboratorio, descricao: str, receita: bool, valor_medicamento: float) -> None:
        self.nome = nome
        self.principal_composto = principal_composto
        self.laboratorio = laboratorio
        self.descricao = descricao
        self.receita = receita
        self.valor_medicamento = valor_medicamento
      
    def __rep__(self) -> str:
        representacao = f'Nome: {self.nome}\n'
        representacao += f'Principal composto: {self.principal_composto}\n'
        representacao += f'Laboratório: {self.laboratorio.nome}\n'
        representacao += f'Descrição: {self.descricao}\n'
        receita = 'sim' if self.receita else 'não'
        representacao += f'Receita: {receita}\n'
        representacao += f'Valor do medicamento: R$ {self.valor_medicamento}'
        return representacao


class MedicamentoFitoterapico(Medicamento):

    quantidade_medicamento_fitoterapico = 0
    cadastro_medicamento_fitoterapico_dict = {}

    def __init__(self, nome: str, principal_composto: str, laboratorio: Laboratorio, descricao: str, receita: bool, valor_medicamento: float) -> None:
        self.tipo = 'fitoterápico'
        super().__init__(nome, principal_composto, laboratorio, descricao, receita, valor_medicamento)
        MedicamentoFitoterapico.quantidade_medicamento_fitoterapico += 1

    def __repr__(self) -> str:
        representacao = f'Nome: {self.nome}\n'
        representacao += f'Principal composto: {self.principal_composto}\n'
        representacao += f'Laboratório: {self.laboratorio.nome}\n'
        representacao += f'Descrição: {self.descricao}\n'
        representacao += f'Tipo: {self.tipo}\n'
        receita = 'sim' if self.receita else 'não'
        representacao += f'Receita: {receita}\n'
        representacao += f'Valor do medicamento: R$ {self.valor_medicamento}'
        return representacao


class MedicamentoQuimioterapico(Medicamento):

    quantidade_medicamento_quimioterapico = 0
    cadastro_medicamento_quimioterapico_dict = {}

    def __init__(self, nome: str, principal_composto: str, laboratorio: Laboratorio, descricao: str, receita: bool, valor_medicamento: float) -> None:
        self.tipo = 'quimioterápico'
        super().__init__(nome, principal_composto, laboratorio, descricao, receita, valor_medicamento)
        MedicamentoQuimioterapico.quantidade_medicamento_quimioterapico += 1
    
    def __repr__(self) -> str:
        representacao = f'Nome: {self.nome}\n'
        representacao += f'Principal composto: {self.principal_composto}\n'
        representacao += f'Laboratório: {self.laboratorio.nome}\n'
        representacao += f'Descrição: {self.descricao}\n'
        representacao += f'Tipo: {self.tipo}\n'
        receita = 'sim' if self.receita else 'não'
        representacao += f'Receita: {receita}\n'
        representacao += f'Valor do medicamento: R$ {self.valor_medicamento}'
        return representacao