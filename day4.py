def do_you_contain_me_fully(array_1, array_2):
    overlap_counter = 0
    for task in array_1:
        if task in array_2:
            overlap_counter += 1

    if overlap_counter == len(array_1):
        return True
    else:
        return False


def do_you_contain_me(array_1, array_2):
    for task in array_1:
        if task in array_2:
            return True
    return False


with open('day4.txt') as f:
    lines = [line.rstrip() for line in f]

part_1 = 0
part_2 = 0

for line in lines:
    elf_1, elf_2 = line.split(',')[0], line.split(',')[1]
    elf_1_tasks = []
    iterator = int(elf_1.split('-')[0])
    while iterator <= int(elf_1.split('-')[1]):
        elf_1_tasks.append(iterator)
        iterator = iterator + 1

    elf_2_tasks = []
    iterator = int(elf_2.split('-')[0])
    while iterator <= int(elf_2.split('-')[1]):
        elf_2_tasks.append(iterator)
        iterator += 1
    if do_you_contain_me_fully(elf_1_tasks, elf_2_tasks):
        part_1 += 1
    else:
        if do_you_contain_me_fully(elf_2_tasks, elf_1_tasks):
            part_1 += 1

    if do_you_contain_me(elf_1_tasks, elf_2_tasks):
        part_2 += 1
    else:
        if do_you_contain_me(elf_1_tasks, elf_2_tasks):
            part_2 += 1


print(part_1)
print(part_2)
