def palin(s:str) -> bool:
    return s == s[::-1]

def mirr(s:str) -> bool:
    slov = {
        'R':'!',
        'Q':'!',
        'P':'!',
        'N':'!',
        'K':'!',
        'G':'!',
        'F':'!',
        'D':'!',
        'C':'!',
        'B':'!',
        '9':'!',
        '7':'!',
        '6':'!',
        '4':'!',
        '0':'0',
        '8':'8',
        '1':'1',
        'Y':'Y',
        'X':'X',
        'W':'W',
        'v':'V',
        'U':'U',
        'T':'T',
        'O':'O',
        'M':'M',
        'I':'I',
        'H':'H',
        'A':'A',
        'E':'3',
        '3':'E',
        'J':'L',
        'L':'J',
        'Z':'5',
        '5':'Z',
        'S':'2',
        '2':'S'
        }
    s1 = ''
    for a in s:
        s1 += slov[a]
    return s == s1[::-1]
    
s = str(input('строка: '))
if palin(s):
    if mirr(s):
        print(f"{s} is a mirrored palindrome.")
    else:
        print(f"{s} is a regular palindrome.")
else:
    if mirr(s):
        print(f"{s} is a mirrored string.")
    else:
        print(f"{s} is not a palindrome.")