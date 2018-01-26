from csc131 import dishearneer


def main():
    print("Main")
    d =dishearneer.get_personal_date()
    print(d)
    for key in sorted(d.keys()):
        print("%s: %s" % (key, d[key]))



if __name__=='__main__':
    main()
