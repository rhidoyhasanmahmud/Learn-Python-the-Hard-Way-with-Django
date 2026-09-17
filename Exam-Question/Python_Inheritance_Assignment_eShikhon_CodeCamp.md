# Python OOP Scenario Assignment

## eShikhon FutureTech Challenge: Smart Campus Robot Fleet

**Topic:** Inheritance and Types of Inheritance in Python  
**Difficulty:** Beginner to Intermediate  
**Suggested time:** ২–৩ ঘণ্টা  
**Total marks:** ৩০

---

# Scenario

eShikhon একটি নতুন **FutureTech Smart Campus** চালু করেছে। Campus-এর বিভিন্ন কাজ automated করার জন্য তারা একটি robot fleet তৈরি করতে চায়।

বর্তমানে campus-এ কয়েক ধরনের robot কাজ করবে। কিছু robot package deliver করবে, কিছু robot campus security দেখবে, কিছু হবে আরও advanced, আর বিশেষ emergency situation-এর জন্য এমন robot থাকবে যেটি একাধিক ধরনের দায়িত্ব পালন করতে পারবে।

আপনাকে Python ব্যবহার করে এই **Smart Campus Robot Fleet Management System** তৈরি করতে হবে।

System design, class selection, parent–child relationship এবং কোন জায়গায় কোন inheritance type ব্যবহার করবেন—এই সিদ্ধান্তগুলো আপনাকেই নিতে হবে।

---

# Campus Requirements

## সব Robot-এর Common Information

Campus-এ register করা প্রতিটি robot-এর অন্তত নিচের information থাকবে:

- একটি unique robot ID
- model name
- বর্তমান battery level
- বর্তমান location

প্রতিটি robot যেন অন্তত নিচের common কাজগুলো করতে পারে:

- নিজের complete status দেখাতে
- এক location থেকে অন্য location-এ যেতে
- battery charge করতে

Battery কখনো `0`-এর নিচে বা `100`-এর উপরে যেতে পারবে না। কোনো operation-এর কারণে battery কমলে updated battery level দেখাতে হবে।

---

## Package Delivery Robot

Campus-এর কিছু robot documents, books এবং ছোট package এক building থেকে অন্য building-এ পৌঁছে দেয়।

একটি delivery-capable robot সম্পর্কে system-কে জানতে হবে:

- এটি সর্বোচ্চ কত kilogram package বহন করতে পারে
- বর্তমানে কোন package বহন করছে
- package-এর destination কোথায়

এটি যেন:

- নতুন package গ্রহণ করতে পারে
- package-এর weight capacity-এর মধ্যে আছে কি না check করতে পারে
- destination-এ package deliver করতে পারে
- delivery শেষে নিজের status update করতে পারে

Battery `20%`-এর কম হলে delivery শুরু করা যাবে না। Capacity-এর চেয়ে বেশি weight-এর package-ও গ্রহণ করা যাবে না।

---

## Campus Security Robot

কিছু robot campus-এর নির্দিষ্ট zone patrol করে।

একটি security-capable robot সম্পর্কে system-কে জানতে হবে:

- assigned security zone
- সর্বশেষ scan-এর result
- detected incident-এর সংখ্যা

এটি যেন:

- নিজের zone patrol করতে পারে
- suspicious activity scan করতে পারে
- incident detect হলে alert তৈরি করতে পারে
- security status দেখাতে পারে

Battery `15%`-এর কম হলে patrol শুরু করা যাবে না।

---

## Express Delivery Robot

FutureTech Campus-এ একটি upgraded delivery robot থাকবে। এটি সাধারণ delivery robot-এর সব কাজ করতে পারবে, তবে urgent package-এর জন্য আরও কিছু feature থাকবে:

- priority level
- express delivery fee
- fastest route calculate করার behavior
- সাধারণ delivery process-কে express delivery অনুযায়ী পরিবর্তন করার behavior

Express robot যখন নিজের পরিচয় বা status দেখাবে, তখন এটিকে সাধারণ delivery robot না বলে express service robot হিসেবে দেখাতে হবে।

---

## Emergency Support Robot

Campus management এমন একটি special robot চায়, যেটি emergency-এর সময়:

- medical kit বা emergency package বহন করতে পারবে
- affected area security scan করতে পারবে
- incident alert করতে পারবে
- emergency response status দেখাতে পারবে

অর্থাৎ এই robot-এর মধ্যে delivery এবং security—দুই ধরনের capability থাকবে।

Emergency support robot-এর অতিরিক্ত information:

- emergency code
- response priority
- assigned response team

Emergency response শুরু হলে robot প্রথমে নিজের battery check করবে। Battery যথেষ্ট থাকলে এটি emergency kit নিয়ে location-এ যাবে, area scan করবে এবং final response report দেখাবে।

---

# Your Mission

উপরের scenario বিশ্লেষণ করে একটি complete Python program তৈরি করুন।

আপনাকে নিজে সিদ্ধান্ত নিতে হবে:

- কোন কোন class প্রয়োজন
- কোন class common parent হবে
- কোন attributes common এবং কোনগুলো role-specific
- কোন methods inherit করা উচিত
- কোন methods child class-এ override করা উচিত
- কোথায় `super()` ব্যবহার করা উচিত
- কোন relationship কোন inheritance type তৈরি করছে
- Multiple inheritance-এর ক্ষেত্রে Python কোন order-এ method খুঁজবে

---

# Mandatory Technical Requirements

আপনার solution-এ অবশ্যই থাকতে হবে:

1. কমপক্ষে **৫টি meaningful class**
2. Constructor বা initializer: `__init__()`
3. Common attributes-এর logical reuse
4. `super()`-এর meaningful ব্যবহার
5. কমপক্ষে **৩টি method overriding**
6. একটি polymorphism demonstration
7. Method Resolution Order বা MRO display
8. অন্তত একবার করে নিচের inheritance types-এর demonstration:
   - Single Inheritance
   - Multilevel Inheritance
   - Hierarchical Inheritance
   - Multiple Inheritance
   - Hybrid Inheritance
9. সব inheritance type কোথায় হয়েছে, তা code comment-এ চিহ্নিত করা
10. অন্তত **৫টি robot object** তৈরি করে system test করা

---

# Required System Demonstration

Program run করলে অন্তত নিচের ঘটনাগুলো demonstrate করতে হবে:

## Test 1: Common Robot Operations

- একটি robot-এর initial status দেখান
- robot-টিকে নতুন location-এ move করান
- battery charge করুন
- updated status দেখান

## Test 2: Successful Delivery

- capacity-এর মধ্যে একটি package assign করুন
- delivery শুরু করুন
- destination ও remaining battery দেখান

## Test 3: Rejected Delivery

নিচের যেকোনো একটি কারণে delivery reject করে meaningful message দেখান:

- package অতিরিক্ত ভারী
- battery `20%`-এর কম

## Test 4: Security Patrol

- একটি security zone assign করুন
- patrol এবং scan operation চালান
- incident পাওয়া গেলে alert দেখান

## Test 5: Express Delivery

- একটি urgent package assign করুন
- fastest route বা priority information দেখান
- express-specific delivery behavior demonstrate করুন

## Test 6: Emergency Response

- emergency code ও response location দিন
- emergency kit delivery করুন
- একই robot দিয়ে security scan চালান
- একটি final emergency response report দেখান

## Test 7: Polymorphism

বিভিন্ন ধরনের robot object একটি collection-এ রাখুন। Loop ব্যবহার করে সবার জন্য একই status বা introduction method call করুন। Object-এর type অনুযায়ী output ভিন্ন হতে হবে।

## Test 8: MRO

একাধিক parent থেকে capability পাওয়া robot class-এর MRO print করুন। Output-এর order একটি code comment-এ ব্যাখ্যা করুন।

---

# Design Freedom

আপনি স্বাধীনভাবে:

- class এবং method-এর meaningful নাম নির্বাচন করতে পারবেন
- প্রয়োজন অনুযায়ী extra attributes যোগ করতে পারবেন
- battery consumption rate নির্ধারণ করতে পারবেন
- package, alert বা report-এর representation ঠিক করতে পারবেন
- helper method তৈরি করতে পারবেন
- extra validation যোগ করতে পারবেন

তবে design থেকে স্পষ্ট হতে হবে যে inheritance শুধু code কমানোর জন্য নয়; logical **IS-A relationship** অনুযায়ী ব্যবহার করা হয়েছে।

---

# Restrictions

- কোনো starter code দেওয়া হবে না
- একই common attributes অকারণে বিভিন্ন class-এ copy-paste করা যাবে না
- Final submission-এ অসম্পূর্ণ `pass` বা `TODO` রাখা যাবে না
- Global variable-এর ওপর system design নির্ভর করতে পারবে না
- External library ব্যবহার করা যাবে না
- Class name হবে `PascalCase`
- Variable, attribute ও method name হবে `snake_case`
- Program error ছাড়া run করতে হবে
- Output readable ও meaningful হতে হবে

---

# Submission Requirements

নিচের দুটি file submit করুন:

## 1. Python Program

Filename:

```text
smart_campus_robot_fleet.py
```

## 2. Design Explanation

Filename:

```text
inheritance_design.md
```

Design explanation-এ লিখবেন:

- আপনার তৈরি class-গুলোর নাম ও দায়িত্ব
- কোন class কোন class থেকে inherit করেছে
- পাঁচ ধরনের inheritance কোথায় demonstrate হয়েছে
- কোথায় method overriding করেছেন
- কোথায় `super()` ব্যবহার করেছেন এবং কেন
- Multiple inheritance-এর MRO কী হয়েছে
- কোনো design challenge থাকলে কীভাবে সমাধান করেছেন

Hand-drawn class hierarchy-এর পরিষ্কার ছবি দিলেও গ্রহণযোগ্য।

---

# Conceptual Questions

`inheritance_design.md` file-এ নিচের প্রশ্নগুলোর সংক্ষিপ্ত উত্তর দিন:

1. আপনার design-এ সবচেয়ে suitable common parent কোনটি এবং কেন?
2. Delivery ও security behavior-এর মধ্যে কোনগুলো common এবং কোনগুলো আলাদা?
3. আপনার solution-এ Single Inheritance কোথায় হয়েছে?
4. Multilevel এবং Hierarchical Inheritance কোথায় হয়েছে?
5. কোন robot Multiple Inheritance ব্যবহার করছে এবং কেন?
6. পুরো design-এ Hybrid Inheritance কীভাবে তৈরি হয়েছে?
7. কোন methods override করেছেন? Overriding প্রয়োজন হয়েছিল কেন?
8. Multiple inheritance class-এর MRO কী এবং method selection-এ এর প্রভাব কী?
9. কোথাও inheritance-এর পরিবর্তে composition ব্যবহার করা ভালো হতো কি? আপনার মতামত দিন।
10. একটি নতুন `CleaningRobot` যোগ করতে হলে আপনার design কীভাবে extend করবেন?

---

# Evaluation Rubric — ৩০ Marks

| Assessment area | Marks |
|---|---:|
| Scenario analysis ও appropriate class identification | ৪ |
| Common parent ও overall class design | ৪ |
| Single, Multilevel ও Hierarchical Inheritance | ৪ |
| Multiple ও Hybrid Inheritance | ৪ |
| `super()`, initialization ও attribute reuse | ৩ |
| Method overriding ও polymorphism | ৩ |
| Business rules ও validation | ৩ |
| Object creation ও complete system demonstration | ২ |
| MRO ও conceptual explanation | ২ |
| Naming, readability ও code organization | ১ |
| **Total** | **৩০** |

---

# Bonus Challenge — সর্বোচ্চ ৫ Marks

যেকোনো দুইটি implement করুন:

1. প্রতিটি robot operation-এর history একটি list-এ রাখুন
2. Class attribute ব্যবহার করে total registered robot count দেখান
3. `__str__()` ব্যবহার করে readable robot information দেখান
4. Low-battery robot-কে automatic charging station-এ পাঠান
5. একটি `FleetManager` তৈরি করুন, যেটি সব robot-এর summary দেখাবে
6. Invalid battery, weight বা location-এর জন্য exception handling যোগ করুন

---

# Submission Checklist

- [ ] Scenario পড়ে নিজস্ব class design করেছি
- [ ] অন্তত ৫টি meaningful class আছে
- [ ] পাঁচ ধরনের inheritance demonstrate করেছি
- [ ] প্রতিটি inheritance type code comment-এ identify করেছি
- [ ] Common data অকারণে duplicate করিনি
- [ ] `super()` ব্যবহার করেছি
- [ ] অন্তত ৩টি method override করেছি
- [ ] Polymorphism demonstrate করেছি
- [ ] MRO print ও explain করেছি
- [ ] অন্তত ৫টি object দিয়ে test করেছি
- [ ] সব required scenario run করেছি
- [ ] Business rules ও battery validation কাজ করছে
- [ ] Python naming convention অনুসরণ করেছি
- [ ] Program error ছাড়া run করে
- [ ] `inheritance_design.md` সম্পূর্ণ করেছি

---

## Final Note

এই assignment-এ শুধু program-এর output মূল্যায়ন করা হবে না। Scenario থেকে সঠিক class, responsibility এবং relationship বের করতে পারা solution-এর গুরুত্বপূর্ণ অংশ। একই scenario-এর একাধিক valid design হতে পারে—আপনার design choice যুক্তিসংগতভাবে ব্যাখ্যা করতে হবে।

