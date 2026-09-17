# Python OOP Scenario Assignment

## eShikhon FutureTech Challenge: Smart Campus Robot Fleet

**Topic:** Inheritance and Types of Inheritance in Python  

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

# Design Freedom

- class এবং method-এর meaningful নাম নির্বাচন করতে পারবেন
- প্রয়োজন অনুযায়ী extra attributes যোগ করতে পারবেন
- battery consumption rate নির্ধারণ করতে পারবেন
- package, alert বা report-এর representation ঠিক করতে পারবেন
- helper method তৈরি করতে পারবেন
- extra validation যোগ করতে পারবেন

তবে design থেকে স্পষ্ট হতে হবে যে inheritance শুধু code কমানোর জন্য নয়; logical **IS-A relationship** অনুযায়ী ব্যবহার করা হয়েছে।


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

