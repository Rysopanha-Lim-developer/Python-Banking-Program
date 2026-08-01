import secrets

otp = ''
for i in range(6):
    a = secrets.randbelow(10)
    otp += str(a)

print(otp)