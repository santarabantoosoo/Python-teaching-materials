# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
# ]
# ///
"""Osama App — Geography Quiz (marimo).

A simple 10-question geography quiz about Egypt (from osama_questions.md).
English UI, Arabic questions rendered RTL. No AI challenge — just play and learn.

Run:    uvx marimo run osama_app.py
Edit:   uvx marimo edit osama_app.py
Export: uvx marimo export html-wasm osama_app.py -o index.html
Serve:  uv run python -m http.server  # preview the WASM build
"""

import marimo

__generated_with = "0.25.2"
app = marimo.App()

with app.setup:
    import base64
    from pathlib import Path

    import marimo as mo

    BACKGROUND_IMAGE = "osama_baraa_football.jpeg"
    STUDENT_CODE_FILE = "osama_code.py"

    # Fallback copy of osama_code.py, used by the deployed WASM build where the
    # browser cannot open files from disk. Locally the real file is read instead.
    STUDENT_CODE_FALLBACK = '''# concepts learned

    name = input("whats ur name?")

    answer= int(input("1+2="))
    if answer==3:
       print("right")
    else:
       print("wrong")


    ## Choosing UI elemets

    radio = mo.ui.radio(
        options=["Python", "Scratch", "R"],
        value="Python",
        label="Radio Buttons",
    )
    radio


    button = mo.ui.button(
        kind="success",
        label="Submit answer",
    )
    button'''

    # 10 questions from osama_questions.md — in the same order, with 4 choices each.
    QUESTIONS = [
        {
            "q": "ما هي عاصمة مصر؟",
            "options": ["القاهرة", "الإسكندرية", "الجيزة", "أسيوط"],
            "correct": "A",
            "explanation": "القاهرة هي عاصمة مصر وأكبر مدنها.",
        },
        {
            "q": "أين تقع مصر؟",
            "options": ["في وسط قارة آسيا", "في شمال شرق قارة أفريقيا", "في جنوب قارة أوروبا", "في وسط قارة أستراليا"],
            "correct": "B",
            "explanation": "تقع مصر في شمال شرق قارة أفريقيا، عند ملتقى قارتي أفريقيا وآسيا.",
        },
        {
            "q": "كم يبلغ عدد سكان مصر؟",
            "options": ["حوالي 25 مليون نسمة", "حوالي 300 مليون نسمة", "حوالي 104 مليون نسمة", "حوالي 5 ملايين نسمة"],
            "correct": "C",
            "explanation": "يتجاوز عدد سكان مصر 100 مليون نسمة (حوالي 104 مليون نسمة).",
        },
        {
            "q": "أشهر البحيرات الموجودة في مصر؟",
            "options": ["بحيرة بايكال", "بحيرة ناصر", "بحيرة أونتاريو", "بحيرة تاهو"],
            "correct": "B",
            "explanation": "بحيرة ناصر أكبر بحيرات مصر، وتتكون خلف سد أسوان.",
        },
        {
            "q": "أشهر الصادرات من مصر؟",
            "options": ["الفحم", "الماس", "الخشب", "القطن"],
            "correct": "D",
            "explanation": "القطن المصري مشهور في العالم كله، وهو أشهر صادرات مصر التقليدية.",
        },
        {
            "q": "ما طبيعة المناخ في مصر؟",
            "options": ["حار جاف صيفاً ودافئ قليل الأمطار شتاءً", "بارد ثلجي طوال العام", "استوائي ممطر غائم طوال العام", "حار ممطر صيفاً وبارد جاف شتاءً"],
            "correct": "A",
            "explanation": "مناخ مصر صحراوي: حار جاف في الصيف، ودافئ قليل الأمطار في الشتاء، وتسقط أمطار الشتاء على الساحل الشمالي.",
        },
        {
            "q": "ما الدول المجاورة لمصر؟",
            "options": ["تركيا واليونان", "السعودية والكويت", "ليبيا والسودان وفلسطين", "الهند وإيران"],
            "correct": "C",
            "explanation": "يحد مصر بالبر: ليبيا غرباً، والسودان جنوباً، وفلسطين شرقاً.",
        },
        {
            "q": "ما البحار التي تحيط بمصر؟",
            "options": ["البحر الأحمر وبحر العرب", "البحر المتوسط والبحر الأحمر", "البحر الأسود والبحر المتوسط", "المحيط الأطلسي والمحيط الهندي"],
            "correct": "B",
            "explanation": "يحد مصر شمالاً البحر المتوسط، وشرقاً البحر الأحمر.",
        },
        {
            "q": "ما طول قناة السويس؟",
            "options": ["حوالي 50 كم", "حوالي 500 كم", "حوالي 1000 كم", "حوالي 193 كم"],
            "correct": "D",
            "explanation": "تمتد قناة السويس بين بورسعيد والسويس، وطولها نحو 193 كم.",
        },
        {
            "q": "ما الحدود الطبيعية لمصر؟",
            "options": ["شمالاً البحر المتوسط وشرقاً البحر الأحمر", "شمالاً البحر الأحمر وغرباً البحر المتوسط", "شرقًا المحيط الأطلسي وغرباً المحيط الهندي", "شمالاً جبال الألب وجنوباً المحيط الهندي"],
            "correct": "A",
            "explanation": "الحدود الطبيعية لمصر: شمالاً البحر المتوسط، وشرقاً البحر الأحمر، وغرباً الصحراء الليبية، وجنوباً الصحراء.",
        },
    ]

    LETTERS = ["A", "B", "C", "D"]
    TOTAL = len(QUESTIONS)


@app.function
def read_local_file(name):
    """Read a file next to this notebook. Returns None in WASM (no disk access)."""
    for base in (Path.cwd(), Path.cwd() / "ai-challenge" / "osama_project"):
        try:
            return (base / name).read_bytes()
        except OSError:
            continue
    return None


@app.function
def student_code():
    """Contents of osama_code.py (embedded fallback for the deployed build)."""
    data = read_local_file(STUDENT_CODE_FILE)
    return data.decode("utf-8") if data is not None else STUDENT_CODE_FALLBACK


@app.function
def background_css():
    """Football photo as background: inlined locally, separate file when deployed."""
    data = read_local_file(BACKGROUND_IMAGE)
    if data is not None:
        b64 = base64.b64encode(data).decode("ascii")
        return f"url('data:image/jpeg;base64,{b64}')"
    return f"url('./{BACKGROUND_IMAGE}')"


@app.function
def format_labels(options):
    return [f"{letter}. {opt}" for letter, opt in zip(LETTERS, options)]


@app.function
def option_letter_to_text(q, letter):
    return q["options"]["ABCD".index(letter)]


@app.function
def new_game():
    """Fresh game: first question loaded, score at 0."""
    return {
        "stage": "playing",  # playing -> feedback -> finished
        "index": 0,
        "score": 0,
        "current": QUESTIONS[0],
        "picked": None,
        "is_correct": None,
    }


@app.function
def submit_answer(g, letter):
    """Python decides: check the picked option, remember feedback, keep score."""
    q = g["current"]
    is_correct = letter == q["correct"]
    return {
        **g,
        "stage": "feedback",
        "picked": letter,
        "is_correct": is_correct,
        "score": g["score"] + int(is_correct),
    }


@app.function
def next_question(g):
    """Move on — after question 10 the quiz is finished."""
    nxt = g["index"] + 1
    if nxt >= TOTAL:
        return {
            **g,
            "stage": "finished",
            "index": nxt,
            "current": None,
            "picked": None,
            "is_correct": None,
        }
    return {
        **g,
        "stage": "playing",
        "index": nxt,
        "current": QUESTIONS[nxt],
        "picked": None,
        "is_correct": None,
    }


@app.cell
def _():
    get_game, set_game = mo.state(new_game(), allow_self_loops=True)
    return get_game, set_game


@app.cell
def _():
    show_code = mo.ui.checkbox(label="Show core python code")
    return (show_code,)


@app.cell
def _(get_game, set_game, show_code):
    sidebar_g = get_game()
    restart_btn = mo.ui.button(
        label="🔄 Restart",
        kind="neutral",
        full_width=True,
        on_click=lambda _: set_game(new_game()),
    )
    if sidebar_g["stage"] == "finished":
        progress_md = f"**Finished!**<br>Score: **{sidebar_g['score']} / {TOTAL}**"
    else:
        progress_md = (
            f"Question **{sidebar_g['index'] + 1} / {TOTAL}**<br>"
            f"Score: **{sidebar_g['score']}**"
        )
    mo.sidebar([
        mo.md("## 🌍 Osama App"),
        mo.md("Geography quiz about Egypt"),
        mo.md("---"),
        mo.md(progress_md),
        restart_btn,
        mo.md("---"),
        show_code,
    ])
    return


@app.cell
def _():
    mo.md(
        f"""<style>
    body {{
        background-image: linear-gradient(rgba(2, 6, 23, 0.70), rgba(2, 6, 23, 0.70)), {background_css()};
        background-size: cover;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
    }}
    .osama-text, .osama-text * {{
        color: #f8fafc !important;
    }}
    .osama-text code {{
        color: #fde68a !important;
        background: rgba(0, 0, 0, 0.45);
    }}
    </style>"""
    )
    return


@app.cell
def _():
    mo.md("""
    <div class="osama-text"><h1>🌍 Osama Geography Challenge</h1><p>Answer <strong>10 questions</strong> about Egypt — Python checks your answers. الأسئلة بالعربي ✍️</p></div>
    """)
    return


@app.cell
def _(get_game, set_game):
    g = get_game()

    if g["stage"] == "playing":
        q = g["current"]
        labels = format_labels(q["options"])
        radio = mo.ui.radio(labels, value=labels[0])
        submit = mo.ui.button(
            label="✅ Submit answer",
            kind="success",
            on_click=lambda _: set_game(lambda s: submit_answer(s, radio.value[0])),
        )
        parts = [
            mo.md(
                f'<div class="osama-text">Question <strong>{g["index"] + 1} / {TOTAL}</strong>'
                f' &nbsp;•&nbsp; Score: <strong>{g["score"]}</strong></div>'
            ),
            mo.md(f'`{"█" * g["index"]}{"░" * (TOTAL - g["index"])}`'),
            mo.md(
                f'<div class="osama-text" dir="rtl" style="text-align:right">'
                f"<strong>{q['q']}</strong></div>"
            ),
            radio,
            submit,
        ]

    elif g["stage"] == "feedback":
        q = g["current"]
        picked_text = option_letter_to_text(q, g["picked"])
        correct_text = option_letter_to_text(q, q["correct"])
        if g["is_correct"]:
            header = mo.callout("✅ Well done!", kind="success", title="Correct")
        else:
            header = mo.callout(
                f"You picked **{picked_text}** — the correct answer is **{correct_text}**",
                kind="danger",
                title="❌ Not quite!",
            )
        is_last = g["index"] == TOTAL - 1
        next_btn = mo.ui.button(
            label="🏁 See results" if is_last else "➡️ Next question",
            kind="primary" if not is_last else "success",
            on_click=lambda _: set_game(lambda s: next_question(s)),
        )
        parts = [
            mo.md(
                f'<div class="osama-text" dir="rtl" style="text-align:right">'
                f"<strong>{q['q']}</strong></div>"
            ),
            header,
            mo.md('<div class="osama-text">💡 <strong>Explanation</strong></div>'),
            mo.md(
                f'<div class="osama-text" dir="rtl" style="text-align:right">'
                f"{q['explanation']}</div>"
            ),
            next_btn,
        ]

    else:  # finished
        score = g["score"]
        if score >= 9:
            verdict = "🏆 Excellent! You really know Egypt's geography."
        elif score >= 6:
            verdict = "👏 Well done! Keep practising."
        else:
            verdict = "💪 Good try — play again and beat your score!"
        play_again = mo.ui.button(
            label="🔁 Play again",
            kind="success",
            on_click=lambda _: set_game(new_game()),
        )
        parts = [
            mo.md('<div class="osama-text"><h1>🏁 Quiz finished!</h1></div>'),
            mo.md(
                f'<div class="osama-text">You scored <strong>{score} / {TOTAL}</strong></div>'
            ),
            mo.md(f'`{"█" * score}{"░" * (TOTAL - score)}`'),
            mo.callout(verdict, kind="info", title="Your result"),
            play_again,
        ]

    view = mo.vstack(parts)
    view
    return


@app.cell
def _(show_code):
    code_view = (
        mo.vstack([
            mo.md(
                '<div class="osama-text"><h2>💻 Core Python code</h2>'
                "<p>From <code>osama_code.py</code> — the concepts you learned.</p></div>"
            ),
            mo.md(f"```python\n{student_code()}\n```"),
        ])
        if show_code.value
        else None
    )
    code_view
    return


if __name__ == "__main__":
    app.run()
