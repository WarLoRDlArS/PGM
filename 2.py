import random as rand
import pandas as pd
import numpy as np


def simulate_student_data():
    with open("student_data.csv", "wt") as f:
        # f.write(f"attendence, grade, pass_percentage,\n")
        for i in range(1000):
            attendence = rand.uniform(0.0, 100.0)
            grade = rand.uniform(0.0, 100.0)
            pass_percent = 1 if grade >= 40.0 else 0
            
            f.write(f"{attendence:.{3}f}, {grade:.{3}f}, {pass_percent}\n")


def probability():
    # data = pd.read_csv("student_data.csv")
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
 
    attendence_more_than_80 = len([x for x in attendance if x >= 80.0])
    p_intersect_a = 0
    for idx, val in enumerate(has_passed):
        if attendance[idx] >= 80.0 and has_passed[idx] == 1:
            p_intersect_a += 1
    
    print(f"Probability of students given attendence is greater than 80% is: {attendence_more_than_80 / len(attendance)}")
    print(f"Probability given that student has passed and attendence is greater than 80% is : {p_intersect_a / 100}")
    print(f"Probability that student has passed given attendence is greater tha 80% is {p_intersect_a / attendence_more_than_80}")
    

def main():
    simulate_student_data()
    probability()

if __name__ == "__main__":
    main()