from input_scores import input_scores
from score_utils import count_pass, max_score, min_score, average_score


def show_menu():
    print("\n---------- โปรแกรมหลัก -----------")
    print("1. แสดงคะแนนทั้งหมด")
    print("2. คะแนนสูงสุด")
    print("3. คะแนนต่ำสุด")
    print("4. คะแนนเฉลี่ย")
    print("5. จำนวนนักเรียนที่ผ่าน")
    print("0. ออก")
    print("---------------------------------")


def main():
    print("---------- เริ่มโปรแกรม -----------")
    print("ใส่คะแนน 0-100 แล้วพิม Enter เพื่อไปเมนู")
    print("---------------------------------")

    scores = input_scores()

    while True:
        show_menu()
        menu_input = input("เลือกเมนูที่คุณต้องการ: ")

        if not menu_input.isdigit():
            print("กรุณาใส่เลขเมนูเท่านั้น")
            continue

        menu = int(menu_input)

        if menu != 0 and not scores:
            print("ยังไม่มีคะแนน กรุณาใส่คะแนนก่อน")
            continue

        match menu:
            case 0:
                print("จบโปรแกรม")
                break
            case 1:
                print("คะแนนทั้งหมด:", scores)
            case 2:
                print("คะแนนสูงสุด:", max_score(scores))
            case 3:
                print("คะแนนต่ำสุด:", min_score(scores))
            case 4:
                print("คะแนนเฉลี่ย:", average_score(scores))
            case 5:
                print("จำนวนนักเรียนที่ผ่าน:", count_pass(scores))
            case _:
                print("เลือกเมนูไม่ถูกต้อง")


if __name__ == "__main__":
    main()