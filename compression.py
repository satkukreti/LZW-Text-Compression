from struct import *

user_file = input("Please enter your input file name: ")
input_file = open(user_file, "r")

user_file_output = input("Please enter your output file name: ")
output_file = open(user_file_output, "wb")

output = []
string_table = {chr(i):i for i in range(32, 127)}
string_table[chr(10)] = 10

rstring_table = {i:chr(i) for i in range(32, 127)}
rstring_table[10] = chr(10)

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
        rstring_table[count] = current
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


print("Testing lossless decryption...\n")

decompressed_data = []

for i in output:
    if i in rstring_table:
        decompressed_data.append(rstring_table[i])

# Join the list of characters into a string
decompressed_text = ''.join(decompressed_data)

# Write the decrypted text to a file
with open("decrypt.txt", "w") as decrypt_file:
    decrypt_file.write(decompressed_text)

print("Decryption completed. Decrypted data written to 'decrypt.txt'.")