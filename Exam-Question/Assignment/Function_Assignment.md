# Assignment: Student Result Management System

## Objective

Create a **Student Result Management System** using Python.

The program will accept information for multiple students, calculate their results using functions, and finally display a class summary.

### Concepts You Must Practice

* Functions
* `while` Loop
* `for` Loop
* `if / elif / else`

---

## Scenario

You are developing a simple **Student Result Management System** for a training institute.

The teacher wants to enter information for multiple students.

For every student, the program should collect:

* Student Name
* Student ID
* Marks for different subjects

The system will calculate:

* Total Marks
* Average Marks
* Grade
* Pass/Fail Status

After all students are processed, the program must display a **Class Summary**.

---

# Part 1 - Display Student Information

Create a function:

```python
def display_student(name, student_id):
```

The function should display the student's basic information.

### Example

```text
Student Name: Hasan
Student ID: ST101
```

This should be a **void function**.

---

# Part 2 - Calculate Total Using `*args`

Create a function:

```python
def calculate_total(*marks):
```

The function may receive any number of subject marks.

### Example Calls

```python
calculate_total(70, 80, 60)

calculate_total(70, 80, 60, 90)

calculate_total(70, 80, 60, 90, 75)
```

Calculate the total using a **loop**.

### Do Not Use

```python
sum()
```

The function must **return** the total marks.

---

# Part 3 — Calculate Average

Create a function:

```python
def calculate_average(total, number_of_subjects=3):
```

The function should calculate and return the average marks.

Here:

```python
number_of_subjects=3
```

is a **default parameter**.

### Example Calls

#### Using Default Argument

```python
calculate_average(210)
```

#### Using Positional Arguments

```python
calculate_average(320, 4)
```

#### Using Keyword Arguments

```python
calculate_average(
    total=400,
    number_of_subjects=5
)
```

Your program should demonstrate:

* Default Argument
* Positional Argument
* Keyword Argument

---

# Part 4 - Determine Grade

Create a function:

```python
def calculate_grade(average):
```

Use the following grading rules:

| Average  | Grade |
| -------- | ----- |
| 80–100   | A+    |
| 70–79    | A     |
| 60–69    | B     |
| 50–59    | C     |
| 40–49    | D     |
| Below 40 | F     |

The function must **return** the grade.

---

# Part 5 - Check Pass or Fail

Create another function:

```python
def check_result(average):
```

### Rules

```text
Average >= 40 → PASS
Average < 40  → FAIL
```

The function should return either:

```text
PASS
```

or:

```text
FAIL
```

---

# Part 6 - Student Details Using `**kwargs`

Create a function:

```python
def print_student_details(**student):
```

The function may receive information such as:

```python
print_student_details(
    name="Hasan",
    student_id="ST101",
    grade="A",
    status="PASS"
)
```

Use a **loop** to display all key-value pairs.

### Example Output

```text
name = Hasan
student_id = ST101
grade = A
status = PASS
```

---

# Part 7 - Process Multiple Students

Your program must continue processing students until the user chooses to stop.

Use a **loop** for this part.

### Example

```text
Add a student? (yes/no): yes

Student Name: Hasan
Student ID: ST101

How many subjects? 3

Mark 1: 70
Mark 2: 80
Mark 3: 60
```

After collecting the information, display:

```text
----------------------------
Student Result
----------------------------
Student Name: Hasan
Student ID: ST101
Total Marks: 210
Average: 70.00
Grade: A
Status: PASS
----------------------------
```

Then ask:

```text
Add another student? (yes/no):
```

If the user enters:

```text
yes
```

continue processing the next student.

If the user enters:

```text
no
```

stop the loop and display the final class report.

---

# Part 8 - Local and Global Scope

Create global variables:

```python
total_students = 0
passed_students = 0
failed_students = 0
```

Update these values whenever a student is successfully processed.

Make sure you understand the difference between:

* **Local Scope** - variable created inside a function
* **Global Scope** - variable available outside functions

---

# Part 9 - Final Class Report

After the main loop ends, display:

```text
================================
       CLASS SUMMARY
================================
Total Students : 4
Passed Students: 3
Failed Students: 1
================================
```

---

# Sample Program Run

```text
====== Student Result Management System ======

Add a student? (yes/no): yes

Student Name: Hasan
Student ID: ST101
How many subjects? 3

Mark 1: 70
Mark 2: 85
Mark 3: 75

----------------------------
Student Result
----------------------------
Student Name: Hasan
Student ID: ST101
Total Marks: 230
Average: 76.67
Grade: A
Status: PASS
----------------------------

Add another student? (yes/no): yes

Student Name: Karim
Student ID: ST102
How many subjects? 3

Mark 1: 30
Mark 2: 40
Mark 3: 35

----------------------------
Student Result
----------------------------
Student Name: Karim
Student ID: ST102
Total Marks: 105
Average: 35.00
Grade: F
Status: FAIL
----------------------------

Add another student? (yes/no): no

================================
       CLASS SUMMARY
================================
Total Students : 2
Passed Students: 1
Failed Students: 1

Highest Scorer : Hasan
Average        : 76.67
================================
```

---

# Minimum Function Requirements

Your program should contain at least the following functions:

```python
display_student(name, student_id)

calculate_total(*marks)

calculate_average(total, number_of_subjects=3)

calculate_grade(average)

check_result(average)

print_student_details(**student)
```

You may create additional functions if necessary.

---

The main goal is **not only to produce the correct output**. The main goal is to learn how to **break one large problem into smaller functions and connect those functions together to build a complete program**.
