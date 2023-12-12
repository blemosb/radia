import unittest
from vento.main import set

#esperado = []


class MyTestCase(unittest.TestCase):
    def test_lista_tesouros_vazia_apos_distribuicao(self):
        # Executar a função setup para distribuir os tesouros
        setup(numero_jogadores=4)

        # Verificar se lista_tesouros está vazia após a distribuição
        #  self.assertEqual(len(lista_tesouros), 0, "A lista de tesouros não está vazia após a distribuição")


if __name__ == '__main__':
    unittest.main()
