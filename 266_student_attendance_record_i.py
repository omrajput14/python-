# 266. Student Attendance Record I
# You are given a string s representing an attendance record for a student where each character signifies whether the student was absent, late, or present on that day.

def check_record(s):
    return s.count('A') < 2 and 'LLL' not in s

if __name__ == "__main__":
    print(check_record("PPALLP"))  # True
    print(check_record("PPALLL"))  # False
