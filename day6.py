with open('day6.txt') as f:
    lines = [line.rstrip() for line in f]
datastream = lines[0]

# part 1
characters_needed = 4
# part 2
# characters_needed = 14

characters = []
for character_index in range(len(datastream)):
    if character_index + 1 >= characters_needed:
        last_x_characters = []
        for j in range(characters_needed):
            # put all characters that need to be compared with each other in their own list
            last_x_characters.append(datastream[character_index - j])

        # if a character only appears once the same counter gets + 1
        same_counter = 0
        for single_character in last_x_characters:
            same_counter += last_x_characters.count(single_character)

        if same_counter == characters_needed:
            print(character_index + 1)
            break
