from pip._vendor.distlib.compat import raw_input

class Util:

    @staticmethod
    def Split_Values(string):
        return string.split(), len(string)


class AutomatoProgram:

    def __init__(self, fileName):
        self.file = self.ReadAutomatoFile(fileName)
        self.alfabeto_entrada, self.tamanho_entrada = Util.Split_Values(self.file[0])
        self.conjunto_estados, self.tamanho_conjunto = Util.Split_Values(self.file[1])
        self.estado_inicial, self.tamanho_inicial = Util.Split_Values(self.file[2])
        self.conjunto_aceitacao, self.tamanho_aceitacao = Util.Split_Values(self.file[3])

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



def automato(programa, palavra, tamanho_palavra):
    tamanho_arquivo = len(programa.file)
    tamanho_aceitacao = len(programa.conjunto_aceitacao)
    estado_atual = programa.estado_inicial[0]

    print("=========================INÍCIO===========================")
    # Percorre toda a palavra informada
    for i in range(0, tamanho_palavra):
        # Percorre as transições lidas no arquivo
        for j in range(4, tamanho_arquivo):
            estado_sequencia, estado_tamanho = Util.Split_Values(programa.file[j])
            if estado_atual == estado_sequencia[0] and palavra[i] == estado_sequencia[1]:
                print("========================TRANSIÇÃO=========================")
                print ("|ESTADO ATUAL:", estado_atual)
                print ("|ESTADO SEQUENCIA:", estado_sequencia[0])
                print ("|SÍMBOLO DA TRANSIÇÃO:", estado_sequencia[1])
                print ("|SÍMBOLO LIDO:", palavra[i])
                print ("|PRÓXIMO ESTADO:", estado_sequencia[2])
                print("==========================================================")

                estado_atual = estado_sequencia[2]

                break


    acept = False
    for l in range(0, tamanho_aceitacao):
        # print( estado_atual )
        # print (programa.conjunto_aceitacao[l])
        if estado_atual == programa.conjunto_aceitacao[l]:
            acept = True
            print("===========================FIM============================")
            print ("|A PALAVRA FOI ACEITA EM: ", estado_atual)
            break

    if not acept:
        print("===========================FIM============================")
        print ("|A PALAVRA FOI REJEITADA.")



print ("===================ARQUIVO DO PROGRAMA====================")
nomeArquivo = raw_input('INFORME O NOME DO ARQUIVO (EX: programa.txt) :')
programaAutomato = AutomatoProgram(nomeArquivo)
print("|ARQUIVO: ", nomeArquivo, "LIDO COM SUCESSO")
print ("==========================================================")

print("\n")

print ("====================DADOS DO PROGRAMA=====================")
print ("|ALFABETO: ", programaAutomato.alfabeto_entrada)
print ("|CONJUNTO DE ESTADOS: ", programaAutomato.conjunto_estados)
print ("|ESTADO INICIAL: ", programaAutomato.estado_inicial)
print ("|CONJUNTO DE ESTADOS FINAIS: ", programaAutomato.conjunto_aceitacao)
print ("==========================================================")

print("\n")

print ("==========AUTOMATO FINITO DETERMINISTICO - AFD============")
palavra = raw_input('|INFORME A PALAVRA (FORMATO: a b) :')
palavra = palavra.split()
print ("|PALAVRA INFORMADA: ", palavra)
tamanho_palavra = len(palavra)
print ("|TAMANHO DA PALAVRA INFORMADA: ", tamanho_palavra)
print ("==========================================================")

automato(programaAutomato, palavra, tamanho_palavra)