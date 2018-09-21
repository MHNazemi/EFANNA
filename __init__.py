from KD_Tree import *
from KNN_Graph import *
import random


def main():
    l = []
    for i in range(36100):
        i = []
        for j in range(25):
            i.append(random.randint(0, 255))

        l.append(i)

    import time
    t_s = time.time()
    for i in range(200):
        t = Tree(l, 25, 10).root
    t_e = time.time()
    print(t_e - t_s)


if __name__ == "__main__":
    main()
