import tkinter as tk
from tkinter import filedialog, scrolledtext
from PIL import Image, ImageTk
from playsound import playsound
import threading
import os

# --- Command Functions ---

def send_text():
    """Sends a text message and clears the entry box."""
    msg = text_entry.get()
    if msg:
        # Insert the message into the chat box
        chat_box.insert(tk.END, f"You: {msg}\n") [cite: 31]
        text_entry.delete(0, tk.END) [cite: 32]
        chat_box.yview(tk.END) # Scroll to the bottom

def send_image():
    """Opens a file dialog, inserts path, and displays a thumbnail of the image."""
    path = filedialog.askopenfilename(filetypes=[("Image Files", "*.jpg *.png *.jpeg")]) [cite: 35]
    if path:
        chat_box.insert(tk.END, f"You sent an image: {path}\n") [cite: 36]
        
        try:
            img = Image.open(path) [cite: 37]
            img.thumbnail((100, 100)) # Resize for thumbnail display [cite: 38]
            img_tk = ImageTk.PhotoImage(img) [cite: 39]
            
            # Use a Label to display the image inside the chat frame
            # The label is packed, but since the ScrolledText is packed, this is complex.
            # A simpler approach for demonstration is to pack directly into the chat_frame
            image_label = tk.Label(chat_frame, image=img_tk) [cite: 40]
            image_label.image = img_tk # Keep a reference to prevent garbage collection [cite: 41]
            image_label.pack() [cite: 42]
            
            # The manual's implementation of mixing a ScrolledText (which is a Text widget)
            # with packed Labels inside a parent frame is tricky for scrolling and layout.
            # For simplicity, this follows the structure provided, but in a real app,
            # you'd use the Text widget's `image_create` method for true in-line images.
            
            chat_box.yview(tk.END) [cite: 43] # Scroll to the bottom
            
        except Exception as e:
            chat_box.insert(tk.END, f"Error displaying image: {e}\n")

def play_audio_file(path):
    """Function to be run in a separate thread to play audio."""
    if not os.path.exists(path):
        print(f"Error: Audio file not found at {path}")
        return
    try:
        playsound(path)
        print(f"Finished playing: {path}")
    except Exception as e:
        print(f"Audio playback error: {e}")

def send_audio():
    """Opens a file dialog, inserts path, and starts audio playback in a thread."""
    path = filedialog.askopenfilename(filetypes=[("Audio Files", "*.mp3 *.wav")]) [cite: 45]
    if path:
        chat_box.insert(tk.END, f"You sent an audio message: {path}\n") [cite: 46]
        chat_box.yview(tk.END)
        # Play the audio in a new thread [cite: 47]
        threading.Thread(target=lambda: play_audio_file(path), daemon=True).start()

# --- GUI Setup ---
window = tk.Tk()
window.title("Multimedia Messaging App") [cite: 51]
window.geometry("400x500") [cite: 52]

# Frame to hold the chat box
chat_frame = tk.Frame(window) [cite: 53]

# Scrollable Text widget for chat history
chat_box = scrolledtext.ScrolledText(chat_frame, wrap=tk.WORD, width=50, height=20) [cite: 55, 56]
chat_box.pack(padx=5, pady=5) [cite: 57]
chat_frame.pack(pady=10) [cite: 58]

# Text Entry for sending text messages
text_entry = tk.Entry(window, width=30) [cite: 59]
text_entry.pack(side=tk.LEFT, padx=5)

# Buttons
btn_text = tk.Button(window, text="Send Text", command=send_text) [cite: 60]
btn_image = tk.Button(window, text="Send Image", command=send_image) [cite: 60]
btn_audio = tk.Button(window, text="Send Audio", command=send_audio) [cite: 60]

btn_text.pack(side=tk.LEFT)
btn_image.pack(side=tk.LEFT) [cite: 61]
btn_audio.pack(side=tk.LEFT) [cite: 61]

window.mainloop()
