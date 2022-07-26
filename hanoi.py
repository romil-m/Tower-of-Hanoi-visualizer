import view

model = [[1, 2, 3, 4], [], []]
counter = 0


def hanoi(ndiscs, src, dest, aux):
    global model
    if ndiscs == 1:
        print(model)
        print(f"Move disc from {src+1} to {dest+1}")
        global counter
        counter += 1
        view.moveDisc(model, src, dest)
        model[dest].append(model[src].pop())  # move disc from src to dest
    else:
        hanoi(ndiscs-1, src, aux, dest)
        hanoi(1, src, dest, aux)
        hanoi(ndiscs-1, aux, dest, src)


ndiscs = 4
view.init(model)
hanoi(ndiscs, 0, 2, 1)

print(f"Number of moves: {counter}")
