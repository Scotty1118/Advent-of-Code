def part_1():
    with open('2016_Day1.txt','r') as route:
        twice=[]
        direction='N'
        compass = {'N':[0,1], 'E':[1,0], 'W':[-1,0], 'S':[0,-1]}

        dist=0

        for r in route.readlines():
            print(len(r))
            loc = [0, 0]
            r=r.strip()
            d=r.split(', ')
            for m in d:
                rot = m[0]

                #print(f'm: {m} rot: {rot} dist: {dist} start loc: {loc}')
                if rot == 'R':
                    if direction == 'N':
                        direction='E'
                    elif direction == 'E':
                        direction='S'
                    elif direction == 'S':
                        direction = 'W'
                    elif direction == 'W':
                        direction = 'N'
                else:
                    if direction == 'N':
                        direction='W'
                    elif direction == 'W':
                        direction = 'S'
                    elif direction == 'S':
                        direction = 'E'
                    elif direction== 'E':
                        direction='N'


                if direction == 'N':
                    loc[1] += dist
                elif direction == 'S':
                    loc[1] -= dist
                elif direction == 'E':
                    loc[0] += dist
                elif direction == 'W':
                    loc[0] -= dist
                twice.append(loc)

                print(f'moved {direction} {dist} spaces, New loc {loc}')
            print(twice)
            print(f'loc: {loc} distance: {abs(loc[0])+abs(loc[1])}')
        for x in twice:
            print(x)



part_1()