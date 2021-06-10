#Assignment 3: HarderSort
def count_numbers(sorted_list,less_than):
    count=0
    for i in range(len(sorted_list)):
        if(sorted_list[i] < less_than):
            count=count+1
    print(count)
    
sorted_list = [1, 3, 5, 7]
count_numbers(sorted_list, 4) # should print 2
