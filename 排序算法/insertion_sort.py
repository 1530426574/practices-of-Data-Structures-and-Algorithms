
def insert_sort(arry):
    for i in range(1,len(arry)):
        card = arry[i]                     #current card
        j = i - 1                          #prev card
        while j >= 0  and card < arry[j]:  #current < prev
            arry[j+1] = arry[j]            #shift right
            j -= 1                         #continue compare
        arry[j+1] =  card                  #find the correct position
    return arry



arry = [12, 11, 13, 5, 6]
print(insert_sort(arry))