class Doce:
    def _init_(self, nome, marca, sabor, preco):
        self.nome = nome
        self.marca = marca
        self.sabor = sabor
        self.preco = preco

    def preco_doce(self):
        return f"O preço do {self.nome} é R${self.preco:.2f}"


class Descricao(Doce):
    def _init_(self, nome, marca, sabor, preco, descricao):
        super()._init_(nome, marca, sabor, preco)
        self.descricao = descricao

    def vender(self):
        return 'Venda Concluída!'

    def mostrar_descricao(self):
        return f"{self.nome}\n Marca: {self.marca}\n Sabor: {self.sabor} - {self.descricao}"


def mostrar_precos():
    for doce in doces:
        print(doce.preco_doce())
    

def mostrar_descricao():
    for doce in doces_com_descricao:
        print(doce.mostrar_descricao())


doces = [
    Doce("Chocolate", "Nestlé", "Ao Leite", 5.00),
    Doce("Bala", "Trident", "Hortelã", 0.50)
]

doces_com_descricao = [
    Descricao("Chocolate", "Nestlé", "Ao Leite", 5.00, "Um delicioso chocolate ao leite."),
    Descricao("Bala", "Trident", "Hortelã", 0.50, "Uma bala refrescante de hortelã.")
]