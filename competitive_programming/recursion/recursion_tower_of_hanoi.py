"""Tower of Hanoi"""

"""
Tower of Hanoi is a mathematical puzzle where we have three rods (A, B, and C) and n disks. 
Initially, all the disks are stacked in decreasing value of diameter i.e., the smallest disk is placed on the top and 
they are on rod A. The objective of the puzzle is to move the entire stack to another rod (here considered C), 
obeying the following simple rules: 

1. Only one disk can be moved at a time.
2. Each move consists of taking the upper disk from one of the stacks and placing it on top of another stack i.e. 
   a disk can only be moved if it is the uppermost disk on a stack.
3. No disk may be placed on top of a smaller disk.

Time Complexity -> 2^n -1 [exponential] where n = number of disks

variables are:
1. disk, n
2. starting_rod, source, A
3. middle_rod, middle, B
4. end_rod, destination, C

Order of the plate:
0
1
2
"""


def hanoi_recursion(disk: int, source: str, middle: str, destination: str):
    # base case - disk 1 is always the smallest plate in the base case
    # so we manipulate the smallest plate in the base case
    if disk == 1:
        print(f'Disk {disk} from {source} to {destination}')
        return

    # this return keyword is used to remove the given function call from the stack memory

    # this is not necessarily the largest plate - this is not the plate 1
    hanoi_recursion(disk - 1, source, destination, middle)
    print(f'Disk {disk} from {source} to {destination}')
    # now we will move the plates from middle rod to destination rod with the help of source rod
    hanoi_recursion(disk - 1, middle, source, destination)


if __name__ == '__main__':
    n = 3
    hanoi_recursion(n, 'A', 'B', 'C')
