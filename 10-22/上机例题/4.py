s = input()
output = ""
for c in s:
    output += chr(ord('A') + (ord(c) - ord('A') + 3) % 26)
print(output)