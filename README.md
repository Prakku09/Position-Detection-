# Human Pose Detection using MediaPipe

A real-time **Human Pose Detection** project built using **Python, OpenCV, and MediaPipe**.

The project uses the computer's **webcam to capture live video frames**. OpenCV handles the webcam feed and converts each frame into the required format, while MediaPipe Pose detects the key landmarks of the human body, such as the **head, shoulders, elbows, wrists, hips, knees, and ankles**.

The detected landmarks are then connected to form a **human body skeleton**, which is displayed directly on the live webcam feed. This allows the system to track body movements in real time.

### Technologies Used

* Python 3.11
* OpenCV
* MediaPipe
* NumPy

### How It Works

**Webcam → OpenCV → RGB Conversion → MediaPipe Pose Detection → Landmark Detection → Skeleton Visualization**

The program can be used as a basic foundation for applications such as **fitness tracking, gesture recognition, sports analysis, and human-computer interaction**.

### Run

```bash
py pose_detection.py
```

Press **Q** to stop the webcam and exit the program.
