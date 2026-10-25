"""AI Challenge Mini — single-question Gradio app (if/else version).

Decision step: choice allowed, Check press allowed,
one if/else decision made, zero error raised.
No while loop, so the game stops after the single question.
Uses only: variables, input, output, lists, if/else.
Plus one hosting adapter for ZeroGPU; lesson logic unchanged.
"""

import gradio as gr
import spaces


@spaces.GPU
def gpu_warmup():
    # Hosting adapter: ZeroGPU scheduler needs one GPU-tagged entry.
    # Never called; lesson logic unchanged.
    return "ready"

SUBJECT = "Science"
QUESTION = "Which gas do plants take in during photosynthesis?"
OPTIONS = ["A. Oxygen", "B. Nitrogen", "C. Carbon dioxide", "D. Hydrogen"]
CORRECT_LETTER = "C"
EXPLANATION = "Plants take in carbon dioxide and release oxygen during photosynthesis."

MESSAGES = [
    "Not quite. Correct answer: C.",
    "Correct! Great job!",
]

INTRO = "Awaiting your decision. Pick one choice, then press Check."
FINISHED = "Game over after 1 question. Restart the app to play again."

# Answer data stays declared above; the if/else below reads it.


def check_answer(picked):
    """Run the if/else decision, then stop (no loop to ask again)."""
    if picked is None:
        # Nothing chosen yet: keep the game running, raise nothing.
        return (
            "Pick one choice first.",
            "Still playing: 0 of 1 questions answered.",
            gr.update(interactive=True),
            gr.update(interactive=True),
        )

    if picked.startswith(CORRECT_LETTER):
        message = MESSAGES[1]
    else:
        message = MESSAGES[0]

    # No while loop here: after this single decision the game stops.
    return (
        f"{message} {EXPLANATION}",
        FINISHED,
        gr.update(interactive=False),
        gr.update(interactive=False),
    )


with gr.Blocks(title="AI Challenge Mini") as demo:
    gr.Markdown("# AI Challenge Mini")
    gr.Markdown("One Science question. Pick one choice, then press Check.")
    gr.Markdown("Current step: if/else gives the result, then the game stops.")
    choice = gr.Radio(OPTIONS, label=QUESTION)
    check_btn = gr.Button("Check")
    result = gr.Textbox(
        label="Result:",
        value=INTRO,
        interactive=False,
    )
    status = gr.Textbox(
        label="Game state:",
        value="Still playing: 0 of 1 questions answered.",
        interactive=False,
    )
    # Planned gap: no while loop, so nothing ever loads a second question.
    check_btn.click(
        fn=check_answer,
        inputs=choice,
        outputs=[result, status, choice, check_btn],
    )

demo.launch(server_name="0.0.0.0", server_port=7860, ssr_mode=False)
