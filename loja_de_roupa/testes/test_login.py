import unittest
from loja_de_roupa.routers import Usuario
from loja_de_roupa import database, app


class TesteLogin(unittest.TestCase):

    def test_login_sucesso(self):
        with app.app_context():
            usuario = Usuario(usuario='tiagolima', email='tiagolima@gmail.com', senha='senha123')
            database.session.add(usuario)
            database.session.commit()
            usuario_salvo = Usuario.query.filter_by(usuario='tiagolima').first()
            self.assertIsNotNone(usuario_salvo)
            self.assertEqual(usuario_salvo.usuario, 'tiagolima')
            self.assertEqual(usuario_salvo.senha, 'senha123')
            Usuario.query.filter_by(usuario='tiagolima').delete()
            database.session.commit()

    def tearDown(self):
        with app.app_context():
            database.session.remove()


if __name__ == '__main__':
    unittest.main()
