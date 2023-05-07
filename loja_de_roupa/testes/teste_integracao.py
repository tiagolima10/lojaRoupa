from teste_roupas import *
from teste_categorias import *
from teste_cadastro_usuario import *
from test_login import *


def suite_teste():
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(TesteRoupas))
    test_suite.addTest(unittest.makeSuite(TesteCadastroUsuario))
    test_suite.addTest(unittest.makeSuite(TesteCategoria))
    test_suite.addTest(unittest.makeSuite(TesteLogin))
    return test_suite


if __name__ == '__main__':
    runner = unittest.TextTestRunner()
    runner.run(suite_teste())
