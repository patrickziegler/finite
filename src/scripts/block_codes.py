from finite import *
import numpy as np


if __name__ == "__main__":
    z2 = FiniteField.factory(modulo=2)

    P = np.array([[1, 1, 0], [0, 1, 1], [1, 1, 1], [1, 0, 1]], dtype=np.int)

    eye = lambda n: np.eye(n, dtype=np.int)

    G = z2.ndmap(np.concatenate((P, eye(4)), axis=1))
    H = z2.ndmap(np.concatenate((eye(3), P), axis=0))

    u = z2.ndmap(np.asarray([1, 0, 1, 0]))
    v = np.dot(u, G)
    r = np.copy(v)

    r[0] = z2(1)  # introducing some error

    s = np.dot(r, H)

    print("Syndrome: " + str(s))
