import os

def find_file(filename: str) -> str:
    # start by figuring out where the program started
    base_path = os.path.dirname(os.path.realpath(__file__))
    print(f"{base_path=}")
    for root, dirs, files in os.walk(base_path):
        for file in files:
            if file == filename:
                return str(os.path.join(root, file))
    return ''

def main():
    full_path = find_file('simple text file.txt')
    print(f'Full path: {full_path}')

    with open(full_path, 'r') as text_file:
        for line in text_file:
            print(line.strip())

if __name__ == '__main__':
    main()