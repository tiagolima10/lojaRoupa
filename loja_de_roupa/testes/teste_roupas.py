import unittest
from loja_de_roupa.models import Roupas
from loja_de_roupa import database, app


class TesteRoupas(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///teste_roupa.db'
        with app.app_context():
            database.create_all()

    def teste_cadastro_roupa(self):
        with app.app_context():
            roupa = Roupas(nome_roupa='Camisola', categoria='Roupa de Dormir', tamanho='M', estoque=10, valor=29.99)
            database.session.add(roupa)
            database.session.commit()

            roupa_salva = Roupas.query.filter_by(nome_roupa='Camisola').first()
            self.assertIsNotNone(roupa_salva)
            self.assertEqual(roupa_salva.nome_roupa, 'Camisola')
            self.assertEqual(roupa_salva.categoria, 'Roupa de Dormir')
            self.assertEqual(roupa_salva.tamanho, 'M')
            self.assertEqual(roupa_salva.estoque, 10)
            self.assertEqual(roupa_salva.valor, 29.99)
            Roupas.query.filter_by(nome_roupa='Camisola').delete()
            database.session.commit()

    def test_remover_roupa(self):
        with app.app_context():
            roupa = Roupas(nome_roupa='Camisola', categoria='Roupa de Dormir', tamanho='M', estoque=10, valor=29.99)
            database.session.add(roupa)
            database.session.commit()

            roupa_salva = Roupas.query.filter_by(nome_roupa='Camisola').first()
            self.assertIsNotNone(roupa_salva)
            self.assertEqual(roupa_salva.nome_roupa, 'Camisola')
            self.assertEqual(roupa_salva.categoria, 'Roupa de Dormir')
            self.assertEqual(roupa_salva.tamanho, 'M')
            self.assertEqual(roupa_salva.estoque, 10)
            self.assertEqual(roupa_salva.valor, 29.99)
            Roupas.query.filter_by(nome_roupa='Camisola').delete()
            database.session.commit()

            roupa_deletada = Roupas.query.filter_by(nome_roupa='Camisola').first()
            self.assertIsNone(roupa_deletada)

    def tearDown(self):
        with app.app_context():
            database.session.remove()


if __name__ == '__main__':
    unittest.main()
