#นับคนที่ผ่าน --> มากกว่า50คะแนน
def count_pass(scores):
    sum_count_pass = 0
    for i in scores:
        if i >= 50:
            sum_count_pass += 1
    return sum_count_pass

#หาค่าที่มากที่สุด
def max_score(scores):
    max_value = scores[0]
    for i in scores:
        if i > max_value:
            max_value = i
    return max_value

#หาค่าที่น้อยที่สุด
def min_score(scores):
    min_value = scores[0]
    for i in scores:
        if i < min_value:
            min_value = i
    return min_value    

#หาค่าเฉลี่ย
def average_score(scores):
    total = 0 
    n = len(scores)
    for i in scores:
        total += i
    return total / n