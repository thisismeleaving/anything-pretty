import fileinput
from rich import print

if __name__ == "__main__":
    with fileinput.input(encoding="utf-8") as fh:
        for line in fh:
            end = "" if line.endswith("\n") else "\n"
            print(line, end=end)
