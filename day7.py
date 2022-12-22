with open('day7.txt') as f:
    lines = [line.rstrip() for line in f]

# $ is a console command
# $ cd X means go to X
# $ cd / means go to top directory
# $ cd .. means go one directory higher
# $ ls means print a list of everything in this directory
# 123 abc means this file has size 123 and is called abc
# dir y means this is a directory called y

# assignment 1: find the sum of all directories with a size smaller than 10.000?
# assignment 2: assuming the most space the top directory can take up is 40000000 what is the size of the smallest file
# you need to delete?

class Directory:
    def __init__(self, name, parent):
        self.name = name
        self.parent = parent
        self.contents = []
        self.size = 0
        self.type = "directory"

    def additems(self, newcontent):
        self.contents.append(newcontent)

    def calculatesize(self):
        for content in self.contents:
            if content.type == "file":
                size_increase = int(content.size)
                self.increasesize(size_increase)
            else:
                content.calculatesize()
                size_increase = int(content.size)
                self.increasesize(size_increase)

    def calcultatescorepartone(self, part_one):
        score = part_one
        if self.size < 100000:
            score += self.size
        for content in self.contents:
            if content.type == "directory":
                score = content.calcultatescorepartone(score)
        return score

    def calculatescoreparttwo(self, part_two, needed_space):
        score = part_two
        if self.size >= needed_space and self.size < score:
            score = self.size
        for content in self.contents:
            if content.type == "directory":
                score = content.calculatescoreparttwo(score, needed_space)
        return score

    def increasesize(self, size):
        self.size += size


class File:
    def __init__(self, name, size):
        self.name = name
        self.size = size
        self.type = "file"


top_dir = Directory("/", None)

current_dir = top_dir
for line in lines:
    if line == "$ cd /":
        continue
    elif line == "$ ls":
        continue
    elif line == "$ cd ..":
        current_dir = current_dir.parent
    elif "$ cd" in line:
        for child in current_dir.contents:
            if child.name == line.split().pop():
                current_dir = child
    elif "dir" in line:
        new_child_dir = Directory(line.split().pop(), current_dir)
        current_dir.additems(new_child_dir)
    else:
        file_size, file_name = line.split()
        new_child_file = File(file_name, file_size)
        current_dir.additems(new_child_file)

top_dir.calculatesize()

part_one = 0
part_one = top_dir.calcultatescorepartone(part_one)

needed_space = top_dir.size - 40000000
part_two = top_dir.calculatescoreparttwo(top_dir.size, needed_space)

print(part_one)
print(part_two)
