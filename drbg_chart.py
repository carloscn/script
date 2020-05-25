#,coding,:,utf-8
# /usr/bin/python3

import matplotlib.pyplot as plt
import numpy as np
import math

x_l = np.array([1,2,3,4,5,6,7,8,9,10,11])
y_norand_sm_rate = np.array([0.97,0.97,0.99,0.98,0.97,0.97,0.97,0.98,0.99,0.96,0.97])
y_norand_nist_p_rate = np.array([0.98, 0.99, 0.97, 0.99, 0.99, 0.99, 0.96, 0.99, 0.97, 0.96, 0.97])
y_norand_nist_a_rate = np.array([0.87, 0.93, 0.93, 0.96, 0.89, 0.94, 0.97, 0.92, 0.9, 0.93, 0.91])
y_norand_nist_s_rate = np.array([0.8526, 0.9207, 0.9021, 0.9504, 0.8811, 0.9306, 0.9312, 0.9108, 0.873, 0.8928, 0.8827])
y_ave_norand_sm_rate = np.average(y_norand_sm_rate)
y_ave_norand_sm_rate_ctr = np.average(y_norand_sm_rate[0:1])
y_ave_norand_sm_rate_hash = np.average(y_norand_sm_rate[1:6])
y_ave_norand_sm_rate_hmac = np.average(y_norand_sm_rate[6:11])
y_ave_norand_nist_p_rate = np.average(y_norand_nist_p_rate)
y_ave_norand_nist_a_rate = np.average(y_norand_nist_a_rate)
y_ave_norand_nist_s_rate = np.average(y_norand_nist_s_rate)
y_ave_norand_nist_s_rate_ctr = np.average(y_norand_nist_s_rate[0:1])
y_ave_norand_nist_s_rate_hash = np.average(y_norand_nist_s_rate[1:6])
y_ave_norand_nist_s_rate_hmac = np.average(y_norand_nist_s_rate[6:11])

y_trng_sm_rate = np.array([0.99, 0.94, 0.97, 0.93, 0.96, 0.96, 0.97, 0.96, 0.94, 0.96, 0.94])
y_trng_nist_p_rate = np.array([1, 0.99, 0.98, 1, 0.97, 0.98, 0.99, 0.99, 0.97, 0.98, 0.98])
y_trng_nist_a_rate = np.array([0.94, 0.88, 0.89, 0.98, 0.95, 0.89, 0.97, 0.87, 0.9, 0.93, 0.89])
y_trng_nist_s_rate = np.array([0.94, 0.8712, 0.8722, 0.98, 0.9215, 0.8722, 0.9603, 0.8613, 0.873, 0.9114, 0.8722])
y_ave_trng_sm_rate = np.average(y_trng_sm_rate)
y_ave_trng_nist_p_rate = np.average(y_trng_nist_p_rate)
y_ave_trng_nist_a_rate = np.average(y_trng_nist_a_rate)
y_ave_trng_nist_s_rate = np.average(y_trng_nist_s_rate)
y_ave_trng_sm_rate_ctr = np.average(y_trng_sm_rate[0:1])
y_ave_trng_sm_rate_hash = np.average(y_trng_sm_rate[1:6])
y_ave_trng_sm_rate_hmac = np.average(y_trng_sm_rate[6:11])
y_ave_trng_nist_s_rate_ctr = np.average(y_trng_nist_s_rate[0:1])
y_ave_trng_nist_s_rate_hash = np.average(y_trng_nist_s_rate[1:6])
y_ave_trng_nist_s_rate_hmac = np.average(y_trng_nist_s_rate[6:11])

y_drbg_sm_rate = np.array([0.98, 0.96, 0.98, 0.95, 0.97, 0.99, 0.96, 0.99, 0.98, 0.96, 0.99])
y_drbg_nist_p_rate = np.array([0.96, 0.99, 0.98, 0.98, 0.99, 1, 0.97, 0.98, 0.97, 0.97, 1])
y_drbg_nist_a_rate = np.array([0.91, 0.92, 0.88, 0.94, 0.94, 0.93, 0.91, 0.88, 0.91, 0.92, 0.95])
y_drbg_nist_s_rate = np.array([0.8736, 0.9108, 0.8624, 0.9212, 0.9306, 0.93, 0.8827, 0.8624, 0.8827, 0.8924, 0.95])
y_ave_drbg_sm_rate = np.average(y_drbg_sm_rate)
y_ave_drbg_sm_rate_ctr = np.average(y_drbg_sm_rate[0:1])
y_ave_drbg_sm_rate_hash = np.average(y_drbg_sm_rate[1:6])
y_ave_drbg_sm_rate_hmac = np.average(y_drbg_sm_rate[6:11])
y_ave_drbg_nist_p_rate = np.average(y_drbg_nist_p_rate)
y_ave_drbg_nist_a_rate = np.average(y_drbg_nist_a_rate)
y_ave_drbg_nist_s_rate = np.average(y_drbg_nist_s_rate)
y_ave_drbg_nist_s_rate_ctr = np.average(y_drbg_nist_s_rate[0:1])
y_ave_drbg_nist_s_rate_hash = np.average(y_drbg_nist_s_rate[1:6])
y_ave_drbg_nist_s_rate_hmac = np.average(y_drbg_nist_s_rate[6:11])

label_ctr_list = ['ctr']
label_hash_list = ['sha1', 'sha224', 'sha256', 'sha384', 'sha512']
label_hmac_list = ['.sha1', '.sha224', '.sha256', '.sha384', '.sha512']
x_ctr = range(len(label_ctr_list))
x_hash = range(len(label_hash_list))
x_hmac = range(len(label_hmac_list))

fig7 = plt.figure(7)
x_label = []
x_label = label_ctr_list + label_hash_list + label_hmac_list

scale_ls = range(11)
plt.grid()
plt.axis([-1,11, 0.6, 1.0])
plt.plot(scale_ls,y_norand_nist_s_rate,'-o',color='r',label='no-rand', linewidth=1, markersize=8)
plt.plot(scale_ls, y_trng_nist_s_rate, '-*',color='b',label='trng', linewidth=1, markersize=8)
plt.plot(scale_ls,y_drbg_nist_s_rate,'-v',color='g',label='drbg', linewidth=1, markersize=8)
plt.hlines(np.average(y_norand_nist_s_rate), -1, 11, 'r', linestyles='dashed')
plt.hlines(np.average(y_trng_nist_s_rate), -1, 11, 'b', linestyles='dashed')
plt.hlines(np.average(y_drbg_nist_s_rate), -1, 11, 'g', linestyles='dashed')
plt.legend()     # 设置题注
plt.xticks(scale_ls,x_label) ## 可以设置坐标字
plt.title("Pass rate of NIST Diff Seed")
plt.show()

fig8 = plt.figure(8)
scale_ls = range(11)
plt.grid()
plt.axis([-1,11, 0.8, 1.0])
plt.plot(scale_ls,y_norand_sm_rate,'-o',color='r',label='no-rand', linewidth=1, markersize=8)
plt.plot(scale_ls, y_trng_sm_rate, '-*',color='b',label='trng', linewidth=1, markersize=8)
plt.plot(scale_ls,y_drbg_sm_rate,'-v',color='g',label='drbg', linewidth=1, markersize=8)
plt.hlines(np.average(y_norand_sm_rate), -1, 11, 'r', linestyles='dashed')
plt.hlines(np.average(y_trng_sm_rate), -1, 11, 'b', linestyles='dashed')
plt.hlines(np.average(y_drbg_sm_rate), -1, 11, 'g', linestyles='dashed')
plt.legend()     # 设置题注
plt.title("Pass rate of SM Diff Seed")
plt.show()

# NORAND DRBG NIST
fig1 = plt.figure(1)
plt.grid(linestyle='-.')
# plt.plot(x_l,y_norand_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
# plt.plot(x_l, y_norand_nist_p_rate, 'b-*',label='P rate', linewidth=2, markersize=6)
# plt.plot(x_l,y_norand_nist_a_rate,'g-v',label='mag', linewidth=2, markersize=6)
# plt.plot(x_l, y_norand_nist_s_rate, 'y-^',label='mag', linewidth=2, markersize=6)
rects_ctr = plt.bar( label_ctr_list, y_norand_nist_s_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
rects_hash = plt.bar( label_hash_list, y_norand_nist_s_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
rects_hmac = plt.bar( label_hmac_list, y_norand_nist_s_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
# plt.plot(x_l,y_norand_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
plt.hlines(y_ave_norand_nist_s_rate_ctr, -1, 11, 'g', linestyles='dashed')
plt.hlines(y_ave_norand_nist_s_rate_hash, -1, 11, 'r', linestyles='dashed')
plt.hlines(y_ave_norand_nist_s_rate_hmac, -1, 11, 'b', linestyles='dashed')
plt.text(11, y_ave_norand_nist_s_rate_ctr - 0.003 , str(y_ave_norand_nist_s_rate_ctr), fontsize=10, color = "green")
plt.text(11, y_ave_norand_nist_s_rate_hash - 0.003 , str(y_ave_norand_nist_s_rate_hash ), fontsize=10, color = "red")
plt.text(11, y_ave_norand_nist_s_rate_hmac - 0.003 , str(y_ave_norand_nist_s_rate_hmac ), fontsize=10, color = "blue")
xdata, ydata = 5, 0

plt.xlabel("DRBG-Subs")
plt.ylabel("Pass Rate")
plt.axis([-1,11, 0.8, 1.0])
plt.title("NIST Pass Rate of DRBG(No Random Number as Seed)")
plt.legend()     # 设置题注


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



# NORAND DRBG SM
fig2 = plt.figure(2)
plt.grid(linestyle='-.')
# plt.plot(x_l,y_norand_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
# plt.plot(x_l, y_norand_nist_p_rate, 'b-*',label='P rate', linewidth=2, markersize=6)
# plt.plot(x_l,y_norand_nist_a_rate,'g-v',label='mag', linewidth=2, markersize=6)
# plt.plot(x_l, y_norand_nist_s_rate, 'y-^',label='mag', linewidth=2, markersize=6)
rects_ctr = plt.bar( label_ctr_list, y_norand_sm_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
rects_hash = plt.bar( label_hash_list, y_norand_sm_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
rects_hmac = plt.bar( label_hmac_list, y_norand_sm_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
# plt.plot(x_l,y_norand_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
plt.hlines(y_ave_norand_sm_rate_ctr, -1, 11, 'g', linestyles='dashed')
plt.hlines(y_ave_norand_sm_rate_hash, -1, 11, 'r', linestyles='dashed')
plt.hlines(y_ave_norand_sm_rate_hmac, -1, 11, 'b', linestyles='dashed')
plt.text(11, y_ave_norand_sm_rate_ctr - 0.003 , str(y_ave_norand_sm_rate_ctr), fontsize=10, color = "green")
plt.text(11, y_ave_norand_sm_rate_hash - 0.003 , str(y_ave_norand_sm_rate_hash ), fontsize=10, color = "red")
plt.text(11, y_ave_norand_sm_rate_hmac - 0.003 , str(y_ave_norand_sm_rate_hmac ), fontsize=10, color = "blue")
xdata, ydata = 5, 0

plt.xlabel("DRBG-Subs")
plt.ylabel("Pass Rate")
plt.axis([-1,11, 0.94, 1.0])
plt.title("SM Pass Rate of DRBG(No Random Number as Seed)")
plt.legend()     # 设置题注
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


###############trng
fig3 = plt.figure(3)
plt.grid(linestyle='-.')

rects_ctr = plt.bar( label_ctr_list, y_trng_nist_s_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
rects_hash = plt.bar( label_hash_list, y_trng_nist_s_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
rects_hmac = plt.bar( label_hmac_list, y_trng_nist_s_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
# plt.plot(x_l,y_trng_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
plt.hlines(y_ave_trng_nist_s_rate_ctr, -1, 11, 'g', linestyles='dashed')
plt.scatter([1.5],[-0.25],s=25,c='r')
plt.hlines(y_ave_trng_nist_s_rate_hash, -1, 11, 'r', linestyles='dashed')
plt.hlines(y_ave_trng_nist_s_rate_hmac, -1, 11, 'b', linestyles='dashed')
plt.text(11, y_ave_trng_nist_s_rate_ctr - 0.003 , str(y_ave_trng_nist_s_rate_ctr), fontsize=10, color = "green")
plt.text(11, y_ave_trng_nist_s_rate_hash - 0.003 , str(y_ave_trng_nist_s_rate_hash ), fontsize=10, color = "red")
plt.text(11, y_ave_trng_nist_s_rate_hmac - 0.003 , str(y_ave_trng_nist_s_rate_hmac ), fontsize=10, color = "blue")
xdata, ydata = 5, 0

plt.xlabel("DRBG-Subs")
plt.ylabel("Pass Rate")
plt.axis([-1,11, 0.8, 1.0])
plt.title("NIST Pass Rate of DRBG(TRNG as Seed)")
plt.legend()     # 设置题注


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
# SM TRNG DRBG
fig4 = plt.figure(4)
plt.grid(linestyle='-.')
rects_ctr = plt.bar( label_ctr_list, y_trng_sm_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
rects_hash = plt.bar( label_hash_list, y_trng_sm_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
rects_hmac = plt.bar( label_hmac_list, y_trng_sm_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
# plt.plot(x_l,y_trng_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
plt.hlines(y_ave_trng_sm_rate_ctr, -1, 11, 'g', linestyles='dashed')
plt.hlines(y_ave_trng_sm_rate_hash, -1, 11, 'r', linestyles='dashed')
plt.hlines(y_ave_trng_sm_rate_hmac, -1, 11, 'b', linestyles='dashed')
plt.text(11, y_ave_trng_sm_rate_ctr - 0.003 , str(y_ave_trng_sm_rate_ctr), fontsize=10, color = "green")
plt.text(11, y_ave_trng_sm_rate_hash - 0.003 , str(y_ave_trng_sm_rate_hash ), fontsize=10, color = "red")
plt.text(11, y_ave_trng_sm_rate_hmac - 0.003 , str(y_ave_trng_sm_rate_hmac ), fontsize=10, color = "blue")
xdata, ydata = 5, 0

plt.xlabel("DRBG-Subs")
plt.ylabel("Pass Rate")
plt.axis([-1,11, 0.88, 1.0])
plt.title("SM Pass Rate of DRBG(TRNG as Seed)")
plt.legend()     # 设置题注


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

# DRBG DRBG NIST
fig5 = plt.figure(5)
plt.grid(linestyle='-.')

rects_ctr = plt.bar( label_ctr_list, y_drbg_nist_s_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
rects_hash = plt.bar( label_hash_list, y_drbg_nist_s_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
rects_hmac = plt.bar( label_hmac_list, y_drbg_nist_s_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
# plt.plot(x_l,y_trng_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
plt.hlines(y_ave_drbg_nist_s_rate_ctr, -1, 11, 'g', linestyles='dashed')
plt.hlines(y_ave_drbg_nist_s_rate_hash, -1, 11, 'r', linestyles='dashed')
plt.hlines(y_ave_drbg_nist_s_rate_hmac, -1, 11, 'b', linestyles='dashed')
plt.text(11, y_ave_drbg_nist_s_rate_ctr - 0.003 , str(y_ave_drbg_nist_s_rate_ctr), fontsize=10, color = "green")
plt.text(11, y_ave_drbg_nist_s_rate_hash - 0.003 , str(y_ave_drbg_nist_s_rate_hash ), fontsize=10, color = "red")
plt.text(11, y_ave_drbg_nist_s_rate_hmac - 0.003 , str(y_ave_drbg_nist_s_rate_hmac ), fontsize=10, color = "blue")
xdata, ydata = 5, 0

plt.xlabel("DRBG-Subs")
plt.ylabel("Pass Rate")
plt.axis([-1,11, 0.8, 1.0])
plt.title("NIST Pass Rate of DRBG(DRBG as Seed)")
plt.legend()     # 设置题注


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


# DRBG DRBG SM
fig6 = plt.figure(6)
plt.grid(linestyle='-.')
rects_ctr = plt.bar( label_ctr_list, y_drbg_sm_rate[0:1], width=0.4, alpha=0.8, color='green', label="CTR")
rects_hash = plt.bar( label_hash_list, y_drbg_sm_rate[1:6], width=0.4, alpha=0.8, color='red', label="HASH")
rects_hmac = plt.bar( label_hmac_list, y_drbg_sm_rate[6:11], width=0.4, alpha=0.8, color='blue', label="HMAC")
# plt.plot(x_l,y_trng_sm_rate,'m-s',label='SM rate', linewidth=2, markersize=6)
plt.hlines(y_ave_drbg_sm_rate_ctr, -1, 11, 'g', linestyles='dashed')
plt.hlines(y_ave_drbg_sm_rate_hash, -1, 11, 'r', linestyles='dashed')
plt.hlines(y_ave_drbg_sm_rate_hmac, -1, 11, 'b', linestyles='dashed')
plt.text(11, y_ave_drbg_sm_rate_ctr - 0.003 , str(y_ave_drbg_sm_rate_ctr), fontsize=10, color = "green")
plt.text(11, y_ave_drbg_sm_rate_hash - 0.003 , str(y_ave_drbg_sm_rate_hash ), fontsize=10, color = "red")
plt.text(11, y_ave_drbg_sm_rate_hmac - 0.003 , str(y_ave_drbg_sm_rate_hmac ), fontsize=10, color = "blue")
xdata, ydata = 5, 0

plt.xlabel("DRBG-Subs")
plt.ylabel("Pass Rate")
plt.axis([-1,11, 0.90, 1.0])
plt.title("SM Pass Rate of DRBG(DRBG as Seed)")
plt.legend()     # 设置题注

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







