import re
import os
from disk.programs import leafpie
from os import listdir
from os.path import isfile, join
import importlib

print("use the info command for help")


def info():
    print("eggthos non bootable os v0.1")
    print("----------------------------")
    print("                    commands")
    print("*type in the name of a command to see its use*")
    print("calc")
    print("disk")
    print("arcade")


def calc(a, b, o, inp):
    if inp == "calc":
        print("calc(a, b, operator) - calculator")

    elif o == "+":
        print(int(a) + int(b))


def disk(inp):
    if inp.startswith("disk.load"):
        load = find_in_pairs("(", ")", inp)[0]
        try:
            exec(str("importlib.reload(disk.games." + load + ")"), globals())
        except:
            pass
        exec(str("import disk." + load), globals())

    if inp.startswith("disk.dir"):
        path = os.getcwd() + "\\disk\\" + find_in_pairs("(", ")", inp)[0]
        print(os.listdir(path))

    if inp.startswith("disk.edit"):
        path = os.getcwd() + "\\disk\\" + find_in_pairs("(", ")", inp)[0]
        leafpie.main(path)

    if inp == "disk":
        print("disk.load(dir) load python file")
        print("disk.dir(dir) print all folders and files in directory")
        print("disk.edit(dir) edit a file using leafpie, if a file is not found it will be automatically made")
        print("")


def arcade(inp):
    if inp == "arcade":
        print("arcade.games list all games on the disk")
        print("arcade.play(name) play a game in the games directory")

    if inp.startswith("arcade.games"):
        path = os.getcwd() + "\\disk\\games"
        onlyfiles = [f for f in listdir(path) if isfile(join(path, f))]
        print(onlyfiles)
        print("(__init__ isnt a game)")

    if inp.startswith("arcade.play"):
        load = find_in_pairs("(", ")", inp)[0]
        try:
            exec(str("importlib.reload(disk.games." + load + ")"), globals())
        except:
            pass
        exec(str("import disk.games." + load), globals())


def find_in_pairs(char_in, char_out, string):
    return re.findall(re.escape(char_in) + '(.*?)' + re.escape(char_out), string)


err = ""


def main(err):
    inp = input("\n:")
    if not inp.startswith("*") and not inp.startswith("exit"):
        try:
            if inp == "info":
                info()
            if inp.startswith("calc"):
                vars = ["1", "1", "+"]
                try:
                    vars = find_in_pairs("(", ")", inp)[0].split(", ")
                except:
                    pass
                calc(vars[0], vars[1], vars[2], inp)

            if inp.startswith("disk"):
                disk(inp)
            if inp.startswith("dev_err"):
                print(err)
            if inp.startswith("dev_py"):
                exec(find_in_pairs("&", "&", inp)[0])
            if inp.startswith("arcade"):
                arcade(inp)
        except Exception as e:
            err = e
            print("error blocked by debugger")

    if not inp.startswith("exit"):
        main(err)


if __name__ == "__main__":
    main(err)
