#-*-coding:utf-8-*-
# Author: LD
import itertools as itl
import numpy as np
import pandas as pd

def sgs_zhong_dist_calculator(loc1, loc2):
    if loc1 == loc2:
        return 0
    list_loc = [2, 3, 4, 5, 6, 7, 8]
    loc1 = int(loc1)
    loc2 = int(loc2)
    try:
        list_loc.index(loc1)
        list_loc.index(loc2)
        dist_from_zhu_1 = min(abs(loc1 - 1), abs(loc1 - 9))
        dist_from_zhu_2 = min(abs(loc2 - 1), abs(loc2 - 9))
        math_dist_zhong = abs(loc1 - loc2)
        dist_between_zhong = min(math_dist_zhong, 8 - math_dist_zhong)
        return dist_between_zhong + dist_from_zhu_1 + dist_from_zhu_2
    except:
        return -1


def sgs_fan_dist_calculator(list_fan_locs):
    list_fan_locs = list(set(list_fan_locs))
    if len(list_fan_locs) != 4:
        return -2
    list_loc = [2, 3, 4, 5, 6, 7, 8]
    g = lambda x: int(x)
    list_fan_locs = [g(x) for x in list_fan_locs]
    try:
        list_loc.index(list_fan_locs[0])
        list_loc.index(list_fan_locs[1])
        list_loc.index(list_fan_locs[2])
        list_loc.index(list_fan_locs[3])
        list_dist_between_fan = []
        for item in list(itl.combinations(list_fan_locs, 2)):
            math_dist_fan = abs(item[0] - item[1])
            dist_between_fan = min(math_dist_fan, 8 - math_dist_fan)
            list_dist_between_fan.append(dist_between_fan)
        return sum(list_dist_between_fan)
    except:
        return -1


def zhong_dist_matrix_generator():
    mat_arr = np.eye(7, dtype=int)
    mat_df_zhong = pd.DataFrame(mat_arr)
    mat_df_zhong.index = range(2, 9)
    mat_df_zhong.columns = range(2, 9)
    for x in range(2, 9):
        for y in range(2, 9):
            mat_df_zhong.loc[x, y] = sgs_zhong_dist_calculator(x, y)
    return mat_df_zhong


if __name__ == '__main__':
    list_zhong_locs = list(input("请输入两位忠臣的位置："))
    print("忠臣分别处于{a}号位和{b}号位时，总距离为{c}"\
          .format(a=list_zhong_locs[0], b=list_zhong_locs[1], c=sgs_zhong_dist_calculator(list_zhong_locs[0], list_zhong_locs[1])))
    list_fan_locs = list(input("请输入四位反贼的位置："))
    print("反贼分别处于{a}号位、{b}号位、{c}号位和{d}号位时，总距离为{e}"\
          .format(a=list_fan_locs[0], b=list_fan_locs[1], c=list_fan_locs[2], d=list_fan_locs[3], e=sgs_fan_dist_calculator(list_fan_locs)))
    print(zhong_dist_matrix_generator())



