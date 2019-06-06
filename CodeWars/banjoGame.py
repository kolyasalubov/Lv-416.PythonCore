def areYouPlayingBanjo(name):
    for i in name.lower():
        if i[0]=="r":
            return name + " plays banjo"
        else:
            return name + " does not play banjo"


 