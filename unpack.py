# first, _ = input("What's your name?").split(" ")
# print(f"hello, {first}")

def total(galleons, sickles, knuts):
    return (galleons * 17 + sickles) * 29 + knuts

# print(total(100, 50, 25), "Knuts")

# coins = [100, 50, 25]
# coins = {"galleons": 100, "sickles": 50, "knuts": 25}
# print(total(coins[0], coins[1], coins[2]), "Knuts")

# print(total(coins), "Knuts")

# print(total(*coins), "Knuts")
# print(*coins)

# print(total(galleons = 100, sickles = 50, knuts = 25), "Knuts")
# print(total(coins["galleons"], coins["sickles"], coins["knuts"]), "Knuts")
# print(total(**coins), "Knuts")

def f(*args, **kwargs):
    print("Positional:", args)
    print("Named:", kwargs)

# f(100, 50, 25)
f(galleons = 100, sickles = 50, knuts = 25)

