import copy


def textToMatrix(cipher_text, n):
    output = []
    line_idx = 0
    output.append([])

    n = len(cipher_text) / n
    for i in range(len(cipher_text)):
        output[line_idx] += cipher_text[i]
        if i != 0 and (i+1) % n == 0:
            output.append([])
            line_idx += 1
    return output


def transposition(matrix, key):
    result = ""
    sorted_key = sorted(key)
    line_size = len(matrix[0])

    # Para cada linha da matrix
    for i in range(line_size):
         # Copiar a chave, para n mudar a chave original, pq ela vai ter q ser usada no loop
        copy_key = copy.copy(sorted_key)

        for char in key:
            key_index = copy_key.index(char)
            # Invalidar o indice, caso tenha letras repetidas na chave
            copy_key[key_index] = None
            result += matrix[key_index][i]

    return result


def decipher(cipher_text, key, n_stages):
    text = cipher_text
    for _ in range(n_stages):
        matrix = textToMatrix(text, len(key))
        text = transposition(matrix, key)

    return text
