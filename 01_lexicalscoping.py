test = int(input("Enter the number of taste case : "))
str1 = ""
for i in range(test):
    str1 = input("Enter the big string : ")
    str2 = input("Enter the small string : ")
    # converting to array
    myarr1 = list(str1)
    myarr2 = list(str2)
    listify = []

    for value in myarr2:
        index = str1.find(value)
        listify.append(index)
    listify.sort()
    for j in listify:
        print(myarr1[j], end="")
    
# Test Case

# 1
# polikujmnhytgbvfredcxswqaz
# abcd
# Output : bdca