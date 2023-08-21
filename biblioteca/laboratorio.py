class Laboratorio:

    quantidade_laboratorio_cadastrado_total = 0

    def __init__(self, nome: str, endereco: str, telefone_contato: str, cidade: str, estado: str) -> None:
        self.nome = nome
        self.endereco = endereco
        self.telefone_contato = telefone_contato
        self.cidade = cidade
        self.estado = estado
        Laboratorio.quantidade_laboratorio_cadastrado_total += 1