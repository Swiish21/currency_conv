# Fixed Rate Currency converter(Python)

x = input("Enter currency you have (Ksh/Usd/Euro/Yen/Yuan):\n").lower()
y = input("Enter currency to convert to (Ksh/Usd/Euro/Yen/Yuan):\n").lower()

z = int(input(f"What amount of {x} do you have exactly now:\n"))

ksh_usd = 0.0076
ksh_euro = 0.0070
ksh_yen = 1.16
ksh_yuan = 0.055

usd_ksh = 131.00
usd_euro = 0.92
usd_yen = 151.52
usd_yuan = 7.22

euro_ksh = 141.93
euro_usd = 1.09
euro_yen = 164.16
euro_yuan = 7.82

yen_ksh = 0.86
yen_usd = 0.0066
yen_euro = 0.0061
yen_yuan = 0.048

yuan_ksh = 18.15
yuan_usd = 0.14
yuan_euro = 0.13
yuan_yen = 20.99

if x == "ksh" and y == "usd":
    def converter():
        return ksh_usd * z
print(f"Your currency is worth {converter()}{y}")

if x == "ksh" and y == "euro":
    def converter():
        return ksh_euro * z
print(f"Your currency is worth {converter()}{y}")

if x == "ksh" and y == "yen":
    def converter():
        return ksh_yen * z
print(f"Your currency is worth {converter()}{y}")

if x == "ksh" and y == "yuan":
    def converter():
        return ksh_yuan * z
print(f"Your currency is worth {converter()}{y}")


if x == "usd" and y == "ksh":
    def converter():
        return usd_ksh * z
print(f"Your currency is worth {converter()}{y}")

if x == "usd" and y == "euro":
    def converter():
        return usd_euro * z
print(f"Your currency is worth {converter()}{y}")

if x == "usd" and y == "yen":
    def converter():
        return usd_yen * z
print(f"Your currency is worth {converter()}{y}")

if x == "usd" and y == "yuan":
    def converter():
        return usd_yuan * z
print(f"Your currency is worth {converter()}{y}")


if x == "euro" and y == "ksh":
    def converter():
        return euro_ksh * z
print(f"Your currency is worth {converter()}{y}")

if x == "euro" and y == "usd":
    def converter():
        return euro_usd * z
print(f"Your currency is worth {converter()}{y}")

if x == "euro" and y == "yen":
    def converter():
        return euro_yen * z
print(f"Your currency is worth {converter()}{y}")

if x == "euro" and y == "yuan":
    def converter():
        return euro_yuan * z
print(f"Your currency is worth {converter()}{y}")


if x == "yen" and y == "ksh":
    def converter():
        return yen_ksh * z
print(f"Your currency is worth {converter()}{y}")

if x == "yen" and y == "usd":
    def converter():
        return yen_usd * z
print(f"Your currency is worth {converter()}{y}")

if x == "yen" and y == "euro":
    def converter():
        return yen_euro * z
print(f"Your currency is worth {converter()}{y}")

if x == "yen" and y == "yuan":
    def converter():
        return yen_yuan * z
print(f"Your currency is worth {converter()}{y}")


if x == "yuan" and y == "ksh":
    def converter():
        return yuan_ksh * z
print(f"Your currency is worth {converter()}{y}")

if x == "yuan" and y == "usd":
    def converter():
        return yuan_usd * z
print(f"Your currency is worth {converter()}{y}")

if x == "yuan" and y == "euro":
    def converter():
        return yuan_euro * z
print(f"Your currency is worth {converter()}{y}")

if x == "yuan" and y == "yen":
    def converter():
        return yuan_yen * z
print(f"Your currency is worth {converter()}{y}")
print("Enf of program!!")
