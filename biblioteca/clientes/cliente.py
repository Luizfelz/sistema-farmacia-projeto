class Cliente:

    def __init__(self, nome : str, data_nascimento : str, cpf : str) -> None:
        self._nome = nome
        self.data_nascimento = data_nascimento
        self.cpf = cpf

    def __repr__(self) -> str:
        representacao = f'Nome: {self._nome}\n'
        representacao += f'CPF: {self.cpf}\n'
        representacao += f'Data de Nascimento: {self.data_nascimento.day}/{self.data_nascimento.month}/{self.data_nascimento.year}'
        return representacao

    @property
    def nome(self) -> str:
        return self._nome

    @nome.setter
    def nome(self, nome) -> None:
        self._nome = nome