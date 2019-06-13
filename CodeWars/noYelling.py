def filter_words(st):
    st=st.lower()
    st=list(st)
    st[0]=st[0].upper()
    st=''.join(st)
    st=st.split()
    st=' '.join(st)
    return st