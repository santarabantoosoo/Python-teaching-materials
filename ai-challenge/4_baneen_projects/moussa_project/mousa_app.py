# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
# ]
# ///
"""Mousa App — Math & Psychology Quiz (marimo).

Built from Mousa's own progress (mousa_code.py): a single-page form — one
radio per question, one submit button, a hard-mode checkbox and score
callouts (win threshold: 4 correct). Two sections from mousa_questions.md:
10 math + 10 psychology questions in Arabic. No background image; brief
English chrome; no AI challenge.

Run:    uvx marimo run mousa_app.py
Edit:   uvx marimo edit mousa_app.py
Export: uvx marimo export html-wasm mousa_app.py -o index.html
Serve:  uv run python -m http.server  # preview the WASM build
"""

import marimo

__generated_with = "0.25.2"
app = marimo.App()

with app.setup:
    from pathlib import Path

    import marimo as mo

    STUDENT_CODE_FILE = "mousa_code.py"

    # Fallback copy of mousa_code.py, used by the deployed WASM build where the
    # browser cannot open files from disk. Locally the real file is read instead.
    # Raw string: Mousa's source contains \n escapes that must stay literal.
    STUDENT_CODE_FALLBACK = r'''# concepts learned

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
])'''

    # Mousa's two sections from mousa_questions.md, in the same order.
    # Each item is (question, options, correct) — the shape mousa_code.py works
    # with (q_item[0] text, q_item[1] options, q[2] correct answer).
    SECTIONS = {
        "Math": {
            "icon": "🧮",
            "questions": [
                ("كم يساوي 2 * 3؟", ["5", "6", "7", "8"], "6"),
                ("كم يساوي 4 * 4؟", ["15", "16", "14", "18"], "16"),
                ("كم يساوي 6 * 4؟", ["18", "22", "24", "26"], "24"),
                ("كم يساوي 7 * 7؟", ["49", "42", "48", "56"], "49"),
                ("كم يساوي 9 * 8؟", ["63", "72", "80", "81"], "72"),
                ("كم يساوي 12 * 11؟", ["112", "132", "122", "143"], "132"),
                ("كم يساوي 13 * 21؟", ["283", "263", "273", "293"], "273"),
                ("كم يساوي 15 * 22؟", ["330", "310", "300", "320"], "330"),
                ("كم يساوي 50 * 33؟", ["1550", "1650", "1600", "1750"], "1650"),
                ("كم يساوي 51 * 17؟", ["817", "867", "777", "877"], "867"),
            ],
        },
        "Psychology": {
            "icon": "🧠",
            "questions": [
                ("ما هو علم النفس؟", ["دراسة السلوك والعمليات العقلية", "دراسة الأدوية", "دراسة المجتمع فقط", "دراسة التراث"], "دراسة السلوك والعمليات العقلية"),
                ("ما الفرع الذي يدرس كيف يتعلم الإنسان داخل المجتمع؟", ["علم النفس الاجتماعي", "علم النفس العصبي", "علم النفس التنظيمي", "علم النفس الإكلينيكي"], "علم النفس الاجتماعي"),
                ("هل يمكن أن يتأثر الإنسان بالبيئة المحيطة؟ (نعم/لا)", ["نعم", "لا"], "نعم"),
                ("ما اسم العملية التي يحتفظ بها الإنسان بالمعلومات والاسترجاع؟", ["الذهن", "الذاكرة", "الانتباه", "الإدراك"], "الذاكرة"),
                ("هل كل شخص حزين يعاني من اكتئاب؟ (نعم/لا)", ["نعم", "لا"], "لا"),
                ("ما الهدف الأساسي من العلاج المعرفي السلوكي؟", ["تغيير الأفكار والسلوكيات السلبية", "تناول الأدوية", "قراءة الكتب", "النوم لفترة أطول"], "تغيير الأفكار والسلوكيات السلبية"),
                ("هل المعالج النفسي يستطيع مساعدة الأطفال؟ (نعم/لا)", ["نعم", "لا"], "نعم"),
                ("هل المعالج النفسي يقدم حلولاً جاهزة لكل مشكلة؟ (نعم/لا)", ["نعم", "لا"], "لا"),
                ("ما الفرع الذي يهتم بسلوك الإنسان في العمل؟", ["علم النفس التنظيمي", "علم النفس الاجتماعي", "علم النفس العصبي", "علم النفس التربوي"], "علم النفس التنظيمي"),
                ("كيف يستطيع الاختصاصي النفسي مساعدة الأفراد الذين مروا بصدمات نفسية كبيرة؟", ["العلاج النفسي وتجهيز استراتيجيات التكيف", "تجاهل الصدمة", "تغيير المكان", "الانتظار والصمت"], "العلاج النفسي وتجهيز استراتيجيات التكيف"),
            ],
        },
    }


@app.function
def read_local_file(name):
    """Read a file next to this notebook. Returns None in WASM (no disk access)."""
    for base in (
        Path.cwd(),
        Path.cwd() / "ai-challenge" / "4_baneen_projects" / "moussa_project",
    ):
        try:
            return (base / name).read_bytes()
        except OSError:
            continue
    return None


@app.function
def student_code():
    """Contents of mousa_code.py (embedded fallback for the deployed build)."""
    data = read_local_file(STUDENT_CODE_FILE)
    return data.decode("utf-8") if data is not None else STUDENT_CODE_FALLBACK


@app.cell
def _():
    get_game, set_game = mo.state(None, allow_self_loops=True)
    return get_game, set_game


@app.cell
def _():
    # From mousa_code.py — Mousa's own hard-mode toggle (verbatim).
    helper_checkbox = mo.ui.checkbox(value=True, label="تفعيل وضع التحدي الصعب")
    return (helper_checkbox,)


@app.cell
def _():
    show_code = mo.ui.checkbox(label="Show core python code")
    return (show_code,)


@app.cell
def _(get_game, helper_checkbox, set_game, show_code):
    _game_section = get_game()
    restart_btn = mo.ui.button(
        label="🔄 Restart",
        kind="neutral",
        full_width=True,
        on_click=lambda _: set_game(None),
    )
    progress_md = (
        "🧮 Math • 🧠 Psychology"
        if _game_section is None
        else f"{SECTIONS[_game_section]['icon']} {_game_section} — "
        f"{len(SECTIONS[_game_section]['questions'])} questions"
    )
    left_panel = mo.vstack([
        mo.md("### 🧠 Mousa App"),
        mo.md(progress_md),
        mo.md("---"),
        restart_btn,
        helper_checkbox,
        show_code,
    ], gap=0.35)
    return (left_panel,)


@app.cell
def _(get_game):
    # Mousa's form pattern (from mousa_code.py, wired across cells): build the
    # radio inputs from questions_data, read their values in later cells only.
    _game_section = get_game()
    if _game_section is None:
        quiz_array, submit_all = None, None
    else:
        _questions_data = SECTIONS[_game_section]["questions"]
        quiz_inputs = []
        for idx, q_item in enumerate(_questions_data):
            radio_group = mo.ui.radio(
                options=q_item[1],
                value=q_item[1][1],
                label=f"**السؤال {idx+1}:** {q_item[0]}",
                inline=len(q_item[1]) == 2,  # yes/no questions: one row
            )
            quiz_inputs.append(radio_group)
        quiz_array = mo.ui.array(quiz_inputs)
        submit_all = mo.ui.run_button(label="🔥 إرسال الإجابات وتحديد المصير")
    return quiz_array, submit_all


@app.cell
def _(get_game, helper_checkbox, quiz_array, submit_all):
    _game_section = get_game()
    if _game_section is None or quiz_array is None:
        result_md = None
    else:
        _questions_data = SECTIONS[_game_section]["questions"]
        score = sum(
            1 for i, q in enumerate(_questions_data) if quiz_array.value[i] == q[2]
        )
        total = len(_questions_data)
        score_text = f"مجموع نقاطك الصحيحة: **{score} من {total}**"
        if not submit_all.value:
            # Mousa's warning before submitting (verbatim).
            result_md = mo.md(
                "⚠️ **الأسئلة صعبة والخيارات متقاربة.. اختر بعناية ثم اضغط على زر الإرسال بالأعلى!**"
            )
        elif helper_checkbox.value:
            # Hard mode: Mousa's win threshold and messages (verbatim logic).
            if score >= 4:
                result_md = mo.callout(
                    f"🏆 **اسطوري! لقد اجتزت التحدي الصعب وفزت بجدارة!**\n\n{score_text}.",
                    kind="success",
                )
            else:
                result_md = mo.callout(
                    f"💀 **للأسف، لقد خسرت في هذا التحدي الصعب!**\n\nمجموع نقاطك: **{score} من {total}**.\nتحتاج إلى 4 نقاط على الأقل للفوز.",
                    kind="danger",
                )
        else:
            result_md = mo.callout(f"{score_text}.", kind="info", title="Your result")
    return (result_md,)


@app.cell
def _(get_game, quiz_array, result_md, set_game, submit_all):
    _game_section = get_game()
    if _game_section is None:
        math_btn = mo.ui.button(
            label=f"🧮 Math — {len(SECTIONS['Math']['questions'])} questions",
            kind="success",
            on_click=lambda _: set_game("Math"),
        )
        psychology_btn = mo.ui.button(
            label=f"🧠 Psychology — {len(SECTIONS['Psychology']['questions'])} questions",
            kind="neutral",
            on_click=lambda _: set_game("Psychology"),
        )
        parts = [
            mo.md("### Pick a section"),
            mo.hstack([math_btn, psychology_btn], justify="start"),
        ]
    else:
        parts = [quiz_array, submit_all, result_md]
    view = mo.vstack([p for p in parts if p is not None])
    return (view,)


@app.cell
def _(left_panel, show_code, student_code, view):
    import html

    # mo.md code fences are always syntax-highlighted by marimo's markdown
    # renderer (even without a language marker). Render a plain <pre> via real
    # HTML instead — no highlighting.
    code_block = mo.Html(
        "<div style='overflow-x:auto'>"
        "<pre style='margin:0;padding:0.9rem 1.1rem;border-radius:0.5rem;"
        "background:rgba(2,6,23,0.55);font-family:ui-monospace,SFMono-Regular,"
        "Menlo,monospace;font-size:0.85rem;line-height:1.55'>"
        f"{html.escape(student_code())}"
        "</pre></div>"
    )
    code_view = (
        mo.vstack([
            mo.md(
                "### 💻 Core Python code — from <code>mousa_code.py</code>"
            ),
            code_block,
        ], gap=0.25)
        if show_code.value
        else None
    )
    layout = mo.vstack(
        [
            c
            for c in (
                code_view,
                mo.hstack(
                    [left_panel, view],
                    justify="start",
                    align="start",
                    widths=[0.27, 0.73],
                ),
            )
            if c is not None  # never stack None — it renders as the text "None"
        ],
        gap=0.4,
    )
    layout
    return


if __name__ == "__main__":
    app.run()
