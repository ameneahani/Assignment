Image Processing Projects (Python & OpenCV)

This repository contains a collection of simple image processing projects built using Python, OpenCV, NumPy, and ImageIO.
Each script demonstrates a different concept related to images, animations, and real-time processing.

📌 Projects Included
1. Batman Image Filtering

Loads an image and converts it to grayscale

Applies binary thresholding

Adds text (“BATMAN”)

Displays the processed result

2. Random Noise GIF Generator

Generates random noise frames

Displays them live

Press Q to stop

Saves all generated frames as output.gif

3. Falling Snow Animation

Loads a winter background image

Simulates falling snow using multithreading

Renders and displays animation in real time

Press Q to stop

Saves frames as winter.gif

4. Real-Time Color Detection (Webcam)

Captures video from the webcam

Converts frames to grayscale

Applies Gaussian blur

Extracts a central region of interest (ROI)

Detects whether dominant pixels are black, gray, or white

Displays the detection result live

🛠 Requirements

Install dependencies:

pip install opencv-python numpy imageio

▶️ How to Run
python filename.py


Some scripts require images such as batman.png and winter2.png in the project directory.