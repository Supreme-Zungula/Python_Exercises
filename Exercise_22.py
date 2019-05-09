# Read from file
import sys

if __name__ == "__main__":
    counter_dict = {}
    if len(sys.argv) != 2:
        exit(0)
    else:
        with open(sys.argv[1], 'r') as f:
            line = f.readline()
            while line:
                line = line.strip()
                if line in counter_dict:
                    counter_dict[line] += 1
                else:
                    counter_dict[line] = 1
                line = f.readline()
    print(counter_dict)
