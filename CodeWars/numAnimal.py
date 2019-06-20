def list_animals(animals):
    list=''
    n=1
    for i in animals:
        i=str(n)+'. '+str(i)+"\n"
        list+=i
        n+=1
    return list