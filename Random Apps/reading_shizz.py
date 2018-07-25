import re

characters_file = open("characters.py")
data = characters_file.read()
characters_file.close()

print(re.match(r'Bard', data))
