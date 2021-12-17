# Algoritmo passeio do cavalo
# Josué Santos CC06

#Tenta move o cavalo pelo tabuleiro
def mover(i, x, y):
    done = i > numSqr
    k = 0
    while not done and k < 8:
        u = x + dx[k]  
        v = y + dy[k]  
        if valida(u, v):
            tabuleiro[u][v] = i
            done = mover(i + 1, u, v) 
            if not done:
                tabuleiro[u][v] = 0
        k += 1
    return done

#Verifica se o movimento pode ser feito
def valida(x, y):
    if (x >= 0 and x <= num - 1 and y >= 0 and y <= num - 1 and tabuleiro[x][y] == 0):
        return True
    else:
        return False

#imprime com a movimetação do cavalo
def imprimir(x, y):
    tabuleiro[x][y] = 1
    done = mover(2, x, y)
    string = ""
    if done:
        for x in range(0, num):
            for y in range(0, num):
                if tabuleiro[x][y] < 10:
                    string += "0"+str(tabuleiro[x][y]) + " "
                else:
                    string += str(tabuleiro[x][y]) + " "
            string += "\n"
        print(string)
    else:
        print("Nao ha passeio possivel\n")


dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]

print("Digite o num de casas do tabuleiro: ")
num = int(input())
print("Digite o x onde o cavalo deve iniciar: ")
x = int(input()) 
print("Digite o y onde o cavalo deve iniciar: ")
y = int(input()) 
numSqr = num * num



tabuleiro = [[], [], [], [], [], [], [], []]
for i in range(0, num):
    for j in range(0, num):
        tabuleiro[i].append(0)

#executa algotimo
imprimir(x, y)