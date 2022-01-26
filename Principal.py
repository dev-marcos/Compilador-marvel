# -*- coding: utf-8 -*-

from Buffer import Buffer
from CodeGenerator import CodeGenerator
from SemanticAnalyzer import printVar
from Token import *
from LexicalAnalyzer import LexicalAnalyzer
from SyntacticAnalyzer import SyntacticAnalyzer, printTree
#from SemanticAnalyzer import SemanticAnalyzer
if __name__ == '__main__':
    Buffer = Buffer()
    Analyzer = LexicalAnalyzer()

    lista = []

    token = []
    lexeme = []
    row = []
    column = []

    
    
    for i in Buffer.load_buffer('exemplo/exemplo1.txt'):
        t, lex, lin, col = Analyzer.tokenize(i)
        
        token += t
        lexeme += lex
        row += lin
        column += col

    #Esse for serve para pegar as 4 lista de retorno do for anterior e criar uma lista com uma classe para cada
    #Fazendo dessa forma, fica mais facil trabalhar com classe, do que com 4 lista separada
    for i in range(len(token)):  
        lista.append(Token(token[i],lexeme[i],row[i],column[i]))


    #Esse for serve para imprimir a lista de classe de Tokens
    #for i in range(len(lista)): 
    #    print("Linha: {0}\tColuna: {1}\n\tToken: {2}\n\tLexema: {3}\t".format(lista[i].row, lista[i].column, lista[i].token, lista[i].lexeme))

    parsetree, numero = SyntacticAnalyzer(lista, 0)
    #printVar()
    printTree(parsetree, 0)
    CodeGenerator(parsetree)
