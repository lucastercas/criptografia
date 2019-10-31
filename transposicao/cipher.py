# Remover espaços em branco e mudar letras maiusculas pra minusculas
def normalizeText(text):
    output = text.lower()
    output = output.replace(" ", "")
    return output


def textToMatrix(text, key_len):
    result = []
    line_index = 0
    result.append([])
    i = 0

    for i in range(len(text)):
        if i % key_len == 0 and i != 0:
            result.append([])
            line_index += 1
        result[line_index] += text[i]

    while (i+1) % key_len != 0:
        result[line_index] += 'x'
        i += 1

    return result


def transposition(matrix, key):
    key_matrix = list(key)
    sorted_key_matrix = sorted(key)

    result = []
    line_index = 0
    result.append([])

    for char in sorted_key_matrix:
        key_index = key_matrix.index(char)
        key_matrix[key_index] = None
        for i in range(len(matrix)):
            result[line_index] += matrix[i][key_index]
        line_index += 1
        result.append([])

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
