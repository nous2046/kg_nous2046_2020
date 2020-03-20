import sys

def isMapping(s1, s2):
    if len(s1) != len(s2):
        return False
    map = {}
    for c1, c2 in zip(s1, s2):
        if c1 in map.keys() and map[c1] != c2:
            return False
        if c1 not in map.keys():
            map[c1] = c2
    return  True     


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