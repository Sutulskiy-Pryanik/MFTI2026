with open('input.txt', 'r') as f:
    text = f.read()
i = 0
c = 0    
while i < len(text):
    if text[i] in ['.', '!', '?']:
        i += 2
        c += 1
    i += 1
print(c)