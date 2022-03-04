import os

allfiles = os.listdir()


def print_files(file_list=allfiles, factor=3):
    """
    Function to loop over file names and print a number of times
    as determined by factor.
    """
    print(file_list * factor)
    for file in file_list * factor:
        print(file)

    return "This worked"


print_files()
