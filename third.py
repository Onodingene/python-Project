a = input("What is your name?")
print(f"Welcome,{a}")
choice = input("Please name your no 1 fine boy in PAU").lower()
sst = ["chisom", "michael", "chike", "kene", "tobe","adrian", "sobe"]
tyd = ["raphael", "oghosa", "cyril", "abdullah", "uche", "rasheed"]

if choice in sst:
    print(f"{choice} is a fine SST boy")
elif choice in tyd:
    print(f"{choice} is a fine boy in TY d")
else:
    print("This boy is not one of the fine boys in TYD or SST")


