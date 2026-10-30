# Python Final Exam — Community Food Bank

**Total: 50 Marks | Individual Assignment | Python Console Application**

## Problem

A food bank registers families, receives food packs, and distributes packs to families. Build a **menu-driven Python program using OOP** to manage this process.

## Requirements

1. Create at least **two classes**: `Family` and `FoodBank`. Use constructors and methods.
2. **Register Family:** Enter family ID, name, and number of members. Reject duplicate IDs and member counts of 0 or less.
3. **Add Food:** Add a positive number of food packs to the available stock (starting stock = 0).
4. **Distribute Food:** Enter a registered family ID and number of packs. Reject unknown families, nonpositive quantities, and requests greater than available stock. **Do not partially distribute:** if stock is insufficient, give 0 packs and leave stock unchanged.
5. **Show Report:** Show registered families, remaining packs, distribution history, and total packs distributed.
6. Use all four Python data structures meaningfully: **list, set, tuple, dict**. For example: list for history, set for unique IDs, tuple for a distribution record, dict for family lookup.
7. Handle invalid menu choices and nonnumeric quantity input without crashing. Keep displaying the menu until Exit is selected.

No Django, database, website, or external packages required.

## Console Menu

```text
===== COMMUNITY FOOD BANK =====
1. Register Family
2. Add Food Packs
3. Distribute Food Packs
4. Show Report
5. Exit
Enter choice:
```

## Sample Test — Enter These Inputs in Order

Run `python main.py` (or `python3 main.py`).

| Step | Choose | Input to enter | Expected result |
|---|---|---|---|
| 1 | 1 | F01, Rahim, 4 | Family registered |
| 2 | 1 | F02, Karim, 3 | Family registered |
| 3 | 2 | 10 | Stock = 10 |
| 4 | 3 | F01, 3 | Successful; stock = 7 |
| 5 | 3 | F02, 8 | Rejected; stock stays 7 |
| 6 | 3 | F02, 5 | Successful; stock = 2 |
| 7 | 4 | — | View report |
| 8 | 5 | — | Exit |

**Expected report after Step 7:**

```text
===== FOOD BANK REPORT =====
Available Packs: 2
Registered Families:
F01 - Rahim - 4 members
F02 - Karim - 3 members

Distribution History:
F01 received 3 packs
F02 received 5 packs

Total Distributed: 8
```

Your program does not need identical text formatting; the **numbers and behavior must match**.

**Also test:** Duplicate family ID, zero members, unknown family ID, zero/negative packs, nonnumeric quantity, and invalid menu choice. Show clear error messages.

## Marking — 50 Marks

| Area | Marks |
|---|---:|
| OOP: classes, constructors, methods | 10 |
| Register family and validate duplicates | 10 |
| Add/distribute food and update stock correctly | 15 |
| List, set, tuple, dict | 5 |
| Report and correct output | 5 |
| GitHub submission and README | 5 |
| **Total** | **50** |

## Submission

Upload **`main.py`** and a short **`README.md`** (student name, how to run, brief class/data structure explanation) to your own GitHub repository. Submit the **repository URL** through the instructor's submission channel.

**Rules:** Work individually. Do not hardcode sample output; your application must work with different inputs. Be prepared to explain your code.
