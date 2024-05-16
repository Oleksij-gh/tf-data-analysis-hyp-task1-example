import pandas as pd
import numpy as np
from scipy.stats import chi2_contingency

chat_id = 581150379 # Ваш chat ID, не меняйте название переменной

def solution(x_success: int, 
             x_cnt: int, 
             y_success: int, 
             y_cnt: int) -> bool:

    alpha = 0.02
    
    contingency_table = [[x_success, x_cnt - x_success],
                         [y_success, y_cnt - y_success]]
    
    # Выполняем тест Хи-квадрат
    chi2, p_value, dof, expected = chi2_contingency(contingency_table, correction=False)
               
    return p_value < alpha
