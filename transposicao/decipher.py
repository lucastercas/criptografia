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

    for i in range(len(matrix[0])):
        copy_key = copy.copy(sorted_key)
        for char in key:
            key_index = copy_key.index(char)
            copy_key[key_index] = None
            result += matrix[key_index][i]

    return result


def decipher(cipher_text, key, n_stages):
    text = cipher_text
    for _ in range(n_stages):
        matrix = textToMatrix(text, len(key))
        text = transposition(matrix, key)

    return text
