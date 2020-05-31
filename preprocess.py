import numpy as np
from mx3tools import ovftools


def generate_rodriguez():
    data = ovftools.group_unpack('./jdh.out')
    # k, theta = ovftools.to_rodrigues(data)
    # np.savez('rodrigues.npz', k=k, theta=theta)
    np.save('data.npy', data)


if __name__ == "__main__":
    generate_rodriguez()
