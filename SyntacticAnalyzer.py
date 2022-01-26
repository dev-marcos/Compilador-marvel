import sys
from CodeGenerator import CodeGenerator
from LexicalAnalyzer import *
from SemanticAnalyzer import compVar, printVar, varAdd, varNotExists, varOpe
from Token import *
from SemanticAnalyzer import *

#pilha para controlar quantidade de abertura if, while 

stackDrestranho = []
stackGroot = []
stackFury = []


def errorMessage(line,error):
    print(f'Erro-Linha {line}: Erro Sintático! "{error}".')
    sys.exit()

#Função inicializa e encerra o programa
def functionIniciatlize(variable,line):
   
    if len(stackGroot) > 0:
        errorMessage(variable[stackGroot[0]].row, "Esperava-se groot -> rocket")  
    if len(stackDrestranho) > 0:
        errorMessage(variable[stackDrestranho[0]].row, "Esperava-se drestranho -> dormamo")  

    if variable[line+1].token=="CHAMADA_DE_FUNCAO":
        if variable[line+2].token=="AVENGERS":
            if len(stackFury) > 0 :
                errorMessage(variable[line].row, "Não é possivel iniciar o programa mais de uma vez!") 
                   
            #print("Programa inicializado de maneira correta")
      
            
            stackFury.append(line)
            return 3
        elif variable[line+2].token=="SHIELD": 
 
            print("COMPILADO COM SUCESSO!!!")
            return 3

        else:
            errorMessage(variable[line+2].row, "Esperava-se AVENGERS ou SHIELD")
    else:
        errorMessage(variable[line+1].row, "Está faltando o comando de atribuição '->'")            
            

#Função atribui variaveis 

def functionVariable(variable,line): 
    _tree = Tree(variable[line])
    if variable[line+1].token=="CHAMADA_DE_FUNCAO":
        if variable[line+2].token=="ID":
            _tree.esq = Tree(variable[line+2])
            if variable[line+3].token=="ATRIBUIR":  

                if variable[line+4].token in ("INTEGER_CONST", "FLOAT_CONST"):#atribuicao por valor
                    
                    varAdd(variable, line+2)
                    #print("Atribuição de variavel por constante")
                    _tree.dir = Tree(variable[line+4])
                    return 5, _tree 
                elif variable[line+4].token=="ID": #por outra variavel
                    
                    
                    varAdd(variable, line+2)
                    #print("Atribuição de variavel ID")
                    _tree.dir = Tree(variable[line+4])
                    return 5, _tree
              
                else:
                    errorMessage(variable[line+4].row, "Atribuição invalida")         
            else:
                errorMessage(variable[line+3].row, "Esperava-se o comando atribuir '.'")
        else:
            errorMessage(variable[line+2].row, "Deve-se informar o ID")
    else:
        errorMessage(variable[line+1].row, "Está faltando o comando de atribuição '->'")

  
#Função para tratar expressões
def functionExpression(variable,line):
        _tree = Tree(variable[line])

        if variable[line+1].token=="CHAMADA_DE_FUNCAO":
            if variable[line+2].token in ["ID", "INTEGER_CONST", "FLOAT_CONST"]:
                
                varNotExists(variable[line+2])
                _tree.esq = Tree(variable[line+2])

                if variable[line+3].token=="ATRIBUIR": 
                    if variable[line+4].token in ["ID", "INTEGER_CONST", "FLOAT_CONST"]:#atribuicao por valor
                        varOpe(variable, line)
                        if variable[line+4].token == "ID":
                            varNotExists(variable[line+4])
                        _tree.dir = Tree(variable[line+4])
                        #printTree(_tree)
                        #print("Atribuição de variavel ID, INTEGER_CONST ou FLOAT_CONST")
                        return 5, _tree
                    elif variable[line+4].token in ["VENOM", "CARNIFICINA", "MADROX", "THANOS"]:
                
                        
                        aux, _tree.dir = functionExpression(variable, line+4)
    
                        return aux + 4, _tree
                    else:
                        errorMessage(variable[line+4].row, f"Atribuição invalida '{variable[line+4].lexeme}'." )
                else:
                    errorMessage(variable[line+3].row, "falta o comando atribuir .")
            else:
                errorMessage(variable[line+2].row, "Deve haver ID.")
        else:
            errorMessage(variable[line+1].row, "Está faltando o comando de atribuição '->'")
        

# Função para print
def functionPrint(variable, line): 
    _tree = Tree(variable[line])
    if variable[line+1].token=="CHAMADA_DE_FUNCAO":
        if variable[line+2].token in ["ID", "INTEGER_CONST", "FLOAT_CONST"]:
            _tree.esq = Tree(variable[line+2])
            varNotExists(variable[line+2])
         #   print("Print correto")
            return 3, _tree
        else:
            errorMessage(variable[line+2].row, "Deve não foi expecificado o que deseja imprimir")
    else:
        errorMessage(variable[line+1].row, "Está faltando o comando de atribuição '->'")


def functionBool(variable,line):
    _tree = Tree(variable[line])
    if variable[line+1].token=="CHAMADA_DE_FUNCAO":
        if variable[line+2].token in ["ID", "INTEGER_CONST", "FLOAT_CONST"]:
            varNotExists(variable[line+2])
            _tree.esq = Tree(variable[line+2])
            if variable[line+3].token=="ATRIBUIR": 
                if variable[line+4].token in ["ID", "INTEGER_CONST", "FLOAT_CONST"]:
                    compVar(variable, line)
                    varNotExists(variable[line+4])
                    _tree.dir = Tree(variable[line+4])
                    if variable[line+5].token in ["AMERICA", "STARK"]:
                        _newTree = Tree(variable[line+5])
                        _newTree.esq = _tree
                        
                        if variable[line+6].token=="CHAMADA_DE_FUNCAO":
                            if variable[line+7].token in ["MISTICA", "GOLIAS", "FORMIGA"]:
                                
                                aux, _newTree.dir = functionBool(variable,line+7)
                                
                                return aux + 7, _newTree
                            else:
                                errorMessage(variable[line+7].row, "Esperava-se um operador de comparação [\"MISTICA\", \"GOLIAS\" ou \"FORMIGA\"]")
                        else:
                            errorMessage(variable[line+6].row, "Está faltando o comando de atribuição '->'")
                    else:
                     #   print("Comparação realizada de maneira correta")
                        return 4, _tree
                else:
                    errorMessage(variable[line+4].row, "valor operacao incorreto")
            else:
                errorMessage(variable[line+3].row, "Operador comparador nao identificado")
        else:
            errorMessage(variable[line+2].row, "valor operacao incorreto")
    else:
        errorMessage(variable[line+1].row, "está faltando o comando de atribuição ->")


#Função para comparação
def functionIf(variable,line): 

    _tree = Tree(variable[line])
    if variable[line+1].token=="CHAMADA_DE_FUNCAO":
        if variable[line+2].token  in ["MISTICA", "GOLIAS", "FORMIGA"]:

            aux, _tree.esq= functionBool(variable,line+2)
            #printTree(_tree, 0)
            stackGroot.append(line)
           # print("Chamada if: ", variable[aux+3+line].lexeme)
            _tree.dir, num = SyntacticAnalyzer(variable, aux + 3 + line)
            return num - line, _tree       
        elif variable[line+2].token=="ROCKET":       
            stackGroot.pop()
            #print("Comparação encerrada com sucesso")
            return 3, _tree
        else:      
            errorMessage(variable[line+2].row, "Esperava-se um operador de comparação [\"MISTICA\", \"GOLIAS\" ou \"FORMIGA\"]")
    else:        
        errorMessage(variable[line+1].row, "Esperado ->") 

#Função para laço                       
def functionLaco(variable,line):  
    _tree = Tree(variable[line]) 
    if variable[line+1].token=="CHAMADA_DE_FUNCAO":
        if variable[line+2].token in ["MISTICA", "GOLIAS", "FORMIGA"]:
            aux, _tree.esq = functionBool(variable,line+2)
            stackDrestranho.append(line)
            _tree.dir, num = SyntacticAnalyzer(variable, aux + 3 + line)
            return num - line, _tree   
            
        elif variable[line+2].token=="DORMAMO":       
            stackDrestranho.pop()
            #print("Laço encerrado com sucesso")
            return 3, _tree
        else:      
            errorMessage(variable[line+2].row, "Esperava-se um operador de comparação [\"MISTICA\", \"GOLIAS\" ou \"FORMIGA\"]")
    else:        
        errorMessage(variable[line+1].row, "Esperado ->") 

def printTree(tree, aux):
    if isinstance(tree, list):
        for x in range(len(tree)):
            printTree(tree[x], aux)
    else:
        print('\t' * aux, f"\t {tree.lexeme}")
        
        #print('#' * aux, "# Linha: {0}\tColuna: {1}\tToken: {2}\tLexema: {3}".format(tree.row, tree.column, tree.token, tree.lexeme))
        if tree.esq is not None:
            printTree(tree.esq, aux+1)
        if tree.dir is not None:
            printTree(tree.dir, aux+1 )

# Função Análise Sintática
def SyntacticAnalyzer(variable,line): 
    
    listTree = []
    tree = Tree(variable[line])
    while (line < len(variable)):

        first_type=variable[line].token
        
        

        if len(stackFury) != 0:
            if first_type=="FURY":
                line +=functionIniciatlize(variable,line)

            elif first_type=="HULK":
                aux, tree = functionVariable(variable,line)
                line += aux
                listTree.append(tree)
                #printTree(tree, 0)

            elif first_type in ["VENOM", "CARNIFICINA", "MADROX", "THANOS"]:
                aux, tree = functionExpression(variable,line)
                line += aux
                listTree.append(tree)
            elif first_type =="VISAO":
                aux, tree = functionPrint(variable,line)
                line += aux
                listTree.append(tree)

            elif first_type=="GROOT":
                aux, tree = functionIf(variable,line)
                
                line += aux
                if aux == 3:
                    return listTree, line
                else:
                    listTree.append(tree)

            elif first_type=="DRESTRANHO":
                aux, tree = functionLaco(variable,line)
                line += aux
                if aux == 3:
                    return listTree, line
                else:
                    listTree.append(tree)
             

            elif first_type=="COMENTARIOS":
                line +=1
            else:
                errorMessage(variable[line+1].row, "Token não identificado")    
        
        elif first_type=="FURY":
            line +=functionIniciatlize(variable,line)

        elif first_type=="COMENTARIOS":
            line +=1
        else:
            errorMessage(variable[line+1].row, "Token não identificado") 
    return listTree, line
    CodeGenerator(variable)

    