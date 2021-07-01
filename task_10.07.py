from random import randint
import json

data = {"matrix": [[randint(0, 20) for _ in range(4)] for _ in range(4)]}
with open("F:/Python/lesson_08/file.json", "w") as file:
    json.dump(data, file)
with open("F:/Python/lesson_08/file.json") as json_file:
    json_data = json.load(json_file)
print(json_data)
matrix = []
for i in range(len(json_data["matrix"])):
    row = []
    for j in range(len(json_data["matrix"][i])):
        if json_data["matrix"][i][j] % 2 == 0:
            row.append(0)
        else:
            row.append(json_data["matrix"][i][j])
    matrix.append(row)
new_data = {"matrix": matrix}
print(new_data)
with open("F:/Python/lesson_08/new_file.json", "w") as new_file:
    json.dump(new_data, new_file)
