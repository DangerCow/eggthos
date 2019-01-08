import re

vn = "0.1.5"

print("leafpie", vn)


def find_in_pairs(char_in, char_out, string):
    return re.findall(re.escape(char_in) + '(.*?)' + re.escape(char_out), string)


def read(i, con):
    if not i == -1:
        print(con[i])
    else:
        i = 0
        for line in con:
            print(i, ":", line)


def write(i, str, con):
    if not i == -1:
        con[i] = str
    else:
        con.append(str)

    read(-1, con)

    return con


def main(file):
    with open(file, "a") as f:
        f.close()

    with open(file, "r") as f:
        content = f.readlines()

    # do stuff with the file here

    print("use the leaf info command for help with leafpie\n\n")
    read(-1, content)

    while True:
        _inp = input("\nleaf pie " + vn + "  :")

        if _inp == "leaf info":
            print("write")
            print("\nuse exit to exit")

        if _inp.startswith("write"):
            if _inp == "write":
                print("write(i) &str& write str to line i, make i -1 to append text to last line of file")
            else:
                i = find_in_pairs("(", ")", _inp)[0]
                string = find_in_pairs("&", "&", _inp)[0]
                content = write(int(i), string, content)

        if _inp == "exit":
            break

    # end

    f.close()
    with open(file, "w") as f:
        f.writelines(content)

    f.close()


if __name__ == '__main__':
    main("test_file.txt")
