def part_1():
    store1 = []
    store2 = []
    with open ('2020_DAY1.txt','r') as expense_report:
       for entries in  expense_report.readlines():
        store1.append(int(entries.strip()))
        sum=0
        count1=0
        count2=0
        answer=0
        store2= store1
        for i in store1:
            number1=int(i)
            count1+=1
            if sum==2020:
                print(f'first number {i}')
                return
            for t in store2:
                number2=int(t)
                sum=number1+number2
                count2+=1
                if sum==2020:
                    answer=i*t
                    print(f'first number {i}')
                    print(f'second number {t}')
                    print(f'the product is {answer}')
                    print(f'loop 1 ran {count1} times')
                    print(f'loop 2 ran {count2} times')
                    return




#--- Part Two ---
#The Elves in accounting are thankful for your help; one of them even offers you a starfish coin they had left over from a past vacation. They offer you a second one if you can find three numbers in your expense report that meet the same criteria.

#Using the above example again, the three entries that sum to 2020 are 979, 366, and 675. Multiplying them together produces the answer, 241861950.

#In your expense report, what is the product of the three entries that sum to 2020?

def part_2():
    store1 = []
    store2 = []
    store3 = []

    with open('2020_DAY1.txt', 'r') as expense_report:
        for entries in expense_report.readlines():
            store1.append(int(entries.strip()))
            sum = 0
            count1 = 0
            count2 = 0
            count3 = 0
            answer = 0
            store2 = store1
            store3= store1

            for i in store1:
                number1 = int(i)
                count1 += 1
                if sum == 2020:
                    print(f'first number {i}')
                    return
                for s in store2:
                    number2 = int(s)
                    count2 += 1
                    if sum == 2020:
                        print(f'first number {i}')
                        return
                    for t in store3:
                        number3 = int(t)
                        sum = number1 + number2 + number3
                        count3 += 1
                        if sum == 2020:
                            answer = i * t * s
                            print(f'first number {i}')
                            print(f'second number {s}')
                            print(f'second number {t}')
                            print(f'the product is {answer}')
                            print(f'loop 1 ran {count1} times')
                            print(f'loop 2 ran {count2} times')
                            print(f'loop 3 ran {count3} times')
                            return

part_2()