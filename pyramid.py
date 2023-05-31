"""pyramid -9
given a number N write a program to print a pyramid inside a rectangle of N rows using zeros to represent the pyramid
and dots. in the remaining places of the rectangle.
input
5
output

. . . . 0 . . . .
. . .0 0 0. . .
. . 0 0 0 0 0 . .
. 0 0 0 0 0 0 0 .
0 0 0 0 0 0 0 0 0"""

n = int(input("Enter Number : "))
for i in range(1, n + 1):
    zeroes = ". " * (n - i)
    ones = "0 " * ((2 * i) - 1)
    print(zeroes + ones + zeroes)