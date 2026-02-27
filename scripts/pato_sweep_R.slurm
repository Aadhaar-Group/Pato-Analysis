#!/bin/bash

## For tc (tinkercliffs) cluster.

## Job, account, queue and output/error file names.
#SBATCH --job-name=1D_pato_test
#SBATCH --account=sensor_placement
#SBATCH --partition=normal_q 
#SBATCH --output=1D_pato_sweep.%j.out
#SBATCH --error=1D_pato_sweep.%j.err
#SBATCH --time=00:05:00 

## Compute resources.
#SBATCH --nodes=1 
#SBATCH --ntasks-per-node=1
#SBATCH --cpus-per-task=4
#SBATCH --mem=32GB
#SBATCH --mail-user=ryana27@vt.edu
#SBATCH --mail-type=END,FAIL

# Reset modules.
# module reset

# Load conda and activate software
module load Miniconda3
source activate pato

export OMP_NUM_THREADS=1

## -----------------------
#cd ${0%/*} || exit 1 # Run from this directory

# Initialize the script
python pato_sweep.py
