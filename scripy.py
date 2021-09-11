import sys

# import requests

print(sys.version)
print(sys.executable)

# r = requests.get("https://google.com")
# print(r.status_code)
# print(r.ok)

if __name__ == "__main__":
    alist = [a for a in range(10)]  # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    print(alist)  # 1,2,3,4,5,6,7,8,9
    blist = alist[2:5]
    print(blist)  # 2,3,4
    clist = alist[::2]
    print(clist)  # 0,2,4,6,8

    # tuple
    c_tuple = (1, 6, 2, 1, 7, 9, 3, 2, 1, 4, 6, 7)
    print("tuple: ", end="")
    print(c_tuple.index(6))  # fist 6 is at index 1

    # dictionary
    mydict = {"name": "Taylor", "age": 99}
    for key in mydict.keys():
        print(key, end=" ")  # name age
    for value in mydict.values():
        print(value, end=" ")
    print()
    for key, value in mydict.items():
        print(key, " ", value)
