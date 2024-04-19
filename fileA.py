from fileB import map_lists, test_conv

if __name__=="__main__":
    print("This is File A")

    #Call map_lists
    conv = map_lists([1,0], [0,1])
    for e in conv:
        print(conv)

    test_conv(map_lists([3,0],[0,-3]))
