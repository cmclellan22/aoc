##################################################################
## AOC day 1 part 2
##################################################################

def main ():

    file1 = open('input.txt', 'r') 
    Lines = file1.readlines() 
    
    target = 2020
    answer = []

    for line in range(len(Lines)):
        for i in range (len(Lines)):
            for j in range (len(Lines)):
                first = int(Lines[line])
                second = int(Lines[i])
                third = int(Lines[j])
                if (first != second & second != third):
                    sum = first + second + third
                    if (sum == target):
                        if (first not in answer) & (second not in answer) & (third not in answer):
                            answer.append(first)
                            answer.append(second)
                            answer.append(third)
    product = 1
    for i in range(len(answer)):
        product = product * answer[i]
    if (product != 1):
        print(product)
    else:
        print("No answer found")

if __name__ == '__main__':
    main()
