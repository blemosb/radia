class Jogador:
    def __init__(self):
        self.mao = []

    def comprar_carta(self, carta):
        self.mao.append(carta)

    def numero_mao(self):
        return len(self.mao)

    def mover(self):
        pass

    def drenar(self):
        pass

    def doar_carta(self):
        pass

    def obter_tesouro(self):
        pass

class Explorador(Jogador):
    def __init__(self):
        self.terreno_inicial = "PORTAO_OURO"
        super().__init__()

    def especial(self):
        pass

    def __repr__(self):
        return "*****EXPLORADOR****🟢"

class Mergulhador(Jogador):
    def __init__(self):
        self.terreno_inicial = "PORTAO_OURO"
        super().__init__()

    def especial(self):
        pass

    def __repr__(self):
        return "****MERGULHADOR***⚫"

class Navegador(Jogador):
    def __init__(self):
        self.terreno_inicial = "PORTAO_OURO"
        super().__init__()

    def especial(self):
        pass

    def __repr__(self):
        return "*****NAVEGADOR*****🟡"

class Piloto(Jogador):
    def __init__(self):
        self.terreno_inicial = "PORTAO_OURO"
        super().__init__()

    def especial(self):
        pass

    def __repr__(self):
        return "*******PILOTO******🔵"

class Engenheiro(Jogador):
    def __init__(self):
        self.terreno_inicial = "PORTAO_OURO"
        super().__init__()

    def especial(self):
        pass

    def __repr__(self):
        return "*****ENGENHEIRO****🔴"

class Mensageiro(Jogador):
    def __init__(self):
        self.terreno_inicial = "PORTAO_OURO"
        super().__init__()

    def especial(self):
        pass

    def __repr__(self):
        return "*****MENSAGEIRO***◐"


