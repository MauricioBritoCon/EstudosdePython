class Pessoa:
    '''Não consigo entender a função do init e do self, o código esta funcionando mas gostaria de saber o porque'''
    def __init__(self, nome, idade, comendo=False, falando=False):
        self.idade = idade
        self.nome = nome
        self.comendo = comendo
        self.falando = falando
        print(nome, idade)
        pass

    def comer(self, comida):
        if self.comendo:
            print(f'{self.nome} já esta comendo.')
            return
        print(f'{self.nome} está comendo {comida}.')
        self.comendo = True

    def pararComer(self):
        if not self.comendo:
            print(f'{self.nome} não está comendo.')
            return
        print(f'{self.nome} parou de comer')
        self.comendo = False
