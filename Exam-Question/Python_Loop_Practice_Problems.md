# Python Loop Practice Problems

## Theme: School Event Management System

These problems are connected to a three-day school event. Solve them using only variables, basic data types, operators, conditions, lists, loops, nested loops, `break`, and `continue`.

---

## Problem 1: Participant Registration

### Problem Statement

A school is registering students for an event. Take the name and age of each student. At the end, show the number of successful and rejected registrations.

### Rules

- First, input the number of students.
- Use a loop to take each student's name and age.
- A name cannot be empty.
- The student's age must be between 10 and 18.
- Reject the registration if the name or age is invalid.

### Input Example

```text
Number of students: 4

Student 1 name: Hasan
Age: 16

Student 2 name: Rahim
Age: 21

Student 3 name:
Age: 15

Student 4 name: Nusrat
Age: 14
```

### Expected Output

```text
Hasan: Registration successful
Rahim: Registration rejected
Student 3: Registration rejected
Nusrat: Registration successful

Successful registrations: 2
Rejected registrations: 2
```

---

## Problem 2: Age Validation with Limited Attempts

### Problem Statement

Improve the registration system. If a student enters an invalid age, allow the student to try again. Each student can try a maximum of three times.

### Rules

- First, input the number of students.
- Use a loop to process all students.
- A valid age is between 10 and 18.
- Each student gets a maximum of three attempts.
- Stop asking when the student enters a valid age.
- Cancel the registration after three invalid attempts.

### Input Example

```text
Number of students: 2

Student name: Hasan
Enter age: 25
Enter age: 8
Enter age: 16

Student name: Rahim
Enter age: 30
Enter age: 20
Enter age: 9
```

### Expected Output

```text
Hasan: Registration successful
Rahim: Registration cancelled

Successful registrations: 1
Cancelled registrations: 1
```

---

## Problem 3: Event Selection

### Problem Statement

Each registered student can join up to three activities. Record the selected activities and count the valid, duplicate, and invalid selections.

### Rules

- First, input the number of students.
- Available activity numbers are:
  - `1` = Quiz
  - `2` = Coding
  - `3` = Debate
  - `4` = Chess
- Use loops to process the students and their selections.
- One student cannot select the same activity more than once.
- Do not use `set`.
- Ignore duplicate and invalid selections.

### Input Example

```text
Number of students: 2

Student name: Hasan
Number of selections: 3
Activity number: 1
Activity number: 2
Activity number: 2

Student name: Nusrat
Number of selections: 2
Activity number: 3
Activity number: 5
```

### Expected Output

```text
Hasan selected 2 activities
Nusrat selected 1 activity

Valid selections: 3
Duplicate selections: 1
Invalid selections: 1
```

---

## Problem 4: Group Ticket Calculator

### Problem Statement

Each student can bring guests to the school event. Calculate the ticket price for every student group and the total ticket revenue.

### Rules

- A student ticket costs RM 10.
- A guest below 12 years old pays RM 8.
- A guest from 12 to 59 years old pays RM 20.
- A guest aged 60 or above pays RM 10.
- A guest's age must be greater than 0.
- Ignore a guest with an invalid age.
- If a group has five or more people, give a 10% discount.
- The student is also counted as a group member.

### Input Example

```text
Number of students: 2

Student name: Hasan
Number of guests: 4
Guest 1 age: 35
Guest 2 age: 9
Guest 3 age: 62
Guest 4 age: 20

Student name: Rahim
Number of guests: 1
Guest 1 age: 30
```

### Expected Output

```text
Hasan's subtotal: RM 68.00
Hasan's discount: RM 6.80
Hasan's final bill: RM 61.20

Rahim's subtotal: RM 30.00
Rahim's discount: RM 0.00
Rahim's final bill: RM 30.00

Total ticket revenue: RM 91.20
```

---

## Problem 5: Competition Score Analyzer

### Problem Statement

The event has several competitions. Each competition has several participants, and every participant completes three rounds. Calculate each participant's result and find the winner of each competition.

### Rules

- First, input the number of competitions.
- For each competition, input its name and number of participants.
- Each participant receives a score in three rounds.
- A valid score is between 0 and 100.
- Use 0 for an invalid score.
- A participant qualifies if the average score is 50 or higher.
- The participant with the highest total score wins the competition.
- Assume that there is no tie.

### Input Example

```text
Number of competitions: 1

Competition name: Quiz
Number of participants: 2

Participant name: Hasan
Round 1 score: 70
Round 2 score: 80
Round 3 score: 60

Participant name: Rahim
Round 1 score: 55
Round 2 score: 40
Round 3 score: 50
```

### Expected Output

```text
Hasan
Total score: 210
Average score: 70.00
Status: Qualified

Rahim
Total score: 145
Average score: 48.33
Status: Not qualified

Quiz winner: Hasan
Winning score: 210
```

---

## Problem 6: Food Stall Sales

### Problem Statement

Several food stalls are selling food at the event. Calculate the revenue of every stall and find the stall with the highest revenue.

### Rules

- First, input the number of stalls.
- For each stall, input its name and number of orders.
- For every order, input the item price and quantity.
- Quantity 0 means the order was cancelled.
- A negative price or quantity means the order is invalid.
- Ignore cancelled and invalid orders.
- Give a 5% discount if one order costs more than RM 50.
- Assume that there is no tie between the stalls.

### Input Example

```text
Number of stalls: 2

Stall name: Burger House
Number of orders: 3
Order 1 price: 10
Order 1 quantity: 2
Order 2 price: 8
Order 2 quantity: 0
Order 3 price: 15
Order 3 quantity: 4

Stall name: Drink Corner
Number of orders: 2
Order 1 price: 5
Order 1 quantity: 4
Order 2 price: 7
Order 2 quantity: 3
```

### Expected Output

```text
Burger House revenue: RM 77.00
Cancelled orders: 1

Drink Corner revenue: RM 41.00
Cancelled orders: 0

Total food revenue: RM 118.00
Best stall: Burger House
```

---

## Problem 7: Budget-Controlled Shopping

### Problem Statement

Each student has a limited food budget. Process the requested items without allowing the student to spend more than the available budget.

### Rules

- First, input the number of students.
- For each student, input the name, budget, and number of requested items.
- For every item, input its price and quantity.
- Ignore an item with a negative price or a quantity less than 1.
- Reject an item if buying it would exceed the budget.
- Stop the student's shopping after two rejected items in a row.
- Show the total spent, remaining budget, and purchased quantity.

### Input Example

```text
Number of students: 1

Student name: Hasan
Budget: 30
Number of requested items: 5

Item 1 price: 5
Item 1 quantity: 2
Item 2 price: 8
Item 2 quantity: 2
Item 3 price: 7
Item 3 quantity: 1
Item 4 price: 10
Item 4 quantity: 1
```

### Expected Output

```text
Item 1 added: RM 10.00
Item 2 added: RM 16.00
Item 3 rejected: Budget exceeded
Item 4 rejected: Budget exceeded
Shopping stopped

Hasan spent: RM 26.00
Remaining budget: RM 4.00
Purchased quantity: 4
```

---

## Problem 8: Auditorium Seat Report

### Problem Statement

The school needs a seat report for the event auditorium. Check every seat and show the booking information for each row and the full auditorium.

### Rules

- First, input the number of rows and seats in each row.
- Use `1` for a booked seat.
- Use `0` for an available seat.
- Ignore any other value as an invalid seat status.
- Show the booked and available seats in every row.
- Show `Fully booked` when all seats in a row are booked.
- Find the row with the highest number of booked seats.
- If several rows have the same highest value, show the first one.

### Input Example

```text
Number of rows: 3
Seats in each row: 4

Row 1 seat statuses: 1 1 0 1
Row 2 seat statuses: 1 1 1 1
Row 3 seat statuses: 0 0 1 0
```

### Expected Output

```text
Row 1: 3 booked, 1 available
Row 2: Fully booked
Row 3: 1 booked, 3 available

Total seats: 12
Booked seats: 8
Available seats: 4
Occupancy: 66.67%
Most booked row: Row 2
```

---

## Problem 9: Three-Day Attendance Tracker

### Problem Statement

The school event continues for three days. Record every student's attendance and prepare an attendance report.

### Rules

- First, input the number of students.
- For each student, take attendance for three days.
- `P` means present and `A` means absent.
- Accept lowercase or uppercase letters.
- If the status is invalid, ask again until the user enters a valid status.
- Three present days means `Perfect Attendance`.
- Two present days means `Regular`.
- Less than two present days means `Irregular`.

### Input Example

```text
Number of students: 2

Student name: Hasan
Day 1: P
Day 2: X
Enter Day 2 again: p
Day 3: A

Student name: Nusrat
Day 1: P
Day 2: P
Day 3: P
```

### Expected Output

```text
Hasan
Present: 2
Absent: 1
Attendance: 66.67%
Status: Regular

Nusrat
Present: 3
Absent: 0
Attendance: 100.00%
Status: Perfect Attendance

Students with perfect attendance: 1
```

---

## Problem 10: Event Championship

### Problem Statement

Several teams are joining the final championship. Each team joins several competitions, and three judges score each competition. Calculate the final scores and find the champion and runner-up.

### Rules

- First, input the number of teams and competitions per team.
- For each team, input the team name.
- Three judges score every competition.
- A valid judge score is between 0 and 10.
- If a score is invalid, ask again until a valid score is entered.
- Calculate the average of the three judge scores.
- Add 3 bonus points if the average is 8 or higher.
- Add 1 bonus point if the average is from 6 to below 8.
- Add no bonus if the average is below 6.
- If the average is below 3, disqualify that competition result and do not add its score.
- Add all valid competition scores to get the team's total.
- Assume that there is no tie.

### Input Example

```text
Number of teams: 3
Competitions per team: 2

Team name: Tigers
Competition 1 scores: 8 9 7
Competition 2 scores: 6 7 5

Team name: Falcons
Competition 1 scores: 7 8 6
Competition 2 scores: 7 6 7

Team name: Lions
Competition 1 scores: 5 6 4
Competition 2 scores: 9 8 8
```

### Expected Output

```text
Tigers competition 1: 11.00 points
Tigers competition 2: 7.00 points
Tigers total: 18.00 points

Falcons competition 1: 8.00 points
Falcons competition 2: 7.67 points
Falcons total: 15.67 points

Lions competition 1: 5.00 points
Lions competition 2: 11.33 points
Lions total: 16.33 points

Champion: Tigers
Champion score: 18.00 points
Runner-up: Lions
Runner-up score: 16.33 points
```
