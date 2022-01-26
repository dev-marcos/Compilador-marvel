class Buffer:
    def load_buffer(self, fileDir):
        arq = open(fileDir, 'r')
        text = arq.readline()

        buffer = []
        cont = 1

        # O tamanho do buffer pode ser alterado alterando cont
        while text != "":
            buffer.append(text)
            text = arq.readline()
            cont += 1

            if cont == 10 or text == '':
                # Retorne um buffer cheio
                buf = ''.join(buffer)
                cont = 1
                yield buf

                # Reinicializar o buffer
                buffer = []

        arq.close()
