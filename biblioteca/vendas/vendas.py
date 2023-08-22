class Vendas:

    def __init__(self, data_venda: str, hora_venda: str, produtos_vendidos: str, cpf_cliente: str, valor_total: float) -> None:
        self.data_venda = data_venda
        self.hora_venda = hora_venda
        self.produtos_vendidos = produtos_vendidos
        self.cpf_cliente = cpf_cliente
        self._valor_total = valor_total

    @property
    def valor_total(self) -> float:
        return self._valor_total