def getscore(ascii_char, score):
    if ascii_char.isupper():
        score += ord(ascii_char) - 38
    else:
        score += ord(ascii_char) - 96
    return score


with open('day3.txt') as f:
    lines = [line.rstrip() for line in f]

part_1 = 0
part_2 = 0
elf_counter = 1
group_array = []

for line in lines:
    length = len(line)
    compartment_1 = line[0:length // 2]
    compartment_2 = line[length // 2:]
    character_that_appears_in_both_strings = ''.join(set(compartment_1).intersection(compartment_2))

    part_1 = getscore(character_that_appears_in_both_strings, part_1)

    group_array.append(line)
    if elf_counter % 3 == 0:
        character_on_elf_1_and_2 = ''.join(set(group_array[0]).intersection(group_array[1]))
        character_on_all_elves = ''.join(set(character_on_elf_1_and_2).intersection(group_array[2]))

        # print(character_on_all_elves)
        group_array = []
        part_2 = getscore(character_on_all_elves, part_2)

    elf_counter = elf_counter + 1

print(part_1)
print(part_2)
