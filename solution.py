import pandas as pd
import numpy as np
from scipy.stats import ttest_ind_from_stats

chat_id = 581150379 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:

    alpha=0.05
    
    x_mean = x_success / x_cnt
    y_mean = y_success / y_cnt
    # Стандартные ошибки для обеих групп
    x_se = math.sqrt(x_mean * (1 - x_mean) / x_cnt)
    y_se = math.sqrt(y_mean * (1 - y_mean) / y_cnt)
    # t-тест
    stat, p_value = ttest_ind_from_stats(x_mean, x_se, x_cnt, y_mean, y_se, y_cnt, equal_var=False)
               
    return p_value < alpha
