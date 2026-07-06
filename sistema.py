def fazer_login(usuario, senha):
    # Simulação simples de autenticação
    if usuario == "admin" and senha == "1234":
        return True
    return False

def test_login_sucesso():
    assert fazer_login("admin", "1234") == True

def test_login_falha():
    assert fazer_login("usuario_errado", "senha_errada") == False
