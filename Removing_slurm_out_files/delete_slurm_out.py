#The file deletes the slurm output files in the presecribed directory
#This often helps to reduce size of the results if the slurm output is not critical to our analysis

import os

def find_and_delete_file(directory, partial_filename):
    # Recursively iterate over all directories and files
    for root, dirs, files in os.walk(directory):
        for file in files:
            if partial_filename in file:
                file_path = os.path.join(root, file)

                # Delete the file
                os.remove(file_path)
                print(f"File '{file}' deleted successfully.")

    print(f"No files matching '{partial_filename}' found in the directory.")


# Example usage
directory_path = "./Normal_case"
partial_filename = "slurm-"

find_and_delete_file(directory_path, partial_filename)
