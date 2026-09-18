with open('input.txt', 'r') as f:
    text = f.read()
print(text)
text1 = ''
i = 0
s = 0
while i < len(text):
    if text[i] in ['а', 'я', 'э', 'е', 'о', 'ё', 'у', 'ю', 'ы', 'и', 'А', 'Я', 'Э', 'Е', 'О', 'Ё', 'У', 'Ю', 'Ы', 'И']:
        if s == 1:
            text1 += text[i] + 'с' + text[i]
        else:
            text1 += text[i]
        s = 0
    else:
        text1 += text[i]
        if text[i] in ['-', ' ', '(', '\"']:
            s = 0
        else:
            s = 1
    i += 1
print(text1)