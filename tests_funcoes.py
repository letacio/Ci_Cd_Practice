import funcao_soma


def test_funcao_soma():
    assert funcao_soma.soma_dois_numeros(1,2) == 3
    print("Teste de soma 1 e 2 passou")
    assert funcao_soma.soma_dois_numeros(4,2) == 6
    print("Teste de soma 4 e 2 passou")
    assert funcao_soma.soma_dois_numeros(-1000,1) == -999
    print("Teste de soma -1000 e 1 passou")
    assert funcao_soma.soma_dois_numeros(-3,4) == 1
    print("Teste de soma -3 e 4 passou")


if __name__ == "__main__":
    print("Executando testes")
    test_funcao_soma()
    print("Testes finalizados")