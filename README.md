# Contents
calc.py - file containing the function nextNumber that takes natural numbers as args and returns the next number 
with the same number of digits and the same sum of all digits.

test_calc.py: - unit testing file

- Run this file with 
```bash
python test_calc.py 
``` 

## Usage + extra notes
- the function can take both ints and strings as arguments 
although it needs to receive a string for cases like "0200" where numbers
start with a 0.

- the function returns have been designed to be strings because of cases 
like "0325" where the result is "0334". I did not know if you want the 0 to
be left there if the next number did not need to use it like in the case 
of "0200" to "1001". If desired output is of int type, it can easily be changed
with int() and the starting zero will be lost.
