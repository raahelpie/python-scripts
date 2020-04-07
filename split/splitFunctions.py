import os


def split_by_lines(file, lines):
    name, extension = os.path.splitext(file)
    count = 0                                                       # Count to keep track of lines written to a file
    file_number = 1                                                 # To name multiple new files
    with open(file, 'r') as rf:                                     # Reading the input file
        for line in rf:                                             # Reading each line
            wf = open(f'{name}child{file_number}{extension}', 'a+')  # Create & write if doesn't exist/append if exists
            wf.write(line)                                          # Writing the line
            count += 1                                              # Incrementing the no. of lines written to file
            if count % lines == 0:                                  # If count is a multiple of specified line,
                file_number += 1                                    # create a fresh file for rest of the lines


def split_by_functions(file):
    f_name, f_ext = os.path.splitext(file)
    function_number = 1
    rf = open(file, 'r')
    lines = rf.readlines()
    i = 0
    while i < len(lines):
        if "def" in lines[i]:
            wf = open(f"{f_name}function{function_number}{f_ext}", 'a+')
            idx = lines[i].index("def")
            wf.write(lines[i])
            i += 1
            while i < len(lines) and lines[i][idx:idx+4] == "    ":
                wf.write(lines[i])
                i += 1
            function_number += 1
        else:
            i += 1
    rf.close()


def main():
    split_mode = int(input("Select the mode (1 or 2) to split:\n 1. Split by lines\n 2. Split by functions (Python)\n"))
    if split_mode == 1:
        file_name = input("File to split: ")                            # Which file to split?
        specific_lines = int(input("Specify lines to split by: "))      # How many lines to split by?
        split_by_lines(file_name, specific_lines)                                # Function call
    elif split_mode == 2:
        file_name = input("File to split: ")
        split_by_functions(file_name)
    else:
        print("Please enter a valid number")
        main()


if __name__ == "__main__":
    main()
