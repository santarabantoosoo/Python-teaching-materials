# concepts learned

score = 0 
print("What is 6 * 7?")
print("a) 42")
print("b) 49")
print("c) 40")

answer = input("Choose your answer (a, b, or c): ")

score = 0
while score <= 4:
    if answer == "a" or answer == "42":
        print("Hooray! 🎉")
        score += 1
    elif answer == "b" or answer == "c":
        print("Wrong answer! Try again.")
        print("your score is ",score)
    else:
        print("Invalid choice! Please pick a, b, or c.")


# UI elements
helper_checkbox = mo.ui.checkbox(
    value=True,
    label="تفعيل وضع التحدي الصعب",
)

quiz_inputs = []
for idx, q_item in enumerate(questions_data):
    radio_group = mo.ui.radio(
        options=q_item[1],
        value=q_item[1][1],
        label=f"**السؤال {idx+1}:** {q_item[0]}"
    )
    quiz_inputs.append(radio_group)

# 3. زر التقديم
submit_btn = mo.ui.run_button(label="🔥 إرسال الإجابات وتحديد المصير")

# 4. عرض العناصر في النوت بوك
mo.vstack([
    helper_checkbox,
    *quiz_inputs,
    submit_btn,
    
    # 5. منطق حساب النتيجة يظهر هنا مباشرة بناءً على زر التقديم
    (
        mo.callout(
            (
                f"🏆 **اسطوري! لقد اجتزت التحدي الصعب وفزت بجدارة!**\n\nمجموع نقاطك الصحيحة: **{sum(1 for i, q in enumerate(questions_data) if quiz_inputs[i].value == q[2])} من {len(questions_data)}**."
                if sum(1 for i, q in enumerate(questions_data) if quiz_inputs[i].value == q[2]) >= 4
                else f"💀 **للأسف، لقد خسرت في هذا التحدي الصعب!**\n\nمجموع نقاطك: **{sum(1 for i, q in enumerate(questions_data) if quiz_inputs[i].value == q[2])} من {len(questions_data)}**.\nتحتاج إلى 4 نقاط على الأقل للفوز."
            ),
            kind="success" if sum(1 for i, q in enumerate(questions_data) if quiz_inputs[i].value == q[2]) >= 4 else "danger"
        )
        if submit_btn.value
        else mo.md("⚠️ **الأسئلة صعبة والخيارات متقاربة.. اختر بعناية ثم اضغط على زر الإرسال بالأعلى!**")
    )
])