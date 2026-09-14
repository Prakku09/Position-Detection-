
import cv2
import mediapipe as mp
import time

# Initialize MediaPipe Pose
mp_pose = mp.solutions.pose
mp_draw = mp.solutions.drawing_utils

pose = mp_pose.Pose(
    static_image_mode=False,
    model_complexity=1,
    smooth_landmarks=True,
    min_detection_confidence=0.5,
    min_tracking_confidence=0.5
)

# Open webcam
cap = cv2.VideoCapture(0)

if not cap.isOpened():
    print("Error: Could not open webcam.")
    exit()

print("Pose Detection Started")
print("Press Q to exit")

# FPS variables
previous_time = 0

while True:

    # Capture frame
    success, frame = cap.read()

    if not success:
        print("Failed to read webcam frame.")
        break

    # Flip frame for mirror view
    frame = cv2.flip(frame, 1)

    # Convert BGR to RGB
    rgb_frame = cv2.cvtColor(
        frame,
        cv2.COLOR_BGR2RGB
    )

    # Detect pose
    results = pose.process(rgb_frame)

    # Check if pose is detected
    if results.pose_landmarks:

        mp_draw.draw_landmarks(
            frame,
            results.pose_landmarks,
            mp_pose.POSE_CONNECTIONS
        )

        cv2.putText(
            frame,
            "Pose Detected",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 255, 0),
            2
        )

    else:

        cv2.putText(
            frame,
            "No Pose Detected",
            (20, 40),
            cv2.FONT_HERSHEY_SIMPLEX,
            1,
            (0, 0, 255),
            2
        )

    # Calculate FPS
    current_time = time.time()

    fps = 1 / (current_time - previous_time) if previous_time != 0 else 0

    previous_time = current_time

    # Display FPS
    cv2.putText(
        frame,
        f"FPS: {int(fps)}",
        (20, 80),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.8,
        (255, 255, 0),
        2
    )

    # Display webcam
    cv2.imshow(
        "MediaPipe Pose Detection",
        frame
    )

    # Press Q to exit
    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

# Release resources
cap.release()
pose.close()
cv2.destroyAllWindows()

print("Pose Detection Stopped")
