words=input().split(" "*7)
morse = [".-", "-...", "-.-.", "-..", ".", "..-.", "--.", "....", "..", ".---", "-.-", ".-..", "--", "-."]
output=""
for w in words:
    chars=w.split(" "*3)
    o=""
    for c in chars:
        for i in range(len(morse)):
            if morse[i] == c:
                o+=chr(ord('a')+i)
    output+=(o+" ")
print(output[:-1])