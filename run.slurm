#!/bin/bash
#SBATCH --job-name=job
#SBATCH --partition=cpu
#SBATCH --nodes=1
#SBATCH --ntasks=24
#SBATCH --ntasks-per-node=24
#SBATCH --time=50:00:00
#SBATCG --mail-type=ALL
#SBATCH --mail-user=name.gmail.com
module load mpi/openmpi-x86_64
ln -s ~/home/code/bin
mpirun ./bin inputfile

