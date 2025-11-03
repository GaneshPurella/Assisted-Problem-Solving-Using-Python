def count_lines(filename):
    with open(filename, 'r') as f:
        return sum(1 for _ in f)
