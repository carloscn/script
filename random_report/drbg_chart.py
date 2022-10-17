# ,coding,:,utf-8
# /usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import math

###########################data prepare##################################################################

x_l = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
num_ctr = 0
num_hash_sha1 = 1
num_hash_sha224 = 2
num_hash_sha256 = 3
num_hash_sha384 = 4
num_hash_sha512 = 5
num_hmac_sha1 = 6
num_hmac_sha224 = 7
num_hmac_sha256 = 8
num_hmac_sha384 = 9
num_hmac_sha512 = 10

y_norand_nist_s_rate = np.array([0.87,0.94,0.93,0.95,0.93,0.92,0.95,0.92,0.9,0.92,0.92])
y_ave_norand_nist_s_rate = np.average(y_norand_nist_s_rate)
y_ave_norand_nist_s_rate_ctr = np.average(y_norand_nist_s_rate[0:1])
y_ave_norand_nist_s_rate_hash = np.average(y_norand_nist_s_rate[1:6])
y_ave_norand_nist_s_rate_hmac = np.average(y_norand_nist_s_rate[6:11])

y_trng_nist_s_rate = np.array([0.96,0.89,0.9,0.92,0.94,0.89,0.95,0.91,0.86,0.88,0.88])
y_ave_trng_nist_s_rate = np.average(y_trng_nist_s_rate)
y_ave_trng_nist_s_rate_ctr = np.average(y_trng_nist_s_rate[0:1])
y_ave_trng_nist_s_rate_hash = np.average(y_trng_nist_s_rate[1:6])
y_ave_trng_nist_s_rate_hmac = np.average(y_trng_nist_s_rate[6:11])


y_drbg_nist_s_rate = np.array([0.92,0.92,0.96,0.92,0.93,0.95,0.92,0.93,0.93,0.9,0.96])
y_ave_drbg_nist_s_rate = np.average(y_drbg_nist_s_rate)
y_ave_drbg_nist_s_rate_ctr = np.average(y_drbg_nist_s_rate[0:1])
y_ave_drbg_nist_s_rate_hash = np.average(y_drbg_nist_s_rate[1:6])
y_ave_drbg_nist_s_rate_hmac = np.average(y_drbg_nist_s_rate[6:11])

y_norand10_nist_s_rate = np.array( [0.9,0.93,0.88,0.91,0.89,0.91,0.9,0.91,0.91,0.92,0.91])

y_ave_norand10_nist_s_rate = np.average(y_norand10_nist_s_rate)
y_ave_norand10_nist_s_rate_ctr = np.average(y_norand10_nist_s_rate[0:1])
y_ave_norand10_nist_s_rate_hash = np.average(y_norand10_nist_s_rate[1:6])
y_ave_norand10_nist_s_rate_hmac = np.average(y_norand10_nist_s_rate[6:11])

y_norand100_nist_s_rate = np.array([0.97,0.91,0.98,0.9,0.95,0.96,0.92,0.95,0.94,0.92,0.95])
y_ave_norand100_nist_s_rate = np.average(y_norand100_nist_s_rate)
y_ave_norand100_nist_s_rate_ctr = np.average(y_norand100_nist_s_rate[0:1])
y_ave_norand100_nist_s_rate_hash = np.average(y_norand100_nist_s_rate[1:6])
y_ave_norand100_nist_s_rate_hmac = np.average(y_norand100_nist_s_rate[6:11])

y_trng10_nist_s_rate = np.array([0.88,0.95,0.91,0.9,0.91,0.96,0.9,0.93,0.95,0.93,0.95])

y_ave_trng10_nist_s_rate = np.average(y_trng10_nist_s_rate)
y_ave_trng10_nist_s_rate_ctr = np.average(y_trng10_nist_s_rate[0:1])
y_ave_trng10_nist_s_rate_hash = np.average(y_trng10_nist_s_rate[1:6])
y_ave_trng10_nist_s_rate_hmac = np.average(y_trng10_nist_s_rate[6:11])


y_trng100_nist_s_rate = np.array([0.95,0.9,0.9,0.91,0.96,0.91,0.9,0.95,0.92,0.94,0.93])
y_ave_trng100_nist_s_rate = np.average(y_trng100_nist_s_rate)
y_ave_trng100_nist_s_rate_ctr = np.average(y_trng100_nist_s_rate[0:1])
y_ave_trng100_nist_s_rate_hash = np.average(y_trng100_nist_s_rate[1:6])
y_ave_trng100_nist_s_rate_hmac = np.average(y_trng100_nist_s_rate[6:11])

y_drbg10_nist_s_rate = np.array([0.91,0.9,0.95,0.93,0.94,0.94,0.9,0.93,0.91,0.95,0.93])
y_ave_drbg10_nist_s_rate = np.average(y_drbg10_nist_s_rate)
y_ave_drbg10_nist_s_rate_ctr = np.average(y_drbg10_nist_s_rate[0:1])
y_ave_drbg10_nist_s_rate_hash = np.average(y_drbg10_nist_s_rate[1:6])
y_ave_drbg10_nist_s_rate_hmac = np.average(y_drbg10_nist_s_rate[6:11])

y_drbg100_nist_s_rate = np.array([0.94,0.92,0.91,0.92,0.96,0.95,0.93,0.94,0.95,0.92,0.94])
y_ave_drbg100_nist_s_rate = np.average(y_drbg100_nist_s_rate)
y_ave_drbg100_nist_s_rate_ctr = np.average(y_drbg100_nist_s_rate[0:1])
y_ave_drbg100_nist_s_rate_hash = np.average(y_drbg100_nist_s_rate[1:6])
y_ave_drbg100_nist_s_rate_hmac = np.average(y_drbg100_nist_s_rate[6:11])
###########################data prepare##################################################################


label_ctr_list = ['ctr']
label_hash_list = ['sha1', 'sha224', 'sha256', 'sha384', 'sha512']
label_hmac_list = ['.sha1', '.sha224', '.sha256', '.sha384', '.sha512']
x_ctr = range(len(label_ctr_list))
x_hash = range(len(label_hash_list))
x_hmac = range(len(label_hmac_list))


def show_all_nist_rate():
    fig7 = plt.figure(7)
    x_label = []
    x_label = label_ctr_list + label_hash_list + label_hmac_list

    scale_ls = range(11)
    plt.grid()
    plt.axis([-1, 11, 0.75, 1.0])
    plt.plot(scale_ls, y_norand_nist_s_rate, '-o', color='r', label='gauss 1M*re', linewidth=1, markersize=8)
    plt.plot(scale_ls, y_trng_nist_s_rate, '-*', color='b', label='trng 1M*re', linewidth=1, markersize=8)
    plt.plot(scale_ls, y_drbg_nist_s_rate, '-v', color='g', label='drbg 1M*re', linewidth=1, markersize=8)
    plt.hlines(np.average(y_norand_nist_s_rate), -1, 11, 'r', linestyles='dashed')
    plt.hlines(np.average(y_trng_nist_s_rate), -1, 11, 'b', linestyles='dashed')
    plt.hlines(np.average(y_drbg_nist_s_rate), -1, 11, 'g', linestyles='dashed')

    plt.plot(scale_ls, y_norand10_nist_s_rate, '-o', color='y', label='gauss 10K*re', linewidth=1, markersize=8)
    plt.plot(scale_ls, y_trng10_nist_s_rate, '-*', color='c', label='trng 10K*re', linewidth=1, markersize=8)
    plt.plot(scale_ls, y_drbg10_nist_s_rate, '-v', color='m', label='drbg 10K*re', linewidth=1, markersize=8)
    plt.hlines(np.average(y_norand10_nist_s_rate), -1, 11, 'y', linestyles='dashed')
    plt.hlines(np.average(y_trng10_nist_s_rate), -1, 11, 'c', linestyles='dashed')
    plt.hlines(np.average(y_drbg10_nist_s_rate), -1, 11, 'm', linestyles='dashed')


    plt.plot(scale_ls, y_norand100_nist_s_rate, '-o', color='k', label='gauss 100K*re', linewidth=1, markersize=8)
    plt.plot(scale_ls, y_trng100_nist_s_rate, '-*', color='olive', label='trng 100K*re', linewidth=1, markersize=8)
    plt.plot(scale_ls, y_drbg100_nist_s_rate, '-v', color='dodgerblue', label='drbg 100K*re', linewidth=1, markersize=8)
    plt.hlines(np.average(y_norand100_nist_s_rate), -1, 11, 'k', linestyles='dashed')
    plt.hlines(np.average(y_trng100_nist_s_rate), -1, 11, 'olive', linestyles='dashed')
    plt.hlines(np.average(y_drbg100_nist_s_rate), -1, 11, 'dodgerblue', linestyles='dashed')

    plt.legend()  # 设置题注
    plt.xticks(scale_ls, x_label)  ## 可以设置坐标字
    plt.title("Pass rate of Diff reseed")
    plt.show()

    fig8 = plt.figure(8)
    label_list = ["gauss", 'trng', 'drbg', 'gauss.', 'trng.', 'drbg.', 'gauss,', 'trng,','drbg,']
    y_sum_nist_s_rate = [np.average(y_norand_nist_s_rate), np.average(y_trng_nist_s_rate), np.average(y_drbg_nist_s_rate), \
                         np.average(y_norand10_nist_s_rate), np.average(y_trng10_nist_s_rate), np.average(y_drbg10_nist_s_rate), \
                         np.average(y_norand100_nist_s_rate), np.average(y_trng100_nist_s_rate),np.average(y_drbg100_nist_s_rate) ]
    recta = plt.bar(label_list[0:3], y_sum_nist_s_rate[0:3], width=0.4, alpha=0.8, color='green', label="Reseed-1M")
    rectb = plt.bar(label_list[3:6], y_sum_nist_s_rate[3:6], width=0.4, alpha=0.8, color='red', label="Reseed-10K")
    rectc = plt.bar(label_list[6:9], y_sum_nist_s_rate[6:9], width=0.4, alpha=0.8, color='blue', label="Reseed-100K")
    ave_a = (np.average(y_norand_nist_s_rate) + np.average(y_trng_nist_s_rate) + np.average(y_drbg_nist_s_rate) ) / 3
    ave_b = (np.average(y_norand10_nist_s_rate) + np.average(y_trng10_nist_s_rate) + np.average(y_drbg10_nist_s_rate)) / 3
    ave_c = (np.average(y_norand100_nist_s_rate) + np.average(y_trng100_nist_s_rate) + np.average(y_drbg100_nist_s_rate)) / 3
    plt.hlines(ave_a, -1, 11, 'g', linestyles='dashed')
    plt.hlines(ave_b, -1, 11, 'r', linestyles='dashed')
    plt.hlines(ave_c, -1, 11, 'b', linestyles='dashed')
    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 9, 0.9, 0.95])
    plt.title("Reseed para impact")
    plt.grid()
    plt.legend()  # 设置题注

    for rect in recta:
        height = round(rect.get_height(),3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rectb:
        height = round(rect.get_height(),3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rectc:
        height = round(rect.get_height(),3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    plt.show()

    fig9 = plt.figure(9)
    label_list = ["1M*re", '10k*re', '100k*re', \
                  '1M*re.', '10K*re.', '100K*re.',  \
                  '.1M*re', '.10K*re','.100K*re']
    y_sum_nist_s_rate = [np.average(y_norand_nist_s_rate), np.average(y_norand10_nist_s_rate), np.average(y_norand100_nist_s_rate), \
                         np.average(y_trng_nist_s_rate), np.average(y_trng10_nist_s_rate), np.average(y_trng100_nist_s_rate), \
                         np.average(y_drbg_nist_s_rate), np.average(y_drbg10_nist_s_rate),np.average(y_drbg100_nist_s_rate) ]
    recta = plt.bar(label_list[0:3], y_sum_nist_s_rate[0:3], width=0.4, alpha=0.8, color='green', label="Guass")
    rectb = plt.bar(label_list[3:6], y_sum_nist_s_rate[3:6], width=0.4, alpha=0.8, color='red', label="TRNG")
    rectc = plt.bar(label_list[6:9], y_sum_nist_s_rate[6:9], width=0.4, alpha=0.8, color='blue', label="DRBG")
    ave_a = (np.average(y_norand_nist_s_rate) + np.average(y_norand10_nist_s_rate) + np.average(y_norand100_nist_s_rate) ) / 3
    ave_b = (np.average(y_trng_nist_s_rate) + np.average(y_trng10_nist_s_rate) + np.average(y_trng100_nist_s_rate)) / 3
    ave_c = (np.average(y_drbg_nist_s_rate) + np.average(y_drbg10_nist_s_rate) + np.average(y_drbg100_nist_s_rate)) / 3
    plt.hlines(ave_a, -1, 11, 'g', linestyles='dashed')
    plt.hlines(ave_b, -1, 11, 'r', linestyles='dashed')
    plt.hlines(ave_c, -1, 11, 'b', linestyles='dashed')
    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 9, 0.9, 0.95])
    plt.title("Reseed para impact")
    plt.grid()
    plt.legend()  # 设置题注

    for rect in recta:
        height = round(rect.get_height(),3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rectb:
        height = round(rect.get_height(),3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rectc:
        height = round(rect.get_height(),3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    plt.show()

def show_norand1m_nist_pass_rate():
    # NORAND DRBG NIST
    fig1 = plt.figure(1)
    plt.grid(linestyle='-.')
    # plt.plot(x_l,y_norand_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
    # plt.plot(x_l, y_norand_nist_p_rate, 'b-*',label='P rate', linewidth=2, markersize=6)
    # plt.plot(x_l,y_norand_nist_a_rate,'g-v',label='mag', linewidth=2, markersize=6)
    # plt.plot(x_l, y_norand_nist_s_rate, 'y-^',label='mag', linewidth=2, markersize=6)
    rects_ctr = plt.bar(label_ctr_list, y_norand_nist_s_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
    rects_hash = plt.bar(label_hash_list, y_norand_nist_s_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
    rects_hmac = plt.bar(label_hmac_list, y_norand_nist_s_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
    # plt.plot(x_l,y_norand_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
    plt.hlines(y_ave_norand_nist_s_rate_ctr, -1, 11, 'g', linestyles='dashed')
    plt.hlines(y_ave_norand_nist_s_rate_hash, -1, 11, 'r', linestyles='dashed')
    plt.hlines(y_ave_norand_nist_s_rate_hmac, -1, 11, 'b', linestyles='dashed')
    plt.text(11, y_ave_norand_nist_s_rate_ctr - 0.003, str(y_ave_norand_nist_s_rate_ctr), fontsize=10, color="green")
    plt.text(11, y_ave_norand_nist_s_rate_hash - 0.003, str(y_ave_norand_nist_s_rate_hash), fontsize=10, color="red")
    plt.text(11, y_ave_norand_nist_s_rate_hmac - 0.003, str(y_ave_norand_nist_s_rate_hmac), fontsize=10, color="blue")
    xdata, ydata = 5, 0

    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 11, 0.8, 1.0])
    plt.title("SM Pass Rate of DRBG(No Random Number as Seed*1MB)")
    plt.legend()  # 设置题注

    for rect in rects_ctr:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hash:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hmac:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    plt.show()





def show_trng1m_nist_pass_rate():
    ###############trng
    fig3 = plt.figure(3)
    plt.grid(linestyle='-.')

    rects_ctr = plt.bar(label_ctr_list, y_trng_nist_s_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
    rects_hash = plt.bar(label_hash_list, y_trng_nist_s_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
    rects_hmac = plt.bar(label_hmac_list, y_trng_nist_s_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
    # plt.plot(x_l,y_trng_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
    plt.hlines(y_ave_trng_nist_s_rate_ctr, -1, 11, 'g', linestyles='dashed')
    plt.scatter([1.5], [-0.25], s=25, c='r')
    plt.hlines(y_ave_trng_nist_s_rate_hash, -1, 11, 'r', linestyles='dashed')
    plt.hlines(y_ave_trng_nist_s_rate_hmac, -1, 11, 'b', linestyles='dashed')
    plt.text(11, y_ave_trng_nist_s_rate_ctr - 0.003, str(y_ave_trng_nist_s_rate_ctr), fontsize=10, color="green")
    plt.text(11, y_ave_trng_nist_s_rate_hash - 0.003, str(y_ave_trng_nist_s_rate_hash), fontsize=10, color="red")
    plt.text(11, y_ave_trng_nist_s_rate_hmac - 0.003, str(y_ave_trng_nist_s_rate_hmac), fontsize=10, color="blue")
    xdata, ydata = 5, 0

    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 11, 0.8, 1.0])
    plt.title("SM Pass Rate of DRBG(TRNG as Seed * 1MB)")
    plt.legend()  # 设置题注

    for rect in rects_ctr:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hash:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hmac:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    plt.show()

def show_sum1m_nist_pass_rate():
    ###############trng
    fig3 = plt.figure(3)
    plt.grid(linestyle='-.')
    y_sum_nist_s_rate = [0,0,0,0,0,0,0,0,0,0,0]

    y_sum_nist_s_rate[num_ctr] = (y_trng_nist_s_rate[num_ctr] + y_drbg_nist_s_rate[num_ctr] + y_norand_nist_s_rate[num_ctr])/3
    y_sum_nist_s_rate[num_hash_sha1] = (y_trng_nist_s_rate[num_hash_sha1] + y_drbg_nist_s_rate[num_hash_sha1] + y_norand_nist_s_rate[num_hash_sha1] )/3
    y_sum_nist_s_rate[num_hash_sha224] = (y_trng_nist_s_rate[num_hash_sha224] + y_drbg_nist_s_rate[num_hash_sha224] + y_norand_nist_s_rate[num_hash_sha224])/3
    y_sum_nist_s_rate[num_hash_sha256] = (y_trng_nist_s_rate[num_hash_sha256] + y_drbg_nist_s_rate[num_hash_sha256] + y_norand_nist_s_rate[num_hash_sha256])/3
    y_sum_nist_s_rate[num_hash_sha384] = (y_trng_nist_s_rate[num_hash_sha384] + y_drbg_nist_s_rate[num_hash_sha384] + y_norand_nist_s_rate[num_hash_sha384])/3
    y_sum_nist_s_rate[num_hash_sha512] = (y_trng_nist_s_rate[num_hash_sha512] + y_drbg_nist_s_rate[num_hash_sha512] + y_norand_nist_s_rate[num_hash_sha512])/3
    y_sum_nist_s_rate[num_hmac_sha1] = (y_trng_nist_s_rate[num_hmac_sha1] + y_drbg_nist_s_rate[num_hmac_sha1] + y_norand_nist_s_rate[num_hmac_sha1])/3
    y_sum_nist_s_rate[num_hmac_sha224] = (y_trng_nist_s_rate[num_hmac_sha224] + y_drbg_nist_s_rate[num_hmac_sha224] + y_norand_nist_s_rate[num_hmac_sha224])/3
    y_sum_nist_s_rate[num_hmac_sha256] = (y_trng_nist_s_rate[num_hmac_sha256] + y_drbg_nist_s_rate[num_hmac_sha256] + y_norand_nist_s_rate[num_hmac_sha256])/3
    y_sum_nist_s_rate[num_hmac_sha384] = (y_trng_nist_s_rate[num_hmac_sha384] + y_drbg_nist_s_rate[num_hmac_sha384] + y_norand_nist_s_rate[num_hmac_sha384])/3
    y_sum_nist_s_rate[num_hmac_sha512] = (y_trng_nist_s_rate[num_hmac_sha512] + y_drbg_nist_s_rate[num_hmac_sha512] + y_norand_nist_s_rate[num_hmac_sha512])/3

    y_ave_sum_nist_s_rate_ctr = round( y_sum_nist_s_rate[num_ctr] ,3)
    y_ave_sum_nist_s_rate_hash = round( np.average(y_sum_nist_s_rate[1:6]), 3)
    y_ave_sum_nist_s_rate_hmac = round( np.average(y_sum_nist_s_rate[6:11]), 3)

    rects_ctr = plt.bar(label_ctr_list, y_sum_nist_s_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
    rects_hash = plt.bar(label_hash_list, y_sum_nist_s_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
    rects_hmac = plt.bar(label_hmac_list, y_sum_nist_s_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
    # plt.plot(x_l,y_trng_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
    plt.hlines(y_ave_sum_nist_s_rate_ctr, -1, 11, 'g', linestyles='dashed')
    plt.scatter([1.5], [-0.25], s=25, c='r')
    plt.hlines(y_ave_sum_nist_s_rate_hash, -1, 11, 'r', linestyles='dashed')
    plt.hlines(y_ave_sum_nist_s_rate_hmac, -1, 11, 'b', linestyles='dashed')
    plt.text(11, y_ave_sum_nist_s_rate_ctr - 0.003, str(y_ave_trng_nist_s_rate_ctr), fontsize=10, color="green")
    plt.text(11, y_ave_sum_nist_s_rate_hash - 0.003, str(y_ave_trng_nist_s_rate_hash), fontsize=10, color="red")
    plt.text(11, y_ave_sum_nist_s_rate_hmac - 0.003, str(y_ave_trng_nist_s_rate_hmac), fontsize=10, color="blue")
    xdata, ydata = 5, 0

    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 11, 0.8, 1.0])
    plt.title("SM Pass Rate of DRBG(SUM * 10KB)")
    plt.legend()  # 设置题注

    for rect in rects_ctr:
        height = round(rect.get_height(),3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hash:
        height =  round(rect.get_height(),3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hmac:
        height =  round(rect.get_height(),3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    plt.show()





def show_drbg1m_nist_pass_rate():
    # DRBG DRBG NIST
    fig5 = plt.figure(5)
    plt.grid(linestyle='-.')

    rects_ctr = plt.bar(label_ctr_list, y_drbg_nist_s_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
    rects_hash = plt.bar(label_hash_list, y_drbg_nist_s_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
    rects_hmac = plt.bar(label_hmac_list, y_drbg_nist_s_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
    # plt.plot(x_l,y_trng_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
    plt.hlines(y_ave_drbg_nist_s_rate_ctr, -1, 11, 'g', linestyles='dashed')
    plt.hlines(y_ave_drbg_nist_s_rate_hash, -1, 11, 'r', linestyles='dashed')
    plt.hlines(y_ave_drbg_nist_s_rate_hmac, -1, 11, 'b', linestyles='dashed')
    plt.text(11, y_ave_drbg_nist_s_rate_ctr - 0.003, str(y_ave_drbg_nist_s_rate_ctr), fontsize=10, color="green")
    plt.text(11, y_ave_drbg_nist_s_rate_hash - 0.003, str(y_ave_drbg_nist_s_rate_hash), fontsize=10, color="red")
    plt.text(11, y_ave_drbg_nist_s_rate_hmac - 0.003, str(y_ave_drbg_nist_s_rate_hmac), fontsize=10, color="blue")
    xdata, ydata = 5, 0

    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 11, 0.875, 1.0])
    plt.title("SM Pass Rate of DRBG(DRBG as Seed * 1MB)")
    plt.legend()  # 设置题注

    for rect in rects_ctr:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hash:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hmac:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    plt.show()








def show_norand10_nist_pass_rate():
    # NORAND DRBG NIST
    fig1 = plt.figure(1)
    plt.grid(linestyle='-.')
    rects_ctr = plt.bar(label_ctr_list, y_norand10_nist_s_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
    rects_hash = plt.bar(label_hash_list, y_norand10_nist_s_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
    rects_hmac = plt.bar(label_hmac_list, y_norand10_nist_s_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
    # plt.plot(x_l,y_norand10_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
    plt.hlines(y_ave_norand10_nist_s_rate_ctr, -1, 11, 'g', linestyles='dashed')
    plt.hlines(y_ave_norand10_nist_s_rate_hash, -1, 11, 'r', linestyles='dashed')
    plt.hlines(y_ave_norand10_nist_s_rate_hmac, -1, 11, 'b', linestyles='dashed')
    plt.text(11, y_ave_norand10_nist_s_rate_ctr - 0.003, str(y_ave_norand10_nist_s_rate_ctr), fontsize=10, color="green")
    plt.text(11, y_ave_norand10_nist_s_rate_hash - 0.003, str(y_ave_norand10_nist_s_rate_hash), fontsize=10, color="red")
    plt.text(11, y_ave_norand10_nist_s_rate_hmac - 0.003, str(y_ave_norand10_nist_s_rate_hmac), fontsize=10, color="blue")
    xdata, ydata = 5, 0

    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 11, 0.8, 1.0])
    plt.title("SM Pass Rate of DRBG(No Random Number as Seed*10KB)")
    plt.legend()  # 设置题注

    for rect in rects_ctr:
        height = round(rect.get_height(), 3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hash:
        height = round(rect.get_height(), 3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hmac:
        height = round( rect.get_height(), 3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    plt.show()





def show_trng10_nist_pass_rate():
    ###############trng
    fig3 = plt.figure(3)
    plt.grid(linestyle='-.')

    rects_ctr = plt.bar(label_ctr_list, y_trng10_nist_s_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
    rects_hash = plt.bar(label_hash_list, y_trng10_nist_s_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
    rects_hmac = plt.bar(label_hmac_list, y_trng10_nist_s_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
    # plt.plot(x_l,y_trng10_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
    plt.hlines(y_ave_trng10_nist_s_rate_ctr, -1, 11, 'g', linestyles='dashed')
    plt.scatter([1.5], [-0.25], s=25, c='r')
    plt.hlines(y_ave_trng10_nist_s_rate_hash, -1, 11, 'r', linestyles='dashed')
    plt.hlines(y_ave_trng10_nist_s_rate_hmac, -1, 11, 'b', linestyles='dashed')
    plt.text(11, y_ave_trng10_nist_s_rate_ctr - 0.003, str(y_ave_trng10_nist_s_rate_ctr), fontsize=10, color="green")
    plt.text(11, y_ave_trng10_nist_s_rate_hash - 0.003, str(y_ave_trng10_nist_s_rate_hash), fontsize=10, color="red")
    plt.text(11, y_ave_trng10_nist_s_rate_hmac - 0.003, str(y_ave_trng10_nist_s_rate_hmac), fontsize=10, color="blue")
    xdata, ydata = 5, 0

    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 11, 0.8, 1.0])
    plt.title("SM Pass Rate of DRBG(TRNG as Seed * 10K)")
    plt.legend()  # 设置题注

    for rect in rects_ctr:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hash:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hmac:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    plt.show()




def show_sum10_nist_pass_rate():
    ###############trng
    fig3 = plt.figure(3)
    plt.grid(linestyle='-.')
    y_sum_nist_s_rate = [0,0,0,0,0,0,0,0,0,0,0]

    y_sum_nist_s_rate[num_ctr] = (y_trng10_nist_s_rate[num_ctr] + y_drbg10_nist_s_rate[num_ctr] + y_norand10_nist_s_rate[num_ctr])/3
    y_sum_nist_s_rate[num_hash_sha1] = (y_trng10_nist_s_rate[num_hash_sha1] + y_drbg10_nist_s_rate[num_hash_sha1] + y_norand10_nist_s_rate[num_hash_sha1] )/3
    y_sum_nist_s_rate[num_hash_sha224] = (y_trng10_nist_s_rate[num_hash_sha224] + y_drbg10_nist_s_rate[num_hash_sha224] + y_norand10_nist_s_rate[num_hash_sha224])/3
    y_sum_nist_s_rate[num_hash_sha256] = (y_trng10_nist_s_rate[num_hash_sha256] + y_drbg10_nist_s_rate[num_hash_sha256] + y_norand10_nist_s_rate[num_hash_sha256])/3
    y_sum_nist_s_rate[num_hash_sha384] = (y_trng10_nist_s_rate[num_hash_sha384] + y_drbg10_nist_s_rate[num_hash_sha384] + y_norand10_nist_s_rate[num_hash_sha384])/3
    y_sum_nist_s_rate[num_hash_sha512] = (y_trng10_nist_s_rate[num_hash_sha512] + y_drbg10_nist_s_rate[num_hash_sha512] + y_norand10_nist_s_rate[num_hash_sha512])/3
    y_sum_nist_s_rate[num_hmac_sha1] = (y_trng10_nist_s_rate[num_hmac_sha1] + y_drbg10_nist_s_rate[num_hmac_sha1] + y_norand10_nist_s_rate[num_hmac_sha1])/3
    y_sum_nist_s_rate[num_hmac_sha224] = (y_trng10_nist_s_rate[num_hmac_sha224] + y_drbg10_nist_s_rate[num_hmac_sha224] + y_norand10_nist_s_rate[num_hmac_sha224])/3
    y_sum_nist_s_rate[num_hmac_sha256] = (y_trng10_nist_s_rate[num_hmac_sha256] + y_drbg10_nist_s_rate[num_hmac_sha256] + y_norand10_nist_s_rate[num_hmac_sha256])/3
    y_sum_nist_s_rate[num_hmac_sha384] = (y_trng10_nist_s_rate[num_hmac_sha384] + y_drbg10_nist_s_rate[num_hmac_sha384] + y_norand10_nist_s_rate[num_hmac_sha384])/3
    y_sum_nist_s_rate[num_hmac_sha512] = (y_trng10_nist_s_rate[num_hmac_sha512] + y_drbg10_nist_s_rate[num_hmac_sha512] + y_norand10_nist_s_rate[num_hmac_sha512])/3
    print(y_sum_nist_s_rate)
    y_ave_sum_nist_s_rate_ctr = y_sum_nist_s_rate[num_ctr]
    print(y_ave_sum_nist_s_rate_ctr)
    y_ave_sum_nist_s_rate_hash = np.average(y_sum_nist_s_rate[1:6])
    print(y_ave_sum_nist_s_rate_hash)
    y_ave_sum_nist_s_rate_hmac = np.average(y_sum_nist_s_rate[6:11])
    print(y_ave_sum_nist_s_rate_hmac)

    rects_ctr = plt.bar(label_ctr_list, y_sum_nist_s_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
    rects_hash = plt.bar(label_hash_list, y_sum_nist_s_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
    rects_hmac = plt.bar(label_hmac_list, y_sum_nist_s_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
    # plt.plot(x_l,y_trng_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
    plt.hlines(y_ave_sum_nist_s_rate_ctr, -1, 11, 'g', linestyles='dashed')
    plt.scatter([1.5], [-0.25], s=25, c='r')
    plt.hlines(y_ave_sum_nist_s_rate_hash, -1, 11, 'r', linestyles='dashed')
    plt.hlines(y_ave_sum_nist_s_rate_hmac, -1, 11, 'b', linestyles='dashed')
    plt.text(11, y_ave_sum_nist_s_rate_ctr - 0.003, str(y_ave_trng_nist_s_rate_ctr), fontsize=10, color="green")
    plt.text(11, y_ave_sum_nist_s_rate_hash - 0.003, str(y_ave_trng_nist_s_rate_hash), fontsize=10, color="red")
    plt.text(11, y_ave_sum_nist_s_rate_hmac - 0.003, str(y_ave_trng_nist_s_rate_hmac), fontsize=10, color="blue")
    xdata, ydata = 5, 0

    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 11, 0.8, 1.0])
    plt.title("SM Pass Rate of DRBG(Reseed * 10K)")
    plt.legend()  # 设置题注

    for rect in rects_ctr:
        height = round(rect.get_height(),3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hash:
        height =  round(rect.get_height(),3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hmac:
        height =  round(rect.get_height(),3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    plt.show()




def show_drbg10_nist_pass_rate():
    # DRBG DRBG NIST
    fig5 = plt.figure(5)
    plt.grid(linestyle='-.')

    rects_ctr = plt.bar(label_ctr_list, y_drbg10_nist_s_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
    rects_hash = plt.bar(label_hash_list, y_drbg10_nist_s_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
    rects_hmac = plt.bar(label_hmac_list, y_drbg10_nist_s_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
    # plt.plot(x_l,y_trng_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
    plt.hlines(y_ave_drbg10_nist_s_rate_ctr, -1, 11, 'g', linestyles='dashed')
    plt.hlines(y_ave_drbg10_nist_s_rate_hash, -1, 11, 'r', linestyles='dashed')
    plt.hlines(y_ave_drbg10_nist_s_rate_hmac, -1, 11, 'b', linestyles='dashed')
    plt.text(11, y_ave_drbg10_nist_s_rate_ctr - 0.003, str(y_ave_drbg10_nist_s_rate_ctr), fontsize=10, color="green")
    plt.text(11, y_ave_drbg10_nist_s_rate_hash - 0.003, str(y_ave_drbg10_nist_s_rate_hash), fontsize=10, color="red")
    plt.text(11, y_ave_drbg10_nist_s_rate_hmac - 0.003, str(y_ave_drbg10_nist_s_rate_hmac), fontsize=10, color="blue")
    xdata, ydata = 5, 0

    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 11, 0.8, 1.0])
    plt.title("SM Pass Rate of DRBG(DRBG as Seed * 10K)")
    plt.legend()  # 设置题注

    for rect in rects_ctr:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hash:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hmac:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    plt.show()





def show_norand100_nist_pass_rate():
    # NORAND DRBG NIST
    fig1 = plt.figure(1)
    plt.grid(linestyle='-.')
    rects_ctr = plt.bar(label_ctr_list, y_norand100_nist_s_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
    rects_hash = plt.bar(label_hash_list, y_norand100_nist_s_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
    rects_hmac = plt.bar(label_hmac_list, y_norand100_nist_s_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
    # plt.plot(x_l,y_norand100_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
    plt.hlines(y_ave_norand100_nist_s_rate_ctr, -1, 11, 'g', linestyles='dashed')
    plt.hlines(y_ave_norand100_nist_s_rate_hash, -1, 11, 'r', linestyles='dashed')
    plt.hlines(y_ave_norand100_nist_s_rate_hmac, -1, 11, 'b', linestyles='dashed')
    plt.text(11, y_ave_norand100_nist_s_rate_ctr - 0.003, str(y_ave_norand100_nist_s_rate_ctr), fontsize=10, color="green")
    plt.text(11, y_ave_norand100_nist_s_rate_hash - 0.003, str(y_ave_norand100_nist_s_rate_hash), fontsize=10, color="red")
    plt.text(11, y_ave_norand100_nist_s_rate_hmac - 0.003, str(y_ave_norand100_nist_s_rate_hmac), fontsize=10, color="blue")
    xdata, ydata = 5, 0

    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 11, 0.8, 1.0])
    plt.title("SM Pass Rate of DRBG(No Random Number as Seed * 100K)")
    plt.legend()  # 设置题注

    for rect in rects_ctr:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hash:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hmac:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    plt.show()





def show_trng100_nist_pass_rate():
    ###############trng
    fig3 = plt.figure(3)
    plt.grid(linestyle='-.')

    rects_ctr = plt.bar(label_ctr_list, y_trng100_nist_s_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
    rects_hash = plt.bar(label_hash_list, y_trng100_nist_s_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
    rects_hmac = plt.bar(label_hmac_list, y_trng100_nist_s_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
    # plt.plot(x_l,y_trng100_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
    plt.hlines(y_ave_trng100_nist_s_rate_ctr, -1, 11, 'g', linestyles='dashed')
    plt.scatter([1.5], [-0.25], s=25, c='r')
    plt.hlines(y_ave_trng100_nist_s_rate_hash, -1, 11, 'r', linestyles='dashed')
    plt.hlines(y_ave_trng100_nist_s_rate_hmac, -1, 11, 'b', linestyles='dashed')
    plt.text(11, y_ave_trng100_nist_s_rate_ctr - 0.003, str(y_ave_trng100_nist_s_rate_ctr), fontsize=10, color="green")
    plt.text(11, y_ave_trng100_nist_s_rate_hash - 0.003, str(y_ave_trng100_nist_s_rate_hash), fontsize=10, color="red")
    plt.text(11, y_ave_trng100_nist_s_rate_hmac - 0.003, str(y_ave_trng100_nist_s_rate_hmac), fontsize=10, color="blue")
    xdata, ydata = 5, 0

    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 11, 0.8, 1.0])
    plt.title("SM Pass Rate of DRBG(TRNG as Seed * 100K)")
    plt.legend()  # 设置题注

    for rect in rects_ctr:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hash:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hmac:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    plt.show()





def show_drbg100_nist_pass_rate():
    # DRBG DRBG NIST
    fig5 = plt.figure(5)
    plt.grid(linestyle='-.')

    rects_ctr = plt.bar(label_ctr_list, y_drbg100_nist_s_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
    rects_hash = plt.bar(label_hash_list, y_drbg100_nist_s_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
    rects_hmac = plt.bar(label_hmac_list, y_drbg100_nist_s_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
    # plt.plot(x_l,y_trng_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
    plt.hlines(y_ave_drbg100_nist_s_rate_ctr, -1, 11, 'g', linestyles='dashed')
    plt.hlines(y_ave_drbg100_nist_s_rate_hash, -1, 11, 'r', linestyles='dashed')
    plt.hlines(y_ave_drbg100_nist_s_rate_hmac, -1, 11, 'b', linestyles='dashed')
    plt.text(11, y_ave_drbg100_nist_s_rate_ctr - 0.003, str(y_ave_drbg100_nist_s_rate_ctr), fontsize=10, color="green")
    plt.text(11, y_ave_drbg100_nist_s_rate_hash - 0.003, str(y_ave_drbg100_nist_s_rate_hash), fontsize=10, color="red")
    plt.text(11, y_ave_drbg100_nist_s_rate_hmac - 0.003, str(y_ave_drbg100_nist_s_rate_hmac), fontsize=10, color="blue")
    xdata, ydata = 5, 0

    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 11, 0.8, 1.0])
    plt.title("SM Pass Rate of DRBG(DRBG as Seed * 100K)")
    plt.legend()  # 设置题注

    for rect in rects_ctr:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hash:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hmac:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    plt.show()


def show_sum100_nist_pass_rate():
    ###############trng
    fig3 = plt.figure(3)
    plt.grid(linestyle='-.')
    y_sum_nist_s_rate = [0,0,0,0,0,0,0,0,0,0,0]

    y_sum_nist_s_rate[num_ctr] = (y_trng100_nist_s_rate[num_ctr] + y_drbg100_nist_s_rate[num_ctr] + y_norand100_nist_s_rate[num_ctr])/3
    y_sum_nist_s_rate[num_hash_sha1] = (y_trng100_nist_s_rate[num_hash_sha1] + y_drbg100_nist_s_rate[num_hash_sha1] + y_norand100_nist_s_rate[num_hash_sha1] )/3
    y_sum_nist_s_rate[num_hash_sha224] = (y_trng100_nist_s_rate[num_hash_sha224] + y_drbg100_nist_s_rate[num_hash_sha224] + y_norand100_nist_s_rate[num_hash_sha224])/3
    y_sum_nist_s_rate[num_hash_sha256] = (y_trng100_nist_s_rate[num_hash_sha256] + y_drbg100_nist_s_rate[num_hash_sha256] + y_norand100_nist_s_rate[num_hash_sha256])/3
    y_sum_nist_s_rate[num_hash_sha384] = (y_trng100_nist_s_rate[num_hash_sha384] + y_drbg100_nist_s_rate[num_hash_sha384] + y_norand100_nist_s_rate[num_hash_sha384])/3
    y_sum_nist_s_rate[num_hash_sha512] = (y_trng100_nist_s_rate[num_hash_sha512] + y_drbg100_nist_s_rate[num_hash_sha512] + y_norand100_nist_s_rate[num_hash_sha512])/3
    y_sum_nist_s_rate[num_hmac_sha1] = (y_trng100_nist_s_rate[num_hmac_sha1] + y_drbg100_nist_s_rate[num_hmac_sha1] + y_norand100_nist_s_rate[num_hmac_sha1])/3
    y_sum_nist_s_rate[num_hmac_sha224] = (y_trng100_nist_s_rate[num_hmac_sha224] + y_drbg100_nist_s_rate[num_hmac_sha224] + y_norand100_nist_s_rate[num_hmac_sha224])/3
    y_sum_nist_s_rate[num_hmac_sha256] = (y_trng100_nist_s_rate[num_hmac_sha256] + y_drbg100_nist_s_rate[num_hmac_sha256] + y_norand100_nist_s_rate[num_hmac_sha256])/3
    y_sum_nist_s_rate[num_hmac_sha384] = (y_trng100_nist_s_rate[num_hmac_sha384] + y_drbg100_nist_s_rate[num_hmac_sha384] + y_norand100_nist_s_rate[num_hmac_sha384])/3
    y_sum_nist_s_rate[num_hmac_sha512] = (y_trng100_nist_s_rate[num_hmac_sha512] + y_drbg100_nist_s_rate[num_hmac_sha512] + y_norand100_nist_s_rate[num_hmac_sha512])/3
    print(y_sum_nist_s_rate)
    y_ave_sum_nist_s_rate_ctr = round( y_sum_nist_s_rate[num_ctr] ,3)
    y_ave_sum_nist_s_rate_hash = round( np.average(y_sum_nist_s_rate[1:6]), 3)
    y_ave_sum_nist_s_rate_hmac = round( np.average(y_sum_nist_s_rate[6:11]), 3)

    rects_ctr = plt.bar(label_ctr_list, y_sum_nist_s_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
    rects_hash = plt.bar(label_hash_list, y_sum_nist_s_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
    rects_hmac = plt.bar(label_hmac_list, y_sum_nist_s_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
    # plt.plot(x_l,y_trng_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
    plt.hlines(y_ave_sum_nist_s_rate_ctr, -1, 11, 'g', linestyles='dashed')
    plt.scatter([1.5], [-0.25], s=25, c='r')
    plt.hlines(y_ave_sum_nist_s_rate_hash, -1, 11, 'r', linestyles='dashed')
    plt.hlines(y_ave_sum_nist_s_rate_hmac, -1, 11, 'b', linestyles='dashed')
    plt.text(11, y_ave_sum_nist_s_rate_ctr - 0.003, str(y_ave_trng_nist_s_rate_ctr), fontsize=10, color="green")
    plt.text(11, y_ave_sum_nist_s_rate_hash - 0.003, str(y_ave_trng_nist_s_rate_hash), fontsize=10, color="red")
    plt.text(11, y_ave_sum_nist_s_rate_hmac - 0.003, str(y_ave_trng_nist_s_rate_hmac), fontsize=10, color="blue")
    xdata, ydata = 5, 0

    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 11, 0.875, 1.0])
    plt.title("SM Pass Rate of DRBG(SUM * 1MB)")
    plt.legend()  # 设置题注

    for rect in rects_ctr:
        height = round(rect.get_height(),3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hash:
        height =  round(rect.get_height(),3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hmac:
        height =  round(rect.get_height(),3)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    plt.show()

def show_alg_subs_nist_compare():
    # DRBG DRBG SM
    fig6 = plt.figure(10)
    plt.grid(linestyle='-.')
    x_label_list = ["ctr", "hash", "hmac"]
    ctr_ave = (y_drbg_nist_s_rate[num_ctr] + y_drbg10_nist_s_rate[num_ctr]+ y_drbg100_nist_s_rate[num_ctr] + \
              y_trng_nist_s_rate[num_ctr] + y_trng10_nist_s_rate[num_ctr] + y_trng100_nist_s_rate[num_ctr] + \
              y_norand10_nist_s_rate[num_ctr] + y_norand10_nist_s_rate[num_ctr] + y_norand100_nist_s_rate[num_ctr])/9

    hash_ave = (y_drbg_nist_s_rate[num_hash_sha1] + y_drbg10_nist_s_rate[num_hash_sha1]+ y_drbg100_nist_s_rate[num_hash_sha1] + \
              y_trng_nist_s_rate[num_hash_sha1] + y_trng10_nist_s_rate[num_hash_sha1] + y_trng100_nist_s_rate[num_hash_sha1] + \
              y_norand_nist_s_rate[num_hash_sha1] + y_norand10_nist_s_rate[num_hash_sha1] + y_norand100_nist_s_rate[num_hash_sha1] + \
                y_drbg_nist_s_rate[num_hash_sha224] + y_drbg10_nist_s_rate[num_hash_sha224]+ y_drbg100_nist_s_rate[num_hash_sha224] + \
              y_trng_nist_s_rate[num_hash_sha224] + y_trng10_nist_s_rate[num_hash_sha224] + y_trng100_nist_s_rate[num_hash_sha224] + \
              y_norand_nist_s_rate[num_hash_sha224] + y_norand10_nist_s_rate[num_hash_sha224] + y_norand100_nist_s_rate[num_hash_sha224] + \
                y_drbg_nist_s_rate[num_hash_sha256] + y_drbg10_nist_s_rate[num_hash_sha256]+ y_drbg100_nist_s_rate[num_hash_sha256] + \
              y_trng_nist_s_rate[num_hash_sha256] + y_trng10_nist_s_rate[num_hash_sha256] + y_trng100_nist_s_rate[num_hash_sha256] + \
              y_norand_nist_s_rate[num_hash_sha256] + y_norand10_nist_s_rate[num_hash_sha256] + y_norand100_nist_s_rate[num_hash_sha256] + \
                y_drbg_nist_s_rate[num_hash_sha384] + y_drbg10_nist_s_rate[num_hash_sha384]+ y_drbg100_nist_s_rate[num_hash_sha384] + \
              y_trng_nist_s_rate[num_hash_sha384] + y_trng10_nist_s_rate[num_hash_sha384] + y_trng100_nist_s_rate[num_hash_sha384] + \
              y_norand_nist_s_rate[num_hash_sha384] + y_norand10_nist_s_rate[num_hash_sha384] + y_norand100_nist_s_rate[num_hash_sha384] + \
                y_drbg_nist_s_rate[num_hash_sha512] + y_drbg10_nist_s_rate[num_hash_sha512]+ y_drbg100_nist_s_rate[num_hash_sha512] + \
              y_trng_nist_s_rate[num_hash_sha512] + y_trng10_nist_s_rate[num_hash_sha512] + y_trng100_nist_s_rate[num_hash_sha512] + \
              y_norand_nist_s_rate[num_hash_sha512] + y_norand10_nist_s_rate[num_hash_sha512] + y_norand100_nist_s_rate[num_hash_sha512])/45

    hmac_ave = (y_drbg_nist_s_rate[num_hmac_sha1] + y_drbg10_nist_s_rate[num_hmac_sha1]+ y_drbg100_nist_s_rate[num_hmac_sha1] + \
              y_trng_nist_s_rate[num_hmac_sha1] + y_trng10_nist_s_rate[num_hmac_sha1] + y_trng100_nist_s_rate[num_hmac_sha1] + \
              y_norand_nist_s_rate[num_hmac_sha1] + y_norand10_nist_s_rate[num_hmac_sha1] + y_norand100_nist_s_rate[num_hmac_sha1] + \
                y_drbg_nist_s_rate[num_hmac_sha224] + y_drbg10_nist_s_rate[num_hmac_sha224]+ y_drbg100_nist_s_rate[num_hmac_sha224] + \
              y_trng_nist_s_rate[num_hmac_sha224] + y_trng10_nist_s_rate[num_hmac_sha224] + y_trng100_nist_s_rate[num_hmac_sha224] + \
              y_norand_nist_s_rate[num_hmac_sha224] + y_norand10_nist_s_rate[num_hmac_sha224] + y_norand100_nist_s_rate[num_hmac_sha224] + \
                y_drbg_nist_s_rate[num_hmac_sha256] + y_drbg10_nist_s_rate[num_hmac_sha256]+ y_drbg100_nist_s_rate[num_hmac_sha256] + \
              y_trng_nist_s_rate[num_hmac_sha256] + y_trng10_nist_s_rate[num_hmac_sha256] + y_trng100_nist_s_rate[num_hmac_sha256] + \
              y_norand_nist_s_rate[num_hmac_sha256] + y_norand10_nist_s_rate[num_hmac_sha256] + y_norand100_nist_s_rate[num_hmac_sha256] + \
                y_drbg_nist_s_rate[num_hmac_sha384] + y_drbg10_nist_s_rate[num_hmac_sha384]+ y_drbg100_nist_s_rate[num_hmac_sha384] + \
              y_trng_nist_s_rate[num_hmac_sha384] + y_trng10_nist_s_rate[num_hmac_sha384] + y_trng100_nist_s_rate[num_hmac_sha384] + \
              y_norand_nist_s_rate[num_hmac_sha384] + y_norand10_nist_s_rate[num_hmac_sha384] + y_norand100_nist_s_rate[num_hmac_sha384] + \
                y_drbg_nist_s_rate[num_hmac_sha512] + y_drbg10_nist_s_rate[num_hmac_sha512]+ y_drbg100_nist_s_rate[num_hmac_sha512] + \
              y_trng_nist_s_rate[num_hmac_sha512] + y_trng10_nist_s_rate[num_hmac_sha512] + y_trng100_nist_s_rate[num_hmac_sha512] + \
              y_norand_nist_s_rate[num_hmac_sha512] + y_norand10_nist_s_rate[num_hmac_sha512] + y_norand100_nist_s_rate[num_hmac_sha512])/45
    y_data = [ctr_ave, hash_ave, hmac_ave]
    rects_ctr = plt.bar(x_label_list[0], ctr_ave, width=0.4, alpha=0.8, color='green', label="CTR")
    rects_hash = plt.bar(x_label_list[1], hash_ave, width=0.4, alpha=0.8, color='red', label="HASH")
    rects_hmac = plt.bar(x_label_list[2], hmac_ave, width=0.4, alpha=0.8, color='blue', label="HMAC")
    xdata, ydata = 5, 0

    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 3, 0.85, 0.94])
    plt.title("SM All Pass Rate")
    plt.legend()  # 设置题注

    for rect in rects_ctr:
        height = round( rect.get_height(), 4)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hash:
        height = round( rect.get_height(), 4)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    for rect in rects_hmac:
        height = round( rect.get_height(), 4)
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")
    plt.show()



def show_alg_hash_sub_nist_compare():
    # DRBG DRBG SM
    fig10 = plt.figure(10)
    plt.grid(linestyle='-.')
    x_label_list = ["sha1", "sha224", "sha256", "sha384", "sha512"]

    hash_sha1_ave = (y_drbg_nist_s_rate[num_hash_sha1] + y_drbg10_nist_s_rate[num_hash_sha1]+ y_drbg100_nist_s_rate[num_hash_sha1] + \
              y_trng_nist_s_rate[num_hash_sha1] + y_trng10_nist_s_rate[num_hash_sha1] + y_trng100_nist_s_rate[num_hash_sha1] + \
              y_norand_nist_s_rate[num_hash_sha1] + y_norand10_nist_s_rate[num_hash_sha1] + y_norand100_nist_s_rate[num_hash_sha1])/9

    hash_sha224_ave = (y_drbg_nist_s_rate[num_hash_sha224] + y_drbg10_nist_s_rate[num_hash_sha224]+ y_drbg100_nist_s_rate[num_hash_sha224] + \
              y_trng_nist_s_rate[num_hash_sha224] + y_trng10_nist_s_rate[num_hash_sha224] + y_trng100_nist_s_rate[num_hash_sha224] + \
              y_norand_nist_s_rate[num_hash_sha224] + y_norand10_nist_s_rate[num_hash_sha224] + y_norand100_nist_s_rate[num_hash_sha224])/9

    hash_sha256_ave = (y_drbg_nist_s_rate[num_hash_sha256] + y_drbg10_nist_s_rate[num_hash_sha256]+ y_drbg100_nist_s_rate[num_hash_sha256] + \
              y_trng_nist_s_rate[num_hash_sha256] + y_trng10_nist_s_rate[num_hash_sha256] + y_trng100_nist_s_rate[num_hash_sha256] + \
              y_norand_nist_s_rate[num_hash_sha256] + y_norand10_nist_s_rate[num_hash_sha256] + y_norand100_nist_s_rate[num_hash_sha256]) /9

    hash_sha384_ave = (y_drbg_nist_s_rate[num_hash_sha384] + y_drbg10_nist_s_rate[num_hash_sha384]+ y_drbg100_nist_s_rate[num_hash_sha384] + \
              y_trng_nist_s_rate[num_hash_sha384] + y_trng10_nist_s_rate[num_hash_sha384] + y_trng100_nist_s_rate[num_hash_sha384] + \
              y_norand_nist_s_rate[num_hash_sha384] + y_norand10_nist_s_rate[num_hash_sha384] + y_norand100_nist_s_rate[num_hash_sha384])/9

    hash_sha512_ave = (y_drbg_nist_s_rate[num_hash_sha512] + y_drbg10_nist_s_rate[num_hash_sha512]+ y_drbg100_nist_s_rate[num_hash_sha512] + \
              y_trng_nist_s_rate[num_hash_sha512] + y_trng10_nist_s_rate[num_hash_sha512] + y_trng100_nist_s_rate[num_hash_sha512] + \
              y_norand_nist_s_rate[num_hash_sha512] + y_norand10_nist_s_rate[num_hash_sha512] + y_norand100_nist_s_rate[num_hash_sha512])/9

    y_data = [round(hash_sha1_ave,4), round(hash_sha224_ave,4), round(hash_sha256_ave,4), round(hash_sha384_ave,4), round(hash_sha512_ave,4)]
    rects_ctr = plt.bar(x_label_list, y_data, width=0.4, alpha=0.8, color='red', label="PassRate")
    xdata, ydata = 5, 0

    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 5, 0.9, 0.94])
    plt.title("HASH SM Pass Rate")
    plt.legend()  # 设置题注

    for rect in rects_ctr:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")

    plt.show()

def show_alg_hmac_sub_nist_compare():
    # DRBG DRBG SM
    fig10 = plt.figure(10)
    plt.grid(linestyle='-.')
    x_label_list = ["sha1", "sha224", "sha256", "sha384", "sha512"]

    hash_sha1_ave = (y_drbg_nist_s_rate[num_hmac_sha1] + y_drbg10_nist_s_rate[num_hmac_sha1]+ y_drbg100_nist_s_rate[num_hmac_sha1] + \
              y_trng_nist_s_rate[num_hmac_sha1] + y_trng10_nist_s_rate[num_hmac_sha1] + y_trng100_nist_s_rate[num_hmac_sha1] + \
              y_norand_nist_s_rate[num_hmac_sha1] + y_norand10_nist_s_rate[num_hmac_sha1] + y_norand100_nist_s_rate[num_hash_sha1])/9

    hash_sha224_ave = (y_drbg_nist_s_rate[num_hmac_sha224] + y_drbg10_nist_s_rate[num_hmac_sha224]+ y_drbg100_nist_s_rate[num_hmac_sha224] + \
              y_trng_nist_s_rate[num_hmac_sha224] + y_trng10_nist_s_rate[num_hmac_sha224] + y_trng100_nist_s_rate[num_hmac_sha224] + \
              y_norand_nist_s_rate[num_hmac_sha224] + y_norand10_nist_s_rate[num_hmac_sha224] + y_norand100_nist_s_rate[num_hmac_sha224])/9

    hash_sha256_ave = (y_drbg_nist_s_rate[num_hmac_sha256] + y_drbg10_nist_s_rate[num_hmac_sha256]+ y_drbg100_nist_s_rate[num_hmac_sha256] + \
              y_trng_nist_s_rate[num_hmac_sha256] + y_trng10_nist_s_rate[num_hmac_sha256] + y_trng100_nist_s_rate[num_hmac_sha256] + \
              y_norand_nist_s_rate[num_hmac_sha256] + y_norand10_nist_s_rate[num_hmac_sha256] + y_norand100_nist_s_rate[num_hmac_sha256]) /9

    hash_sha384_ave = (y_drbg_nist_s_rate[num_hmac_sha384] + y_drbg10_nist_s_rate[num_hmac_sha384]+ y_drbg100_nist_s_rate[num_hmac_sha384] + \
              y_trng_nist_s_rate[num_hmac_sha384] + y_trng10_nist_s_rate[num_hmac_sha384] + y_trng100_nist_s_rate[num_hmac_sha384] + \
              y_norand_nist_s_rate[num_hmac_sha384] + y_norand10_nist_s_rate[num_hmac_sha384] + y_norand100_nist_s_rate[num_hmac_sha384])/9

    hash_sha512_ave = (y_drbg_nist_s_rate[num_hmac_sha512] + y_drbg10_nist_s_rate[num_hmac_sha512]+ y_drbg100_nist_s_rate[num_hmac_sha512] + \
              y_trng_nist_s_rate[num_hmac_sha512] + y_trng10_nist_s_rate[num_hmac_sha512] + y_trng100_nist_s_rate[num_hmac_sha512] + \
              y_norand_nist_s_rate[num_hmac_sha512] + y_norand10_nist_s_rate[num_hmac_sha512] + y_norand100_nist_s_rate[num_hmac_sha512])/9

    y_data = [round(hash_sha1_ave,4), round(hash_sha224_ave,4), round(hash_sha256_ave,4), round(hash_sha384_ave,4), round(hash_sha512_ave,4)]
    rects_ctr = plt.bar(x_label_list, y_data, width=0.4, alpha=0.8, color='red', label="PassRate")
    xdata, ydata = 5, 0

    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 5, 0.9, 0.94])
    plt.title("HMAC SM Pass Rate")
    plt.legend()  # 设置题注

    for rect in rects_ctr:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")

    plt.show()


def show_seeds_sum_nist_compare():
    re1m = (np.sum(y_drbg_nist_s_rate) + np.sum(y_norand_nist_s_rate) + np.sum(y_trng_nist_s_rate)) / 33
    re10k = (np.sum(y_drbg10_nist_s_rate) + np.sum(y_norand10_nist_s_rate) + np.sum(y_trng10_nist_s_rate)) / 33
    re100k = (np.sum(y_drbg100_nist_s_rate) + np.sum(y_norand100_nist_s_rate) + np.sum(y_trng100_nist_s_rate)) / 33
    y_data = [round(re1m, 4), round(re10k, 4), round(re100k, 4)]
    x_label_list = ['1MB', '10KB', '100KB']
    rects_ctr = plt.bar(x_label_list, y_data, width=0.4, alpha=0.8, color='red', label="PassRate")
    xdata, ydata = 5, 0
    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 3, 0.5, 1])
    plt.title("Seeds SM Pass Rate")
    plt.legend()  # 设置题注
    plt.grid()
    for rect in rects_ctr:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")

    plt.show()

def show_seed_10k_sum_nist_compare():
    drbg = (np.sum(y_drbg_nist_s_rate)) / 11
    norand = (np.sum(y_norand10_nist_s_rate)) / 11
    trng = (np.sum(y_trng10_nist_s_rate)) / 11
    y_data = [round(drbg, 4), round(norand, 4), round(trng, 4)]
    x_label_list = ['DRBG', 'NORAND', 'TRNG']
    rects_ctr = plt.bar(x_label_list, y_data, width=0.4, alpha=0.8, color='red', label="PassRate")
    xdata, ydata = 5, 0
    plt.xlabel("DRBG-Subs")
    plt.ylabel("Pass Rate")
    plt.axis([-1, 3, 0.5, 1])
    plt.title("Reseed 10K SM Pass Rate")
    plt.legend()  # 设置题注
    plt.grid()
    for rect in rects_ctr:
        height = rect.get_height()
        plt.text(rect.get_x() + rect.get_width() / 2, height, str(height), ha="center", va="bottom")

    plt.show()


if __name__ == "__main__":
    # show_all_nist_rate()
    # show_norand1m_nist_pass_rate()
    # show_trng1m_nist_pass_rate()
    # show_drbg1m_nist_pass_rate()
    # show_sum1m_nist_pass_rate()


    # show_norand100_nist_pass_rate()
    # show_trng100_nist_pass_rate()
    # show_drbg100_nist_pass_rate()
    # show_sum100_nist_pass_rate()


    #show_norand10_nist_pass_rate()
    #show_trng10_nist_pass_rate()
    #show_drbg10_nist_pass_rate()
    # show_sum10_nist_pass_rate()

    #show_alg_hash_sub_nist_compare()
    #show_alg_hmac_sub_nist_compare()
    #
    #show_seed_10k_sum_nist_compare()
     #show_alg_subs_nist_compare()
    #
     show_all_nist_rate()
