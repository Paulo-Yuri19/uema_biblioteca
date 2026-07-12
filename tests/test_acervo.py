from biblioteca.acervo import Acervo
from biblioteca.livro import Livro


def test_adicionar_livro():
    acervo = Acervo("Biblioteca")

    livro = Livro("Livro", "Autor", "1")

    acervo.adicionar_livro(livro)

    assert acervo.total_livros() == 1


def test_buscar_por_titulo():
    acervo = Acervo("Biblioteca")

    livro = Livro("Dom Casmurro", "Machado", "1")

    acervo.adicionar_livro(livro)

    resultado = acervo.buscar_por_titulo("dom")

    assert len(resultado) == 1


def test_buscar_por_autor():
    acervo = Acervo("Biblioteca")

    livro = Livro("Livro", "Machado", "1")

    acervo.adicionar_livro(livro)

    resultado = acervo.buscar_por_autor("machado")

    assert len(resultado) == 1


def test_livros_disponiveis():
    acervo = Acervo("Biblioteca")

    livro = Livro("Livro", "Autor", "1")

    acervo.adicionar_livro(livro)

    assert len(acervo.livros_disponiveis()) == 1


def test_livros_emprestados():
    acervo = Acervo("Biblioteca")

    livro = Livro("Livro", "Autor", "1")

    acervo.adicionar_livro(livro)

    livro.emprestar()

    assert len(acervo.livros_emprestados()) == 1