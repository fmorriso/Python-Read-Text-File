import os, sys

def find_file_from_current(filename: str) -> str:
    """
    Find a file starting from the directory where program execution started.
    If more than one occurrence of the file is available, the first one found will be used.
    :param filename:  A filename with extension, such as "example.txt".
    :return: The full path of the file where it was found.
    """
    # start by figuring out where the program started
    base_path = os.path.dirname(os.path.realpath(__file__))
    print(f"{base_path=}")
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file == filename:
                return str(os.path.join(root, file))
    return ''

def get_python_version() -> str:
    return f'{sys.version_info.major}.{sys.version_info.minor}.{sys.version_info.micro}'

def main():
    full_path = find_file_from_current('simple text file.txt')
    print(f'Full path: {full_path}')

    with open(full_path, 'r') as text_file:
        for line in text_file:
            print(line.strip())

if __name__ == '__main__':
    print(f'Python version: {get_python_version()}')
    main()