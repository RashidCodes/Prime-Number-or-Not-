# Prime Number or Not?
A simple function that returns **True** for a **prime number** and returns **False** otherwise.


## Intuition
- The prime numbers from ***1 to 7*** are ***2, 3, 5 and 7***. The numbers ***1, 4 and 6*** are **not** prime numbers.

- Every even number **except** 2, is **not** a prime number. This condition leaves us with the odd numbers. I would like to assume that all odd numbers are indeed prime, but the base odd numbers (3, 5, 7 - not including 1) make this assumption an invalid one. Any odd number number that is indivisible by any one of the base odd numbers is indeed prime. Combining these 2 conditions solves the problem for numbers greater than 7.
