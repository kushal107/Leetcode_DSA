user_list = [int(x) for x in input("Enter numbers: ").split()]
sum_number = input("\nEnter Sum: ")
sum_number = int(sum_number)
user_list.sort()

def twosum(userlist, sumnumber):
    length = len(user_list)
    first = 0
    last = length - 1
    flag = False
    while(flag == False and first < last):
        tempsum = userlist[first]+userlist[last]
        if tempsum == sumnumber:
            flag = True
            break
        elif tempsum > sumnumber:
            last -= 1
        else:
            first += 1
    
    if flag == True:
        return(first,last)
    else:
        return('Not found')

result = twosum(user_list,sum_number)
print(result)
