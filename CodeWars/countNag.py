def count_positives_sum_negatives(arr):
    s=0
    count=0
    if not arr:
        return []
    for i in arr:
        if i<0:
            s+=i
        elif i>0:
            count+=1
    return [count,s]