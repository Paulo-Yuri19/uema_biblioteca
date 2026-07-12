import pytest
from biblioteca.livro import Livro


# ── Testes existentes ─────────────────────────────────────────────────────

def test_criar_livro():
    livro = Livro("Dom Casmurro", "Machado de Assis", "978-85-359-0277-5")
    assert livro.titulo == "Dom Casmurro"
    assert livro.autor == "Machado de Assis"
    assert livro.disponivel is True


def test_emprestar_livro_disponivel():
    livro = Livro("O Cortico", "Azevedo", "978-85-001-0001-1")
    livro.emprestar()
    assert livro.disponivel is False


def test_emprestar_livro_ja_emprestado_levanta_erro():
    livro = Livro("Memorias Postumas", "Machado de Assis", "978-85-001-0002-2")
    livro.emprestar()
    with pytest.raises(ValueError):
        livro.emprestar()

def test_devolver_livro_emprestado():
    livro = Livro("Teste", "Autor", "123")
    livro.emprestar()
    livro.devolver()
    assert livro.disponivel is True


def test_devolver_livro_disponivel():
    livro = Livro("Teste", "Autor", "123")
    with pytest.raises(ValueError):
        livro.devolver()


def test_str_livro():
    livro = Livro("Dom Casmurro", "Machado", "123")
    texto = str(livro)

    assert "Dom Casmurro" in texto
    assert "Machado" in texto
    assert "Disponivel" in texto

# Foram adiconadas os testes: test_devolver_livro_emprestado, test_devolver_livro_disponivel, test_str_livro
