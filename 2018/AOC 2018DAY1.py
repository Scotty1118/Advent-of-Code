def part_1():
    result=0
    with open('AOC2018 DAY1', 'r') as frequency:
        for i in frequency:
            result+=int(i)
    print(result)


def part_2():
    number_seen=set()
    result=0
    iterations=0
    with open('AOC2018 DAY1', 'r') as frequency:
        lines = frequency.readlines()
        while result not in number_seen:
            for t in lines:
                number_seen.add(result)
                result+=int(t)
                print ("current result",result)
                if result in number_seen:
                    print('first number seen',result)
                    return result
                iterations+=1
                print('iterations',iterations)
                print('size of number seen', len(number_seen))

part_2()