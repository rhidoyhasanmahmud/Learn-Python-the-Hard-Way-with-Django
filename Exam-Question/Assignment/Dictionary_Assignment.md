# Python Dictionary Scenario-Based Assignment

## Assignment Title

**Student Academic Record Management System**

## Scenario

Greenfield School currently keeps student information and examination marks on paper. The school wants a small Python program to manage one student's profile, contact information, subjects, and marks.

Your task is to build a beginner-friendly **Student Academic Record Management System** using Python dictionaries.

The program must demonstrate all the dictionary concepts covered in class. You do not need to use functions, classes, loops, files, or a database.

## Initial Student Information

Use the following data:

| Field | Value |
|---|---|
| Roll number | 1201 |
| Name | Nadia Rahman |
| Age | 15 |
| Class | Ten |
| Email | nadia@example.com |
| City | Dhaka |
| Area | Uttara |
| Registration status | Active |

Use these subject and mark lists later in the assignment:

```python
subjects = ["Mathematics", "Physics", "Chemistry", "Biology"]
marks_list = [95, 88, 91, 86]
```

---

## Requirements

### Task 1: Create the Student Profile

Create a dictionary named `student_profile` using dictionary literal syntax (`{}`).

It must contain:

- `roll_number`
- `name`
- `age`
- `class`
- `email`
- `registration_status`
- `address`

The value of `address` must be another dictionary containing `city` and `area`.

Print the complete dictionary and its data type.

### Task 2: Use the `dict()` Constructor

Create another dictionary named `school_info` using the `dict()` constructor.

Store:

- School name: `Greenfield School`
- School code: `GFS-101`
- Academic year: `2026`

Print the dictionary and its data type.

### Task 3: Test Duplicate Keys

Create the following dictionary:

```python
status_test = {
    "status": "Pending",
    "status": "Active"
}
```

Print `status_test`.

Write a Python comment explaining:

- Which value remains in the dictionary?
- Why does that value remain?

### Task 4: Read Dictionary Values

From `student_profile`:

1. Print the student's name using square-bracket notation.
2. Print the student's city from the nested `address` dictionary.
3. Try to read `guardian_phone` using `get()`.
4. If it does not exist, display `Not Available` instead of producing an error.

### Task 5: Add and Update One Field

Use square-bracket notation to:

1. Change the student's age from `15` to `16`.
2. Add a new key named `phone_number` with the value `01700000000`.

Print the updated dictionary.

### Task 6: Update Multiple Fields

Use the `update()` method to make all the following changes in one operation:

- Change the email to `nadia.rahman@example.com`
- Change the area to `Dhanmondi` inside the address information
- Add `blood_group` with the value `B+`

> Hint: Update the nested `address` dictionary separately where necessary.

Print the updated `student_profile`.

### Task 7: Add a Default Value Safely

Use `setdefault()` to add:

```text
guardian_phone: Not Available
```

Call `setdefault()` a second time with a different guardian phone number.

Print the dictionary and observe whether the existing value changes. Add a comment explaining the result.

### Task 8: Inspect the Dictionary

Print:

1. All keys using `keys()`
2. All values using `values()`
3. All key-value pairs using `items()`
4. The total number of top-level fields using `len()`
5. The field names in alphabetical order using `sorted()`

### Task 9: Create a Backup

Create a shallow copy of `student_profile` named `student_backup` using `copy()`.

Add this field only to the original dictionary:

```text
profile_updated: True
```

Print both dictionaries and confirm that adding a new top-level field to the original does not add it to the backup.

### Task 10: Prepare an Empty Marks Dictionary

Use `dict.fromkeys()` with the `subjects` list to create a dictionary named `empty_marks`.

Every subject must initially have a mark of `0`.

Expected structure:

```python
{
    "Mathematics": 0,
    "Physics": 0,
    "Chemistry": 0,
    "Biology": 0
}
```

Print `empty_marks`.

### Task 11: Combine Subjects and Marks

Use `zip()` and `dict()` to combine `subjects` and `marks_list` into a dictionary named `subject_marks`.

Do not manually type the subject-mark pairs.

Add `subject_marks` to `student_profile` using the key `marks`.

Print:

- The `subject_marks` dictionary
- The student's Mathematics mark
- The complete updated `student_profile`

### Task 12: Remove Data Safely

Perform the removal operations on a separate copy so that the main student record is not destroyed.

```python
cleanup_record = student_profile.copy()
```

Then:

1. Add a temporary key named `temporary_note`.
2. Remove it using `pop()` and print the returned value.
3. Try to remove `medical_note` using `pop()` with `Not Found` as the default value.
4. Remove the last inserted key-value pair using `popitem()` and print the returned pair.
5. Remove all remaining items using `clear()` and print the empty dictionary.
6. Delete the `cleanup_record` variable using `del`.

> Do not try to print `cleanup_record` after deleting it, because the variable will no longer exist.

### Task 13: Display the Final Record

Print a clean final summary with appropriate labels:

```text
Student Name       : Nadia Rahman
Roll Number        : 1201
Class              : Ten
City               : Dhaka
Registration Status: Active
Subject Marks      : {'Mathematics': 95, ...}
Total Profile Fields: ...
```

The values must be read from the dictionaries. Do not manually type the final values inside the `print()` statements.

---
