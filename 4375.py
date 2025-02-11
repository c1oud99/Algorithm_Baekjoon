while True:
    try:
        n = int(input())
        figure = 1
        length = 1
        while figure % n != 0:
            figure = (figure * 10 + 1) % n
            length += 1
        print(length)
    except EOFError:
        break