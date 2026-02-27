import os
import sys
import shutil
import numpy as np
import subprocess
import matplotlib.pyplot as plt
from multiprocessing import Pool, cpu_count

top_dir = os.getcwd() + '/'
top_dir = top_dir.strip()

## input samples file
samples_file = 'samples.txt' 

# path to model
model_path = top_dir + '/sim'

# path to model executable relative to model path
model_exec = '/Allrun'

def patch_case(case_dir: str, i: int) -> None:
    # Boundary Condition Case file here
    return

def run_case(dest_dir):

    subprocess.run([dest_dir + '/hegel/exec/' + model_exec])

    with open(conv_path, "r") as f:

        lines = f.readlines()
        last_line = lines[-1].split()
        step = int(last_line[0])

    # Success if last step is np_wind 
    if step >= np_wind:
        return "success"

    else:
        return "fail"


def eval_stag(i):

    print(f'Sample {i+1} ==================================')
    # make model directory and change to that dir --------------------------
    dest_dir = top_dir + f'/sim{i}'
    if os.path.isdir(dest_dir):
        shutil.rmtree(dest_dir)

    shutil.copytree(model_path, dest_dir)
    os.chdir(dest_dir)

    ## run 
    os.chdir(dest_dir + '/hegel/exec/')
    stat = run_case(dest_dir)

    ## delete model directory
    os.chdir(top_dir)
    shutil.rmtree(dest_dir)
    print('DONE===========================================')

    return


# %% Run in parallel
if __name__ == '__main__':

    nsamples_to_run = 10 
    pool = Pool(4)
    pool.map(eval_stag, range(nsamples_to_run))
    pool.close()
