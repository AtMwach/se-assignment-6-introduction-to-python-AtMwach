with open('names.txt', 'r') as f:
    content = f.read()
    print(content)


with open('output.txt', 'w') as f: f.write('\n'.join(["Hello", "World", "Python", "Land"]))
