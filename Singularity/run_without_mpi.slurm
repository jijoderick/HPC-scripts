#!/bin/bash
#SBATCH --job-name=JDAHFpEF
#SBATCH --partition=cpu
#SBATCH --nodes=1
#SBATCH --ntasks=1
#SBATCH --cpus-per-task=1
#SBATCH --ntasks-per-node=1
#SBATCH --time=24:00:00
#SBATCG --mail-type=ALL
#SBATCH --mail-user=jijoderick.abraham@uq.net.au
singularity exec /home/s4657117/HCM-project/SingularitY/hcm-project.img python Normal_case_HO_model_Mojumder_Values.py
