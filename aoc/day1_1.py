##################################################################
## AOC day 1 part 1
##################################################################

def main ():

    file1 = open('input.txt', 'r') 
    Lines = file1.readlines() 
    
    #Lines = [1,2,3,4,5,6,7,8,9,10,11,12]
    target = 2020
    answer = []

    for line in range(len(Lines)):
        for i in range (len(Lines)):
            first = int(Lines[line])
            second = int(Lines[i])
            sum = first + second
            #print('sum: ', sum)
            if (sum == target):
                if (first not in answer) & (second not in answer):
                    #print(first)
                    #print(second)
                    answer.append(first)
                    answer.append(second)
                #print(line, ' plus ', i, " equals ", target)
    product = 1
    for i in range(len(answer)):
        #print(answer[i])
        product = product * answer[i]
    if (product != 1):
        print(product)
    else:
        print("No answer found")

if __name__ == '__main__':
    main()
