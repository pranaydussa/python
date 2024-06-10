for a in range(5):
    print("outer: "+str(a))
    for b in range(5,8):
        if b==6:
            break
        print("inner: "+str(b))