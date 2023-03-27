def draw_triangle(size):
    for i in range(size):
        if i == size-1:
            print((" "*(size-i)) + "/" + (size*"_") + "\\")
        elif i < size:
            print((" "*(size-i)) + "/" + (i*" ") + "\\")


draw_triangle(5)

