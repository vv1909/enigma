from parts import Parts

plugboard = Parts.plugboard

rotors_stored = [0, Parts.rotor1, Parts.rotor2, Parts.rotor3]
letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
letters_lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

rotor_positions = [22, 10, 4]
rotors = [rotors_stored[1], rotors_stored[2], rotors_stored[3]]
rots = '123'
turnovers = [16, 4, 21]
def to_number(letter):
    return ord(letter.upper()) - 65

def plugboard_set():
    while True:
        pair = input('Write a pair of letters (example: ag ): or 0 for exit: ')
        if len(pair) == 2:
            # print(len(pair))
            pf = str(to_number(pair[0]))
            ps = str(to_number(pair[1]))
            if len(pair) == 2 and pf in plugboard and ps in plugboard:
                # pair = f'{pair[0].upper()}{pair[1].upper()}'
                if plugboard[pf] != pf:
                    plugboard[plugboard[pf]] = plugboard[pf]
                    plugboard[pf] = pf
                if plugboard[ps] != ps:
                    plugboard[plugboard[ps]] = plugboard[ps]
                    plugboard[ps] = ps
                plugboard[pf] = ps
                plugboard[ps] = pf
            else:
                break
        else:
            break
    return plugboard

def rotors_set():
    rots = input('write rotor hertakanutyun(213)')
    # print(len(rots))
    rotors = [rotors_stored[int(rots[0])], rotors_stored[int(rots[1])], rotors_stored[int(rots[2])]]
    positions = input('write rotor positions (1-26) with spaces (7 14 22)')
    positions = positions.split(' ')
    rotor_positions = [1, 2, 3]
    for i in range(0,3):
        rotor_positions[i] = int(positions[i]) - 1
    return rotors, rotor_positions, rots
    # print(rotors)

# rotors_set()

def rotate(positions):
    positions[2] = (positions[2] + 1) % 26
    if positions[2] == (turnovers[2] + 1):
        positions[1] = (positions[1] + 1)%26
        if positions[1] == turnovers[1] + 1:
            positions[0] = positions[0] %26
    return positions

def write(rotors, rotor_positions, rots, plugboard):
    left = rotors[0]
    middle = rotors[1]
    right = rotors[2]

    reflector = Parts.reflector
    positions = rotor_positions

    left_set = list(left.keys())[positions[0]]
    middle_set = list(middle.keys())[positions[1]]
    right_set = list(right.keys())[positions[2]]
    rotor_signs = [0, 0, 0]
    rotor_signs[0] = rots[0].replace('1', 'I').replace('2', 'II').replace('3', 'III')
    rotor_signs[1] = rots[1].replace('1', 'I').replace('2', 'II').replace('3', 'III')
    rotor_signs[2] = rots[2].replace('1', 'I').replace('2', 'II').replace('3', 'III')
    # print(rots)

    print(f"{rotor_signs[0]}({positions[0]}) | {rotor_signs[1]}({positions[1]}) | {rotor_signs[2]}({positions[2]})")

    # print(positions)
    text = input('Enter your text: ')
    encrypted_text = ''
    for character in text:
        if character in letters or character in letters_lower:
            positions = rotate(positions)
            character = character.upper()
            char = str(to_number(character))
            t1 = letters[int(char)]

            char = plugboard[char]
            t2 = letters[int(char)]

            char = right[str((int(char)+int(positions[2]))%26)]
            t3 = letters[int(char)]
            
            char = middle[str((int(char)-int(positions[2])+int(positions[1]))%26)]
            t4 = letters[int(char)]

            char = left[str((int(char)+int(positions[0])-int(positions[1]))%26)]
            t5 = letters[int(char)]

            char = reflector[str((int(char)-int(positions[0]))%26)]
            t6 = letters[int(char)]
            
            char = next((key for key, val in left.items() if val == str((int(char)+int(positions[0]))%26)), None)
            
            t7 = letters[int(char)]

            char = next((key for key, val in middle.items() if val == str((int(char)-int(positions[0])+int(positions[1]))%26)), None)
            t8 = letters[int(char)]

            char = next((key for key, val in right.items() if val == str((int(char)+int(positions[2])-int(positions[1]))%26)), None)
            t9 = letters[int(char)]

            char = plugboard[str((int(char)-(int(positions[2])))%26)]
            t10 = letters[int(char)]
            encrypted_text+=letters[int(char)]
            print(f"{t1} >> {t2} >> {t3} >> {t4} >> {t5} >> {t6} >> {t7} >> {t8} >> {t9} >> {t10}")
        else:
            encrypted_text+=character
            print("\n")
    # print("\n")
    print(encrypted_text)
    # write(rotors, rotor_positions, rots, plugboard)

plugboard = plugboard_set()
# rotors, rotor_positions,rots = rotors_set()
write(rotors, rotor_positions, rots, plugboard)