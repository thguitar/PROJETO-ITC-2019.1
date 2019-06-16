from pip._vendor.distlib.compat import raw_input

##Classe que Abstrai a Pilha do Autômato
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)


class Util:

    @staticmethod
    def Split_Values(string):
        return string.split(), len(string)

    @staticmethod
    def Print_Stack(Stack):
        while not Stack.isEmpty():
            print("|NA PILHA: ", Stack.pop())

        print("==========================================================")


class AutomatoProgram:

    def __init__(self, fileName):
        self.file = self.ReadAutomatoFile(fileName)
        self.alfabeto_entrada, self.tamanho_entrada = Util.Split_Values(self.file[0])
        self.alfabeto_pilha, self.tamanho_pilha = Util.Split_Values(self.file[1])
        self.simbolo_epsilon = self.file[2]
        self.simbolo_inicial, self.tamanho_inicial = Util.Split_Values(self.file[3])
        self.conjunto_estados, self.tamanho_conjunto = Util.Split_Values(self.file[4])
        self.estado_inicial, self.tamanho_inicial = Util.Split_Values(self.file[5])
        self.conjunto_aceitacao, self.tamanho_aceitacao = Util.Split_Values(self.file[6])

    # Lê o arquivo com o programa do Autômato e transforma cada linha
    # do arquivo em um array
    def ReadAutomatoFile(self, fileName):
        try:
            string = open(fileName, 'r').read()
            string = string.splitlines()
            return string
        except:
            print("|NÃO FOI POSSÍVEL ENCONTRAR O ARQUIVO ESPECIFICADO: ", fileName)
            exit()



def automato_pilha(initialStack, programa, palavra, tamanho_palavra):
    tamanho_arquivo = len(programa.file)
    tamanho_aceitacao = len(programa.conjunto_aceitacao)
    estado_atual = programa.estado_inicial[0]
    pilha_ = Stack()
    pilha = initialStack

    print("=========================INÍCIO===========================")
    # Percorre toda a palavra informada
    for i in range(0, tamanho_palavra):
        # Percorre as transições lidas no arquivo
        for j in range(7, tamanho_arquivo):
            estado_sequencia, estado_tamanho = Util.Split_Values(programa.file[j])
            if estado_atual == estado_sequencia[0] and palavra[i] == estado_sequencia[1]:
                print("========================TRANSIÇÃO=========================")
                print ("|ESTADO ATUAL:", estado_atual)
                print ("|ESTADO SEQUENCIA:", estado_sequencia[0])
                print ("|SÍMBOLO DA TRANSIÇÃO:", estado_sequencia[1])
                print ("|SÍMBOLO LIDO:", palavra[i])
                print ("|PRÓXIMO ESTADO:", estado_sequencia[3])
                print ("|EMPILHADOS:", estado_sequencia[4])
                print("==========================================================")

                estado_atual = estado_sequencia[3]
                auxiliar = estado_sequencia[4]
                lista = list(auxiliar)

                if estado_sequencia[4] != 'epsilon':
                    topStack = pilha.pop()
                    pilha.push(topStack)
                    pilha.push(lista[0])
                    break
                else:
                    if pilha.isEmpty():
                        break
                    else:
                        pilha.pop()
                        break

    acept = False
    for l in range(0, tamanho_aceitacao):
        if estado_atual == programa.conjunto_aceitacao[l]:
            acept = True
            print("===========================FIM============================")
            print ("|A PALAVRA FOI ACEITA EM: ", estado_atual)
            break

    if not pilha.isEmpty():
        topStack = pilha.peek()
        if topStack[0] == 'Z':
            acept = True
            print("===========================FIM============================")
            print ("|A PALAVRA FOI ACEITA POR PILHA VAZIA.")

    if not acept:
        print("===========================FIM============================")
        print ("|A PALAVRA FOI REJEITADA.")

    Util.Print_Stack(pilha)


print ("===================ARQUIVO DO PROGRAMA====================")
nomeArquivo = raw_input('INFORME O NOME DO ARQUIVO (EX: programa.txt) :')
programaAutomato = AutomatoProgram(nomeArquivo)
print("|ARQUIVO: ", nomeArquivo, "LIDO COM SUCESSO")
print ("==========================================================")

print("\n")

print ("====================DADOS DO PROGRAMA=====================")
print ("|ALFABETO: ", programaAutomato.alfabeto_entrada)
print ("|ALFABETO AUXILIAR: ", programaAutomato.alfabeto_pilha)
print ("|SÍMBOLO DE EPSILON :", programaAutomato.simbolo_epsilon)
print ("|SÍMBOLO INÍCIAL: ", programaAutomato.simbolo_inicial)
print ("|CONJUNTO DE ESTADOS: ", programaAutomato.conjunto_estados)
print ("|ESTADO INICIAL: ", programaAutomato.estado_inicial)
print ("|CONJUNTO DE ESTADOS FINAIS: ", programaAutomato.conjunto_aceitacao)
print ("==========================================================")

print("\n")

print ("====================AUTOMATO DE PILHA=====================")
palavra = raw_input('|INFORME A PALAVRA (FORMATO: a b) :')
palavra = palavra.split()
print ("|PALAVRA INFORMADA: ", palavra)
tamanho_palavra = len(palavra)
print ("|TAMANHO DA PALAVRA INFORMADA: ", tamanho_palavra)
print ("==========================================================")

initialStack = Stack()
initialStack.push(programaAutomato.simbolo_inicial)

automato_pilha(initialStack, programaAutomato, palavra, tamanho_palavra)