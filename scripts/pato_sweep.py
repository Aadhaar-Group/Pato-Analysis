import os
import sys
import shutil
import numpy as np
import subprocess
import matplotlib.pyplot as plt
from multiprocessing import Pool, cpu_count

# SETUP
top_dir = os.path.abspath(os.getcwd())
template_dir = os.path.join(top_dir, "sim")
ALLRUN = "Allrun"
nsamples_to_run = 10

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
    allrun_path = os.path.join(case_dir, ALLRUN)
    if not os.path.exists(allrun_path):
        return ("Fail", f"Missing {AllRUN} in {case_dir}")

    log_path = os.path.join(case_dir, "run.log")
    if p.returncode != 0:
        return ("Fail", f"Allrun return code {p.returncode} (see run.log")



def eval_case(i: int) -> tuple[in]:


    return


# %% Run in parallel
if __name__ == '__main__':


    pool = Pool(4)
    pool.map(eval_stag, range(nsamples_to_run))
    pool.close()
