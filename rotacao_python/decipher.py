def getRotorOutput(char, rotor, position):
    alphabet = "abcdefghijklmnopqrstuvwxyz"

    # Calcular a posição da letra no rotor
    rotor_idx = rotor.index(char)

    # Retornar essa posição no alfabeto
    return alphabet[(rotor_idx-position)%26]


def decipher(cipher_text, rotors, rotors_positions):
    deciphered_text = ""
    for char in cipher_text:
        if char is ' ':
            continue

        rotor_input = char
        # Para cada rotor (em ordem reversa)
        for rotor_idx in reversed(range(len(rotors))):
            rotor_input = getRotorOutput(
                rotor_input,
                rotors[rotor_idx],
                rotors_positions[rotor_idx],
            )

        deciphered_text += rotor_input
    return deciphered_text
