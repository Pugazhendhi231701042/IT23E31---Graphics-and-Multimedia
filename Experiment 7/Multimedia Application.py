import tkinter as tk
from PIL import Image, ImageTk
from playsound import playsound
import cv2
import threading
import os # For checking if files exist

# --- Configuration: Replace these file paths with your own ---
# Ensure these files are in the same directory as your Python script
IMAGE_FILE = 'sample_image.jpg' 
AUDIO_FILE = 'sample_audio.mp3'
VIDEO_FILE = 'sample_video.mp4'

# --- Media Functions ---

def play_audio():
    """Plays an audio file in a separate thread."""
    if not os.path.exists(AUDIO_FILE):
        print(f"Error: Audio file not found at {AUDIO_FILE}")
        return
    try:
        print(f"Playing audio: {AUDIO_FILE}")
        playsound(AUDIO_FILE)
    except Exception as e:
        print(f"Audio playback error: {e}")

def play_video():
    """Plays a video file using OpenCV in a separate thread/window."""
    if not os.path.exists(VIDEO_FILE):
        print(f"Error: Video file not found at {VIDEO_FILE}")
        return
        
    cap = cv2.VideoCapture(VIDEO_FILE)
    if not cap.isOpened():
        print(f"Error: Could not open video file {VIDEO_FILE}")
        return
        
    cv2.namedWindow("Video Player", cv2.WINDOW_AUTOSIZE)
    
    print(f"Playing video: {VIDEO_FILE}. Press 'q' to stop.")
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break
        
        cv2.imshow("Video Player", frame)
        
        # Wait 25ms, check for 'q' key press
        if cv2.waitKey(25) & 0xFF == ord('q'):
            break
    
    cap.release()
    cv2.destroyAllWindows()
    print("Video playback stopped.")

def load_image():
    """Loads and displays an image in the tkinter Label widget."""
    if not os.path.exists(IMAGE_FILE):
        panel.configure(text=f"Error: Image file not found at {IMAGE_FILE}")
        return
        
    try:
        img = Image.open(IMAGE_FILE)
        # Resize image for display
        img = img.resize((300, 300), Image.Resampling.LANCZOS)
        img_tk = ImageTk.PhotoImage(img)
        
        # Update the Label
        panel.configure(image=img_tk)
        panel.image = img_tk # Keep a reference!
        panel.configure(text="") # Clear any error text
        print(f"Image loaded: {IMAGE_FILE}")
    except Exception as e:
        panel.configure(text=f"Error loading image: {e}")

# --- GUI Setup ---
window = tk.Tk()
window.title("Multimedia App")

# Image Display Panel (Label)
panel = tk.Label(window, text="Press 'Show Image' to load image", width=40, height=15, relief="groove")
panel.pack(pady=10, padx=10)

# Buttons
btn_img = tk.Button(window, text="Show Image", command=load_image)
# Audio and Video are run in a thread to prevent freezing the GUI
btn_audio = tk.Button(window, text="Play Audio", 
                      command=lambda: threading.Thread(target=play_audio, daemon=True).start())
btn_video = tk.Button(window, text="Play Video", 
                      command=lambda: threading.Thread(target=play_video, daemon=True).start())

btn_img.pack(pady=5)
btn_audio.pack(pady=5)
btn_video.pack(pady=5)

window.mainloop()
