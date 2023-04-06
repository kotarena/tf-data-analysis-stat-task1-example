import pandas as pd
import numpy as np
import math

chat_id = 5334335970 # Ваш chat ID, не меняйте название переменной

def solution(x: np.array) -> float:
    # Измените код этой функции
    # Это будет вашим решением
    # Не меняйте название функции и её аргументы
    return math.sqrt(2 / (((x/2500)**2).mean() - ((x/2500).mean())**2)) # Ваш ответ
