from cProfile import label


students = [
    {"sno":101,"name":"小花","sgrade":837},
    {"sno":102,"name":"小国","sgrade":378},
    {"sno":104,"name":"小庄","sgrade":933},
    {"sno":141,"name":"小立","sgrade":627},
]
students_sort = sorted(students,key=lambda x:x["sgrade"],reverse=True)
print(students_sort)