import matplotlib.pyplot as plt

def all_in_one():
    fig, ax = plt.subplots()
    
    x1 = [1, 0, 3, 2, 1]
    y1 = [1, 0, 0, 1, 1]
    #red solid line and square markers
    ax.plot(x1, y1, "-rs")

    x2 = [1, 0, 3, 2, 1]
    y2 = [1.5, 2.5, 2.5, 1.5, 1.5]
    #green dashed circle and circle markers
    ax.plot(x2, y2, "--go")

    x3 = [0, 0, 1, 0]
    y3 = [0.5, 2, 1.25, 0.5]
    #blue dash-dot line and pentagon
    ax.plot(x3, y3, "-.bp")

    x4 = [3, 3, 2, 3]
    y4 = [0.5, 2, 1.25, 0.5]
    #yellow dotted line and star markers
    ax.plot(x4, y4, ":y*")
    
    plt.show()


def one_per_subplot():
    fig, axs = plt.subplots(2, 2)
    
    x1 = [1, 0, 3, 2, 1]
    y1 = [1, 0, 0, 1, 1]
    axs[0,0].plot(x1, y1, "-rs")

    x2 = [1, 0, 3, 2, 1]
    y2 = [1.5, 2.5, 2.5, 1.5, 1.5]
    axs[0,1].plot(x2, y2, "--go")

    x3 = [0, 0, 1, 0]
    y3 = [0.5, 2, 1.25, 0.5]
    axs[1,0].plot(x3, y3, "-.bp")

    x4 = [3, 3, 2, 3]
    y4 = [0.5, 2, 1.25, 0.5]
    axs[1,1].plot(x4, y4, ":y*")
    
    plt.show()

def shapes():
    shapes = []
    shapes.append({"x": [1, 0, 3, 2, 1], "y": [1, 0, 0, 1, 1], "format": "-rs"})
    shapes.append({"x": [1, 0, 3, 2, 1], "y": [1.5, 2.5, 2.5, 1.5, 1.5], "format": "--go"})
    shapes.append({"x": [0, 0, 1, 0], "y": [0.5, 2, 1.25, 0.5], "format": "-.bp"})
    shapes.append({"x": [3, 3, 2, 3], "y": [0.5, 2, 1.25, 0.5], "format": ":y*"})
    return shapes

def with_dict():
    fig, axs = plt.subplots(2, 2)
    shape_list = shapes()
    
    for num in range(4):
        shape = shape_list[num]
        row = int(num/2)
        col = int(num%2)
        axs[row,col].plot(shape["x"], shape["y"], shape["format"])
    
    plt.show()

#all_in_one()
#one_per_subplot()
#with_dict()
