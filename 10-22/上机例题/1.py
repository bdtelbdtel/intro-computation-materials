s = input()
flag = "YES"
for i in range(len(s)):
    if s[i] >= 'a' and s[i] <='z':
        pass
    else:
        flag = "NO"
print(flag)