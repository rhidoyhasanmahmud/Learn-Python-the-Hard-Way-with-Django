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

## Sample Test — Try It in Your Console

Run `python main.py` (or `python3 main.py`). The menu appears after each action.

**Step 1 — Register two families (choose `1` twice)**

```text
Enter choice: 1
Family ID: F01
Family Name: Hasan
Number of Members: 4
✓ Family registered!

Enter choice: 1
Family ID: F02
Family Name: Mahmud
Number of Members: 3
✓ Family registered!
```

**Step 2 — Add food (choose `2`)**

```text
Enter choice: 2
Packs to add: 10
Current stock: 10
```

**Step 3 — Distribute food (choose `3` for each request)**

```text
Enter choice: 3
Family ID: F01
Packs requested: 3
Success! Remaining stock: 7

Enter choice: 3
Family ID: F02
Packs requested: 8
Not enough food! Remaining stock: 7

Enter choice: 3
Family ID: F02
Packs requested: 5
Success! Remaining stock: 2
```

**Step 4 — View report (choose `4`)**

```text
===== FOOD BANK REPORT =====
Available Packs: 2

Registered Families:
F01 - Hasan - 4 members
F02 - Mahmud - 3 members

Distribution History:
F01 received 3 packs
F02 received 5 packs

Total Distributed: 8
```

**Step 5 — Exit (choose `5`)**

Your output wording can be different, but the stock and distribution totals must match.

**Quick checks:** Try a duplicate family ID, zero members, unknown family, zero/negative packs, a nonnumeric quantity, and an invalid menu choice. Your program should show an error without crashing.

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

Upload **`main.py`** and a short **`README.md`** (student name, how to run, brief class/data structure explanation) to your own GitHub repository. **[Submit your GitHub repository URL using this Google Form](https://forms.gle/QH2bKw32ZVbb413k6)**. Make sure the repository is public and accessible.

**Rules:** Work individually. Do not hardcode sample output; your application must work with different inputs. Be prepared to explain your code.
