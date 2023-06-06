class Name:
    name = input("Hello there! Can I please have your first name?: ")
    print("Okay " + name + " lets get started!")

class Table:
    #initial Number
    invest = int(input("Can you provide the investigative number please? Enter 0 at anytime if you wish to exit: \n"))
    if invest == 0 : print("Have a great day!")
    if invest == 0 : exit()
    if invest > 10 : invest = int(input("Enter something no greater than 10 please!: \n"))

    #Minimum Number
    min = int(input("Can you provide the minimum number of the range?: \n"))
    if min == 0 : print("Have a great day!")
    if min == 0 : exit()

    #Maximum Number
    max = int(input("Now can you provide the maximum number of the range?: \n"))
    if max == 0 : print("Have a great day!")
    if max == 0 : exit()
    
    #Math set up for the list
    list1 = [x for x in range(min,max + 1)]
    list2 = [invest]
    list3 = list2 * 1000
    print(list(zip(list1, list3)))
    print()
    math = [x * y for x,y in zip(list1, list3)]
    print()
    print(math)