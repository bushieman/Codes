# write to a text file
file = open('file.txt', 'w') # overwrites anything inside the text file
file.write('Hi there\n')
file.write('My name is bushman\n')
file.write('I am a programmer\n')
file.close()

# also
with open('file.txt', 'w') as file:
    file.write('Hi there\n')
    file.write('My name is bushman\n')
    file.write('I am a programmer\n')
    file.write('And i love solving complex stuffs\n')

# read text file
file = open('file.txt', 'r')
paragraph = file.readlines()
new_paragraph = []
for line in paragraph:
    new_paragraph.append(line.strip())

for line in new_paragraph:
    print(line)
file.close()

with open('file.txt', 'r') as file:
    paragraph = file.readlines()
    new_paragraph = []
    for line in paragraph:
        new_paragraph.append(line.strip())

    for line in new_paragraph:
        print(line)
    file.close()

with open('file.txt', 'rw') as file: # both read & write capabilities
    file.write('longformers are performing better than normal models')
    text = file.read()
