# 🎓 Grade Calculator (Python Project)

This is a simple **command-line grade calculator** built using Python. It takes a student's marks in 5 subjects, converts each mark into a grade (A to F), calculates the total and average marks, and assigns a final grade using Python's `match-case`.

---

## 📌 User Story

> "As a student, I want to enter my subject marks and receive both subject-wise and overall grade evaluations, so I can understand my academic performance easily."

---

## ✅ Features

- Takes student name, roll number, and 5 subject marks
- Converts each subject mark into a grade (A, B, C, D, E, F)
- Calculates:
  - Total Marks
  - Average Percentage
  - Final Grade using `match-case`
- Clean terminal output

---

## 🛠️ Technologies Used

- Python 3.10+
- Standard libraries only (no external dependencies)
- Functional programming using `map()` and `match-case`

---

## 📋 Grade Criteria

| Marks Range | Grade |
|-------------|-------|
| 90–100      | A     |
| 80–89       | B     |
| 70–79       | C     |
| 60–69       | D     |
| 50–59       | E     |
| Below 50    | F     |

---

## 🧪 Sample Output

Enter student name: Jaya
Enter roll number: 101
Enter subject1 Marks: 92
Enter subject2 Marks: 84
Enter subject3 Marks: 76
Enter subject4 Marks: 65
Enter subject5 Marks: 45

Subject 1 Grade: A
Subject 2 Grade: B
Subject 3 Grade: C
Subject 4 Grade: D
Subject 5 Grade: F
Total marks obtained : 362
Percentage obtained 72.4 %
Total Grade obtained : C
