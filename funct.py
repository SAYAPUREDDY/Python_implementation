import sys
def usage():
    print("Appname by Author, Uni, 2023")
    print("Usage: appname ‐‐arg value")
    # exit()
def main (args):
    if len(args) == 1 or "‐h" in args:
        usage()
        if __name__ == "__main__":
            print(sys.argv)
            # main(sys.argv)
main("a")

