with open('arab.html', mode='r') as arabic:
    arabic_digits = arabic.read()

with open('english.html', mode='w+') as english:
    for c in arabic_digits:
        c = chr(ord(c) - 1632 + 48) if ord(c) in range(1632, 1642) else c
        english.write(c)
