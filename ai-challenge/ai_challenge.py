# /// script
# requires-python = ">=3.12"
# dependencies = [
#     "marimo",
# ]
# ///
"""AI Challenge Battle — marimo app (converted from the Streamlit original).

Run:    uvx marimo run ai_challenge.py
Edit:   uvx marimo edit ai_challenge.py
Export: uvx marimo export html-wasm ai_challenge.py -o docs/index.html
Serve:  uv run python -m http.server --directory docs  # preview the WASM build

How it maps to the project spec:
  Stage 1: 15 teacher questions, need 4 correct IN A ROW (streak).
  Unlock:  "HORRAAY! AI HAS JOINED THE BATTLE!"
  Stage 2: while answer_is_correct: AI generates Q, PYTHON evaluates it.
  End: first mistake -> explanation + concept illustration.
  Limit: 5 AI battles (offline in WASM; server-side rate_limit.py in Streamlit).
"""

import marimo

__generated_with = "0.25.1"
app = marimo.App()


with app.setup:
    import random

    import marimo as mo

    QUESTIONS = {
        "Science": [
            {"q": "Which gas do plants take in during photosynthesis?", "options": ["Oxygen", "Nitrogen", "Carbon dioxide", "Hydrogen"], "correct": "C", "explanation": "Plants take in carbon dioxide and release oxygen during photosynthesis.", "concept": "photosynthesis"},
            {"q": "What happens when water reaches its boiling point?", "options": ["It becomes ice", "It becomes water vapor", "It disappears", "It becomes soil"], "correct": "B", "explanation": "Liquid water heated to boiling point changes into a gas called water vapor.", "concept": "states of matter"},
            {"q": "Which planet is known as the Red Planet?", "options": ["Venus", "Mars", "Jupiter", "Mercury"], "correct": "B", "explanation": "Mars looks red because of iron oxide (rust) on its surface.", "concept": "solar system"},
            {"q": "What force pulls objects toward the Earth?", "options": ["Magnetism", "Friction", "Gravity", "Push"], "correct": "C", "explanation": "Gravity pulls everything toward the centre of the Earth.", "concept": "gravity"},
            {"q": "Which part of the plant makes food?", "options": ["Root", "Stem", "Leaf", "Flower"], "correct": "C", "explanation": "Leaves contain chlorophyll and make food by photosynthesis.", "concept": "plant structure"},
            {"q": "How many states of matter are commonly taught (solid, liquid, gas)?", "options": ["2", "3", "4", "5"], "correct": "B", "explanation": "The three common states are solid, liquid and gas.", "concept": "states of matter"},
            {"q": "What does a food chain always start with?", "options": ["A carnivore", "A producer", "A decomposer", "A consumer"], "correct": "B", "explanation": "Every food chain starts with a producer, usually a green plant.", "concept": "food chain"},
            {"q": "Which material lets electricity pass easily?", "options": ["Rubber", "Wood", "Copper", "Plastic"], "correct": "C", "explanation": "Copper is a conductor; rubber, wood and plastic are insulators.", "concept": "electricity"},
            {"q": "Where does the water cycle start when water rises into the air?", "options": ["Precipitation", "Collection", "Evaporation", "Condensation"], "correct": "C", "explanation": "Evaporation is when liquid water becomes vapor and rises.", "concept": "water cycle"},
            {"q": "Which simple machine uses a fulcrum?", "options": ["Lever", "Rope", "Wheel", "Screw"], "correct": "A", "explanation": "A lever turns around a fixed point called the fulcrum.", "concept": "forces and motion"},
            {"q": "What do we call animals that eat only plants?", "options": ["Carnivores", "Herbivores", "Omnivores", "Predators"], "correct": "B", "explanation": "Herbivores eat only plants.", "concept": "food chain"},
            {"q": "Which planet is closest to the Sun?", "options": ["Earth", "Venus", "Mercury", "Mars"], "correct": "C", "explanation": "Mercury is the closest planet to the Sun.", "concept": "solar system"},
            {"q": "What is ice an example of?", "options": ["Gas", "Liquid", "Solid", "Vapor"], "correct": "C", "explanation": "Ice is water in its solid state.", "concept": "states of matter"},
            {"q": "Which part of the plant absorbs water?", "options": ["Leaf", "Flower", "Stem", "Root"], "correct": "D", "explanation": "Roots absorb water from the soil.", "concept": "plant structure"},
            {"q": "What pushes a falling parachute upward?", "options": ["Gravity", "Air resistance", "Magnetism", "Light"], "correct": "B", "explanation": "Air resistance pushes up while gravity pulls down.", "concept": "forces and motion"},
        ],
        "Geography": [
            {"q": "Which is the largest ocean?", "options": ["Atlantic", "Indian", "Arctic", "Pacific"], "correct": "D", "explanation": "The Pacific is the largest ocean.", "concept": "oceans"},
            {"q": "Which continent is Egypt in?", "options": ["Asia", "Africa", "Europe", "South America"], "correct": "B", "explanation": "Egypt is in Africa.", "concept": "continents"},
            {"q": "What is the capital of France?", "options": ["London", "Paris", "Rome", "Madrid"], "correct": "B", "explanation": "Paris is the capital of France.", "concept": "capitals"},
            {"q": "Which river flows through Egypt?", "options": ["Amazon", "Nile", "Mississippi", "Danube"], "correct": "B", "explanation": "The Nile flows through Egypt.", "concept": "rivers"},
            {"q": "What is a mountain with an opening that erupts?", "options": ["Hill", "Valley", "Volcano", "Plateau"], "correct": "C", "explanation": "A volcano erupts lava and ash.", "concept": "volcano"},
            {"q": "Which desert is the largest hot desert?", "options": ["Gobi", "Sahara", "Kalahari", "Atacama"], "correct": "B", "explanation": "The Sahara is the largest hot desert.", "concept": "deserts"},
            {"q": "How many continents are there?", "options": ["5", "6", "7", "8"], "correct": "C", "explanation": "There are 7 continents.", "concept": "continents"},
            {"q": "What do we call land completely surrounded by water?", "options": ["Peninsula", "Island", "Isthmus", "Delta"], "correct": "B", "explanation": "An island is land surrounded by water.", "concept": "landforms"},
            {"q": "Which direction does the sun rise from?", "options": ["North", "South", "East", "West"], "correct": "C", "explanation": "The sun rises in the east.", "concept": "compass"},
            {"q": "What is the imaginary line around the middle of Earth?", "options": ["Prime Meridian", "Equator", "Tropic", "Axis"], "correct": "B", "explanation": "The Equator circles the middle of Earth.", "concept": "globe"},
            {"q": "Which is the longest river in the world (often listed)?", "options": ["Nile", "Amazon", "Yangtze", "Congo"], "correct": "A", "explanation": "The Nile is usually listed as the longest river.", "concept": "rivers"},
            {"q": "What map symbol shows height above sea level?", "options": ["Compass", "Scale", "Contour line", "Legend"], "correct": "C", "explanation": "Contour lines join places of equal height.", "concept": "maps"},
            {"q": "Which climate has rain all year and dense trees?", "options": ["Desert", "Polar", "Rainforest", "Mediterranean"], "correct": "C", "explanation": "Rainforests are wet all year.", "concept": "climate"},
            {"q": "What is the capital of Egypt?", "options": ["Giza", "Alexandria", "Cairo", "Luxor"], "correct": "C", "explanation": "Cairo is the capital of Egypt.", "concept": "capitals"},
            {"q": "Which ocean is west of Africa?", "options": ["Pacific", "Atlantic", "Indian", "Arctic"], "correct": "B", "explanation": "The Atlantic Ocean is west of Africa.", "concept": "oceans"},
        ],
        "Mathematics": [
            {"q": "What is 7 x 8?", "options": ["54", "56", "63", "48"], "correct": "B", "explanation": "7 times 8 equals 56.", "concept": "multiplication"},
            {"q": "What is 1/2 + 1/4?", "options": ["1/6", "2/4", "3/4", "1/4"], "correct": "C", "explanation": "1/2 = 2/4, so 2/4 + 1/4 = 3/4.", "concept": "fractions"},
            {"q": "Which number is prime?", "options": ["4", "6", "9", "7"], "correct": "D", "explanation": "7 has only factors 1 and 7.", "concept": "primes"},
            {"q": "What is 100 - 37?", "options": ["63", "73", "53", "67"], "correct": "A", "explanation": "100 minus 37 is 63.", "concept": "subtraction"},
            {"q": "How many degrees in a right angle?", "options": ["45", "90", "180", "360"], "correct": "B", "explanation": "A right angle is 90 degrees.", "concept": "angles"},
            {"q": "What is the next number: 2, 4, 8, 16, ...?", "options": ["20", "24", "32", "18"], "correct": "C", "explanation": "Each number doubles, so next is 32.", "concept": "patterns"},
            {"q": "What is 3/4 as a decimal?", "options": ["0.34", "0.75", "0.43", "0.5"], "correct": "B", "explanation": "3 divided by 4 is 0.75.", "concept": "fractions"},
            {"q": "How many sides does a hexagon have?", "options": ["5", "6", "7", "8"], "correct": "B", "explanation": "A hexagon has 6 sides.", "concept": "shapes"},
            {"q": "What is 12 x 12?", "options": ["124", "132", "144", "142"], "correct": "C", "explanation": "12 squared is 144.", "concept": "multiplication"},
            {"q": "Which fraction is biggest?", "options": ["1/4", "1/3", "1/5", "1/8"], "correct": "B", "explanation": "1/3 is the largest piece.", "concept": "fractions"},
            {"q": "What is the area of 5cm by 4cm rectangle?", "options": ["9 sq cm", "20 sq cm", "18 sq cm", "10 sq cm"], "correct": "B", "explanation": "Area = 5 x 4 = 20 square cm.", "concept": "area"},
            {"q": "What is 15% of 200?", "options": ["15", "20", "30", "25"], "correct": "C", "explanation": "10% is 20 and 5% is 10, so 30.", "concept": "percentages"},
            {"q": "Which is an even number?", "options": ["13", "17", "22", "31"], "correct": "C", "explanation": "22 divides by 2 exactly.", "concept": "numbers"},
            {"q": "What is 9 + 9 + 9?", "options": ["18", "27", "29", "36"], "correct": "B", "explanation": "9 three times is 27.", "concept": "addition"},
            {"q": "How many minutes in 2 hours?", "options": ["60", "100", "120", "180"], "correct": "C", "explanation": "2 x 60 = 120 minutes.", "concept": "time"},
        ],
        "History": [
            {"q": "Who recorded one of the oldest algorithms around 300 BC?", "options": ["Pythagoras", "Euclid", "Aristotle", "Archimedes"], "correct": "B", "explanation": "Euclid recorded a famous algorithm around 300 BC.", "concept": "ancient greece"},
            {"q": "The pyramids of Giza were built as...?", "options": ["Palaces", "Tombs", "Schools", "Markets"], "correct": "B", "explanation": "Pyramids were tombs for pharaohs.", "concept": "ancient egypt"},
            {"q": "Which civilization used hieroglyphs?", "options": ["Roman", "Greek", "Egyptian", "Viking"], "correct": "C", "explanation": "Ancient Egyptians wrote with hieroglyphs.", "concept": "ancient egypt"},
            {"q": "The Romans spoke which language?", "options": ["Greek", "Latin", "Arabic", "French"], "correct": "B", "explanation": "Romans spoke Latin.", "concept": "rome"},
            {"q": "Which invention helped ships navigate with direction?", "options": ["Compass", "Engine", "Telescope", "Anchor"], "correct": "A", "explanation": "The compass shows direction.", "concept": "exploration"},
            {"q": "Who was the first man on the moon (1969)?", "options": ["Yuri Gagarin", "Buzz Aldrin", "Neil Armstrong", "Michael Collins"], "correct": "C", "explanation": "Neil Armstrong stepped first in 1969.", "concept": "modern history"},
            {"q": "The Great Wall is in which country?", "options": ["India", "China", "Egypt", "Mexico"], "correct": "B", "explanation": "The Great Wall is in China.", "concept": "china"},
            {"q": "Vikings came from which region?", "options": ["South America", "Scandinavia", "Africa", "Australia"], "correct": "B", "explanation": "Vikings came from Scandinavia.", "concept": "vikings"},
            {"q": "What do we call objects from the past in museums?", "options": ["Artefacts", "Souvenirs", "Toys", "Copies"], "correct": "A", "explanation": "Artefacts are historical objects.", "concept": "history skills"},
            {"q": "Which scholar is linked to algebra (Al-Khwarizmi)?", "options": ["Ibn Battuta", "Al-Khwarizmi", "Ibn Khaldun", "Averroes"], "correct": "B", "explanation": "Al-Khwarizmi's work gave us the word algorithm and algebra.", "concept": "islamic golden age"},
            {"q": "Ancient Olympic games began in which country?", "options": ["Egypt", "Greece", "Rome", "Persia"], "correct": "B", "explanation": "Olympics began in ancient Greece.", "concept": "ancient greece"},
            {"q": "What material did ancient Egyptians write on?", "options": ["Paper", "Papyrus", "Silk", "Clay tablets"], "correct": "B", "explanation": "Egyptians made papyrus from reeds.", "concept": "ancient egypt"},
            {"q": "Which empire built roads across Europe?", "options": ["Ottoman", "Roman", "Mongol", "Aztec"], "correct": "B", "explanation": "Romans built long straight roads.", "concept": "rome"},
            {"q": "A decade is how many years?", "options": ["10", "100", "12", "50"], "correct": "A", "explanation": "A decade is 10 years.", "concept": "history skills"},
            {"q": "A century is how many years?", "options": ["10", "50", "100", "1000"], "correct": "C", "explanation": "A century is 100 years.", "concept": "history skills"},
        ],
        "Python": [
            {"q": "Which function displays a message in Python?", "options": ["show()", "print()", "display()", "echo()"], "correct": "B", "explanation": "print() displays output, e.g. print('Hello').", "concept": "output"},
            {"q": "Which symbol assigns a value to a variable?", "options": ["==", "=", "->", ":="], "correct": "B", "explanation": "Single = assigns, e.g. x = 5. Double == compares.", "concept": "variables"},
            {"q": "What does input() do?", "options": ["Prints text", "Reads keyboard text", "Adds numbers", "Stops the program"], "correct": "B", "explanation": "input() reads text typed on the keyboard.", "concept": "input"},
            {"q": "What is the result of 7 // 2 in Python?", "options": ["3.5", "3", "4", "2"], "correct": "B", "explanation": "// is floor division: 7 // 2 = 3.", "concept": "operators"},
            {"q": "Which keyword starts a loop that repeats while true?", "options": ["for", "if", "while", "repeat"], "correct": "C", "explanation": "while repeats as long as its condition stays True.", "concept": "loops"},
            {"q": "How do we check equality in Python?", "options": ["=", "==", "!=", "==="], "correct": "B", "explanation": "== compares two values for equality.", "concept": "conditions"},
            {"q": "What type is 'Hello' in Python?", "options": ["int", "float", "str", "bool"], "correct": "C", "explanation": "'Hello' in quotes is a string (str).", "concept": "types"},
            {"q": "What type is 13 in Python?", "options": ["str", "int", "float", "list"], "correct": "B", "explanation": "13 without a point is an integer (int).", "concept": "types"},
            {"q": "Which line fixes: print('Hi'  ?", "options": ["print('Hi')", "print('Hi'", "Print('Hi')", "print(Hi)"], "correct": "A", "explanation": "Brackets must close: print('Hi').", "concept": "syntax errors"},
            {"q": "What does this do? user = 'Claude'", "options": ["Compares user", "Assigns the string Claude to user", "Prints Claude", "Deletes user"], "correct": "B", "explanation": "It assigns (stores) the string in the variable.", "concept": "variables"},
            {"q": "Which name is a valid Python variable?", "options": ["2cool", "my-score", "my_score", "my score"], "correct": "C", "explanation": "Variables use letters, digits, underscore and cannot start with a digit or contain spaces/dashes.", "concept": "variables"},
            {"q": "What happens after a SyntaxError?", "options": ["Program runs anyway", "Python shows an error and stops that line", "Computer shuts down", "Nothing"], "correct": "B", "explanation": "Python reports the error and does not run the broken line.", "concept": "syntax errors"},
            {"q": "Which block runs when if is False and else exists?", "options": ["if block", "else block", "both", "none"], "correct": "B", "explanation": "else runs when the if condition is False.", "concept": "conditions"},
            {"q": "How many times does this run? i=0; while i<3: i+=1", "options": ["2", "3", "4", "forever"], "correct": "B", "explanation": "i becomes 1,2,3 then stops: 3 times.", "concept": "loops"},
            {"q": "Which function gets the length of a list?", "options": ["size()", "len()", "length()", "count()"], "correct": "B", "explanation": "len() returns the number of items.", "concept": "lists"},
        ],
    }

    FALLBACK_AI_BANK = {
        "Science": [
            {"q": "Which gas do plants release during photosynthesis?", "options": ["Carbon dioxide", "Oxygen", "Nitrogen", "Hydrogen"], "correct": "B", "explanation": "Plants release oxygen as they make food.", "concept": "photosynthesis"},
            {"q": "What is water vapor?", "options": ["Solid water", "Liquid water", "Water as a gas", "Frozen water"], "correct": "C", "explanation": "Vapor is water in gas form after heating.", "concept": "states of matter"},
            {"q": "Why does a parachute fall slowly?", "options": ["No gravity", "Air resistance pushes up", "It is heavy", "Wind pushes down"], "correct": "B", "explanation": "Air resistance pushes up against gravity.", "concept": "forces and motion"},
        ],
        "Geography": [
            {"q": "Which continent has the Sahara desert?", "options": ["Asia", "Africa", "Europe", "Australia"], "correct": "B", "explanation": "The Sahara is in Africa.", "concept": "deserts"},
            {"q": "What is the Equator?", "options": ["Top of Earth", "Middle line of Earth", "A country", "An ocean"], "correct": "B", "explanation": "The Equator circles Earth's middle.", "concept": "globe"},
            {"q": "Where does the sun set?", "options": ["East", "West", "North", "South"], "correct": "B", "explanation": "Sun rises east, sets west.", "concept": "compass"},
        ],
        "Mathematics": [
            {"q": "What is 6 x 7?", "options": ["42", "36", "48", "40"], "correct": "A", "explanation": "6 times 7 is 42.", "concept": "multiplication"},
            {"q": "Which is equal to 1/2?", "options": ["1/4", "2/4", "3/4", "1/3"], "correct": "B", "explanation": "2/4 simplifies to 1/2.", "concept": "fractions"},
            {"q": "What is the perimeter of a 3cm square?", "options": ["6cm", "9cm", "12cm", "7cm"], "correct": "C", "explanation": "4 sides x 3 = 12cm.", "concept": "area"},
        ],
        "History": [
            {"q": "What were Egyptian pyramids used for?", "options": ["Schools", "Tombs", "Shops", "Bridges"], "correct": "B", "explanation": "Pyramids were tombs for pharaohs.", "concept": "ancient egypt"},
            {"q": "Where did the Olympics begin?", "options": ["Rome", "Greece", "Egypt", "China"], "correct": "B", "explanation": "The Olympics began in ancient Greece.", "concept": "ancient greece"},
            {"q": "How many years in a century?", "options": ["10", "50", "100", "1000"], "correct": "C", "explanation": "A century is 100 years.", "concept": "history skills"},
        ],
        "Python": [
            {"q": "What does print('Hi') do?", "options": ["Reads input", "Shows Hi on screen", "Saves a file", "Deletes text"], "correct": "B", "explanation": "print() displays output.", "concept": "output"},
            {"q": "Which line stores 10 in x?", "options": ["x == 10", "x = 10", "x -> 10", "10 = x"], "correct": "B", "explanation": "= assigns the value.", "concept": "variables"},
            {"q": "What keyword repeats while a condition is True?", "options": ["if", "for", "while", "else"], "correct": "C", "explanation": "while loops while True.", "concept": "loops"},
        ],
    }

    ILLUSTRATIONS = {
        "photosynthesis": "☀️ sunlight\n   ↓\n🍃 LEAF takes in CO₂\n   ↓\n🌱 FOOD + O₂ out",
        "states of matter": "      HEAT\n        ↓\n 💧 LIQUID WATER\n        ↓\n   💨 WATER VAPOR",
        "water cycle": "☀️ EVAPORATION\n   💨 vapor up\n☁️ CONDENSATION\n   🌧️ PRECIPITATION\n🌊 COLLECTION",
        "solar system": "☀️ — ☿ Mercury — ♀ Venus — 🌍 Earth — ♂ Mars",
        "gravity": "🍎 apple\n  ↓ gravity\n🌍 Earth",
        "plant structure": "🌸 flower\n🌿 stem\n🍃 leaf makes food\n🌱 root absorbs water",
        "food chain": "🌱 producer → 🐛 consumer → 🦊 consumer",
        "electricity": "🔋 —🔌 copper wire (conductor) → 💡 ON\n🚫 rubber/plastic = insulator",
        "forces and motion": "◀— fulcrum —▶\n   LEVER turns here",
        "oceans": "🌊 Pacific (largest) | Atlantic | Indian | Arctic",
        "continents": "7 continents:\nAfrica • Asia • Europe • N.America • S.America • Australia • Antarctica",
        "capitals": "🇫🇷 Paris = France\n🇪🇬 Cairo = Egypt",
        "rivers": "🏞️ Nile flows through Egypt → Mediterranean",
        "volcano": "🌋 VOLCANO\n  lava + ash erupt",
        "deserts": "🏜️ Sahara = largest hot desert",
        "landforms": "🏝️ ISLAND = land + water all around",
        "compass": "    N\nW ─┼─ E  (sun rises in East)\n    S",
        "globe": "— Equator (middle of Earth) —",
        "maps": "🗺️ contour lines = equal height",
        "climate": "🌧️🌧️ rainforest: rain all year",
        "multiplication": "7 × 8 = 56\n12 × 12 = 144",
        "fractions": "½ = 2/4\n2/4 + 1/4 = 3/4 🍕",
        "primes": "7 = PRIME (only 1 × 7)",
        "subtraction": "100 − 37 = 63",
        "angles": "∟ = 90° right angle",
        "patterns": "2 → 4 → 8 → 16 → 32 (×2)",
        "shapes": "⬡ hexagon = 6 sides",
        "area": "▭ 5cm × 4cm = 20 sq cm",
        "percentages": "15% of 200 = 30",
        "numbers": "22 = EVEN (÷2 exactly)",
        "addition": "9 + 9 + 9 = 27",
        "time": "⏰ 1h = 60min → 2h = 120min",
        "ancient greece": "🏛️ Greece: Euclid (~300 BC) + Olympics",
        "ancient egypt": "🔺 pyramids = tombs\n📜 hieroglyphs on papyrus",
        "rome": "🏟️ Rome: Latin + straight roads",
        "exploration": "🧭 compass shows direction",
        "modern history": "🌙 1969: Neil Armstrong first on moon",
        "china": "🧱 Great Wall = China",
        "vikings": "🛶 Vikings from Scandinavia",
        "history skills": "🏺 artefacts = objects from the past\n10y = decade, 100y = century",
        "islamic golden age": "📐 Al-Khwarizmi → algebra + algorithm",
        "output": "print('Hello')\n  ↓\n🖥️ Hello",
        "variables": "📦 user = 'Claude'\n(variable = labelled box)",
        "input": "⌨️ input() → reads keyboard",
        "operators": "7 // 2 = 3  (floor division)",
        "loops": "🔁 while True:\n    keep going!",
        "conditions": "if True: ...\nelse: ... (runs when if is False)",
        "types": "'Hello' = str (text)\n13 = int (whole number)",
        "syntax errors": "⚠️ SyntaxError →\nPython stops that line\ncheck brackets: print('Hi')",
        "lists": "len([a, b, c]) = 3",
    }

    SUBJECTS = list(QUESTIONS.keys())
    SUBJECT_EMOJI = {"Science": "🔬", "Geography": "🌍", "Mathematics": "📐", "History": "🏛️", "Python": "💻"}
    LETTERS = ["A", "B", "C", "D"]
    MAX_BATTLES = 5


# ---------- pure game logic (importable + testable outside the notebook) ----------


@app.function
def generate_ai_question(subject, used_questions=None):
    """Offline AI question (WASM has no network — always returns a valid MCQ)."""
    used_questions = used_questions or []
    pool = [q for q in FALLBACK_AI_BANK.get(subject, []) if q["q"] not in used_questions]
    if not pool:
        pool = FALLBACK_AI_BANK.get(subject, [])
    q = random.choice(pool).copy()
    q["source"] = "ai-fallback (offline)"
    return q


@app.function
def get_illustration(concept):
    return ILLUSTRATIONS.get(concept, "💡 Remember the concept and try again!")


@app.function
def format_labels(options):
    return [f"{letter}. {opt}" for letter, opt in zip(LETTERS, options)]


@app.function
def option_letter_to_text(q, letter):
    return q["options"]["ABCD".index(letter)]


@app.function
def new_game(subject):
    """Fresh game: shuffled teacher-question order, first question loaded."""
    bank = QUESTIONS[subject]
    order = random.sample(range(len(bank)), len(bank))
    first = {**bank[order[0]], "source": "teacher"}
    return {
        "subject": subject,
        "stage": "challenge",
        "order": order,
        "q_index": 1,
        "streak": 0,
        "score": 0,
        "current": first,
        "ai_score": 0,
        "ai_used": [],
        "ai_explain": None,
        "feedback": None,
    }


@app.function
def answer_challenge(g, letter):
    """Python (not AI) decides. Correct: streak up (4 unlocks the AI). Wrong: reset + explain."""
    q = g["current"]
    bank = QUESTIONS[g["subject"]]
    nxt = {**bank[g["q_index"] % len(g["order"])], "source": "teacher"}
    base = {**g, "q_index": g["q_index"] + 1, "current": nxt, "feedback": None}
    if letter == q["correct"]:
        streak = g["streak"] + 1
        if streak >= 4:
            return {**base, "streak": streak, "score": g["score"] + 1,
                    "stage": "unlocked", "current": None}
        return {**base, "streak": streak, "score": g["score"] + 1}
    return {**base, "streak": 0, "feedback": q}


@app.function
def start_battle(g):
    q = generate_ai_question(g["subject"])
    return {**g, "stage": "ai_battle", "ai_score": 0, "ai_used": [q["q"]],
            "current": q, "ai_explain": None, "feedback": None}


@app.function
def answer_battle(g, letter):
    """First mistake ends the battle (spec: while answer_is_correct)."""
    q = g["current"]
    if letter == q["correct"]:
        nxt = generate_ai_question(g["subject"], used_questions=g["ai_used"])
        return {**g, "ai_score": g["ai_score"] + 1, "current": nxt,
                "ai_used": g["ai_used"] + [nxt["q"]], "feedback": None}
    return {**g, "stage": "gameover", "current": None, "ai_explain": q}


# ---------- state (accumulated game memory — replaces st.session_state) ----------


@app.cell
def _(mo, new_game):
    get_game, set_game = mo.state(new_game("Science"), allow_self_loops=True)
    get_battles, set_battles = mo.state(0, allow_self_loops=True)
    return get_battles, get_game, set_battles, set_game


# ---------- sidebar (was: st.sidebar) ----------


@app.cell
def _(MAX_BATTLES, SUBJECTS, SUBJECT_EMOJI, get_battles, mo, new_game, set_game):
    subject_buttons = [
        mo.ui.button(
            label=f"{SUBJECT_EMOJI[s]} {s}",
            kind="neutral",
            full_width=True,
            on_click=lambda _, s=s: set_game(new_game(s)),
        )
        for s in SUBJECTS
    ]
    restart_btn = mo.ui.button(
        label="🔄 Restart",
        kind="neutral",
        full_width=True,
        on_click=lambda _: set_game(lambda g: new_game(g["subject"])),
    )
    show_logic = mo.ui.checkbox(label="👀 Show student Python logic")
    mo.sidebar([
        mo.md("## Choose your subject"),
        *subject_buttons,
        mo.md("---"),
        mo.md(f"🤖 AI battles left: **{MAX_BATTLES - get_battles()} / {MAX_BATTLES}**"),
        restart_btn,
        show_logic,
    ])
    return (show_logic,)


# ---------- header (was: st.title / st.caption / st.header) ----------


@app.cell
def _(SUBJECT_EMOJI, get_game, mo):
    subject = get_game()["subject"]
    mo.vstack([
        mo.md("# 🧠 AI CHALLENGE"),
        mo.md("Python controls the game. The AI provides the challenge. You control the outcome."),
        mo.md(f"## {SUBJECT_EMOJI[subject]} {subject}"),
    ])
    return


# ---------- game view: all four stages in one cell (was: if/elif stage blocks) ----------


@app.cell
def _(
    MAX_BATTLES,
    answer_battle,
    answer_challenge,
    format_labels,
    get_battles,
    get_game,
    get_illustration,
    mo,
    new_game,
    option_letter_to_text,
    set_battles,
    set_game,
    start_battle,
):
    g = get_game()
    battles = get_battles()

    if g["stage"] == "challenge":
        q = g["current"]
        labels = format_labels(q["options"])
        radio = mo.ui.radio(labels, value=labels[0], label=q["q"])
        submit = mo.ui.button(
            label="Submit answer",
            kind="success",
            on_click=lambda _: set_game(lambda s: answer_challenge(s, radio.value[0])),
        )
        parts = [
            mo.md(
                f"Goal: get **4 correct in a row** to unlock the AI. "
                f"Streak: **{g['streak']}/4**  |  Score: {g['score']}"
            ),
            mo.md(f"`{'█' * g['streak']}{'░' * (4 - g['streak'])}`"),
        ]
        if g["feedback"]:
            missed = g["feedback"]
            parts.append(mo.callout(
                f"❌ Correct was **{missed['correct']}: "
                f"{option_letter_to_text(missed, missed['correct'])}**. "
                f"Streak reset to 0 — keep going!\n\n💡 {missed['explanation']}",
                kind="danger",
                title="Not quite!",
            ))
        parts += [radio, submit]

    elif g["stage"] == "unlocked":
        mo.status.toast("🎉 HORRAAAAAAY! The AI has joined the battle!")
        start_btn = mo.ui.button(
            label="⚔️ Start AI Battle",
            kind="warn",
            disabled=battles >= MAX_BATTLES,
            on_click=lambda _: (
                set_battles(lambda n: n + 1),
                set_game(lambda s: start_battle(s)),
            ),
        )
        parts = [
            mo.md("# 🎉 HORRAAAAAAY! You got 4 correct answers in a row!"),
            mo.md("# 🤖 THE AI HAS JOINED THE BATTLE!"),
        ]
        if battles >= MAX_BATTLES:
            parts.append(mo.callout(
                "🤖 WHOA! Five champions have already challenged me! "
                "My AI brain needs a rest. Come back later!",
                kind="warn",
            ))
        else:
            parts.append(start_btn)

    elif g["stage"] == "ai_battle":
        q = g["current"]
        labels = format_labels(q["options"])
        radio = mo.ui.radio(labels, value=labels[0], label=q["q"])
        submit = mo.ui.button(
            label="Submit AI battle answer",
            kind="success",
            on_click=lambda _: set_game(lambda s: answer_battle(s, radio.value[0])),
        )
        parts = [
            mo.callout(
                f"🤖 AI BATTLE — score: **{g['ai_score']}** (a wrong answer ends the battle)",
                kind="info",
            ),
            mo.md(f"*AI question #{g['ai_score'] + 1} ({q.get('source', 'ai')})*"),
            radio,
            submit,
        ]

    else:  # gameover
        def restart_game(_):
            set_game(lambda s: new_game(s["subject"]))

        q = g["ai_explain"]
        replay_btn = mo.ui.button(
            label="🔁 Play again (same subject)", kind="success", on_click=restart_game
        )
        choose_btn = mo.ui.button(
            label="🏠 Choose subject", kind="neutral", on_click=restart_game
        )
        parts = [
            mo.md(f"# 🏆 AI Battle Score: {g['ai_score']} correct!"),
            mo.callout("❌ Not quite!", kind="danger"),
            mo.md(
                f"The correct answer was **{q['correct']}: "
                f"{option_letter_to_text(q, q['correct'])}**.\n\n"
                f"**Remember:** {q['explanation']}"
            ),
            mo.md(f"```text\n{get_illustration(q.get('concept', ''))}\n```"),
            mo.hstack([replay_btn, choose_btn], widths="equal"),
        ]

    view = mo.vstack(parts)
    view
    return


# ---------- student logic panel (was: if show_logic: st.code) ----------


@app.cell
def _(mo, show_logic):
    spec_logic = """streak = 0
while streak < 4:
    question = get_prepared_question()
    answer = get_student_answer()
    if answer == question["correct_answer"]:
        streak = streak + 1
    else:
        streak = 0   # reset!

print("AI HAS JOINED THE BATTLE!")
answer_is_correct = True
while answer_is_correct:
    question = generate_ai_question()  # AI makes Q, Python checks it
    answer = get_student_answer()
    if answer == question["correct_answer"]:
        print("Correct!")
    else:
        answer_is_correct = False
        show_explanation(question)
        show_illustration(question)"""
    logic_view = (
        mo.vstack([
            mo.md("---"),
            mo.md("## 👀 Student Python logic (from the project spec)"),
            mo.md(f"```python\n{spec_logic}\n```"),
        ])
        if show_logic.value
        else None
    )
    logic_view
    return


if __name__ == "__main__":
    app.run()
