def getRotorOutput(input, rotor, rotor_position):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    input_idx = alphabet.index(input)
    return rotor[input_idx]


def cipher(plain_text, rotors, rotors_position):
    cipher_text = ""
    for char in plain_text:
        # Pular espaços em branco
        if char is ' ':
            continue

        # Primeiro Rotor
        first_rotor_output = getRotorOutput(
            char,
            rotors["left-rotor"],
            rotors_position["left-rotor"],
        )

        # Segundo Rotor:
        second_rotor_output = getRotorOutput(
            first_rotor_output,
            rotors["middle-rotor"],
            rotors_position["middle-rotor"],
        )

        # Terceiro Rotor:
        third_rotor_output = getRotorOutput(
            second_rotor_output,
            rotors["right-rotor"],
            rotors_position["right-rotor"],
        )

        # print("        First  Second  Third")
        # print(
        #     f"Input:  {char}\t{first_rotor_output}\t{second_rotor_output}")
        # print(
        #     f"Output: {first_rotor_output}\t{second_rotor_output}\t{third_rotor_output}")
        # print("\n")
        cipher_text += third_rotor_output

    return cipher_text
