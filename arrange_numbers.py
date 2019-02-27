import os

working_directory = os.getcwd() + '/Raw Data/'

file_paths = ["Bus 4","Bus 75"]

for file_path in file_paths:
    i = 1
    full_file_path = working_directory + file_path
    for file_name in os.listdir(full_file_path):
        old_file_name = full_file_path + '/' + file_name
        new_file_name = full_file_path + '/' + str(i)+ '.jpg'
        i += 1
        os.rename(old_file_name, new_file_name)
