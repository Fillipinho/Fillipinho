# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

print("ZOMBIE DICE ")
print("Seja bem-vindo ao jogo Zombie Dice!")

numeroJogadores = 0

while numeroJogadores < 2:
    numeroJogadores = int(input("Informe a quantidade de jogadores: "))
    if numeroJogadores < 2:
        print ("AVISO: Voce precisa de pelo menos 2 jogadores!")

listaJogadores = []

i = 0

for jogador in range(numeroJogadores):
    nome = input('informeonomedojogador')
    listaJogadores[i]= nome
    i = i+1

DADOVERDE = "CPCTPC"
DADOAMARELO = "TPCTPC"
DADOVERMELHO = "TPTCPT"

listaDados = [
					DADOVERDE,DADOVERDE,DADOVERDE,DADOVERDE,DADOVERDE,DADOVERDE,
					DADOAMARELO, DADOAMARELO, DADOAMARELO, DADOAMARELO,
					DADOVERMELHO,DADOVERMELHO,DADOVERMELHO
]

print("iniciando o jogo...")

jodagorAtual = 0
dadosSorteados = []
tiros = 0
cerebros = 0
passos = 0
i=0
while(true):
     print("TURNO DO JOGADOR ", listaJogadores[jogadorAtual])
while i<=2:
    numSorteado = aleatorio(0,12)
    dadoSorteado = listaDados[numSorteado]
    if(dadoSorteado = 'CPCTPC')
    print (corDado = 'VERDE')
    elif (dadoSorteado = 'TPCTPC')
    print (corDado = 'AMARELO')
    else ('corDado <- 'VERMELHO')
    i+=1: