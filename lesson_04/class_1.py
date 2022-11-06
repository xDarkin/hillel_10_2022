names = ["John", "Mary", "Carl"]


def get_name_gen():
    for name in names:
        yield name


gen = get_name_gen()

for n in gen:
    print(n)
