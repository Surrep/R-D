import matplotlib.pyplot as plt

from matplotlib.widgets import Slider
from matplotlib.animation import FuncAnimation as animation


def plot(*args):
    plt.plot(*args)
    plt.show()


def imshow(image, legend=True):
    plt.imshow(image, aspect='auto')

    if legend:
        plt.colorbar()

    plt.show()


def imshow_many(images, rows, cols):
    fig, grid = plt.subplots(nrows=rows, ncols=cols, figsize=(10, 10))

    i = 0
    for r in range(rows):
        for c in range(cols):
            grid[r][c].axis('off')
            grid[r][c].imshow(images[i], aspect='auto')
            i += 1

    plt.tight_layout()
    plt.show()


def animate(data, impl, frames, plot_size=13000):
    fig, ax = plt.subplots()
    lines, = plt.plot(0, 0, '.')

    plt.axis([-plot_size, plot_size, -plot_size, plot_size])

    _ = animation(fig=fig,
                  func=lambda step: impl(data, step, lines),
                  init_func=lambda: None,
                  frames=frames,
                  repeat=False,
                  interval=1)

    plt.show()


def slide(data, impl, vals, plot_size=13000):
    figure, axis = plt.subplots()
    lines, = plt.plot(0, 0, '.')

    plt.axis([-plot_size, plot_size, -plot_size, plot_size])

    axamp = plt.axes([0.25, .03, 0.50, 0.02])

    samp = Slider(ax=axamp, label='',
                  valmin=vals[0],
                  valmax=vals[-1],
                  valinit=0,
                  valstep=1)

    samp.on_changed(lambda time_step: impl(data, time_step, lines, figure))

    plt.show()
