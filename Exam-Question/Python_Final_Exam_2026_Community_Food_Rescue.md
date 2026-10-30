# Python Final Examination — Community Food Rescue & Smart Distribution System

**Course:** Python Programming Bootcamp (eShikhon)  
**Exam date:** 30 October 2026  
**Total marks:** 50  
**Problem type:** Individual, practical, real-life problem solving  
**Required:** Python 3, OOP, list, set, tuple, dictionary, conditional logic, loops, functions, Git

> **Important:** This is a problem specification, not a programming tutorial. You must design your own classes, methods, and allocation algorithm. No starter solution is provided.

## The Story

A community organization collects surplus food packs from local shops and distributes them to registered families. Every evening, the volunteers receive requests from families, but there may not be enough food for everyone. Some packs expire earlier than others, and families have different urgency levels.

Your task is to build a **console-based Food Rescue Management System** that allocates available food fairly and predictably, while minimizing waste.

**You are not building a website, database, or Django project.** A working Python console application is enough.

## Part A — Requirements

### 1. Model the system with OOP

Design at least **three meaningful classes** to represent the problem. You decide the class names, attributes, methods, and responsibilities.

Your design must demonstrate:
- Creating objects and calling instance methods.
- Constructors (`__init__`).
- Encapsulation: keep state changes controlled through methods.
- Clear separation between data objects and distribution logic.

Do not put the entire solution inside one giant function.

### 2. Represent the data using all four collections

Use each collection for a real purpose, not just to satisfy a checklist:

| Structure | Required purpose |
| --- | --- |
| `list` | Store food batches, requests, or distribution records |
| `dict` | Look up families and/or build a distribution summary |
| `set` | Prevent duplicate registered family IDs and/or duplicate request IDs |
| `tuple` | Represent a fixed value such as `(expiry_day, batch_id)` or a read-only distribution record |

Explain the reason for your choices in your submission README.

### 3. Business rules (implement all)

1. Each food batch has a unique ID, food type, quantity (number of packs), and expiry day (positive integer). A batch with zero or negative quantity is invalid.
2. A food batch is usable on **day D only if `expiry_day >= D`**. Earlier-expiring usable batches must be consumed first. If expiry days tie, use batch ID in ascending lexicographic order.
3. A registered family has a unique family ID, family name, and an urgency level: **HIGH**, **MEDIUM**, or **LOW**.
4. Each request contains a unique request ID, a registered family ID, a food type, the number of packs requested, and the day the request was placed. Only requests made **on the distribution day** are processed in that day's run.
5. A family may submit **at most one request per food type per day**. Reject a second request for the same combination, even if it has a different request ID. A request ID cannot be reused.
6. Requests must be processed in this order: **HIGH → MEDIUM → LOW**. Within the same priority, sort by request ID (ascending lexicographic order). This order is deterministic, not dependent on insertion order.
7. A request can be **partially fulfilled**. Give as many packs as available up to the requested amount. Never give more than requested, and never allow negative inventory.
8. Packs of the same food type may be taken from multiple usable batches to fulfill one request.
9. Do not substitute one food type for another. Expired stock must never be distributed.
10. Running the distribution for the **same day a second time** must not distribute any additional packs or reduce inventory again. You may reject the repeat run with a clear error or return the saved result.
11. After distribution, generate a report showing requested packs, allocated packs, unmet packs, remaining usable stock, expired stock, and each request's status: `FULFILLED`, `PARTIAL`, or `UNFULFILLED`.

**Assumptions:** Each run distributes on one specified integer day. Food quantities are whole packs. A request is not carried automatically to another day. You do not need persistent storage, authentication, or a user interface beyond the console.

## Part B — Provided Test Scenario

Use **distribution day = 5**.

### Food batches

| Batch ID | Food type | Packs | Expiry day |
| --- | --- | ---: | ---: |
| B01 | RICE | 4 | 5 |
| B02 | RICE | 5 | 7 |
| B03 | RICE | 3 | 4 |
| B04 | MILK | 4 | 6 |
| B05 | MILK | 2 | 5 |

### Families

| Family ID | Name | Urgency |
| --- | --- | --- |
| F01 | Rahman Family | HIGH |
| F02 | Karim Family | MEDIUM |
| F03 | Saha Family | HIGH |
| F04 | Ali Family | LOW |

### Requests

| Request ID | Family ID | Food type | Packs | Request day |
| --- | --- | --- | ---: | ---: |
| R04 | F04 | RICE | 3 | 5 |
| R02 | F02 | RICE | 5 | 5 |
| R03 | F03 | MILK | 4 | 5 |
| R01 | F01 | RICE | 6 | 5 |
| R05 | F01 | MILK | 3 | 5 |

**Important:** The requests above are deliberately **not listed in processing order**. Your program must calculate the order itself.

### Expected allocation (for checking your work)

| Processing order | Request | Allocated | Status |
| ---: | --- | ---: | --- |
| 1 | R01 | 6 RICE | FULFILLED |
| 2 | R03 | 4 MILK | FULFILLED |
| 3 | R05 | 2 MILK | PARTIAL |
| 4 | R02 | 3 RICE | PARTIAL |
| 5 | R04 | 0 RICE | UNFULFILLED |

**Expected batch consumption:** R01 takes 4 from B01 and 2 from B02; R03 takes 2 from B05 and 2 from B04; R05 takes the remaining 2 from B04; R02 takes the remaining 3 from B02. B03 is expired on day 5 and cannot be used.

**Expected totals:** requested = **21 packs**; allocated = **15 packs**; unmet = **6 packs**. Remaining usable stock after distribution = **0 packs**. Expired stock = **3 RICE packs** (B03).

The exact console formatting is up to you. **The allocation numbers and statuses must match.**

## Part C — Additional Cases You Must Test

Demonstrate the result of each case, either through tests or clearly labeled console output:

1. Register a family with an already-used family ID.
2. Add a batch with quantity `0` or negative quantity.
3. Submit a request for an unregistered family.
4. Submit two requests for the same family, food type, and day (different request IDs).
5. Submit two requests with an identical request ID.
6. Request an unavailable food type.
7. Run distribution again for the same day; confirm inventory is not deducted twice.
8. Confirm a batch whose expiry day is **exactly** the distribution day is usable.
9. Confirm a request for a different day is not processed in day 5's run.

For invalid input, handle the problem safely. You may raise and catch suitable exceptions or show informative validation messages. Do not allow invalid records to corrupt the system.

## Part D — Student Deliverables

Submit the following to your own GitHub repository:

```text
python-final-exam/
├── main.py              # runnable demo of the scenario
├── README.md            # explanation, assumptions, how to run
└── tests.py             # tests OR a script demonstrating edge cases
```

You may add extra Python files to organize your classes. The program must run using Python 3 with **no third-party dependencies**. Use only the standard library. You may use `unittest`, but it is not mandatory.

Your `README.md` must include:
- Your name and student/batch identification.
- How to run the application.
- The main classes and why each exists.
- How and why you used `list`, `dict`, `set`, and `tuple`.
- An explanation of your distribution algorithm in **your own words**.
- Your test results and at least one design trade-off.

**Submit:** the URL of your GitHub repository (or the exact folder containing your work) through the instructor's official submission channel.

## Marking Rubric — 50 Marks

| Area | Marks | Assessment |
| --- | ---: | --- |
| OOP design and encapsulation | 10 | At least 3 purposeful classes, meaningful methods, responsibilities separated, state protected |
| Python data structures | 10 | Correct, practical usage of list, set, tuple, and dictionary |
| Allocation logic | 15 | Priority ordering, batch expiry ordering, partial allocation, stock integrity, deterministic results, idempotent day processing |
| Validation and edge cases | 5 | Duplicate detection, invalid input handling, day/expiry boundaries |
| Tests and correct output | 5 | Provided test scenario matches; additional cases demonstrated |
| Git and documentation | 5 | Runnable repository, logical commit history, clear README |
| **Total** | **50** | |

**Evaluation note:** The example output alone is not enough for full marks. The instructor may change the batch quantities, priorities, request order, or day to verify that the **algorithm works for new data**, not just the sample.

## Academic Integrity & Rules

- Work **individually**. Do not copy another student's source code.
- You may consult documentation and learning resources, but you must understand and be able to explain every line of the code you submit.
- Be prepared for a short code walkthrough where the instructor changes inputs and asks you to explain your decisions.
- A hard-coded output, a solution that only works for the provided numbers, or code that ignores the required business rules will lose significant marks.
- There is **no requirement** to use inheritance; apply it only when it improves your design.
- Prefer clean, readable Python over unnecessary complexity.

**Good luck! Think like a problem solver, not just a syntax memorizer.**
