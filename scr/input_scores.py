#รับค่าคะแนน
def input_scores():
    scores = []
    while True:
        score_input = input("ใส่คะแนน: ")
        if score_input.lower() == "enter":
            break

        if score_input.isdigit():
            score = int(score_input)
            if score <= 100 and score >=0:
                scores.append(score)
            else:
                print("กรุณาใส่คะแนน 0-100 เท่านั้น")
        else:
            print("กรุณาใส่ตัวเลข หรือพิมพ์ enter เพื่อหยุด")
    return scores