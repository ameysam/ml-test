import numpy as np
import matplotlib.pyplot as plt



def line(model):
    """
    make line and represent in plot
    :param model:
    :return:
    """
    x = np.linspace(0, 4.3)

    x = x[:, None]

    x = np.hstack((np.ones_like(x), x))

    plt.plot(x[:, 1], x @ model, c='k', lw=2)



def rss(model, data):
    """
    calculate and return RSS
    :param model: [[W0], [W1]]
    :param data:
    :return:
    """
    y = data[:, 1]

    x = data[:, 0]

    temp = (y - (model[0][0] + model[1][0] * x))

    error = np.sum(temp.T @ temp)

    return  error


if __name__ == '__main__':

    x = np.array([
        [.5, .6],
        [.7, 1.2],
        [2.2, 2],
        [3, 3.2],
        [1.7, 2],
        [3.7, 4.0],
    ])


    error = 10000

    model = None

    #check if error less than 0.3

    while error > .3:

        W = np.random.rand(2)[:, None]

        model = np.array(W)

        error = rss(model=model, data=x)

    #plot data
    plt.scatter(x[:, 0], x[:, 1])

    #plot model
    line(model)

    plt.show()

    print("RSS error: {}".format(error), '\n')
    print("Model = W0 + W1*X")
    print("W0: {}".format(model[0][0]))
    print("W1: {}".format(model[1][0]))