import random as rand
import pandas as pd
import numpy as np

def simulate_student_data():
    with open("student_data.csv", "wt") as f:
        # f.write(f"attendence, grade, pass_percentage,\n")
        for i in range(100):
            attendence = rand.uniform(0.0, 100.0)
            grade = rand.uniform(0.0, 100.0)
            pass_percent = 1 if grade >= 35.0 else 0
            
            f.write(f"{attendence:.{3}f}, {grade:.{3}f}, {pass_percent}\n")


def probability():
    data = pd.read_csv("student_data.csv")
    # print(data)

    grade, attendance, has_passed = [], [], []

    with open("student_data.csv", "rt") as f:
        while True:
            data = f.readline()
            if data == "":
                break 
            x, y, z = data.split(", ")  
            attendance.append(float(x))
            grade.append(float(y))
            has_passed.append(int(z))

    print(has_passed)
    attendence_more_than_80 = len([x for x in attendance if x >= 80.0])
    p_intersect_a = []
    for idx, val in enumerate(has_passed):
        if attendance[idx] >= 80.0 and has_passed == 1:
            p_intersect_a.append(list(grade[idx], attendance[idx], has_passed[idx]))
    print(len(p_intersect_a))



def main():
    simulate_student_data()
    probability()

if __name__ == "__main__":
    main()