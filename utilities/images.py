import matplotlib.pyplot as plt
from mpl_toolkits.axes_grid1 import AxesGrid


def show_image_grid(images, rows, cols):
    fig = plt.figure(figsize=(10, 10))

    grid = AxesGrid(fig, 111,
                    nrows_ncols=(rows, cols),
                    cbar_mode='single',
                    cbar_location='top',
                    cbar_pad=0.1)

    for i, ax in enumerate(grid):
        ax.set_axis_off()
        im = ax.imshow(images[i])

    ax.cax.colorbar(im)
    plt.show()
