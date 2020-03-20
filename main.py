import sys

def isMapping(s1, s2):
    pass

if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("argument doesn't meet the requirement")
        exit()
    s1 = sys.argv[1]
    s2 = sys.argv[2]
    if isMapping(s1, s2):
        print("true")
    else:
        print("false")