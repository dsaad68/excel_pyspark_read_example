# %%

import os
import time
import pandas as pd
from joblib import Parallel, delayed

# %%

files_folder = os.path.join("data", 'sales')
files_list = os.listdir(files_folder)


def read_my_excel_file(file_name):
    file_path = os.path.join("data", 'sales', file_name)
    return pd.read_excel(file_path, header=None)


# %%

start = time.time()
df_list = Parallel(n_jobs=8, verbose=10)(delayed(read_my_excel_file)(file_name) for file_name in files_list)
end = time.time()
print(end - start)
