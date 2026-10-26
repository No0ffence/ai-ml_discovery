import sys

def main():
    try:
        if len(sys.argv) != 3:
            print("Usage: python3 main.py <min> <max>")
            return
        min_temp = sys.argv[1]
        max_temp = sys.argv[2]
    except Exception as e:
        print(e)


if __name__ == "__main__":
    main()
