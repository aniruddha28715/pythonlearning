# The provided code stub is read in a dictionary containing key/value pairs of name:[Marks] for a list of students. 
# Print the average of the marks array for the student name is provided, showing 2 places after the decimal.

# Example
# marks key: value pairs are

# ‘alpha’:[20, 30, 40]
# ‘beta’:[30, 50, 70]
# query_name = ‘beta’

# The query_name is ‘beta’. beta’s average score is (30 + 50 + 70)/3 = 50.0.



if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    l1 = list(student_marks[query_name])
    add  = sum(l1)
    result = add/len(l1)
    print('%.2f'% result)



