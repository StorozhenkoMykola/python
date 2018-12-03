def enough(cap, on, wait):
    a=0
    if (cap-on)<wait:
        a=wait-(cap-on)
    return a