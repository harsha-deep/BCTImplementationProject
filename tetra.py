import matplotlib.pyplot as plt
import plotly.graph_objects as go
import numpy as np
import os


def convert_float(nested):
    return [[float(x) for x in lst] for lst in nested]


def convert_int(nested):
    return [[int(x) for x in lst] for lst in nested]


def main(file_name):
    try:
        with open(file_name, 'r') as f:
            line = f.readline()
            lst = line.split(' ')
            no_vertices = int(lst[0])
            no_edges = int(lst[1])
            no_faces = int(lst[2])
            print("Number of vertices:", no_vertices)
            print("Number of edges:", no_edges)
            print("Number of faces:", no_faces)

            vertices = []
            edges = []
            faces = []

            for i in range(no_vertices):
                line = f.readline()
                vertices.append(list(line.replace('\n', '').split(' ')))

            for i in range(no_edges):
                line = f.readline()
                edges.append(list(line.replace('\n', '').split(' ')))

            for i in range(no_faces):
                line = f.readline()
                faces.append(list(line.replace('\n', '').split(' ')))

    except OSError as e:
        print(e.strerror)

    print("vertices:", convert_float(vertices))
    print("edges:", convert_int(edges))
    print("faces:", convert_int(faces))

    try:
        os.mknod('vertices.txt')

    except FileExistsError as e:
        print(e.strerror)

    with open("vertices.txt", "a") as f:
        for lst in vertices:
            f.write(lst[0] + ' '+lst[1] + ' ' + lst[2] + '\n')

    # Make data
    xlist = []
    ylist = []
    zlist = []
    with open("vertices.txt", "r") as f:
        for line in f:
            lst = line.rstrip().split(' ')
            xlist.append(lst[0])
            ylist.append(lst[1])
            zlist.append(lst[2])

    fig = go.Figure(data=[
        go.Mesh3d(
            x=xlist,
            y=ylist,
            z=zlist,
            colorbar_title='z',
            colorscale=[[0, 'gold'],
                        [0.5, 'mediumturquoise'],
                        [1, 'magenta']],
            # Intensity of each vertex, which will be interpolated and color-coded
            intensity=[0, 0.33, 0.66, 1],
            # i, j and k give the vertices of triangles
            # here we represent the 4 triangles of the tetrahedron surface
            i=[0, 0, 0, 1],
            j=[1, 2, 3, 2],
            k=[2, 3, 1, 3],
            name='y',
            showscale=True
        )
    ])

    fig.show()

    os.remove('vertices.txt')


if __name__ == "__main__":
    file_name = input("Enter the name of file: ")
    main(file_name)
