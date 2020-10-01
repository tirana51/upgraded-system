# Problem Statement
Consider the fraction, a/b, where a and b are positive integers. If a<b and GCD(a,b)=1, it is called a reduced proper fraction.

If we list the set of a reduced proper fraction for d≤8, (where d is the denominator) in ascending order of size, we get:

1/8, 1/7, 1/6, 1/5, 1/4, 2/7, 1/3, 3/8, 2/5 , 3/7, 1/2, 4/7, 3/5, 5/8, 2/3, 5/7, 3/4, 4/5, 5/6, 6/7, 7/8
It can be seen that 2/5 is the fraction immediately to the left of 3/7.

By listing the set of reduced proper fractions for d≤N in ascending order of value, find the numerator and denominator of the fraction immediately to the left of a/b when a and b are given.

## Input
 - First line of input contains an integer T, number of test cases
 - Next T lines contain a b N separated by space

## Output
Print the numerator and denominator separated by a space corresponding to each test case on a new line

## Constraints
 - 1<=T<=50
 - 1<=a<b<=10^9
 - GCD(a,b)=1
 - b<N<=10^15