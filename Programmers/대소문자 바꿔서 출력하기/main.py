str = input()
for idx in range(len(str)):
    i = str[idx]
    if ord(i) >= ord('a') and ord(i) <= ord('z'):
        print(chr(ord(i) + ord('A') - ord('a')), end ='')
    elif ord(i) >= ord('A') and ord(i) <= ord('Z'):
        print(chr(ord(i) - ord('A') + ord('a')), end='')