chars = input('Символы для удаления')
add = ';'
try:
    with open('input.txt', 'r') as text_file:
        with open('output.txt', 'w') as txt_file:
            for line in text_file:
                line = line.strip()
                line = line.strip(chars)
                line = line.strip(';')
                line = line[::-1]
                print(line)
                txt_file.write(line + '\n')
except FileNotFoundError:
    print('This file does not exist, please come back later')
