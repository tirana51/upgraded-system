# Problem Statement
Due to the COVID pandemic, there has been an increase in the number of cases if a hospital. The management has decided to clear a large square area for the patients and arrange for beds. But the beds can't be too near to each other.

The area is of dimension N x N
The whole area is already divided into blocks. 1 means there's a bed in the block, 0 denotes there isn't. Note, beds placed on consecutive diagonal blocks are safe.

This is a SAFE example:

1 0

0 1

This is an UNSAFE example:

0 1 1

0 0 0

1 0 0

To avoid spreading the virus even further, you have to make sure no two adjacent blocks have beds in them. This is done to maintain distance between beds.

Return an output of "SAFE" if you find the workers have arranged the beds with due consideration to the distance needed. Return "UNSAFE" otherwise.

## Input
 - First line will contain T, number of testcases. Then the testcases follow.
 - Next line contains N.
 - Next N lines will contain N number of space-separated integers Ai which make denote the beds in the area.

## Output
For each test case, output in a single line whether the total arrangement is "SAFE" or "UNSAFE". Even if there's a single unsafe bed in the whole area, report the whole area as "UNSAFE".

## Constraints
 - 1<=T<=100
 - 0<=Ai<=1
 - 2<=N<=100