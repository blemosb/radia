# radia.vento.main.py


"""Página de entrada do jogo Ilha Proibida.

LOG - http://bit.ly/Dev_Agile_23

.. codeauthor:: Glaucio de Sousa Santos <glaucio75@ufrj.br>
.. codeauthor:: Bruno Lemos Barroso <blemosb@gmail.com>
.. codeauthor:: Filipe Tanus Marçal <filipetanusmarcal2004@gmail.com>
.. codeauthor:: José André Bernardo <josebernardo@tecnico.ulisboa.pt>

Equipe Vento
Changelog
---------
.. versionadded::    23.11
    Classes Ilha, Terreno, Peao (07).
    
.. versionadded::    23.09
    Versão Inicial (26).

|   **Open Source Notification:** This file is part of open source program **Ilha Proibida**
|   **Copyright © 2023  Carlo Oliveira** <carlo@nce.ufrj.br>,
|   **SPDX-License-Identifier:** `GNU General Public License v3.0 or later <http://is.gd/3Udt>`_.
|   `Labase <http://labase.selfip.org/>`_ - `NCE <https://portal.nce.ufrj.br>`_ - `UFRJ <https://ufrj.br/>`_.
"""

from _spy.vitollino.main import Cena, Elemento, STYLE
from collections import namedtuple
Ter = namedtuple("Ter", "nome imagem tafv")
LADO = 90
STYLE["width"] = 800
STYLE["height"] = "600px"
IMAGEM = "https://imgur.com/gVHmY2v.jpg"
PORTAO_BRONZE = "https://imgur.com/BL6lB7H.jpg"
PALACIO_CORAL = "https://imgur.com/tLDbzd2.jpg"
PAWN = "https://imgur.com/zO3kiRp.png"
TAFVS = "KXZXTei LK4p1xG rUNsKEH qp5Zbn8".split()
NOMES = ("PISTA_POUSO PORTAO_BRONZE PALACIO_CORAL VALE_TENEBROSO PORTAO_OURO PORTAO_PRATA PORTAO_COBRE "
"PORTAO_FERRO ATALAIA JARDIM_SUSSUROS JARDIM_UIVOS TEMPLO_SOL "
"TEMPLO_LUA CAVERNA_LAVA CAVERNA_SOMBRAS OBSERVATORIO PANTANO_BRUMAS ROCHA_FANTASMA "
"PALACIO_MARES PENEDO_BALDIO BOSQUE_CARMESIM DUNAS_ENGANO PONTE_SUSPENSA LAGOA_PERDIDA").split()
LINKS = ("CU3TLYh BL6lB7H tLDbzd2 OZE1myn J6ow4jR v0g7eGm 45aU3nf "
"yKU6ngz sdJ4W5O pjVcyoy ZNuPWqZ O0OSVFt "
"J160xpm 2j1IAyf b4xtltc E9MflTP NDioDZg TCmLjeT "
"rYxQaTa MvN7kTU Uni02EK cG5UYCf GC8V8CQ 7o1qq10").split()


class IlhaProibida:
    """ Representa a classe principal do Jogo.
    
    Terrenos 
        Locais onde os peões podem ficar.
        
    """

    def __init__(self):
        self.oceano = Cena(IMAGEM).vai()
        self.terrenos = []
        self.monta_tabuleiro_oceano()
        self.peao = Peao(self)
        self.peao.mover(self.terrenos[0])

    def monta_tabuleiro_oceano(self):
        """ Montar o tabuleiro em forma de diamante.
        
        """
        from random import shuffle
        tafv = [None]*16+TAFVS*2
        info_terrenos = it = [Ter(nome=NOMES.pop(0), imagem=LINKS.pop(0),
        tafv=tafv.pop()) for _ in range(24)]
        # como introduzir os elementos no info_terrenos?
        # Agora info_terrenos é uma lista de Ter -> Como criar?
        #info_terrenos = [PORTAO_BRONZE, PALACIO_CORAL, PORTAO_BRONZE, PALACIO_CORAL] * 9
        shuffle(info_terrenos)
        # Cada terreno realmente criado "puxa" um terreno da lista de "Ter's
        self.terrenos = [Terreno(cena=self.oceano, posy=px // 6,
                                 posx=((px % 6) + int(abs(2.5 - px // 6))), local=it.pop(0), ilha=self)
                         for px in range(36) if px % 6 < 6 - int(abs(2.5 - px // 6)) * 2]
        self.terrenos[4].afundar()

    def desocupa_e_vai_para(self, terreno_destino):
        self.peao.move(terreno_destino)

    def direita(self, terreno):
        """ Move o peão para a direita.
        
        :param terreno: O terreno onde está o peão
        :return: O terreno onde o peão vai
        """
        aqui = self.terrenos.index(terreno)
        return self.terrenos[aqui + 1]


class Terreno:
    """ Local onde um peão pode ficar.

    :param local: Imagem do terreno
    :param posx: Coordenada x do terreno.
    :param posy: Coordenada y do terreno.
    :param cena: Cena do local.
    :param ilha: Referência ao tabuleiro.
    """

    def __init__(self, local: Ter, posx, posy, cena, ilha):
        #img = local.imagem
        #self.local = Elemento(img
        img = f"https://imgur.com/{local.imagem}.jpg"
        self.local = Elemento(img, x=posx * LADO + 10, y=posy * LADO + 50, w=LADO-5, h=LADO-5,
                              cena=cena)
        estilo = {'background-color': 'slategray', 'color': 'white'}
        letreiro = Elemento("", w=100, h=20, style=estilo, cena=self.local)
        letreiro.elt.text = local.nome
        img = f"https://imgur.com/{local.tafv}.png" if local.tafv else ""
        
        tafv = Elemento(img, w=40, h=50, x=0, tit=img, y=50, cena=self.local)
        #tafv = Elemento(local.tafv, ....)
        self.peao, self.ilha = None, ilha
        self.posx, self.posy = posx, posy
        self.local.vai = self.vai
        self.afunda = False

    def vai(self, _=0):
        self.ilha.peao.mover(self)

    def afundar(self):
        self.afunda = True
        self.local.o = 0.2

    def desocupa_e_vai_para(self, terreno_destino):
        def contiguos(origem, destino):
            if not origem:
                return True
            from operator import xor
            return xor(abs(origem.posx - destino.posx) == 1,
            abs(origem.posy - destino.posy) == 1) and not destino.afunda

        peao_pode_ir = contiguos(self, terreno_destino)
        # executar o movimento do peão agora que foi autorizado pelo pode ir
        self.peao.move(terreno_destino) if peao_pode_ir else None

    def ocupa(self, peao):
        self.peao = peao
        peao.mover(self.posx, self)


class Peao:
    """ Marcador usado para definir a posição do jogador nos terrenos.
        
        :param ilha: Referência ao tabuleiro.
    """

    def __init__(self, ilha):
        """
        """
        self.peao = Elemento(PAWN, x=10, y=15, w=LADO-20, h=LADO-20,
                             cena=ilha.oceano)
        self.terreno = ilha  # era None, mas o peão agora nasce na ilha
        self.ilha = ilha

    def move(self, terreno):  # Corrigir: não está condizente!
        self.terreno = terreno
        terreno.peao = self
        self.peao.entra(terreno.local)
        #self.peao.x, self.peao.y = terreno.posx * LADO + 10, terreno.posy * LADO + 50

    def mover(self, terreno_destino):
        self.terreno.desocupa_e_vai_para(terreno_destino)


if __name__ == "__main__":
    # IlhaProibida()
    IlhaProibida()
    ata = Ter(nome="atalaia", imagem='imgur/xyz', tafv=None)
    #ata.nome = "pista"
    #print(ata.nome, ata.tafv)
    # print([(px, int(abs(2.5-px//6))) for px in range(36)])
