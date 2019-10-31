# Remover espaços em branco e mudar letras maiusculas pra minusculas
def normalizeText(text):
    output = text.lower()
    output = output.replace(" ", "")
    return output


def textToMatrix(text, line_size):
    result = []
    line_index = 0  # Para saber em que linha cada letra será inserida
    result.append([])  # Adicionar a primeira linha a matriz

    i = 0

    # Para cada letra do texto claro:
    for i in range(len(text)):
        # O tamanho de uma linha da matriz é o tamanho da chave.
        # Quando o i é multiplo do tamanho da chave, adicionar uma nova linha a matriz
        if i % line_size == 0 and i != 0:
            result.append([])  # Adicionar uma linha pra matriz
            line_index += 1

        result[line_index] += text[i]

    # Caso a ultima linha esteja faltando letras, adicionar "x" ate completar a linha
    while (i+1) % line_size != 0:
        result[line_index] += 'x'
        i += 1

    return result


def transposition(matrix, key):
    key_matrix = list(key)
    sorted_key_matrix = sorted(key)  # Ordenar a chave por ordem alfabetica

    result = []
    line_index = 0
    result.append([])

    # Para cada letra da chave ordenada alfabeticamente
    for char in sorted_key_matrix:

        # Calcular o indice da letra na chave normal
        key_index = key_matrix.index(char)

        # Invalidar esse indice (caso haja letras repetidas na chave
        key_matrix[key_index] = None

        for i in range(len(matrix)):
            result[line_index] += matrix[i][key_index]

        line_index += 1
        result.append([])

    # Concatenar a matriz em uma string so
    output = ""
    for line in result:
        output += ''.join(line)
    return output


def cipher(plain_text, key, n_stages):
    text = normalizeText(plain_text)

    for _ in range(n_stages):
        matrix = textToMatrix(text, len(key))
        text = transposition(matrix, key)

    return text
