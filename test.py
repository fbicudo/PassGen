from itertools import permutations


s = "abc"

asd = []


p = permutations(s, len(s))

# print(f"Total of {len(p)} possible permutations")

for x in p:
    # print(x)
    new_s = ""
    for c in x:
        new_s = new_s + c
    print(new_s)