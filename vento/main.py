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
import random
from carta import CartaTesouro, CartaEnchente, CartaSacoAreia, CartaAlagamento, CartaHelicoptero
from jogador import Explorador, Navegador, Piloto, Engenheiro, Mensageiro, Mergulhador
from artefato import Artefato

class Terreno:
    class PORTAO_COBRE:
        nome = "🟢 Portão de Cobre   "
        visual = '\u2fa8C'
        contagem = 0
        jogadores = ['explorador']

    class PISTA_POUSO:
        nome = "   Pista de Pouso  🚁"
        visual = '\U0001f681 '
        contagem = 0
        jogadores = ['piloto']

    class PORTAO_BRONZE:
        nome = "🔴 Portão de Bronze🌊"
        visual = '\u2fa8 B'
        contagem = 0
        tesouro = "TESOURO AGUA"
        jogadores = ['engenheiro']

    class PALACIO_CORAL:
        nome = "  Palácio de Coral🌊"
        visual = '\U0001f3f0 💧'
        contagem = 0
        tesouro = "TESOURO AGUA"

    class VALE_TENEBROSO:
        nome = "   Vale Tenebroso   "
        visual = '\U0001f332 \U0001f47b'
        contagem = 0

    class PORTAO_OURO:
        nome = "   Portão de Ouro   "
        visual = '\u2fa8 O'
        contagem = 0
        jogadores = ['navegador']

    class PORTAO_PRATA:
        nome = "◐  Portão de Prata  "
        visual = '\u2fa8 P'
        contagem = 0
        jogadores = ['mensageiro']

    class PORTAO_FERRO:
        nome = "⚫ Portão de Ferro   "
        visual = '\u2fa8 F'
        contagem = 0
        jogadores = ['mergulhador']

    class ATALAIA:
        nome = "       Atalaia      "
        visual = '\u265c '
        contagem = 0

    class JARDIM_SUSSUROS:
        nome = "Jardim dos Sussurros🍃"
        visual = '\u2698 '
        contagem = 0
        tesouro = "TESOURO VENTO"

    class JARDIM_UIVOS:
        nome = "  Jardim dos Uivos🍃"
        visual = '\u2698 \U0001f43a'
        contagem = 0
        tesouro = "TESOURO VENTO"

    class TEMPLO_SOL:
        nome = "    Templo do Sol 🌎"
        visual = "\uf90a \u263c"
        contagem = 0
        tesouro = "TESOURO TERRA"

    class TEMPLO_LUA:
        nome = "   Templo da Lua  🌎"
        visual = "\uf90a \u263e"
        contagem = 0
        tesouro = "TESOURO TERRA"

    class CAVERNA_LAVA:
        nome = "   Caverna de Lava 🔥"
        visual = '🏔 ️ \U0001f525'
        contagem = 0
        tesouro = "TESOURO FOGO"

    class CAVERNA_SOMBRAS:
        nome = "Caverna das Sombras🔥"
        visual = "🏔 ️ 🏔 ️"
        contagem = 0
        tesouro = "TESOURO FOGO"

    class OBSERVATORIO:
        nome = "    Observatório    "
        visual = "\u265c\U0001f52d"
        contagem = 0

    class PANTANO_BRUMAS:
        nome = "  Pântano de Brumas "
        visual = "🏞  ️\u2601"
        contagem = 0

    class ROCHA_FANTASMA:
        nome = "   Rocha Fantasma   "
        visual = "🪨 👻"
        contagem = 0

    class PALACIO_MARES:
        nome = " Palácio dos Mares  "
        visual = "\U0001f3f0 🌊"
        contagem = 0

    class PENEDO_BALDIO:
        nome = "    Penedo Baldio   "
        visual = "ㄱ "
        contagem = 0

    class BOSQUE_CARMESIM:
        nome = "   Bosque Carmesim  "
        visual = "🌳 ❤️"
        contagem = 0

    class DUNAS_ENGANO:
        nome = "   Dunas do Engano  "
        visual = "🫓 🦴"
        contagem = 0

    class PONTE_SUSPENSA:
        nome = "   Ponte Suspensa   "
        visual = "🌉"
        contagem = 0

    class LAGOA_PERDIDA:
        nome = "    Lagoa Perdida   "
        visual = "🏞 🏞"
        contagem = 0


def criar_artefatos():
    lista_de_artefatos = []

    # Criando os objetos da classe Artefato e adicionando à lista
    artefato1 = Artefato("   TESOURO FOGO  🔥", "")
    artefato2 = Artefato("   TESOURO ÁGUA  🌊", "")
    artefato3 = Artefato("   TESOURO VENTO  🍃", "")
    artefato4 = Artefato("   TESOURO TERRA  🌎", "")

    lista_de_artefatos.append(artefato1)
    lista_de_artefatos.append(artefato2)
    lista_de_artefatos.append(artefato3)
    lista_de_artefatos.append(artefato4)

    return lista_de_artefatos


def setup(numero_jogadores):
    ilha = [
        ["                    ", "                    ", "", "", "                    ", "                    "],
        ["                    ", "", "", "", "", "                    "],
        ["", "", "", "", "", ""],
        ["", "", "", "", "", ""],
        ["                    ", "", "", "", "", "                    "],
        ["                    ", "                    ", "", "", "                    ", "                    "],
    ]

    # definir aqui quais os terrenos em que se pode pegar o tesouro correspondente
    terrenos_terra = []
    terrenos_fogo = []
    terrenos_vento = []
    terrenos_oceano = []

    jogador = ['explorador', 'mergulhador', 'piloto', 'navegador', 'engenheiro', 'mensageiro']
    tesouros = criar_artefatos()
    # tesouros = ["    TESOURO FOGO    ", "    TESOURO ÁGUA    ", "    TESOURO VENTO   ", "    TESOURO TERRA   "]
    baralho_alagamento = []
    baralho_tesouros = []
    baralho_descarte_tesouro = []
    baralho_descarte_alagamento = []
    jogadores = []
    tesouros_coletados = 0

    ter = [Terreno.PISTA_POUSO.nome, Terreno.PORTAO_COBRE.nome, Terreno.PORTAO_BRONZE.nome,
           Terreno.PALACIO_CORAL.nome, Terreno.VALE_TENEBROSO.nome, Terreno.PORTAO_OURO.nome,
           Terreno.PORTAO_PRATA.nome, Terreno.PORTAO_FERRO.nome, Terreno.ATALAIA.nome,
           Terreno.JARDIM_SUSSUROS.nome, Terreno.JARDIM_UIVOS.nome, Terreno.TEMPLO_SOL.nome,
           Terreno.TEMPLO_LUA.nome, Terreno.CAVERNA_LAVA.nome, Terreno.CAVERNA_SOMBRAS.nome,
           Terreno.OBSERVATORIO.nome, Terreno.PANTANO_BRUMAS.nome, Terreno.ROCHA_FANTASMA.nome,
           Terreno.PALACIO_MARES.nome, Terreno.PENEDO_BALDIO.nome, Terreno.BOSQUE_CARMESIM.nome,
           Terreno.DUNAS_ENGANO.nome, Terreno.PONTE_SUSPENSA.nome, Terreno.LAGOA_PERDIDA.nome]

    # Adicionando terrenos aleatóriamente na ilha

    incluir_terrenos = ter.copy()
    for linha in range(len(ilha)):
        for coluna in range(len(ilha[linha])):
            if ilha[linha][coluna] == "":
                elemento = random.choice(incluir_terrenos)
                ilha[linha][coluna] = elemento
                incluir_terrenos.remove(elemento)
    # **********************************************************************************

    lista_tesouros = tesouros.copy()
    # acrescentando aleatoriamente os tesouros nas extremidades do ilha
    tesouro = random.choice(lista_tesouros)
    ilha[0][0] = tesouro.nome
    lista_tesouros.remove(tesouro)

    tesouro = random.choice(lista_tesouros)
    ilha[0][5] = tesouro.nome
    lista_tesouros.remove(tesouro)

    tesouro = random.choice(lista_tesouros)
    ilha[5][0] = tesouro.nome
    lista_tesouros.remove(tesouro)

    tesouro = random.choice(lista_tesouros)
    ilha[5][5] = tesouro.nome
    lista_tesouros.remove(tesouro)

    # **************************************************************************************************

    # Acrescentando as mãos dos jogdores no ilha
    nomes_jogadores = ["Mão de Jogador 1", "Mão de Jogador 2", "Mão de Jogador 3", "Mão de Jogador 4"]
    for nome in nomes_jogadores:
        nova_linha = ["|" + " " * 18 + "|"]
        for _ in range(5):
            nova_linha.append("|" + " " * 18 + "|")
        ilha.append(nova_linha)

    for i, nome in enumerate(nomes_jogadores, start=len(ilha) - 4):
        ilha[i][0] = "|" + nome.center(18) + "|"

        # **********************************************************************************************

        # acrescentar baralho de alagamento
    cartas_alagamento = ter.copy()
    for i in range(len(ter)):
        elemento = random.choice(cartas_alagamento)
        baralho_alagamento.append(elemento)
        cartas_alagamento.remove(elemento)
        # ******************************************************************************

        # acrescentar baralho de tesouros
    for tesouro in tesouros:
        for _ in range(5):
            baralho_tesouros.append(CartaTesouro(tesouro.nome))
        # ******************************************************************************

        # acrescentar 3 fugas de helicoptero no baralho de tesouro
    for _ in range(3):
        baralho_tesouros.append(CartaHelicoptero())
    # ****************************************************************************

    # Acrescentar 2 cartas saco de areia no baralho de tesouro
    for _ in range(2):
        baralho_tesouros.append(CartaSacoAreia())
    # *************************************************************************************

    # baralhar cartas de tesouro
    random.shuffle(baralho_tesouros)
    # ********************************************************

    # gerar aleatoriamente os aventureiros dependendo no numero de jogadores
    for jogador in random.sample(jogador, numero_jogadores):
        if jogador == 'explorador':
            jogadores.append(Explorador())
        elif jogador == 'mergulhador':
            jogadores.append(Mergulhador())
        elif jogador == 'navegador':
            jogadores.append(Navegador())
        elif jogador == 'piloto':
            jogadores.append(Piloto())
        elif jogador == 'engenheiro':
            jogadores.append(Engenheiro())
        elif jogador == 'mensageiro':
            jogadores.append(Mensageiro())
        else:
            raise ValueError('Aventureiro sinistro')
            # *****************************************************************************

            # distribuir 2 cartas tesouro a cada Jogador
    linha = 5
    for jogador in jogadores:
        coluna = 1
        linha += 1
        while jogador.numero_mao() < 2:
            # compra carta do baralho de tesouros
            carta_tesouro = baralho_tesouros.pop()
            jogador.comprar_carta(carta_tesouro)
            ilha[linha][coluna] = str(carta_tesouro)
            ilha[linha][0] = jogador.__repr__()
            coluna += 1
            #************************************************************************

    # adiciona enchente agora apenas
    for _ in range(3):
        baralho_tesouros.append(CartaEnchente())
    #**************************************************************************

    # baralha outra vez mas com as cartas de enchente
    random.shuffle(baralho_tesouros)
#*******************************************************************************

    # Adicionando uma linha com 6 colunas abaixo do ilha
    ilha.extend([
        ["|Baralho Tesouro" + str(len(baralho_tesouros)).center(5), "| Baralho Alagamento " + str(len(baralho_alagamento)).center(1) + " ", "  Descarte Tesouro"+ str(len(baralho_descarte_tesouro)).center(5),
         "  Descarte Alagamento " + str(len(baralho_descarte_alagamento)) + "  ", " Nível de Enchente = 1".center(16) + " "]
    ])

    larguras_colunas = [2, 4, 6, 6, 6, 6, 4, 2]

    while True:
        for linha in ilha:
            linha_formatada = [("|" + celula + " " * (20 - len(celula)) + "|") for celula in linha]

            linha_para_imprimir = ""
            for i, largura in enumerate(larguras_colunas):
                linha_para_imprimir += "|" + "|".join(linha_formatada[:largura]) + "|"
                linha_formatada = linha_formatada[largura:]

            print(linha_para_imprimir)
            print("-" * (sum(larguras_colunas) * 21 + 1))  # Ajusta a linha horizontal conforme o número de colunas

        mover_jogador = input("Para mover um jogador, digite 'M'. Para sair, digite 'Q': ").upper()

        if mover_jogador == 'Q':
            print("Encerrando o programa...")
            break

        elif mover_jogador == 'M':
            while True:
                try:
                    linha = int(input("Digite o número da linha (de 0 a 5): "))
                    coluna = int(input("Digite o número da coluna (de 0 a 5): "))

                    if 0 <= linha <= 5 and 0 <= coluna <= 5:
                        print(f"Jogador movido para a linha {linha} e coluna {coluna}.")
                        break
                    else:
                        print("Por favor, insira valores válidos para linha e coluna (de 0 a 5).")
                except ValueError:
                    print("Por favor, insira números inteiros para linha e coluna.")


setup(numero_jogadores=4)