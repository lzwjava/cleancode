import os
import re
import argparse
import shutil


def clean_code(input_file):
    if not input_file.endswith(".py"):
        print("Error: Input file must have a '.py' extension.")
        return

    if not os.path.isfile(input_file):
        print(f"Error: Input file '{input_file}' does not exist.")
        return

    filename, file_extension = os.path.splitext(input_file)
    backup_file = f"{filename}_original{file_extension}"

    shutil.copy(input_file, backup_file)

    with open(input_file, 'r') as file:
        code = file.read()

    cleaned_code = re.sub(r'(?:^|\n)\s*""".*?"""', '', code, flags=re.DOTALL)
    cleaned_code = re.sub(r'#.*', '', cleaned_code)

    with open(input_file, 'w') as file:
        file.write(cleaned_code)

    print(f"Cleaned code saved to {input_file}")
    print(f"Original code backed up to {backup_file}")


def main():
    parser = argparse.ArgumentParser(description="Clean Python code by removing comments.")
    parser.add_argument("input_file", help="Input Python file to clean (must have a '.py' extension).")
    args = parser.parse_args()
    clean_code(args.input_file)


if __name__ == "__main__":
    main()
