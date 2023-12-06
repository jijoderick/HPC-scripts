Command to see the working directory of all my simulations running
```
squeue -o "%.18i %.9P %.20j %.8u %.2t %.10M %.6D %R" -u username --noheader | while read job_id partition job_name user state memory time nodes; do echo -e "$job_id\t$partition\t$job_name\t$user\t$state\t$memory\t$time\t$nodes\t$(scontrol show job $job_id | awk -F= '/Command=/{print $2}' | xargs dirname)"; done
```
