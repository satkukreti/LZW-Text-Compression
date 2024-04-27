from struct import *
import copy 

with open("output.txt", "rb") as output_file:
    stringed_string_table_length = unpack('>H', output_file.read(2))[0]
    # print(stringed_string_table_length)
    stringed_string_table = output_file.read(stringed_string_table_length - 1)
    stringed_string_table_copy = copy.deepcopy(stringed_string_table).decode("utf-8")
    print(stringed_string_table)


    string_table = {num: chr(seq) for num, seq in enumerate(stringed_string_table)}

    output = []
    while True:
        data = output_file.read(2)
        if len(data) < 2:
            break
        (unpacked_data,) = unpack('>H', data)
        output.append(unpacked_data)

# print(len(string_table))
print(string_table)

decompressed_file = open("decompressed_file.txt", "w", encoding="utf-8")
for i in output:
    if i in string_table:
        decompressed_file.write(string_table[i])
decompressed_file.close()