# -*- coding: utf-8 -*-
import re
import sys
#from Parser import *

variable = []

class LexicalAnalyzer:
    
    lin_num = 1

    def tokenize(self, code):
        rules = [
            ('FURY', r'fury'),                      # main
            ('HULK', r'hulk'),                      # variavel
            ('VISAO', r'visao'),                    # print
            ('GROOT', r'groot'),                    # if
            ('ROCKET', r'rocket'),                  # endif
            ('VENOM', r'venom'),                    # +
            ('CARNIFICINA', r'carnificina'),        # -
            ('MADROX', r'madrox'),                  # *
            ('GOLIAS', r'golias'),                  # >
            ('MISTICA', r'mistica'),                # ==
            ('THANOS', r'thanos'),                  # /
            ('DRESTRANHO', r'drestranho'),          # while
            ('DORMAMO', r'dormamo'),                # endwhile
            ('FORMIGA', r'formiga'),                # <
            ('AMERICA', r'america'),                # &&
            ('STARK', r'stark'),                    # ||
            ('SHIELD', r'shield'),                  # end main
            ('AVENGERS', r'avengers'),              # open main
            ('LINCE', r'lince'),                    # read file
            ('CHAMADA_DE_FUNCAO', r'\-\>'),         # atribuição
            ('ATRIBUIR', r'\.'),                    # ANOTHER CHARACTER
            ('ID', r'[a-zA-Z]\w*'),                 # IDENTIFIERS
            ('FLOAT_CONST', r'\d(\d)*\,\d(\d)*'),   # FLOAT
            ('INTEGER_CONST', r'\d(\d)*'),          # INT
            ('NEWLINE', r'\n'),                     # NEW LINE
            ('SKIP', r'[ \t]+'),                    # SPACE and TABS
            ('COMENTARIOS', r'\#')                  # comentarios
        ]

        tokens_join = '|'.join('(?P<%s>%s)' % x for x in rules)
        lin_start = 0
        isComment = False
        
        token = []
        lexeme = []
        row = []
        column = []

        erro = 0
        
        # Analisa o código para encontrar lexemas e seus respectivos tokens
        for m in re.finditer(tokens_join, code):
            aux_var = variable
            
            token_type = m.lastgroup
            token_lexeme = m.group(token_type)
           
            if token_lexeme == '#':
                isComment = not isComment
            if not isComment :
              #  if token_type == 'HULK':
               #     erro = 1
                #if token_type == 'CHAMADA_DE_FUNCAO':
                #    if(erro == 1):
                #        erro = 2
                 #   else:
                 #       erro = 0
                #if token_type == 'ID':
                #    if erro == 2 and not (token_lexeme in aux_var):
                 #       variable.append(token_lexeme)
                #        erro = 0
                #    elif (erro != 2) and not (token_lexeme in aux_var):
                #        print("Erro léxico! linha {0}, Token -> {1}".format(self.lin_num, token_lexeme))
                #        erro = 0
                #    else:
                 #       erro = 0

                if token_type == 'NEWLINE':
                    lin_start = m.end()
                    self.lin_num += 1
                elif token_type == 'SKIP':
                    continue
                elif token_type == 'MISMATCH':
                    raise RuntimeError('%r não esperado na linha %d' % (token_lexeme, self.lin_num))
                else:
                        col = m.start() - lin_start
                        column.append(col)
                        token.append(token_type)
                        lexeme.append(token_lexeme)
                        row.append(self.lin_num)
                         #Imprime informações sobre os tokens
                        #print('Token = {0}, Lexeme = \'{1}\', Row = {2}, Column = {3}'.format(token_type, token_lexeme, self.lin_num, col))
                        
        return token, lexeme, row, column
