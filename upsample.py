from scipy.ndimage import zoom

def upsample (x, cutfrac, outsize=224) :
    assert 0.0<cutfrac<=1.0
    totinsize = x.shape[-1]
    assert totinsize == x.shape[-2]

    insize = round(cutfrac * totinsize)
    rmv = totinsize - insize
    xcut = x[..., rmv//2:-rmv//2][..., rmv//2:-rmv//2, :]

    z = outsize/insize
    z = [1, ] * (len(x.shape)-2) + [z, z, ]

    return zoom(xcut, z)


if __name__ == '__main__' :

    import numpy as np
    from matplotlib import pyplot as plt
    
    rng = np.random.default_rng()

    z = rng.random()
    print(z)
    a = rng.random(size=(4, 106, 106))
    b = upsample(a, z)
    print(b.shape)

    fig, ax = plt.subplots(ncols=2)
    ax[0].imshow(a[0], vmin=0, vmax=1)
    ax[1].imshow(b[0], vmin=0, vmax=1)

    plt.show()
