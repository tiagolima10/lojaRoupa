import unittest
from loja_de_roupa.models import Categoria
from loja_de_roupa import database, app


class TesteCategoria(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teste_categorias'
        with app.app_context():
            database.create_all()

    def test_criar_categoria(self):
        with app.app_context():
            categoria = Categoria(nome_categoria='Camisas')
            database.session.add(categoria)
            database.session.commit()

            categoria_salva = Categoria.query.filter_by(nome_categoria='Camisas').first()
            self.assertIsNotNone(categoria_salva)
            self.assertEqual(categoria_salva.nome_categoria, 'Camisas')
            Categoria.query.filter_by(nome_categoria='Camisas').delete()
            database.session.commit()

    def test_deletar_categoria(self):
        with app.app_context():
            categoria = Categoria(nome_categoria='Camisas')
            database.session.add(categoria)
            database.session.commit()

            categoria_deletada = Categoria.query.filter_by(nome_categoria='Camisas').delete()
            database.session.commit()

            categoria_deletada2 = Categoria.query.filter_by(nome_categoria='Camisas').first()
            self.assertIsNone(categoria_deletada2)

    def tearDown(self):
        with app.app_context():
            database.session.remove()


if __name__ == '__main__':
    unittest.main()
