from typing import List


troco = 28
moedas = [1, 2, 8, 14, 25]
qtd_moedas = len(moedas)
solucao: List[int] = []
m = [[None for _ in range(troco + 1)] for _ in range(qtd_moedas)]

def passa_troco(valor, index_moeda = 0):
    
    if valor == 0:
        print(solucao)
        return 0 # Retorna 0 caso seja troco para 0 reais

    if valor < 0:
        return float("inf") # Retorna infinito caso seja troco para valores negativos


    if valor > 0 and index_moeda == qtd_moedas:

        return float("inf") # Retorna infinito caso seja troco valores positivos maiores do que a quantidade de moedas

    if m[index_moeda][valor] is None:
        
        solucao.append(moedas[index_moeda])

        passa_troco(valor - moedas[index_moeda], index_moeda)
        
        solucao.pop()
        
        passa_troco(valor, index_moeda + 1)
    
    return m[index_moeda][valor]



passa_troco(troco)

