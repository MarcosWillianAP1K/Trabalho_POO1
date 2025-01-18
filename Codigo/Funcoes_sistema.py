import Classes as clas




def criar_gerente(sistema:clas.SISTEMA ,nome:str, salario:float):
    gerente = clas.GERENTE(nome, salario)
    sistema.adicionar_gerente(gerente)





def inciar_sistema():
    sistema = clas.SISTEMA()
    criar_gerente(sistema, "gerente_inicial", 1500)
    return sistema