from struct import *

user_file = input("Please enter your input file name: ")
input_file = open(user_file, "r")

user_file_output = input("Please enter your output file name: ")
output_file = open(user_file_output, "wb")

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
    
    # if len(string_table) > 4096:
    #     break 

    if current not in string_table.keys():
        string_table[current] = count
        output.append(string_table[current[:-1]])
        current = char
        count += 1

stringed_string_table = ''.join(chr(string_table[key]) for key in sorted(string_table.keys()))
output_file.write(pack('>H', len(stringed_string_table)))
output_file.write(stringed_string_table.encode('utf-8'))

for data in output:
    output_file.write(pack('>H', data))

input_file.close()    
output_file.close()