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

    return result


def matrixToText(matrix):
    result = ""
    for line in matrix:
        result += ''.join(line)
    return result


def cipher(plain_text, key):
    cipher_text = ""
    normalized_text = normalizeText(plain_text)

    first_stage_matrix = textToMatrix(normalized_text, len(key))
    first_stage_transposition = transposition(first_stage_matrix, key)
    first_stage_text = matrixToText(first_stage_transposition)

    second_stage_matrix = textToMatrix(first_stage_text, len(key))
    second_stage_transposition = transposition(second_stage_matrix, key)
    second_stage_text = matrixToText(second_stage_transposition)

    cipher_text = second_stage_text
    print(f"--> Cipher Text: {cipher_text}")
    return cipher_text
