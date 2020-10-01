# Problem Statement
Due to the COVID pandemic, maintaining social distancing is of utmost importance. In this problem, you'd calculate how many days would it take to reach an apocalypse from an initial case if nobody maintains social distancing.

The Earth is flat (for this question) and it's dimensions are R x C
The whole Earth is already divided into blocks and now the virus has learnt to spread in ALL directions, even diagonally. The virus from each newly infected person will spread in all directions in the next day, thus growing exponentially.

## Input
 - First line will contain T, number of testcases. Then the testcases follow.
 - Next line contains R and C respectively separated by a space.
 - Next line contains x and y respectively separated by a space, denoting the indices of the initial case in the world.
 
## Output
For each testcase, output in a single line an integer denoting the number of days after which everyone will be infected.

## Constraints
 - 1<=T<=10^4
 - 2<=R,C<=10^7
 - 0<=x,y<=10^7