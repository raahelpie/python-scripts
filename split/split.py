import os


def split(file, lines):
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


def main():
    file_name = input("File to split: ")                            # Which file to split?
    specific_lines = int(input("Specify lines to split by: "))      # How many lines to split by?
    split(file_name, specific_lines)                                # Function call


if __name__ == "__main__":
    main()
