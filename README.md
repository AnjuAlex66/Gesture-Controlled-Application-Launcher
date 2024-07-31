# Gesture-Controlled-Application-Launcher


# Objective


This project captures hand gestures via a webcam, interprets them using MediaPipe's advanced hand-tracking capabilities, and translates these gestures into commands to launch web pages or desktop applications. 

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
