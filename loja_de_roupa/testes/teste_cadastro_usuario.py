import unittest
from loja_de_roupa.models import Usuario
from loja_de_roupa import database, app


class TesteCadastroUsuario(unittest.TestCase):
    def setUp(self):
        app.config['TESTING'] = True
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///testeUsuario.db'
        with app.app_context():
            database.create_all()

    def teste_criar_usuario(self):
        with app.app_context():
            usuario = Usuario(usuario='tiagolima', email='tiagolima@gmail.com', senha='senha123')
            database.session.add(usuario)
            database.session.commit()

            usuario_salvo = Usuario.query.filter_by(usuario='tiagolima').first()
            self.assertIsNotNone(usuario_salvo)
            self.assertEqual(usuario_salvo.usuario, 'tiagolima')
            self.assertEqual(usuario_salvo.email, 'tiagolima@gmail.com')
            self.assertEqual(usuario_salvo.senha, 'senha123')
            Usuario.query.filter_by(usuario='tiagolima').delete()
            database.session.commit()

    def teste_criar_usuario2(self):
        with app.app_context():
            usuario = Usuario(usuario='tiagoteste', email='tiagoteste@gmail.com', senha='senha789')
            database.session.add(usuario)
            database.session.commit()

            usuario_salvo = Usuario.query.filter_by(usuario='tiagoteste').first()
            self.assertIsNotNone(usuario_salvo)
            self.assertEqual(usuario_salvo.usuario, 'tiagoteste')
            self.assertEqual(usuario_salvo.email, 'tiagoteste@gmail.com')
            self.assertEqual(usuario_salvo.senha, 'senha789')
            Usuario.query.filter_by(usuario='tiagoteste').delete()
            database.session.commit()

    def tearDown(self):
        with app.app_context():
            database.session.remove()


if __name__ == '__main__':
    unittest.main()
