class Student:
    def __init__(self,name, grades):
        self.name = name
        self.grades = grades

    def add_grade(self, grade, subject):
        self.grades[subject].append(grade)
        return self.grades[subject]

    def avg_subj_grades(self,subject):
        avg=0
        for i in range(len(self.grades[subject])):
            avg += self.grades[subject][i]
        return avg/len(self.grades[subject])
    def avg_grades(self):
        avg=0
        count=0
        for i in self.grades:
            for j in range(len(self.grades[i])):
                avg += self.grades[i][j]
                count += 1
        return avg/count

Tolya = Student (
    name = "Толя",
    grades={
        'математика':[2,3,5,4,],
        'русский': [2,4,5,4],
        'физкультура':[4,5,5,5]
    }
 )
print(Tolya.add_grade(5,'математика'))
print(Tolya.avg_subj_grades ('математика'))
print(Tolya.avg_grades())