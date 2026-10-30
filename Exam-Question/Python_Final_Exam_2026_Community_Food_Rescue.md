# Python Final Exam (50 Marks)
## Community Food Bank — A Simple OOP Project

**Course:** Python Programming Bootcamp  
**Exam Date:** 30 October 2026  
**Total Marks:** 50  
**Difficulty:** Beginner friendly  
**Language:** Python 3 (console application)

> **Your challenge:** Build a small Python program to help a community food bank keep track of families and distribute food packs. There is no need to build a website, use a database, or learn Django for this exam.

## 1. Real-Life Story

A community food bank starts the day with some food packs. Families can register and request food. The volunteers want to avoid giving more packs than they have, and they need a record of how many packs each family received.

**Example:** There are 10 food packs in stock. Rahim's family receives 3 packs, so 7 remain. Karim's family then requests 8 packs, but only 7 remain. The system must say there is not enough stock and **must not give any packs for that request**.

You will build a menu-driven program where a volunteer can enter information from the keyboard.

## 2. What You Must Build — Step by Step

### Task 1 — Create Classes (10 marks)

Create at least these **two classes**:

- **`Family`** — stores a family ID, family name, and number of members.
- **`FoodBank`** — manages available food packs, registered families, and distribution records.

Use `__init__` constructors and meaningful methods. Example method names (suggestions only): `register_family()`, `add_food()`, `distribute_food()`, `show_report()`.

You can choose your own variable and method names. **You must use OOP**, not only global variables and functions.

### Task 2 — Register Families (10 marks)

The volunteer enters:
- Family ID (example: `F01`)
- Family name (example: `Rahim`)
- Number of family members (example: `4`)

Your program must:
1. Save the family information.
2. Prevent registering the **same family ID twice**.
3. Reject a family size of `0` or less.
4. Show a clear success or error message.

### Task 3 — Add and Distribute Food (15 marks)

1. The food bank starts with **0 packs**.
2. Volunteers can add food packs to stock.
3. Volunteers can distribute a requested number of packs to a **registered family**.
4. If there are not enough packs, **reject the entire request** and leave stock unchanged.
5. Reject requests of `0` or negative packs.
6. Reject requests from unregistered families.
7. After a successful distribution, reduce stock and save the transaction.

**No priority, expiry date, sorting algorithm, or partial distribution is required.** Process each request when the volunteer enters it.

### Task 4 — Use Python Data Structures (5 marks)

Use **all four** somewhere meaningful:

| Data structure | Simple example of usage |
| --- | --- |
| `dict` | Family ID → family information |
| `set` | Keep track of registered family IDs |
| `list` | Store distribution history |
| `tuple` | Represent one distribution record, e.g. `("F01", 3)` |

The examples are hints, not a full solution.

### Task 5 — Show Report (5 marks)

When the user chooses **Show Report**, print:
- Food packs currently available.
- Number of registered families.
- List of registered families (ID, name, members).
- Distribution history (family ID and packs received).
- Total number of packs distributed.

### Task 6 — GitHub Submission (5 marks)

Upload your solution to **your own GitHub repository** with at least:
- `main.py` — runnable Python application.
- `README.md` — your name, instructions to run, brief explanation of your classes and data structures.

**Submit your GitHub repository URL** to your instructor using the announced submission channel.

---

## 3. Console Menu — Your Application Should Look Similar to This

When you run `python main.py`, show this menu repeatedly until the user selects Exit:

```text
===== COMMUNITY FOOD BANK =====
1. Register Family
2. Add Food Packs
3. Distribute Food Packs
4. Show Report
5. Exit
Enter your choice:
```

You may change the wording or formatting, but **all five actions must work**.

## 4. Complete Example — What the Student Types and Sees

The example below is **one continuous run**. Text after `Enter ...:` is what the volunteer types. The output messages are examples; your wording can differ.

```text
===== COMMUNITY FOOD BANK =====
1. Register Family
2. Add Food Packs
3. Distribute Food Packs
4. Show Report
5. Exit
Enter your choice: 1

Enter Family ID: F01
Enter Family Name: Rahim
Enter Number of Members: 4
Family registered successfully!

===== COMMUNITY FOOD BANK =====
1. Register Family
2. Add Food Packs
3. Distribute Food Packs
4. Show Report
5. Exit
Enter your choice: 1

Enter Family ID: F02
Enter Family Name: Karim
Enter Number of Members: 3
Family registered successfully!

===== COMMUNITY FOOD BANK =====
1. Register Family
2. Add Food Packs
3. Distribute Food Packs
4. Show Report
5. Exit
Enter your choice: 2

How many food packs to add? 10
Food added successfully! Current stock: 10

===== COMMUNITY FOOD BANK =====
1. Register Family
2. Add Food Packs
3. Distribute Food Packs
4. Show Report
5. Exit
Enter your choice: 3

Enter Family ID: F01
How many packs? 3
Distribution successful! Remaining stock: 7

===== COMMUNITY FOOD BANK =====
1. Register Family
2. Add Food Packs
3. Distribute Food Packs
4. Show Report
5. Exit
Enter your choice: 3

Enter Family ID: F02
How many packs? 8
Not enough stock! Only 7 packs available.

===== COMMUNITY FOOD BANK =====
1. Register Family
2. Add Food Packs
3. Distribute Food Packs
4. Show Report
5. Exit
Enter your choice: 3

Enter Family ID: F02
How many packs? 5
Distribution successful! Remaining stock: 2

===== COMMUNITY FOOD BANK =====
1. Register Family
2. Add Food Packs
3. Distribute Food Packs
4. Show Report
5. Exit
Enter your choice: 4

===== FOOD BANK REPORT =====
Available Food Packs: 2
Total Registered Families: 2

Registered Families:
F01 - Rahim - 4 members
F02 - Karim - 3 members

Distribution History:
F01 received 3 packs
F02 received 5 packs

Total Packs Distributed: 8

===== COMMUNITY FOOD BANK =====
1. Register Family
2. Add Food Packs
3. Distribute Food Packs
4. Show Report
5. Exit
Enter your choice: 5

Thank you! Goodbye.
```

**Check your result:** Food added = 10, food successfully distributed = 3 + 5 = 8, food remaining = **2**. The failed 8-pack request must **not** reduce stock or appear in the successful distribution history.

## 5. How to Run and Test Your Program

### Step A — Create the project

Make a folder named `python-final-exam` and save your code as `main.py`.

### Step B — Open the terminal

Open Terminal on macOS/Linux or Command Prompt/PowerShell on Windows. Navigate to the folder where `main.py` is saved.

### Step C — Run

```bash
python main.py
```

If your computer uses `python3`, use:

```bash
python3 main.py
```

### Step D — Follow the test checklist

Run your application and enter these actions in order:

| Step | Menu option | Input | Expected result |
| --- | --- | --- | --- |
| 1 | 1 | `F01`, `Rahim`, `4` | Family registered |
| 2 | 1 | `F02`, `Karim`, `3` | Family registered |
| 3 | 2 | `10` | Stock becomes 10 |
| 4 | 3 | `F01`, `3` | Success, stock becomes 7 |
| 5 | 3 | `F02`, `8` | Rejected, stock stays 7 |
| 6 | 3 | `F02`, `5` | Success, stock becomes 2 |
| 7 | 4 | No input | Report shows 2 stock, 2 families, 8 distributed |
| 8 | 5 | No input | Program exits |

### Step E — Try these extra cases yourself

| Test | What you enter | What should happen |
| --- | --- | --- |
| Duplicate ID | Register `F01` again | Rejected |
| Invalid members | Register `F03` with `0` members | Rejected |
| Unknown family | Distribute to `F99` | Rejected |
| Invalid packs | Add `-5` packs | Rejected, stock unchanged |
| Zero request | Distribute `0` packs | Rejected |
| Invalid menu | Type `9` as menu choice | Message shown; app continues |
| Non-number | Type `abc` for a pack quantity | Friendly error; app should not crash |

**Tip:** You may use `try/except` to handle invalid numeric input. You are not required to write an automated test framework.

## 6. Marking Rubric (50 Marks)

| Criteria | Marks |
| --- | ---: |
| Two working classes, constructors, appropriate methods | 10 |
| Register family, duplicates, family-member validation | 10 |
| Add food, distribute food, correct stock calculation, invalid requests | 15 |
| Meaningful use of list, set, tuple, dict | 5 |
| Report with correct information | 5 |
| GitHub submission and basic README | 5 |
| **TOTAL** | **50** |

## 7. Exam Rules

1. Write your own solution individually.
2. You can read Python documentation or course notes, but you should be able to explain your code.
3. Do **not** hardcode the example report. Your program must work when the instructor enters different values.
4. Console input/output is enough. A GUI, API, database, Django, or extra Python library is **not** needed.
5. Focus on a working program, simple OOP design, readable code, and correct calculations.

**Good luck — solve the problem one step at a time!**
