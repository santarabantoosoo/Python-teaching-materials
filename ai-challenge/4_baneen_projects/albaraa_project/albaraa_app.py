# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
# ]
# ///
"""Albaraa App — Math & Science Quiz (marimo).

A simple two-section quiz (from albaraa_questions.md): 10 math questions and
4 science questions. English UI, Arabic questions rendered RTL.
No AI challenge — just play and learn.

Run:    uvx marimo run albaraa_app.py
Edit:   uvx marimo edit albaraa_app.py
Export: uvx marimo export html-wasm albaraa_app.py -o index.html
Serve:  uv run python -m http.server  # preview the WASM build
"""

import marimo

__generated_with = "0.25.2"
app = marimo.App()

with app.setup:
    import base64
    from pathlib import Path

    import marimo as mo

    BACKGROUND_IMAGE = "baraa_app_background.jpeg"
    STUDENT_CODE_FILE = "albaraa_code.py"

    # Fallback copy of albaraa_code.py, used by the deployed WASM build where the
    # browser cannot open files from disk. Locally the real file is read instead.
    STUDENT_CODE_FALLBACK = '''# concepts learned

name = input("whats ur name?")

answer= int(input("1+2="))
if answer==3: 
   print("right")
else: 
   print("wrong")


## Choosing UI elemets 

button = mo.ui.button(
    kind="success",
    label="submit answer",
)
button


radio = mo.ui.radio(
    options=["Python", "JavaScript", "Rust"],
    value="Python",
    label="Radio Buttons",
)
radio


datetime_picker = mo.ui.datetime(
    value="2026-01-15T09:30",
    label="Datetime Picker",
)
datetime_picker


slider = mo.ui.slider(
    start=0,
    stop=100,
    step=5,
    value=50,
    show_value=True,
    label="Slider",
)
slider'''

    # Two sections, questions from albaraa_questions.md — in the same order,
    # with 4 choices each. (Math q8 is 4×7=28; the list's "42" was a typo.)
    SECTIONS = {
        "Math": {
            "icon": "🧮",
            "questions": [
                {"q": "كم يساوي 2 × 2؟", "options": ["2", "4", "6", "8"], "correct": "B",
                 "explanation": "الناتج 4 لأن 2 × 2 = 4."},
                {"q": "كم يساوي 4 × 5؟", "options": ["9", "20", "25", "15"], "correct": "B",
                 "explanation": "الناتج 20 لأن 4 × 5 = 20 (4 مجموعات من 5)."},
                {"q": "كم يساوي 6 × 2؟", "options": ["8", "10", "12", "14"], "correct": "C",
                 "explanation": "الناتج 12 لأن 6 × 2 = 12."},
                {"q": "كم يساوي 2 × 8؟", "options": ["16", "18", "14", "10"], "correct": "A",
                 "explanation": "الناتج 16 لأن 2 × 8 = 16."},
                {"q": "كم يساوي 5 × 3؟", "options": ["10", "18", "15", "8"], "correct": "C",
                 "explanation": "الناتج 15 لأن 5 × 3 = 15."},
                {"q": "كم يساوي 6 × 1؟", "options": ["6", "7", "1", "12"], "correct": "A",
                 "explanation": "أي عدد مضروبًا في 1 يبقى نفسه: 6 × 1 = 6."},
                {"q": "كم يساوي 7 × 3؟", "options": ["24", "18", "27", "21"], "correct": "D",
                 "explanation": "الناتج 21 لأن 7 × 3 = 21."},
                {"q": "كم يساوي 4 × 7؟", "options": ["24", "28", "32", "26"], "correct": "B",
                 "explanation": "الناتج 28 لأن 4 × 7 = 28."},
                {"q": "كم يساوي 10 × 2؟", "options": ["20", "22", "12", "30"], "correct": "A",
                 "explanation": "الناتج 20 لأن 10 × 2 = 20."},
                {"q": "كم يساوي 6 × 4؟", "options": ["26", "22", "24", "28"], "correct": "C",
                 "explanation": "الناتج 24 لأن 6 × 4 = 24."},
            ],
        },
        "Science": {
            "icon": "🔬",
            "questions": [
                {"q": "ما هي عاصمة إنجلترا؟", "options": ["باريس", "لندن", "روما", "مدريد"], "correct": "B",
                 "explanation": "لندن هي عاصمة إنجلترا."},
                {"q": "أين يقع لسان المزمار؟", "options": ["أعلى الجهاز التنفسي", "في المعدة", "في القلب", "في الكبد"], "correct": "A",
                 "explanation": "لسان المزمار يقع أعلى الجهاز التنفسي، ويغلق مجرى الهواء أثناء البلع."},
                {"q": "أين تقع قناة استاكيوس؟", "options": ["في الأنف", "في الأذن", "في الحلق", "في العين"], "correct": "B",
                 "explanation": "قناة استاكيوس تقع في الأذن وتوازِن ضغط الهواء فيها."},
                {"q": "كم يستغرق نمو الطماطم؟", "options": ["شهر واحد", "3 أشهر", "6 أشهر", "سنة كاملة"], "correct": "C",
                 "explanation": "يستغرق نمو نبات الطماطم حوالي 6 أشهر."},
            ],
        },
    }

    LETTERS = ["A", "B", "C", "D"]


@app.function
def read_local_file(name):
    """Read a file next to this notebook. Returns None in WASM (no disk access)."""
    for base in (
        Path.cwd(),
        Path.cwd() / "ai-challenge" / "4_baneen_projects" / "albaraa_project",
    ):
        try:
            return (base / name).read_bytes()
        except OSError:
            continue
    return None


@app.function
def student_code():
    """Contents of albaraa_code.py (embedded fallback for the deployed build)."""
    data = read_local_file(STUDENT_CODE_FILE)
    return data.decode("utf-8") if data is not None else STUDENT_CODE_FALLBACK


@app.function
def background_css():
    """Albaraa's photo as background: inlined locally, separate file when deployed."""
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
def questions_of(g):
    return SECTIONS[g["section"]]["questions"]


@app.function
def new_start():
    """Fresh app: show the section picker."""
    return {
        "stage": "start",  # start -> playing -> feedback -> (next | finished)
        "section": None,
        "index": 0,
        "score": 0,
        "current": None,
        "picked": None,
        "is_correct": None,
    }


@app.function
def new_quiz(section):
    """Start a section: first question loaded, score at 0."""
    return {
        "stage": "playing",
        "section": section,
        "index": 0,
        "score": 0,
        "current": SECTIONS[section]["questions"][0],
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
    """Move on — after the last question of the section the quiz is finished."""
    total = len(questions_of(g))
    nxt = g["index"] + 1
    if nxt >= total:
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
        "current": questions_of(g)[nxt],
        "picked": None,
        "is_correct": None,
    }


@app.cell
def _():
    get_game, set_game = mo.state(new_start(), allow_self_loops=True)
    return get_game, set_game


@app.cell
def _():
    show_code = mo.ui.checkbox(label="Show core python code")
    return (show_code,)


@app.cell
def _(get_game, set_game, new_start, show_code):
    sidebar_g = get_game()
    restart_btn = mo.ui.button(
        label="🔄 Restart",
        kind="neutral",
        full_width=True,
        on_click=lambda _: set_game(new_start()),
    )
    if sidebar_g["stage"] == "start":
        progress_md = "🧮 Math • 🔬 Science"
    elif sidebar_g["stage"] == "finished":
        progress_md = (
            f"**Finished {sidebar_g['section']}!**<br>"
            f"Score: **{sidebar_g['score']} / {len(questions_of(sidebar_g))}**"
        )
    else:
        progress_md = (
            f"{SECTIONS[sidebar_g['section']]['icon']} "
            f"{sidebar_g['section']} — "
            f"Question **{sidebar_g['index'] + 1} / {len(questions_of(sidebar_g))}**<br>"
            f"Score: **{sidebar_g['score']}**"
        )
    # Left panel rendered as normal app content (not mo.sidebar): the sidebar
    # custom element copies stylesheet rules we cannot override, so text on
    # the dark photo was unreadable. Inline panel = fully controllable CSS.
    left_panel = mo.vstack([
        mo.md('<div class="albaraa-text"><h2>🌟 Albaraa App</h2></div>'),
        mo.md(f'<div class="albaraa-text">{progress_md}</div>'),
        mo.md("---"),
        restart_btn,
        show_code,
    ])
    return (left_panel,)


@app.cell
def _():
    mo.md(
        f"""<style>
    body {{
        background-image: linear-gradient(rgba(2, 6, 23, 0.70), rgba(2, 6, 23, 0.70)), {background_css()};
        background-size: 100% 100%, contain;
        background-position: center;
        background-repeat: no-repeat;
        background-attachment: fixed;
        background-color: #020617;
    }}
    .albaraa-text, .albaraa-text * {{
        color: #f8fafc !important;
    }}
    .albaraa-text code {{
        color: #fde68a !important;
        background: rgba(0, 0, 0, 0.45);
    }}
    /* Photo shows through the WHOLE app: cells and app shells are
       transparent, not just the side panel (classes from marimo's CSS). */
    #App, .marimo-cell, .bg-background, .bg-background\\/80,
    .bg-background\\/90, .bg-background\\/95 {{
        background-color: transparent !important;
    }}
    /* Readable text on the dark photo: default-colored text (sidebar prose,
       headings, radio/checkbox labels, progress code) forced to light colors.
       .mo-label / code are real marimo classes; marimo-sidebar is marimo's
       own custom element tag. */
    #App, #App h1, #App h2, #App h3, #App h4, #App h5, #App h6,
    #App label, .mo-label, .marimo-sidebar {{
        color: #f8fafc !important;
    }}
    #App code {{
        color: #fde68a !important;
        background: rgba(0, 0, 0, 0.45);
    }}
    </style>"""
    )
    return


@app.cell
def _():
    mo.md("""
    <div class="albaraa-text"><h1>🌟 Albaraa's Math & Science Challenge</h1><p>Two sections: <strong>10 math</strong> 🧮 and <strong>4 science</strong> 🔬 questions. Python checks your answers.</p></div>
    """)
    return


@app.cell
def _(SECTIONS, get_game, new_quiz, set_game):
    g = get_game()

    if g["stage"] == "start":
        math_btn = mo.ui.button(
            label=f"🧮 Math — {len(SECTIONS['Math']['questions'])} questions",
            kind="success",
            on_click=lambda _: set_game(new_quiz("Math")),
        )
        science_btn = mo.ui.button(
            label=f"🔬 Science — {len(SECTIONS['Science']['questions'])} questions",
            kind="neutral",
            on_click=lambda _: set_game(new_quiz("Science")),
        )
        parts = [
            mo.md('<div class="albaraa-text"><p><strong>Pick a section</strong></p></div>'),
            mo.hstack([math_btn, science_btn], justify="start"),
        ]

    elif g["stage"] == "playing":
        total = len(questions_of(g))
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
                f'<div class="albaraa-text">{SECTIONS[g["section"]]["icon"]} '
                f'{g["section"]} — Question <strong>{g["index"] + 1} / {total}</strong>'
                f' &nbsp;•&nbsp; Score: <strong>{g["score"]}</strong></div>'
            ),
            mo.md(f'`{"█" * g["index"]}{"░" * (total - g["index"])}`'),
            mo.md(
                f'<div class="albaraa-text" dir="rtl" style="text-align:right">'
                f"<strong>{q['q']}</strong></div>"
            ),
            radio,
            submit,
        ]

    elif g["stage"] == "feedback":
        total = len(questions_of(g))
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
        is_last = g["index"] == total - 1
        next_btn = mo.ui.button(
            label="🏁 See results" if is_last else "➡️ Next question",
            kind="success",
            on_click=lambda _: set_game(lambda s: next_question(s)),
        )
        parts = [
            mo.md(
                f'<div class="albaraa-text" dir="rtl" style="text-align:right">'
                f"<strong>{q['q']}</strong></div>"
            ),
            header,
            mo.md('<div class="albaraa-text">💡 <strong>Explanation</strong></div>'),
            mo.md(
                f'<div class="albaraa-text" dir="rtl" style="text-align:right">'
                f"{q['explanation']}</div>"
            ),
            next_btn,
        ]

    else:  # finished
        total = len(questions_of(g))
        score = g["score"]
        if score == total:
            verdict = "🏆 Perfect score!"
        elif score * 2 >= total:
            verdict = "👏 Well done!"
        else:
            verdict = "💪 Good try — play again and beat your score!"
        play_again = mo.ui.button(
            label="🔁 Play again",
            kind="success",
            on_click=lambda _: set_game(new_quiz(g["section"])),
        )
        other_btn = mo.ui.button(
            label="🎯 Try the other section",
            kind="neutral",
            on_click=lambda _: set_game(new_start()),
        )
        parts = [
            mo.md(
                f'<div class="albaraa-text"><h1>🏁 {SECTIONS[g["section"]]["icon"]} '
                f'{g["section"]} quiz finished!</h1></div>'
            ),
            mo.md(
                f'<div class="albaraa-text">You scored <strong>{score} / {total}</strong></div>'
            ),
            mo.md(f'`{"█" * score}{"░" * (total - score)}`'),
            mo.callout(verdict, kind="info", title="Your result"),
            mo.hstack([play_again, other_btn], justify="center"),
        ]

    view = mo.vstack(parts)
    return (view,)


@app.cell
def _(left_panel, view):
    layout = mo.hstack(
        [left_panel, view], justify="start", align="start", widths=[0.27, 0.73]
    )
    layout
    return


@app.cell
def _(show_code, student_code):
    import html

    # mo.md code fences are always syntax-highlighted by marimo's markdown
    # renderer (even without a language marker), which made the code hard to
    # read. Render a plain <pre> via real HTML instead — no highlighting.
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
                '<div class="albaraa-text"><strong>💻 Core Python code</strong> '
                "— from <code>albaraa_code.py</code></div>"
            ),
            code_block,
        ], gap=0.25)
        if show_code.value
        else None
    )
    code_view
    return


if __name__ == "__main__":
    app.run()
