import random

# =====================================
# SHIVAJI MAHARAJ QUIZ QUESTION BANK
# (TUPLES - IMMUTABLE)
# =====================================

def load_questions():

    questions = (
        ("Who was the father of Chhatrapati Shivaji Maharaj?",
         "A. Shahaji Bhosale",
         "B. Sambhaji",
         "C. Maloji",
         "D. Baji Rao",
         "A"),

        ("In which year was Shivaji Maharaj born?",
         "A. 1627",
         "B. 1630",
         "C. 1645",
         "D. 1650",
         "B"),

        ("What was the capital of Shivaji Maharaj's kingdom?",
         "A. Pune",
         "B. Raigad",
         "C. Mumbai",
         "D. Satara",
         "B"),

        ("Which fort is known as the capital fort of Shivaji Maharaj?",
         "A. Sinhagad",
         "B. Raigad Fort",
         "C. Pratapgad",
         "D. Shivneri",
         "B"),

        ("What title was given to Shivaji Maharaj?",
         "A. Emperor",
         "B. Peshwa",
         "C. Chhatrapati",
         "D. Nawab",
         "C"),

        ("Which treaty was signed between Shivaji and the Mughals?",
         "A. Treaty of Surat",
         "B. Treaty of Purandar",
         "C. Treaty of Delhi",
         "D. Treaty of Agra",
         "B"),

        ("Which fort was first captured by Shivaji Maharaj?",
         "A. Torna Fort",
         "B. Raigad Fort",
         "C. Rajgad Fort",
         "D. Pratapgad",
         "A"),

        ("When did Shivaji Maharaj become Chhatrapati?",
         "A. 1645",
         "B. 1674",
         "C. 1680",
         "D. 1659",
         "B")
    )

    return list(questions)

# =====================================
# DISPLAY QUESTION
# =====================================
def show_question(q, i):

    print("\n----------------------------------")
    print(f"Q{i+1}: {q[0]}")
    print(q[1])
    print(q[2])
    print(q[3])
    print(q[4])

# =====================================
# GET VALID ANSWER
# =====================================
def get_answer():

    while True:

        ans = input("Your Answer (A/B/C/D): ").strip().upper()

        if ans in ["A", "B", "C", "D"]:
            return ans

        print("Invalid input! Please enter A, B, C, or D.")

# =====================================
# GRADE SYSTEM
# =====================================
def calculate_grade(percent):

    if percent >= 90:
        return "A+"
    elif percent >= 80:
        return "A"
    elif percent >= 70:
        return "B+"
    elif percent >= 60:
        return "B"
    elif percent >= 50:
        return "C"
    else:
        return "F"

# =====================================
# MAIN QUIZ
# =====================================
def start_quiz():

    print("\n===== CHHATRAPATI SHIVAJI MAHARAJ QUIZ =====")

    name = input("Enter Student Name: ")
    roll = input("Enter Roll No: ")

    questions = load_questions()

    # Shuffle questions (BONUS FEATURE)
    random.shuffle(questions)

    score = 0
    wrong_answers = []

    total = len(questions)

    for i, q in enumerate(questions):

        show_question(q, i)

        answer = get_answer()

        correct = q[5]

        if answer == correct:
            print("✓ Correct!")
            score += 1
        else:
            print("✗ Wrong!")
            wrong_answers.append((q[0], answer, correct))

    percent = (score / total) * 100
    grade = calculate_grade(percent)

    result = "PASS" if percent >= 50 else "FAIL"

    # =====================================
    # FINAL RESULT
    # =====================================
    print("\n====== RESULT REPORT ======")
    print("Name   :", name)
    print("Roll   :", roll)
    print("Score  :", f"{score}/{total}")
    print("Percent:", f"{percent:.2f}%")
    print("Grade  :", grade)
    print("Result :", result)

    # =====================================
    # WRONG ANSWERS
    # =====================================
    if wrong_answers:

        print("\n===== WRONG ANSWERS REVIEW =====")

        for w in wrong_answers:
            print("\nQuestion :", w[0])
            print("Your Ans :", w[1])
            print("Correct  :", w[2])

# =====================================
# RUN PROGRAM
# =====================================
if __name__ == "__main__":
    start_quiz()