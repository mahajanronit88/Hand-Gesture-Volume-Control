<img width="640" height="480" alt="Hand volume control_outputs4" src="https://github.com/user-attachments/assets/e6dc4db7-7d3e-42ba-9aca-c068cbf68a71" />
<img width="640" height="480" alt="Volunme controll with hands5" src="https://github.com/user-attachments/assets/30db0649-1284-4274-9d62-f84dcf95bddb" />
# 🖐️ Hand Gesture Volume Control 

Hey! Welcome to my project. This is a super fun Python tool I built that lets you control your PC's system volume using nothing but your hand gestures. No more searching for your keyboard or adjusting the mouse slider—just use your thumb and index finger like a virtual remote control! 🚀

### How it works behind the scenes:
It uses your webcam to track your hand. The script constantly measures the distance between your **Thumb** and your **Index Finger**. 
* If you open up your hand wide (distance > 40), it triggers **Volume Up**.
* If you bring your fingers close together, it turns the **Volume Down**.

---

## 🔥 Why I Built This (Features)
* **Real-time & Responsive:** Powered by Google's MediaPipe framework for crazy-fast hand tracking.
* **Lag-Free:** I spent time optimizing the code so that it checks the distance at smart intervals. No webcam freezing or PC stuttering!
* **Pure Automation:** Uses PyAutoGUI to simulate hardware keypresses, meaning it works system-wide (on YouTube, Spotify, VLC, or anything playing in the background).

---

## 🛠️ Things You Need to Run It (Tech Stack)
Make sure you have Python installed on your machine. The main libraries used are:
* **OpenCV** (To get the live webcam feed)
* **MediaPipe** (The AI engine that finds the hand and fingers)
* **PyAutoGUI** (The tool that actually talks to your OS to change the volume)

---

## 🚀 How to Setup and Run This on Your PC

### 1. Download the code
Just download the `volume_controll.py` file from this repository into a folder on your computer.

### 2. Install the requirements
Open up your terminal or command prompt inside that folder and run this single command to install everything needed:
```bash
pip install opencv-python mediapipe pyautogui
