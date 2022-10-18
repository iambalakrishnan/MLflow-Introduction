import os
import numpy as np

alpha_s=np.linspace(0.1, 1.0, 5)
l1_ratio_s=np.linspace(0.1, 1.0, 5)

for alpha in alpha_s:
    for l1_ratio in l1_ratio_s:
        os.system(f"python simple_ML_model_2.py -a {alpha} -l1 {l1_ratio}")