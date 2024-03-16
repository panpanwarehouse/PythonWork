students = []
student_ids = input("请输入学生学号，用','隔开: ").split(',')
python_scores = eval( input("请输入学生Python语言成绩，用','隔开: "))
c_scores = eval( input("请输入学生C语言成绩，用','隔开: "))
for student_id, python_score, c_score in zip(student_ids, python_scores, c_scores):
    student = {
        '学号': student_id,
        'Python成绩': python_score,
        'C语言成绩': c_score
    }
    students.append(student)
# 计算每个学生的平均分和班级的平均分
class_avg_python = sum(student['Python成绩'] for student in students) / len(students)
class_avg_c = sum(student['C语言成绩'] for student in students) / len(students)
a = class_avg_python+class_avg_c
print(f"\n班级的平均成绩: {a:.2f}")
# 计算每个学生的平均分
student_avgs = [(student['Python成绩'] + student['C语言成绩']) / 2 for student in students]

print(f"\n各个学生的平均分: {', '.join(map(lambda x: f'{x:.1f}', student_avgs))}")
# 找出平均分最高的学生
highest_avg_index = student_avgs.index(max(student_avgs))
highest_avg_student = students[highest_avg_index]
# 输出平均分最高的学生学号和对应平均分
print(f"\n平均分最高的学生学号: {highest_avg_student['学号']}")
print(f"对应的平均分: {student_avgs[highest_avg_index]:.1f}")