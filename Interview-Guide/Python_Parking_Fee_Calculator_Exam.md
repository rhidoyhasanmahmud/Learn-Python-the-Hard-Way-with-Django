# Python Programming Exam

## Parking Fee Calculator

**Time:** 3 Hours\
**Total Marks:** 100

------------------------------------------------------------------------

## Problem Statement

A shopping mall needs a simple **Parking Fee Calculator**.

Your program will process vehicles one by one. For each vehicle, the
operator will enter:

-   Vehicle number
-   Parking hours

The program will calculate the parking fee and show the bill.

After finishing one vehicle, the program must ask if the operator wants
to add another vehicle.

------------------------------------------------------------------------

## 1. Start the Program

Ask the operator:

``` text
Add a new vehicle? (yes/no):
```

### Rules

-   If the answer is `yes`, process a new vehicle.
-   If the answer is `no`, stop taking new vehicles and show the final
    parking report.
-   Accept both uppercase and lowercase answers.

Example:

``` text
Add a new vehicle? (yes/no): yes
```

------------------------------------------------------------------------

## 2. Vehicle Information

For each vehicle, take:

``` text
Vehicle Number: ABC1234
Parking Hours: 8
```

------------------------------------------------------------------------

## 3. Parking Hour Validation

A vehicle can park for **1 to 24 hours**.

If the parking hours are less than 1 or greater than 24, the input is
invalid.

The operator can try again, but only **3 times**.

If all 3 attempts are invalid, reject the vehicle.

Example:

``` text
Vehicle Number: BAD111

Parking Hours: 30
Invalid parking hours. Try again.

Parking Hours: 0
Invalid parking hours. Try again.

Parking Hours: 25
Parking rejected.
```

After rejecting the vehicle, continue with the next vehicle.

------------------------------------------------------------------------

## 4. Parking Fee Rules

Calculate the parking fee using the following rules:

  Parking Time                            Fee
  ---------------- --------------------------
  Exactly 1 hour                         Free
  Up to 2 hours                          RM 5
  Next 3 hours       RM 3 per additional hour
  After 5 hours      RM 2 per additional hour

### Examples

#### Example 1 --- 1 Hour

``` text
Parking Hours: 1
Parking Fee: RM 0.00
```

#### Example 2 --- 2 Hours

``` text
Parking Hours: 2
Parking Fee: RM 5.00
```

#### Example 3 --- 4 Hours

``` text
First 2 hours = RM 5
Next 2 hours  = 2 × RM 3

Parking Fee = RM 11
```

#### Example 4 --- 8 Hours

``` text
First 2 hours = RM 5
Next 3 hours  = 3 × RM 3
Remaining 3 hours = 3 × RM 2

Parking Fee = RM 20
```

------------------------------------------------------------------------

## 5. Overnight Charge

If a vehicle parks for **more than 18 hours**, add an extra **RM 10**
overnight charge.

Example:

``` text
Parking Fee: RM 40.00
Overnight Charge: RM 10.00

Final Bill: RM 50.00
```

If the vehicle parks for 18 hours or less:

``` text
Overnight Charge: RM 0.00
```

### Final Bill

``` text
Final Bill = Parking Fee + Overnight Charge
```

------------------------------------------------------------------------

## 6. Vehicle Bill

For every successfully processed vehicle, display a bill.

Example:

``` text
Vehicle Number: ABC1234
Parking Hours: 8
Parking Fee: RM 20.00
Overnight Charge: RM 0.00
Final Bill: RM 20.00
```

------------------------------------------------------------------------

## 7. Process More Vehicles

After processing a vehicle, ask again:

``` text
Add a new vehicle? (yes/no):
```

Example:

``` text
Add a new vehicle? (yes/no): yes

Vehicle Number: ABC1234
Parking Hours: 8

...bill...

Add a new vehicle? (yes/no): yes

Vehicle Number: XYZ7788
Parking Hours: 4

...bill...

Add a new vehicle? (yes/no): no
```

When the answer is `no`, stop processing vehicles.

------------------------------------------------------------------------

## 8. Final Parking Report

At the end, display:

-   Number of successfully processed vehicles
-   Number of rejected vehicles
-   Total parking hours of successful vehicles
-   Total revenue
-   Vehicle with the highest final bill
-   Highest final bill
-   Vehicle that parked for the longest time
-   Longest parking hours

Example:

``` text
========== PARKING REPORT ==========

Successful Vehicles: 3
Rejected Vehicles: 1

Total Parking Hours: 29
Total Revenue: RM 65.40

Highest Bill Vehicle: CAR9000
Highest Bill: RM 47.40

Longest Parked Vehicle: CAR9000
Parking Hours: 20
```

If two or more vehicles have the same highest bill, show all of their
vehicle numbers.

------------------------------------------------------------------------

# Sample Input

``` text
Add a new vehicle? (yes/no): yes

Vehicle Number: ABC1234
Parking Hours: 8

Add a new vehicle? (yes/no): yes

Vehicle Number: BKE7788
Parking Hours: 1

Add a new vehicle? (yes/no): yes

Vehicle Number: VAN9001
Parking Hours: 20

Add a new vehicle? (yes/no): yes

Vehicle Number: BAD111
Parking Hours: 30
Parking Hours: 0
Parking Hours: 25

Add a new vehicle? (yes/no): no
```

------------------------------------------------------------------------

# Expected Output

``` text
Vehicle Number: ABC1234
Parking Hours: 8
Parking Fee: RM 20.00
Overnight Charge: RM 0.00
Final Bill: RM 20.00

--------------------------------

Vehicle Number: BKE7788
Parking Hours: 1
Parking Fee: RM 0.00
Overnight Charge: RM 0.00
Final Bill: RM 0.00

--------------------------------

Vehicle Number: VAN9001
Parking Hours: 20
Parking Fee: RM 44.00
Overnight Charge: RM 10.00
Final Bill: RM 54.00

--------------------------------

Parking rejected.

========== PARKING REPORT ==========

Successful Vehicles: 3
Rejected Vehicles: 1

Total Parking Hours: 29
Total Revenue: RM 74.00

Highest Bill Vehicle: VAN9001
Highest Bill: RM 54.00

Longest Parked Vehicle: VAN9001
Parking Hours: 20
```

------------------------------------------------------------------------

## Allowed Python Topics

Use the Python topics learned in class:

-   Variables
-   Basic data types
-   Operators
-   `input()` and `print()`
-   `if`, `elif`, `else`
-   Lists
-   `for` loop
-   `while` loop
-   Nested loops
-   `break`
-   `continue`

## Do Not Use

-   Functions
-   Classes or objects
-   Dictionaries
-   Sets
-   File handling
-   External libraries
-   List comprehensions

------------------------------------------------------------------------

## Important Notes

-   Your program must work for different inputs, not only the sample
    input.
-   The output format does not need to look exactly like the sample.
-   All required calculations and information must be correct.
-   Keep your code simple and readable.
