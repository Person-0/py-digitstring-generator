# Digits Sequence Generator
This python code takes a number n and generates a string of digits. It runs n times and after each iteration instead of adding the current number entirely, it adds the last digit of the number, then the second last, third last and so on eg. (12 becomes 1, 2) until the entire number is in the string, after which it increments the current number by 1 and continues the process. It finally returns the generated string and the final number at which the iterations stopped. Eg. if n is 4, the generated string is 1 2 3 4 and the number returned is 4.

External Dependencies: None

Sample Output: 
```
? n = 12

final number:  1 2 3 4 5 6 7 8 9 1 0 1

generated string: 11
```
```

? n = 4

final number:  1 2 3 4 

generated string: 4 

```
```

? n = 20

final number:  1 2 3 4 5 6 7 8 9 1 0 1 1 1 2 1 3 1 4 1 

generated string: 15 

```
