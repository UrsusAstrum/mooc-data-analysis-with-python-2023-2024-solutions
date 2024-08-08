#!/usr/bin/env python3

def file_extensions(filename):
    no_ext = []
    ext = {}
    with open(filename, "r") as file:
        for line in file:
            line = line.strip()
            line_lst = line.split('.')
            if len(line_lst) == 1:
                no_ext.append(line)
            else:
                if line_lst[-1] not in ext.keys():
                    ext[line_lst[-1]] = [line]
                else:
                    ext[line_lst[-1]].append(line)
                
    return (no_ext, ext)

def main():
    no_ext, ext = file_extensions("src/filenames.txt")
    print(f"{len(no_ext)} files with no extension")
    for key, values in ext.items():
        print(f"{key} {len(values)}")

if __name__ == "__main__":
    main()
