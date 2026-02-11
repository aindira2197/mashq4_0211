# 1
import re
print(bool(re.match(r"\+998\d{9}$", input())))

# 2
email = input()
print("@" in email and "." in email)

# 3
kurs = 12000
usd = float(input())
print(usd * kurs)

# 4
balans = 1000
chiqim = int(input())
balans -= chiqim
print(balans)

# 5
kitoblar = []
kitoblar.append(input())
print(len(kitoblar))
