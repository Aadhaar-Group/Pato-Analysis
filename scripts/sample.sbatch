#!/bin/bash

## Setup SLURM submission options ##

#SBATCH --time=71:00:00                     ## total expected computing time
#SBATCH --nodes=1                          ## number of nodes
#SBATCH --ntasks-per-node=20
#SBATCH --output="Sampling.log"              ## output file , ( recommended to debug )
#SBATCH --job-name="tacc_SL"                      ## specify a custom name for the job
#SBATCH --partition=chess                           ## queue
#SBATCH --mail-user="vkuppa2@illinois.edu"         ## email address to notify
#SBATCH --mem=5G

## ######## Run your executable ######################

## Load required modules
module load hegel/hegel_27_01_25_wPRECICE 
module load pato/old_pato_wadapter_no_UQ
module load anaconda3/2024.10 

source activate test_env 

## Run script
python main_time.py
