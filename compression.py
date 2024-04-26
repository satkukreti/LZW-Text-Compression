user_file = input("Please enter your file name: ")
input_file = open(user_file, "r")

output = []
string_table = {chr(i):i for i in range(32, 127)}
string_table[chr(10)] = 10
count = 128
current = ""

while True:
    char = input_file.read(1)
    if not char:
        if current:
            output.append(string_table[current])
        break

    current += char
    if current not in string_table.keys():
        string_table[current] = count
        output.append(string_table[current[:-1]])
        current = char
        count += 1

print(len(output) + len(string_table))
# print(string_table)