names = []
while True:
    try:
        name = input()
    except EOFError:
        break
    names.append(name)

n = len(names)
if n == 1:
    print(f"Adieu, adieu, to {names[0]}")
elif n == 2:
    print(f"Adieu, adieu, to {names[0]} and {names[1]}")
else:
    names[-1] = "and " + names[-1]
    if n == 3:
        print(f"Adieu, adieu, to {', '.join(names)}")
    else:
        print(f"Adieu, adieu, to {', '.join(names[:-1])}, {names[-1]}")
