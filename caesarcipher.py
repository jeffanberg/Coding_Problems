# PicoCTF Caesar Cipher problem

cipher = 'ynkooejcpdanqxeykjrbdofgkq'

for x in range(26):
    plain = ''
    for c in cipher:
        var = (ord(c) + x)
        if var > 122:
            var -= 26
        plain += (chr(var))
    print(plain)
