
import sys

lista_final = []
lista_auxiliar = []
lista_final_tipo = []
#temp; goto;
lista = [0, 0]

def printTemp():
    if len(lista_auxiliar) > 0:
        print (lista_auxiliar.pop)

def imprimeCodigo(parseTree, saida, nivel):

    if isinstance(parseTree, list):
        for x in range(len(parseTree)):
            imprimeCodigo(parseTree[x], saida, nivel)
    
    elif parseTree.token == "HULK" :
        saida.write('\t' * nivel)
        saida.write(f"{parseTree.esq.lexeme} := {parseTree.dir.lexeme}\n")

    elif parseTree.token == "VISAO" :
        saida.write('\t' * nivel)
        saida.write(f"print ({parseTree.esq.lexeme})\n")

    elif parseTree.token in ("VENOM", "CARNIFICINA", "MADROX","THANOS"):
        if parseTree.token == "VENOM" :
                operador =  "+"
        elif parseTree.token == "CARNIFICINA" :
                operador = "-"
        elif parseTree.token == "MADROX" :
                operador = "*"
        elif parseTree.token == "THANOS" :
                operador = "/"

        if parseTree.dir.token in ("ID", "INTEGER_CONST", "FLOAT_CONST") :
            saida.write('\t' * nivel)
            saida.write(f"{parseTree.esq.lexeme} := {parseTree.esq.lexeme} {operador} {parseTree.dir.lexeme}\n")
            
        else:

            imprimeCodigo(parseTree.dir,saida, nivel)
            saida.write('\t' * nivel)
            saida.write(f"{parseTree.esq.lexeme} := {parseTree.esq.lexeme} {operador} {parseTree.dir.esq.lexeme}\n")
           

    elif parseTree.token == "GROOT" :
    
        lista[1] += 1
        _tempGoto = lista[1]
        _tempTree = parseTree.esq
        if _tempTree.token == "MISTICA":
            operador = "==" 
        elif _tempTree.token == "GOLIAS":
            operador = ">"
        elif _tempTree.token == "FORMIGA":
            operador = "<"

        saida.write('\t' * nivel)
        saida.write(f"if ({_tempTree.esq.lexeme}{operador}{_tempTree.dir.lexeme}) goto L{_tempGoto}\n")
        imprimeCodigo(parseTree.dir,saida, nivel+1)
        saida.write('\t' * nivel)
        saida.write(f"L{_tempGoto}:\n") 
        


    elif parseTree.token == "DRESTRANHO" :
        
        lista[1] += 2
        _tempGoto = lista[1]
        _tempTree = parseTree.esq
        if _tempTree.token == "MISTICA":
            operador = "==" 
        elif _tempTree.token == "GOLIAS":
            operador = ">"
        elif _tempTree.token == "FORMIGA":
            operador = "<"

        saida.write('\t' * nivel)
        saida.write(f"L{_tempGoto-1}: if ({_tempTree.esq.lexeme}{operador}{_tempTree.dir.lexeme}) goto L{_tempGoto}\n")
        imprimeCodigo(parseTree.dir, saida,nivel+1)
        saida.write('\t' * nivel)
        saida.write(f"goto L{_tempGoto-1}\n") 
        saida.write('\t' * nivel)
        saida.write(f"L{_tempGoto}:\n") 


def CodeGenerator(parseTree):
    saida = open('saida.txt', 'w')
    imprimeCodigo(parseTree, saida, 0)

    saida.close()
