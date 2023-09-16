import funcao_soma


def test_funcao_soma():
    assert funcao_soma.soma_dois_numeros(1,2) == 3
    assert funcao_soma.soma_dois_numeros(4,2) == 6
    assert funcao_soma.soma_dois_numeros(-1000,1) == -999
    assert funcao_soma.soma_dois_numeros(-3,4) == 1


if __name__ == "__main__":
    print("Executando testes")
    test_funcao_soma()
    print("Testes finalizados")