import os
import sys
### rename.py ###
# usage: py ./rename.py PATH PREFIX
# renames all files in PATH with "PREFIX_i"

def main():

    if len(sys.argv) == 3:
        folder_path = sys.argv[1]
        prefix = sys.argv[2]

        list_dir = os.listdir(folder_path)
        folder_prefix = folder_path + "/"
        for i in range(len(list_dir)):
            img = list_dir[i]
            img_ext = os.path.splitext(img)
            os.rename(folder_prefix + img, folder_prefix + prefix + "_" + str(i) + img_ext[1])

    else:
        print("### rename.py ###")
        print("# usage: py ./rename.py PATH PREFIX")
        print("# renames all files in PATH with 'PREFIX_i'")


if __name__ == "__main__":
    main()
