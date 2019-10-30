def getRotorOutput(input, rotor, position):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    input_idx = ((alphabet.index(input) + position ) % 26)
    return rotor[input_idx]


def cipher(plain_text, rotors, rotors_positions):
    cipher_text = ""
    for char in plain_text:
        # Pular espaços em branco
        if char is ' ':
            continue

        rotor_input = char
        # Para cada rotor:
        for rotor_idx in range(len(rotors)):
            rotor_input = getRotorOutput(
                rotor_input,
                rotors[rotor_idx],
                rotors_positions[rotor_idx],
            )
        cipher_text += rotor_input

    return cipher_text
