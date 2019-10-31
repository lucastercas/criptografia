def getRotorOutput(input, rotor, position):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    # Calcular a posição da letra atual no alfabeto, somar com a posição, e calcular o resto disso com 26
    input_idx = ((alphabet.index(input) + position) % 26)
    return rotor[input_idx]


def cipher(plain_text, rotors, rotors_positions):
    cipher_text = ""

    # Para cada letra do texto claro
    for char in plain_text:
        # Pular espaços em branco
        if char is ' ':
            continue

        # Salvar a entrada do primeiro rotor
        rotor_input = char
        # Para cada rotor:
        for rotor_idx in range(len(rotors)):
            # A entrada do proximo rotor vai ser a saida do rotor atual
            rotor_input = getRotorOutput(
                rotor_input,  # Saida do rotor anterior
                rotors[rotor_idx],  # Rotor atual
                rotors_positions[rotor_idx],  # Posição do rotor atual
            )
            if rotor_idx == 0:  # Se for o primeiro rotor, sempre girar ele
                rotors_positions[rotor_idx] = (
                    rotors_positions[rotor_idx]+1) % 26
            else:  # Para os outros rotores, se o rotor anterior fez uma volta completa, rodar o rotor atual
                if rotors_positions[rotor_idx-1] == 0:
                    rotors_positions[rotor_idx] += 1
        # Adicionar a saida do ultimo rotor no texto cifrado
        cipher_text += rotor_input

    return cipher_text
