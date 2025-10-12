import tkinter as tk
import cv2
import threading

# Note: The original manual uses 'sounddevice' (sd) and 'scipy.io.wavfile.write' (write) 
# for audio. You may need to install these libraries: 
# pip install sounddevice numpy scipy
# For simplicity and to match the manual, the code assumes these are installed.
try:
    import sounddevice as sd
    from scipy.io.wavfile import write
except ImportError:
    print("Warning: 'sounddevice' and/or 'scipy' not found. Audio functions will not work.")
    sd = None
    write = None

# --- Audio Recording Function ---

def record_audio():
    """Records audio from the microphone and saves it as a WAV file."""
    if sd is None or write is None:
        print("Audio recording failed. Missing 'sounddevice' or 'scipy'.")
        return
        
    duration = 5  # seconds [cite: 781]
    fs = 44100    # sampling rate [cite: 782]
    
    print("Recording Audio...")
    try:
        # 2 channels for stereo, adjust if needed
        audio = sd.rec(int(duration * fs), samplerate=fs, channels=2, dtype='float64') 
        sd.wait() # Wait until recording is finished [cite: 786]
        write('recorded_audio.wav', fs, audio) # Save as WAV file [cite: 787]
        print("Audio recording saved to 'recorded_audio.wav'.")
    except Exception as e:
        print(f"An error occurred during audio recording: {e}")

# --- Video Capture Function ---

def capture_video():
    """Captures live video from the webcam and displays it."""
    # 0 typically refers to the default camera
    cap = cv2.VideoCapture(0) [cite: 791]
    
    if not cap.isOpened():
        print("Error: Could not open webcam.")
        return

    cv2.namedWindow('Webcam Feed', cv2.WINDOW_AUTOSIZE)
    print("Press 'q' to stop video.") [cite: 792]
    
    while True:
        ret, frame = cap.read() [cite: 794]
        
        if not ret:
            print("Error: Could not read frame from webcam.") [cite: 795]
            break
            
        cv2.imshow('Webcam Feed', frame) [cite: 800]
        
        # Break the loop if 'q' is pressed [cite: 801]
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
            
    cap.release() [cite: 803]
    cv2.destroyAllWindows() [cite: 804]
    print("Webcam feed stopped.")

# --- GUI Setup ---

window = tk.Tk()
window.title("Capture Audio and Video") [cite: 807]

# Buttons, using threading to prevent the GUI from freezing 
btn_audio = tk.Button(window, text="Record Audio (5s)", 
                      command=lambda: threading.Thread(target=record_audio, daemon=True).start())
                      
btn_video = tk.Button(window, text="Start Webcam (Press 'q' to stop)", 
                      command=lambda: threading.Thread(target=capture_video, daemon=True).start())

btn_audio.pack(pady=10) [cite: 811]
btn_video.pack(pady=10) [cite: 812]

window.mainloop()
