with open('day2.txt') as f:
    lines = [line.rstrip() for line in f]

# A: rock, B: paper, C: scissors
# X: rock, Y: paper, Z: scissors
part1_score = 0
part2_score = 0
rules = {
    "A X": "draw",
    "A Y": "win",
    "A Z": "loss",
    "B X": "loss",
    "B Y": "draw",
    "B Z": "win",
    "C X": "win",
    "C Y": "loss",
    "C Z": "draw"
}

part2_rules = {
    'X': 'loss',
    'Y': 'draw',
    'Z': 'win'
}

outcome_points = {'win': 6, 'loss': 0, 'draw': 3}

rock_paper_scissors_points = {'X': 1, 'Y': 2, 'Z': 3}

for line in lines:
    my_input = line[-1]
    opponent_input = line[0:1]
    # in part 2 the letters mean loss win draw instead of rock paper scissors
    part2_needed_outcome = part2_rules[my_input]
    # find all keys that contain the needed result
    keys = [k for k, v in rules.items() if v == part2_needed_outcome]
    for key in keys:
        # if the first part of the key is the same as the opponents input we need this key, we also immedeately know if
        # we need to play rock paper or scissors
        if key[0:1] == opponent_input:
            part2_score += outcome_points[rules[key]] + rock_paper_scissors_points[key[-1]]

    part1_score += outcome_points[rules[line]] + rock_paper_scissors_points[my_input]

print(part1_score)
print(part2_score)
