with open('day5.txt') as f:
    lines = [line.rstrip() for line in f]
all_stacks = {
    '1': [],
    '2': [],
    '3': [],
    '4': [],
    '5': [],
    '6': [],
    '7': [],
    '8': [],
    '9': [],
}

stack_input = []
for line in lines:
    if line == '':
        break
    stack_input.append(line)

for crate_line in stack_input:
    if '1' in crate_line:
        break
    n = 4
    broken_crate_line = [crate_line[i:i + n] for i in range(0, len(crate_line), n)]
    for crate_number in range(len(broken_crate_line)):
        index = crate_number + 1
        if not broken_crate_line[crate_number] == '    ':
            all_stacks[str(index)].append(broken_crate_line[crate_number])

for crate_number in all_stacks:
    all_stacks[crate_number].reverse()

move_commands = []
for line in lines:
    if 'move' in line:
        move_commands.append(line)

for line in move_commands:
    amount_moved, move_from_to = line.split(' from ')
    amount_moved = amount_moved.split(' ')[1]
    move_from, move_to = move_from_to.split(' to ')
    for i in range(int(amount_moved)):
        crate_number = all_stacks[move_from].pop()
        all_stacks[move_to].append(crate_number)

part_1 = ''
for stack_number in all_stacks:
    part_1 += all_stacks[stack_number][-1]

print(part_1)
