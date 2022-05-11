import time
import numpy as np

begin = time.time()


def convert_float(nested):
    return [[float(x) for x in lst] for lst in nested]


def convert_int(nested):
    return [[int(x) for x in lst] for lst in nested]


def open_file(file_name):
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


if __name__ == '__main__':
    file_name = input("Enter the name of the file: ")
    open_file(file_name)
    end = time.time()
    print("Time elapsed:", end - begin, 's')
