import os
import sys
from collections import defaultdict


def get_second_row(file_path):
    try:
        with open(file_path, "r") as file:
            lines = file.readlines()
            if len(lines) >= 2:
                return lines[1].strip()
            else:
                return None
    except Exception as e:
        print(f"Error reading file {file_path}: {e}")
        return None


def group_files_by_second_row(directory):
    grouped_files = defaultdict(list)

    for root, _, files in os.walk(directory):
        for file in files:
            if file.endswith(".md"):
                file_path = os.path.join(root, file)
                second_row = get_second_row(file_path)
                if second_row is not None:
                    grouped_files[second_row].append(file_path)

    return grouped_files


def main():
    if len(sys.argv) != 2:
        print("USAGE: python group.py [directory]")
        return
    directory = sys.argv[1]
    grouped_files = group_files_by_second_row(directory)

    for second_row, files in grouped_files.items():
        if second_row and second_row[0] == "(" and second_row[-1] == ")":
            grppath = os.path.join(directory, "grouped", second_row[1:-1])
            os.makedirs(grppath, exist_ok=True)
            print(f"Group: {second_row}")
            for file in files:
                print(f"  - {file}")
                os.symlink(
                    os.path.join("..", "..", "..", file),
                    os.path.join(grppath, file.replace("CZ 1/", "").replace("/", "_")),
                )

        else:
            print(f"Invalid Group: {second_row}")
            for file in files:
                print(f"  - {file}")


if __name__ == "__main__":
    main()
