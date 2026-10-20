class Course:
    def __init__(self):
        self.hour = 45
        self.credit = 2
        self.place = "教学楼"

    def final_grades(self, exam_score, regular_score):
        return exam_score * 0.5 + regular_score * 0.5


class ComputerScience(Course):
    def xx(self):
        print("实验楼404")
        print("吴老师")
        print(f"学分：{self.credit}")
        print(f"单节课时长：{self.hour}")


class PythonCourse(Course):
    def __init__(self):
        super().__init__()

    def xx(self):
        print("实验楼101")
        print("邱老师")
        print(f"学分：{self.credit}")
        print(f"单节课时长：{self.hour}")


if __name__ == "__main__":
    p = PythonCourse()
    p.xx()
