import os
import sys

FILE_TO_ACCESS = 'Keys.txt'
TEXT_TO_WRITE = "Replace this line with consumer key!\nReplace this line with consumer secret!\nReplace this line " \
                "with access key!\nReplace this line with consumer secret!"
global fileEmpty


# If the file exists, do nothing. If it doesn't catch the error resulting from no file found and create it.
def check_key_file():
    global fileEmpty
    try:
        fileEmpty = os.stat(FILE_TO_ACCESS).st_size == 0
    except OSError:
        print("File not found.Creating txt.Write down keys within the file. File location=program was run.\n")
        consumerFileWrite = open(FILE_TO_ACCESS, "w")
        consumerFileWrite.close()
        consumerFileWrite = open(FILE_TO_ACCESS, "a")
        consumerFileWrite.write(TEXT_TO_WRITE)
        consumerFileWrite.close()
        sys.exit()


def get_keys():
    cfr = open(FILE_TO_ACCESS, "r")
    ck = cfr.read().split("\n")
    cfr.close()
    return ck
