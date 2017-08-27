import argparse
import uflash
import re

parser = argparse.ArgumentParser(description='Build and flash a Python program for your micro:bit')
parser.add_argument("source_file", type=argparse.FileType('r'))
parser.add_argument("-o", "--output-filename")

def main():
    args = parser.parse_args()
    src = args.source_file.read()
    output_file = args.output_filename or "program-src.py"
    with open("mycrobit.py", "r") as lib:
        with open(output_file, "w") as output:
            # library code
            output.write(lib.read())
            # program source code
            output.write("\n")
            output.write("# your source code")
            output.write("\n\n")
            output.write(src)
            # program main
            classname = re.search("(\w+)\(Microbit\):", src).group(1)
            output.write("\n")
            output.write("# run program")
            output.write("\n\n")
            output.write("""if __name__ == "__main__":\n    app = """)
            output.write(classname)
            output.write("""(get_time, get_a_pressed, get_b_pressed)\n    app.start()\n""")
        uflash.main([output_file])
    return

if __name__ == "__main__":
    main()
