class counter:
    count = 0

    def __init__(self):
        counter.count += 1

c1 = counter()

c2 = counter()


print(counter.count)
