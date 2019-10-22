def getRotorOutput(char, rotor, position):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    rotor_idx = rotor.index(char)
    return alphabet[rotor_idx]


def decipher(cipher_text, rotors, initial_rotors_position):
    deciphered_text = ""
    for char in cipher_text:
        if char is ' ':
            continue

        first_rotor_output = getRotorOutput(
            char,
            rotors['right-rotor'],
            initial_rotors_position['right-rotor']
        )
        second_rotor_output = getRotorOutput(
            first_rotor_output,
            rotors['middle-rotor'],
            initial_rotors_position['middle-rotor']
        )
        third_rotor_output = getRotorOutput(
            second_rotor_output,
            rotors['left-rotor'],
            initial_rotors_position['left-rotor']
        )
        deciphered_text += third_rotor_output
    return deciphered_text
