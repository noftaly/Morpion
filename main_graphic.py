# Créé par Elliot Maisl, le 22/11/2018 en Python
"""
TODO
[V] Egalité
[ ] Pseudo
[V] Compteur de manches
"""
from tkinter import *
from tkinter import font

grid = [['.', '.', '.'],
        ['.', '.', '.'],
        ['.', '.', '.']]
playerX = input('Entrez le pseudo du premier joueur : ')
playerO = input('Entrez le pseudo du second joueur : ')
player = 'X'
startingPlayer = player
roundCounter = 0
win = False
scoreX = 0
scoreO = 0


def playerToPseudo(player):
    if player == 'X':
        return playerX
    return playerO


def possible(row, col):
    if buttons[row][col]['text'] != ' ':
        return False
    return True


def isWinner(row, col, player):
    global scoreO, scoreX
    test = True
    # Test Colonne
    for i in range(3):
        if grid[i][col] != player:
            test = False
    # Test ligne
    if not test:
        test = True
        for i in range(3):
            if grid[row][i] != player:
                test = False
    # Test diagonales
    if not test:
        test = True
        for i in range(3):
            if grid[i][i] != player:
                test = False
    if not test:
        test = True
        for i in range(3):
            if grid[2 - i][i] != player:
                test = False
    if test:
        if player == 'X':
            scoreX += 1
            textScoreX.set(playerX + ' (X) : ' + str(scoreX))
        elif player == 'O':
            scoreO += 1
            textScoreO.set(playerO + ' (O) : ' + str(scoreO))
    return test


def isEquality():
    for i in range(3):
        for j in range(3):
            if grid[i][j] == '.':
                return False
    return True


def restartGame(resetScore):
    global grid, win, text1, scoreO, scoreX, startingPlayer, player, roundCounter
    for i in range(3):
        for j in range(3):
            buttons[i][j]['text'] = ' '
    grid = [['.', '.', '.'],
            ['.', '.', '.'],
            ['.', '.', '.']]
    win = False
    roundCounter += 1
    if startingPlayer == 'X':
        startingPlayer = 'O'
    else:
        startingPlayer = "X"
    text1.set('Au tour de ' + playerToPseudo(startingPlayer))
    player = startingPlayer
    if resetScore is True:
        roundCounter = 0
        scoreO = 0
        scoreX = 0
        textScoreX.set(playerX + ' (X) : ' + str(scoreX))
        textScoreO.set(playerO + ' (O) : ' + str(scoreO))
        infoScoreX.grid(row=4, column=0)
        infoScoreO.grid(row=4, column=2)
    dispRound.set(str(roundCounter) + ' manche(s) jouée(s)')


def playRound(row, col):
    global player, win
    if not win and possible(row, col):
        grid[row][col] = player
        buttons[row][col]['text'] = player
        win = isWinner(row, col, player)
        if not win:
            win = isEquality()
            if not win:
                if player == 'X':
                    player = 'O'
                else:
                    player = 'X'
                text1.set('Au tour de ' + playerToPseudo(player))
            else:
                text1.set('Égalité.')
        else:

            text1.set(playerToPseudo(player) + ' a gagné !')


# Création de la fenêtre
window = Tk()
window.title('Morpion')
window.geometry('500x600')
# Initialisation des fontes
helv = font.Font(family='Helvetica', size=60, weight='bold')
littleHelv = font.Font(family='Helvetica', size=12)

# Affichage de la phrase d'information
text1 = StringVar()
text1.set('Au tour de ' + playerToPseudo(startingPlayer))
info = Label(textvariable=text1, font=littleHelv)
info.grid(row=0, column=0)

# Affichage du nombre de manches
dispRound = StringVar()
dispRound.set(str(roundCounter) + ' manche(s) jouée(s)')
info2 = Label(textvariable=dispRound, font=littleHelv)
info2.grid(row=4, column=1)

# Affichage des scores
textScoreX = StringVar()
textScoreO = StringVar()
textScoreX.set(playerX + ' (X) : ' + str(scoreX))
textScoreO.set(playerO + ' (O) : ' + str(scoreO))
infoScoreX = Label(textvariable=textScoreX, font=littleHelv)
infoScoreO = Label(textvariable=textScoreO, font=littleHelv)
infoScoreX.grid(row=4, column=0)
infoScoreO.grid(row=4, column=2)

# Création du bouton pour rejouer
replay = Button(text='Nouvelle manche', command=lambda: restartGame(False))
replay.grid(row=0, column=2)
restart = Button(text='Nouvelle partie', command=lambda: restartGame(True))
restart.grid(row=0, column=1)

buttons = [[0 for x in range(3)] for x in range(3)]

# Affichage des boutons
for i in range(3):      # Lignes
    for j in range(3):  # Colonnes
        buttons[i][j] = Button(text=' ', font=helv, command=lambda row=i, col=j: playRound(row, col))
        buttons[i][j]['width'] = 3
        buttons[i][j]['height'] = 1
        buttons[i][j].grid(row=i + 1, column=j)

window.mainloop()

"""
for i in range(3):      # Lignes
    for j in range(3):  # Colonnes
        print(grid[i][j], end='')
    print('')
print('-------')
"""