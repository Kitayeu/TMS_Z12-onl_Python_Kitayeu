string_example = str(input("Enter string: "))
list_from_string = string_example.split()
reverse_list = []
answer: str = ""
for i in range(len(list_from_string)):
    reverse_list.append(list_from_string[-1-i])
answer = " ".join(reverse_list)
print(answer)
