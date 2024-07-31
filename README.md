# Gesture-Controlled-Application-Launcher


# Objective


This innovative system leverages the power of MediaPipe and OpenCV to recognize hand gestures and use them to open and control various applications. By integrating machine learning and computer vision techniques, it interprets specific hand gestures captured through a webcam and translates them into commands to open web pages or desktop applications.

# Key Features:

Real-Time Hand Gesture Recognition: Utilizes MediaPipe's state-of-the-art hand tracking capabilities to detect and interpret hand gestures in real time.

Customizable Application Launcher: Maps specific hand gestures to different web pages or desktop applications, making it a versatile tool for various use cases.

Smooth User Experience: Ensures a seamless interaction with a user-friendly interface and quick response time.

# Technical Highlights:

MediaPipe Hands: Employs the robust hand detection and tracking solution from MediaPipe, allowing for accurate recognition of hand gestures.

OpenCV: Integrates with OpenCV to process webcam feed and overlay gesture recognition data on the video stream.

Web Integration: Uses Python's webbrowser module to open web applications based on recognized gestures.


# How It Works:

Hand Detection: Captures video feed from the webcam and processes it to detect hands using MediaPipe.

Gesture Recognition: Analyzes hand landmarks to determine the number of fingers extended and maps it to a predefined action.

Application Launch: Opens the corresponding web page or application when a recognized gesture is detected.
