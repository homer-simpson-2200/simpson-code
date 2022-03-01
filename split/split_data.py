import numpy as np


def split_num_data(how_many, result_data, what_data):
    x_num_train, y_num_train, x_validation_test, y_validation_test, x_next = [], [], [], [], []
    su = how_many + result_data
    x_train_data = np.delete(what_data, (len(what_data)-1, len(what_data)-2))  # this data use for forming x high data
    y_train_data = np.delete(what_data, (len(what_data)-1))  # this data use for forming y high data
    x_val_data = np.delete(what_data, len(what_data)-1)
    y_val_data = what_data
    x_val_data, y_val_data = x_val_data[::-1], y_val_data[::-1]
    for i in range(len(what_data) - su):
        x_num_train.append(x_train_data[i:i + su])
        y_num_train.append(y_train_data[i + su])
    for ii in range(how_many):
        x_validation_test.append(x_val_data[ii])
        x_next.append(y_val_data[ii])
    y_validation_test.append(y_val_data[0])
    x_validation_test = x_validation_test[::-1]
    xnt, ynt, xvt, yvt, xr = np.array(x_num_train), \
        np.array(y_num_train).reshape(-1), np.array(x_validation_test), \
        np.array(y_validation_test).reshape(-1), np.array(x_next)
    xr, xnt, xvt = np.reshape(xr, (xr.shape[0], xr.shape[1], 1)), \
        np.reshape(xnt, (xnt.shape[0], xnt.shape[1], 1)), np.reshape(xvt, (xvt.shape[0], xvt.shape[1], 1))
    return xnt, ynt, xvt, yvt, xr
