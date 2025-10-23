# Python Learning Repository

A personal repository to learn Python from basics to advanced topics, plus small projects to practice concepts.

## 📂 Folder Overview

- 01_datatypes — Numbers, strings, tuples, lists, sets, dicts, operator overloading
- 02_conditionals — If/elif/else mini-projects
- 03_loops — For/while, enumerate, break/continue, for-else, walrus operator
- 04_functions — Function basics, scopes, parameters/returns, traceability
- 05_chai_business — A small app to practice modules and structure
- 06_comprehensions — List/Set/Dict comprehensions, generator expressions
- 07_generator — Generators, send/close, infinite generators
- 08_decorator — Basics, logging and auth decorators
- 09_oop — Classes, inheritance vs composition, static/class methods, properties
- 10_exception_handling — Try/except patterns, custom exceptions, file handling
- 11_thread_consurrency — Threads, multiprocessing, GIL, locks, queues
- 12_asyncIO — asyncio basics, tasks, thread/process interop, race/deadlocks
- 13_pydantic — BaseModel, validation, nested models, serialization
- 14_projects — Small, self-contained practice projects
- 15_foundation_of_GenAI — Foundations of Generative AI: tokenization, Google GenAI, prompting, examples (see requirements.txt)
- JARVIS — AI/voice assistant prototype (see `JARVIS/main.py`, `voice/`, `ai/`, `system/`)

## 🗂 Project Descriptions (14_projects)

- 01_dice_roll — Random dice roller
- 02_number_guessing — Guess-the-number game
- 03_rock_paper_scissor — Play rock-paper-scissors vs the computer
- 04_qr_code_generator — Generate QR codes from text/links
- 05_currency_converter — Convert between USD/EUR/CAD (static rates)
- 06_to-do_list — Simple CLI to-do tracker
- 07_simple_text_editor — Minimal file-based editor
- 08_password_checker — Password strength feedback
- 09_ATM_simulation — ATM-like CLI operations
- 10_whatsapp_message_sender — Schedule/send a WhatsApp Web message using pywhatkit

## 🚀 Run a Script (Windows cmd)

```cmd
python path\to\file.py
```

Example:

```cmd
python 14_projects\03_rock_paper_scissor\main.py
```

## ✅ Notes

- Python version: any recent 3.x
- Recommended VS Code extensions: Python (Microsoft), Pylance

## JARVIS — AI Voice Assistant (overview)

An always-on assistant that listens via microphone, understands your voice, and performs actions through intent handling. Entry point: `JARVIS/main.py`.

### What it does

- Greets you and listens continuously
- Converts your speech to text (SpeechRecognition + PyAudio)
- Routes the text to an intent handler (`ai/intent_handler.py`)
- Speaks responses back to you (pyttsx3)
- Stops when you say "exit" or "stop"

### Folder structure

- `JARVIS/main.py` — main loop: listen → handle intent → speak
- `JARVIS/voice/` — speech I/O (e.g., `listen.py`, `speak.py`)
- `JARVIS/ai/` — intent processing (e.g., `intent_handler.py`)
- `JARVIS/system/` — system-level helpers (window control, etc.)

### Dependencies

Declared in `JARVIS/requirements.txt`:

- speechrecognition, pyttsx3, pyaudio
- pygetwindow, pyautogui
- openai
- pywin32 (Windows)

### How to run (Windows cmd)

```cmd
pip install -r JARVIS\requirements.txt
python JARVIS\main.py
```

Tips:

- Ensure your microphone is available and selected as default input
- First run may prompt permissions for microphone access
- Say "exit" or "stop" to quit
