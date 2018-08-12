num_list=[5, 2, 0, 6, 9, 4, 3, 1, 8, 10, 8, 8, 8]
for i in range(len(num_list)-1, 0, -1):
    for j in range(i):
        if num_list[j]>num_list[j+1]:
            num_list[j], num_list[j+1]=num_list[j+1], num_list[j]
print(num_list)
