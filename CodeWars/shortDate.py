def shorten_to_date(long_date):
    signPos=long_date.find(',')
    return long_date[0:signPos]