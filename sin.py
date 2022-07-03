import math

k = int(input())

for i in range(1, 10**9):
    if 0 <= math.sin(i) <= 1/k:
        print(i)
        exit()
 ...

<!---
FarzadABou/FarzadABou is a ✨ special ✨ repository because its `README.md` (this file) appears on your GitHub profile.
You can click the Preview link to take a look at your changes.
--->
