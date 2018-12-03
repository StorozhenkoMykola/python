def areYouPlayingBanjo(name):
    # Implement me!
    for i in name:
        if i=="r" or i=="R":
            name=name+" plays banjo"
        else: name=name+" does not play banjo"
        break
    return name