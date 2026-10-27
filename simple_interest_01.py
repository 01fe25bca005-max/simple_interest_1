import sys

def simple_interest(p, t, r):
    return (p * t * r) / 100

if __name__ == "__main__":
    if len(sys.argv) >= 4:
        p = int(sys.argv[1])
        t = int(sys.argv[2])
        r = int(sys.argv[3])
        print("Simple interest is:", simple_interest(p, t, r))