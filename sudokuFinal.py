import numpy as np
board = [["5","3",".",".","7",".",".",".","."],
        ["6",".",".","1","9","5",".",".","."],
        [".","9","8",".",".",".",".","6","."],
        ["8",".",".",".","6",".",".",".","3"],
        ["4",".",".","8",".","3",".",".","1"],
        ["7",".",".",".","2",".",".",".","6"],
        [".","6",".",".",".",".","2","8","."],
        [".",".",".","4","1","9",".",".","5"],
        [".",".",".",".","8",".",".","7","9"]]

#transformando todos os valores da lista board em inteiros 
for lista in range(9):
    for indice in range(9):
        if board[lista][indice] != '.':
            board[lista][indice] = int(board[lista][indice])
        else:
            board[lista][indice] = 0
#tornando a lista de outras listas (board) em uma so lista (sudoku)
sudoku = []
for i in range (9):
    sudoku.append(board[i])
#transformando a lista sudoku em uma matriz
sudoku = np.array(sudoku) 
#criando um loop que so termina ao resolver o sudoku
while 0 in sudoku:
#declarando variaveis para os 9 quadrantes
    for q in range(9):
        globals()[f'quadrante{q}'] = []
#declarando as possiveis respostas para cada quadrante
    i_ = 0
    j_ = 0
    q = 0
    for qi in range(3):
        for qj in range(3):
            for i in range(3):
                for j in range(3):
                    globals()[f'quadrante{q}'].append(sudoku[i_,j_])
                    j_ += 1
                j_ -= 3
                i_ += 1
            j_+=3
            i_ -= 3
            q+=1
        j_=0
        i_+=3

#transformando cada quadrante em uma matriz
    for q in range(9):
        globals()[f'quadrante{q}'] = np.array(globals()[f'quadrante{q}'])
        globals()[f'quadrante{q}'] = globals()[f'quadrante{q}'].reshape(3,3)

#declarando as possiveis respostas para cada linha
    for i in range (9):
        globals()[f'possiLinha{i}'] = []
        globals()[f'linha{i}'] = sudoku[i,:]
        for n in range (1,10):
            if n not in globals()[f'linha{i}']:
                globals()[f'possiLinha{i}'].append(n)
    
#declarando as possiveis respostas para cada coluna
    for j in range(9):
        globals()[f'possiColuna{j}'] = []
        globals()[f'coluna{j}'] = sudoku[:,j]
        for n in range(1,10):
            if n not in globals()[f'coluna{j}']:
                globals()[f'possiColuna{j}'].append(n)
    
#Declarando os possiveis valores para cada quadrante
    for q in range(9):
        globals()[f'possiQuadrante{q}'] = []
        for n in range(1,10):
            if n not in globals()[f'quadrante{q}']:
                globals()[f'possiQuadrante{q}'].append(n)

#verificando cada posição da matriz 9x9 para encontrar as respostas
    for i in range(9):
        for j in range(9):
            globals()[f'possiVetor{i}{j}'] = []
            if i in range(0,3):
                if j in range(0,3):
                    q = 0
                elif j in range(3,6):
                    q = 1
                elif j in range(6,9):
                    q = 2
            elif i in range(3,6):
                if j in range(0,3):
                    q = 3
                elif j in range(3,6):
                    q = 4
                elif j in range(6,9):
                    q = 5
            elif i in range(6,9):
                if j in range(0,3):
                    q = 6
                elif j in range(3,6):
                    q = 7
                elif j in range(6,9):
                    q = 8

            if sudoku[i,j] == 0:
                for n in range(1,10):
                    if n in globals()[f'possiLinha{i}'] and n in globals()[f'possiColuna{j}'] and n in globals()[f'possiQuadrante{q}']:
                        globals()[f'possiVetor{i}{j}'].append(n)
                    elif len(globals()[f'possiLinha{i}']) == 1:
                        sudoku[i,j] = (globals()[f'possiLinha{i}'][0])
                    elif len(globals()[f'possiColuna{j}']) == 1:
                        sudoku[i,j] = (globals()[f'possiColuna{j}'][0])
                    elif len(globals()[f'possiQuadrante{q}']) == 1:
                        sudoku[i,j] = (globals()[f'possiQuadrante{q}'][0])
            if len(globals()[f'possiVetor{i}{j}']) == 1:
                sudoku[i,j] = globals()[f'possiVetor{i}{j}'][0]

print(sudoku)




