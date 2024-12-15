#--- Day 1: Historian Hysteria ---
#The Chief Historian is always present for the big Christmas sleigh launch, but nobody has seen him in months! Last anyone heard, he was visiting locations that are historically significant to the North Pole; a group of Senior Historians has asked you to accompany them as they check the places they think he was most likely to visit.

#As each location is checked, they will mark it on their list with a star. They figure the Chief Historian must be in one of the first fifty places they'll look, so in order to save Christmas, you need to help them get fifty stars on their list before Santa takes off on December 25th.

#Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

#You haven't even left yet and the group of Elvish Senior Historians has already hit a problem: their list of locations to check is currently empty. Eventually, someone decides that the best place to check first would be the Chief Historian's office.

#Upon pouring into the office, everyone confirms that the Chief Historian is indeed nowhere to be found. Instead, the Elves discover an assortment of notes and lists of historically significant locations! This seems to be the planning the Chief Historian was doing before he left. Perhaps these notes can be used to determine which locations to search?

#Throughout the Chief's office, the historically significant locations are listed not by name but by a unique number called the location ID. To make sure they don't miss anything, The Historians split into two groups, each searching the office and trying to create their own complete list of location IDs.

#There's just one problem: by holding the two lists up side by side (your puzzle input), it quickly becomes clear that the lists aren't very similar. Maybe you can help The Historians reconcile their lists?

#For example:

#3   4
#4   3
#2   5
#1   3
#3   9
#3   3
#Maybe the lists are only off by a small amount! To find out, pair up the numbers and measure how far apart they are. Pair up the smallest number in the left list with the smallest number in the right list, then the second-smallest left number with the second-smallest right number, and so on.

#Within each pair, figure out how far apart the two numbers are; you'll need to add up all of those distances. For example, if you pair up a 3 from the left list with a 7 from the right list, the distance apart is 4; if you pair up a 9 with a 3, the distance apart is 6.

#In the example list above, the pairs and distances would be as follows:

#The smallest number in the left list is 1, and the smallest number in the right list is 3. The distance between them is 2.
#The second-smallest number in the left list is 2, and the second-smallest number in the right list is another 3. The distance between them is 1.
#The third-smallest number in both lists is 3, so the distance between them is 0.
#The next numbers to pair up are 3 and 4, a distance of 1.
#The fifth-smallest numbers in each list are 3 and 5, a distance of 2.
#Finally, the largest number in the left list is 4, while the largest number in the right list is 9; these are a distance 5 apart.
#To find the total distance between the left list and the right list, add up the distances between all of the pairs you found. In the example above, this is 2 + 1 + 0 + 1 + 2 + 5, a total distance of 11!

#Your actual left and right lists contain many location IDs. What is the total distance between your lists?
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
