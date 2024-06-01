**Hand Tracking and Gesture Control**

This project uses OpenCV, MediaPipe, and PyAutoGUI to implement hand tracking and gesture control functionalities. The program captures video from the webcam, detects hand landmarks, and recognizes gestures to control the mouse pointer on the screen.

**Features**

1)Hand Detection: Utilizes MediaPipe's Hand solution to detect hand landmarks.<br>
2)Gesture Recognition: Identifies gestures such as finger positions and distances between fingers.<br>
3)Mouse Control: Controls mouse movement and clicking actions based on hand gestures.

**Requirements**

Python 3.x <br>
OpenCV<br>
MediaPipe<br>
PyAutoGUI<br>
NumPy<br>

**Installation:<br>
Install the required packages:**
```python
pip install opencv-python mediapipe pyautogui numpy
```

**Usage**:<br>
**Run the hand tracking module:**<br>
`python handTrackingModule.py`

**Run the main script to start the gesture control:**<br>
`python main.py`

-->**Project Structure**<br>
`handTrackingModule.py`: Contains the `handDetector` class for hand tracking and gesture recognition.<br>
`main.py`: Main script that captures video from the webcam and controls the mouse pointer based on detected gestures.

**`handDetector`** Class<br>
The `handDetector` class provides the following methods:

`findHands(img, draw=True)`: Detects hands in the given image and optionally draws landmarks.<br>
`findPosition(img, handNo=0, draw=True)`: Finds the position of hand landmarks and optionally draws them.<br>
`fingersUp()`: Returns a list indicating which fingers are up.<br>

-->**How It Works**

**Hand Detection**: The `findHands` method processes the image to detect hand landmarks.<br>
**Position Calculation**: The `findPosition` method calculates the positions of the landmarks.<br>
**Gesture Recognition**: The `fingersUp` method determines which fingers are up.<br>
**Mouse Control**: Based on the gesture (e.g., index finger up for moving, both index and middle fingers up for clicking), the mouse pointer is moved or clicked using PyAutoGUI.<br>

-->**Customization**

**Frame Reduction**: Adjust the `frameR` variable to set the region within which hand movements are tracked.<br>
**Smoothening**: Modify the `smoothening` variable to change the smoothening factor for mouse movement.<br>
**Detection and Tracking Confidence**: Change `detectionCon` and `trackCon` values in the `handDetector` class initialization to adjust the confidence levels for detection and tracking.<br>

-->**Troubleshooting**

Ensure the webcam is properly connected and accessible.<br>
Check if the required libraries are installed correctly.<br>
If the captured image is empty or the program fails to capture an image, verify the webcam setup.<br>
findDistance(p1, p2, img, draw=True, r=15, t=3): Finds the distance between two points and optionally draws the line and circles on the image.<br>
