import tkinter as tk
from tkinter import ttk, messagebox
from googletrans import Translator

# Initialize translator
translator = Translator()

# Language codes
LANGUAGES = {
    "English": "en",
    "Urdu": "ur",
    "Korean": "ko",
    "Hindi": "hi",
    "Arabic": "ar",
    "French": "fr",
    "Spanish": "es",
    "Chinese": "zh-cn"
}

# Translate function
def translate_text():
    try:
        text = input_text.get("1.0", tk.END).strip()
        if text == "":
            messagebox.showwarning("Warning", "Please enter text to translate")
            return

        src_lang = LANGUAGES[source_lang.get()]
        dest_lang = LANGUAGES[target_lang.get()]

        translated = translator.translate(text, src=src_lang, dest=dest_lang)

        output_text.delete("1.0", tk.END)
        output_text.insert(tk.END, translated.text)

    except:
        messagebox.showerror("Error", "Translation failed.\nCheck internet connection.")

# Clear text
def clear_text():
    input_text.delete("1.0", tk.END)
    output_text.delete("1.0", tk.END)

# Swap languages
def swap_languages():
    src = source_lang.get()
    tgt = target_lang.get()
    source_lang.set(tgt)
    target_lang.set(src)

# Main window
root = tk.Tk()
root.title("🌍 Smart Multilingual Translator")
root.configure(bg="#1e1e2f")

# Start maximized (Solution 2)
root.state('zoomed')
root.resizable(True, True)

# Title
tk.Label(
    root,
    text="🌐 Smart Language Translator",
    font=("Arial", 18, "bold"),
    bg="#1e1e2f",
    fg="#ffffff"
).pack(pady=12)

# Frame for language selection
lang_frame = tk.Frame(root, bg="#1e1e2f")
lang_frame.pack(pady=5)

# Source Language
tk.Label(
    lang_frame, text="Source Language",
    bg="#1e1e2f", fg="white"
).grid(row=0, column=0, padx=10)

source_lang = tk.StringVar(value="English")
ttk.Combobox(
    lang_frame,
    textvariable=source_lang,
    values=list(LANGUAGES.keys()),
    state="readonly",
    width=15
).grid(row=1, column=0, padx=10)

# Swap Button
tk.Button(
    lang_frame,
    text="⇄ Swap",
    command=swap_languages,
    bg="#ff9800",
    fg="white",
    font=("Arial", 10, "bold")
).grid(row=1, column=1, padx=10)

# Target Language
tk.Label(
    lang_frame, text="Target Language",
    bg="#1e1e2f", fg="white"
).grid(row=0, column=2, padx=10)

target_lang = tk.StringVar(value="Urdu")
ttk.Combobox(
    lang_frame,
    textvariable=target_lang,
    values=list(LANGUAGES.keys()),
    state="readonly",
    width=15
).grid(row=1, column=2, padx=10)

# Input Text
tk.Label(
    root, text="Enter Text",
    bg="#1e1e2f", fg="white"
).pack(pady=5)

input_text = tk.Text(root, height=6, width=60, font=("Arial", 11))
input_text.pack()

# Buttons Frame
btn_frame = tk.Frame(root, bg="#1e1e2f")
btn_frame.pack(pady=10)

tk.Button(
    btn_frame,
    text="Translate",
    command=translate_text,
    bg="#4CAF50",
    fg="white",
    font=("Arial", 11, "bold"),
    width=12
).grid(row=0, column=0, padx=10)

tk.Button(
    btn_frame,
    text="Clear",
    command=clear_text,
    bg="#f44336",
    fg="white",
    font=("Arial", 11, "bold"),
    width=12
).grid(row=0, column=1, padx=10)

# Output Text
tk.Label(
    root, text="Translated Text",
    bg="#1e1e2f", fg="white"
).pack(pady=5)

output_text = tk.Text(root, height=6, width=60, font=("Arial", 11))
output_text.pack()

# Footer
tk.Label(
    root,
    text="✨ AI Powered Real-Time Translator ✨",
    bg="#212131",
    fg="#9e9e9e",
    font=("Arial", 9)
).pack(pady=8)

# Run app
root.mainloop()