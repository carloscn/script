import matplotlib.pyplot as plt
import numpy as np
import math

# settings -> python interpreter

def show_zynq_write_performance():
    fig1 = plt.figure(1)

    label_performance = ['10', '50', '100', '150', '200', '500', '1000', '2000']
    y_zynq_enc_soft = [13.15789474, 13.47708895, 12.93661061, 13.04347826,
                       12.91989664, 13.69863014, 14.02721279, 14.89757914]
    y_zynq_enc_hard = [12.98701299, 13.05483029, 13.29787234, 13.06620209,
                       13.13197636, 13.8121547, 14.91646778, 15.0954789]
    y_zynq_plain = [12.65822785, 12.82051282, 13.07189542, 12.9982669,
                    12.93661061, 13.56483993, 14.88981537, 15.94769157]
    plt.xlabel("Block Size (MiB)")
    plt.ylabel("MiB/s")

    x_label = label_performance
    plt.grid(linestyle='-.')
    plt.axis([0, len(label_performance), 10, 18])
    scale_ls = range(len(label_performance))
    plt.plot(scale_ls, y_zynq_enc_soft, '-o', color='r', label='zynq-encrypted-soft', linewidth=1, markersize=8)
    plt.plot(scale_ls, y_zynq_enc_hard, '-*', color='b', label='zynq-encrypted-engine', linewidth=1, markersize=8)
    plt.plot(scale_ls, y_zynq_plain, '-v', color='g', label='zynq-plain', linewidth=1, markersize=8)
    plt.hlines(np.average(y_zynq_enc_soft), 0, len(label_performance), 'r', linestyles='dashed')
    plt.hlines(np.average(y_zynq_enc_hard), 0, len(label_performance), 'b', linestyles='dashed')
    plt.hlines(np.average(y_zynq_plain), 0, len(label_performance), 'g', linestyles='dashed')

    plt.legend()
    plt.xticks(scale_ls, label_performance)
    plt.title("Write Performance speed (MiB/s)")
    plt.show()

def show_zynq_read_performance():
    fig2 = plt.figure(2)
    label_performance = ['10', '50', '100', '150', '200', '500', '1000', '2000']
    y_zynq_enc_soft = [21.73913043, 22.83105023, 22.83105023, 22.83105023,
                       22.83105023, 22.83105023, 22.83626399, 22.83887176]
    y_zynq_enc_hard = [21.73913043, 22.83105023, 22.83105023, 22.83105023,
                       22.83105023, 22.84148013, 22.84148013, 22.84148013]
    y_zynq_plain =    [22.72727273, 22.83105023, 22.83105023, 22.83105023,
                       22.85714286, 22.84148013, 22.84669865, 22.84408909]
    plt.xlabel("Block Size (MiB)")
    plt.ylabel("MiB/s")

    x_label = label_performance
    plt.grid(linestyle='-.')
    plt.axis([0, len(label_performance), 21, 23])
    scale_ls = range(len(label_performance))
    plt.plot(scale_ls, y_zynq_enc_soft, '-o', color='r', label='zynq-encrypted-soft', linewidth=1, markersize=8)
    plt.plot(scale_ls, y_zynq_enc_hard, '-*', color='b', label='zynq-encrypted-engine', linewidth=1, markersize=8)
    plt.plot(scale_ls, y_zynq_plain, '-v', color='g', label='zynq-plain', linewidth=1, markersize=8)
    plt.hlines(np.average(y_zynq_enc_soft), 0, len(label_performance), 'r', linestyles='dashed')
    plt.hlines(np.average(y_zynq_enc_hard), 0, len(label_performance), 'b', linestyles='dashed')
    plt.hlines(np.average(y_zynq_plain), 0, len(label_performance), 'g', linestyles='dashed')

    plt.legend()
    plt.xticks(scale_ls, label_performance)
    plt.title("Read Performance speed (MiB/s)")
    plt.show()

def show_ubuntu_enc_performance():
    fig2 = plt.figure(3)
    label_performance = ['10', '50', '100', '150', '200', '500', '1000', '2000']

    y_ubuntu_enc_soft = [   8.710801394,
                            10.45150502,
                            10.53407774,
                            10.65189604,
                            10.74402364,
                            10.8208713,
                            11.6184501,
                            11.65936013]

    y_ubuntu_plain = [      10.02004008,
                            10,
                            10.09896991,
                            10.02271816,
                            9.946784702,
                            10.82790134,
                            11.10790216,
                            12.18947317]

    plt.xlabel("Block Size (MiB)")
    plt.ylabel("MiB/s")

    x_label = label_performance
    plt.grid(linestyle='-.')
    plt.axis([0, len(label_performance), 5, 13])
    scale_ls = range(len(label_performance))
    plt.plot(scale_ls, y_ubuntu_enc_soft, '-o', color='r', label='ubuntu-encrypted', linewidth=1, markersize=8)
    plt.plot(scale_ls, y_ubuntu_plain, '-*', color='b', label='ubuntu-plain', linewidth=1, markersize=8)
    plt.hlines(np.average(y_ubuntu_enc_soft), 0, len(label_performance), 'r', linestyles='dashed')
    plt.hlines(np.average(y_ubuntu_plain), 0, len(label_performance), 'b', linestyles='dashed')
    print(np.average(y_ubuntu_enc_soft))
    print(np.average(y_ubuntu_plain))

    plt.legend()
    plt.xticks(scale_ls, label_performance)
    plt.title("Write Performance speed (MiB/s)")
    plt.show()


if __name__ == "__main__":
     show_zynq_write_performance()
     show_zynq_read_performance()
     show_ubuntu_enc_performance()
