#CSCI 1913
#Izra Bereket

def is_sorted(gradebook):
    '''Purpose: Takes a gradebook which is a list of tuples and returns either True or False'''

    if gradebook == []:
        return True

    for i in range(len(gradebook)-1):
        if gradebook[i][1] > gradebook[i+1][1]:
            return False
    return True
def grade_average(gb):
    '''purpose: Takes a gradebook which is a list of tuples and returns the average grade of all the students'''
    avg_grad = 0.0
    if gb == []:
        return 0.0
    for i in range(len(gb)):
        avg_grad += gb[i][0]
    return avg_grad / len(gb)
def unsorted_get(uns_grade, stud_name):
    ''' purpose: looks for the students name in the gradebook and returns their grade if not returns none'''
    if uns_grade == []:
        return None

    for i in range(len(uns_grade)):
        if uns_grade[i][1] == stud_name:
            return uns_grade[i][0]

def unsorted_put(uns_grade, stud_name, stud_grade):
    '''  purpose: The function uses three parameters the unsorted grade the student name and the student grade. It then updates
    the gradebook to record the students new grade either updating or adding on to the list'''
    for i in range(len(uns_grade)):
        if stud_name == uns_grade[i][1]:
            uns_grade[i] = (stud_grade, stud_name)
            return uns_grade
    uns_grade.append((stud_grade, stud_name))
    return uns_grade

def sorted_get(sort_grad, stud_name):
    ''' purpose: the function uses two parameters the sorted grade and the student grade. It then checks if the student is in
    gradebook if the student is in the gradebook it returns the grade otherwise None is returned'''
    low = 0
    high = len(sort_grad) - 1
    while high >= low:
        mid = (high + low) // 2
        if sort_grad[mid][1] < stud_name:
            low = mid + 1
        elif sort_grad[mid][1] > stud_name:
            high = mid - 1
        else:
            return sort_grad[mid][0]
    return None

def sorted_put(sort_grad, stud_name, stud_grade):
    '''purpose: given a sorted grade book, update the name and grade of passed in paramters
        if the grade book is empty then just add the student name and grade
        if len of grade book is 1, add the student name sorted alphabetically
        loop through the list and find the thing that is closest to the input input'''
    if len(sort_grad) == 0:
        sort_grad.append((stud_grade,stud_name))
        return None
    for i in range(len(sort_grad)):
        if stud_name == sort_grad[i][1]:
            sort_grad[i] = (stud_grade, stud_name)
            return sort_grad
            print("i is = ", i)
    if stud_name > sort_grad[len(sort_grad)-1][1]:
        sort_grad.append((stud_grade, stud_name))
        return sort_grad
    if len(sort_grad) == 1:
        if sort_grad[0][1] > stud_name:
            sort_grad.insert(0,(stud_grade, stud_name))
        elif sort_grad[0][1] < stud_name:
            sort_grad.append((stud_grade, stud_name))
        return
    for i in range(len(sort_grad)):
        if sort_grad[i-1][1] <= stud_name and sort_grad[i][1] > stud_name:
            sort_grad.insert(i, (stud_grade, stud_name))
            return
    if stud_name < sort_grad[0][1]:
        sort_grad.insert(0, (stud_grade, stud_name))
    return