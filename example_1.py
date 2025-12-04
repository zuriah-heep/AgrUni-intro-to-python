'''
მოცემულია სტუდენტების სია.

1. შექმენით {name: average_score}.
2. sorted + lambda-ს გამოყენებით შექმენით ახალი სია ranking, რომელიც იქნება
   გადალაგებული students სია საშუალო ქულის კლებადობის და ასაკის ზრდადობის მიხედვით.
3. map + lambda-ს გამოყენებით გარდაქმენით თითოეული სტუდენტი (name, highest_score, lowest_score) კორტეჟში.
4. შექმენით {age: [ამ ასაკის სტუდენტის სახელები]}
'''

from statistics import mean

students = [
    {"name": "Alice", "scores": [90, 92, 94], "age": 21},
    {"name": "Bob",   "scores": [55, 67],     "age": 24},
    {"name": "Carl",  "scores": [91, 91, 94], "age": 20},
    {"name": "John",  "scores": [86, 87, 100], "age": 20}
]