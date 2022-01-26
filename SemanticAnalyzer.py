import sys


from Token import *

stackVarName = []
stackVarType = []



arvore = None

def errorMessage(line,error):
    print(f'Erro-Linha {line}: Erro Semantico! "{error}".')
    sys.exit()

def varExists(var):
    if var.token == "ID":
        if var.lexeme in stackVarName:
            errorMessage(var.row, f"Variavel '{var.lexeme}' já declarada")

def varNotExists(var):
    if var.token == "ID":
        if var.lexeme not in stackVarName:
            errorMessage(var.row, f"Variavel '{var.lexeme}' não declada")

def compVar(var, line):

    if var[line+4].token == "ID":
        if stackVarType[stackVarName.index(var[line+2].lexeme)] != stackVarType[stackVarName.index(var[line+4].lexeme)]:
            errorMessage(var[line+2].row, f"Comparação com tipo diferente variavel: '{stackVarType[stackVarName.index(var[line+2].lexeme)]}'  e '{stackVarType[stackVarName.index(var[line+4].lexeme)]}'")   
   
    if var[line+4].token in ("INTEGER_CONST", "FLOAT_CONST"):
        if stackVarType[stackVarName.index(var[line+2].lexeme)] != var[line+4].token:
            errorMessage(var[line+2].row, f"Comparação com tipo diferente variavel: '{stackVarType[stackVarName.index(var[line+2].lexeme)]}'  e '{var[line+4].token}'")   
        
def varOpe(var, line):

    if var[line].token == "THANOS":
        if var[line+4].token == "INTEGER_CONST":
            if int(var[line+4].lexeme) == 0 :
                errorMessage(var[line].row, f"Divisão por zero! Indeterminação")
        elif var[line+4].token == "FLOAT_CONST":
            if float(var[line+4].lexeme.replace(',', '.')) == 0.0 :
                errorMessage(var[line].row, f"Divisão por zero! Indeterminação")
            
            
    if var[line+4].token == "ID":
        if stackVarType[stackVarName.index(var[line+2].lexeme)] != stackVarType[stackVarName.index(var[line+4].lexeme)]:
            errorMessage(var[line+2].row, f"Comparação com tipo diferente variavel: '{stackVarType[stackVarName.index(var[line+2].lexeme)]}'  e '{stackVarType[stackVarName.index(var[line+4].lexeme)]}'")   
   
    if var[line+4].token in ("INTEGER_CONST", "FLOAT_CONST"):
        if stackVarType[stackVarName.index(var[line+2].lexeme)] != var[line+4].token:
            errorMessage(var[line+2].row, f"Comparação com tipo diferente variavel: '{stackVarType[stackVarName.index(var[line+2].lexeme)]}'  e '{var[line+4].token}'")   

def varAdd(var, line):
    varExists(var[line])

    if var[line+2].token in ("INTEGER_CONST", "FLOAT_CONST"):
        stackVarName.append(var[line].lexeme)
        stackVarType.append(var[line+2].token) 
    elif var[line+2].token=="ID":
        if var[line+2].lexeme not in stackVarName:
            errorMessage(var[line+2].row, f"Variavel '{var[line+2].lexeme}' não declarada")
    
        stackVarName.append(var[line].lexeme)
        stackVarType.append(stackVarType[stackVarName.index(var[line+2].lexeme)])
    else:
        errorMessage(var[line].row, f"Não é possivel definir tipo da variavel")

    
def printVar():
    for x in range(len(stackVarName)): 
        print(f"Variavel: {stackVarName[x]} \t Tipo: {stackVarType[x]}")

def SemanticAnalyzer(code_list):
    
    
    print("nao tem nada")
    #variableAnalyzer(code_list,0)
    #CodeGenerator(code_list) #chama a função para gerar codigo 


