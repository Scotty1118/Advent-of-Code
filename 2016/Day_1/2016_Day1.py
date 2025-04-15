'''
--- Day 1: No Time for a Taxicab ---
Santa's sleigh uses a very high-precision clock to guide its movements, and the clock's oscillator is regulated by stars. Unfortunately, the stars have been stolen... by the Easter Bunny. To save Christmas, Santa needs you to retrieve all fifty stars by December 25th.

Collect stars by solving puzzles. Two puzzles will be made available on each day in the Advent calendar; the second puzzle is unlocked when you complete the first. Each puzzle grants one star. Good luck!

You're airdropped near Easter Bunny Headquarters in a city somewhere. "Near", unfortunately, is as close as you can get - the instructions on the Easter Bunny Recruiting Document the Elves intercepted start here, and nobody had time to work them out further.

The Document indicates that you should start at the given coordinates (where you just landed) and face North. Then, follow the provided sequence: either turn left (L) or right (R) 90 degrees, then walk forward the given number of blocks, ending at a new intersection.

There's no time to follow such ridiculous instructions on foot, though, so you take a moment and work out the destination. Given that you can only walk on the street grid of the city, how far is the shortest path to the destination?

For example:

Following R2, L3 leaves you 2 blocks East and 3 blocks North, or 5 blocks away.
R2, R2, R2 leaves you 2 blocks due South of your starting position, which is 2 blocks away.
R5, L5, R5, R3 leaves you 12 blocks away.
How many blocks away is Easter Bunny HQ?
'''



def part_1():
    with open('2016_Day1.txt', 'r') as route:
        twice=[]
        direction='N'
        compass = {'N':[0,1], 'E':[1,0], 'W':[-1,0], 'S':[0,-1]}
        count=0
        dist=0
        for r in route.readlines():

            loc = [0, 0]
            r=r.strip()
            d=r.split(', ')
            for m in d:
                count += 1
                rot = m[0]
                dist=int(m[1:])
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
                    twice.append(loc)
                elif direction == 'W':
                    loc[0] -= dist
                twice.append(loc)


                #print(f'moved {direction} {dist} spaces, New loc {loc}')

            print(f'Part 1 answer is {abs(loc[0])+abs(loc[1])} loc: {loc} distance: {abs(loc[0])+abs(loc[1])}')
        print(twice)
        for z in twice:

            for x in twice:
                if z==x:
                   continue
                if z==x:
                    print(f' First Place twice {x}')





part_1()