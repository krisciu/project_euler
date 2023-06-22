f = open("./resources/0022_names.txt", "r")
raw_names = f.read()
quoted_names_list = raw_names.split(",")
names_list = [name.strip('"\'') for name in quoted_names_list]
sorted_names_list = sorted(names_list)
total_score = 0
for i, name in enumerate(sorted_names_list):
    score = 0
    for character in name:
        score = score + (ord(character) - 64)
    total_score += score * (i + 1)
print(total_score)
