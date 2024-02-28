import os
import sys

# usage: py ./rename.py PATH PREFIX
# renames all images in PATH with "PREFIX_i.png"

def main():

    folder_path = sys.argv[1]
    prefix = sys.argv[2]

    list_dir = os.listdir(folder_path)
    folder_prefix = folder_path + "\\"
    for i in range(len(list_dir)):
        img = list_dir[i]
        os.rename(folder_prefix + img, folder_prefix + prefix + "_" + str(i) + ".png")


if __name__ == "__main__":
    main()