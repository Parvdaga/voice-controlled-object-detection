import cv2
import numpy as np
from ultralytics import YOLO
import speech_recognition as sr
import pyttsx3

# Function to detect the dominant color in a region
def detect_color(roi):
    hsv_roi = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)
    color_ranges = {
        "red": [(0, 50, 50), (10, 255, 255)],
        "blue": [(110, 50, 50), (130, 255, 255)],
        "green": [(50, 50, 50), (70, 255, 255)],
        "yellow": [(20, 50, 50), (30, 255, 255)]
    }
    color_counts = {
        color: cv2.inRange(hsv_roi, np.array(lower), np.array(upper)).sum()
        for color, (lower, upper) in color_ranges.items()
    }
    return max(color_counts, key=color_counts.get) if color_counts else None

# Speech input for query
def get_speech_input():
    recognizer = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening for object name...")
        try:
            audio = recognizer.listen(source, timeout=5)
            query = recognizer.recognize_google(audio)
            print(f"Detected Speech: {query}")
            return query
        except sr.UnknownValueError:
            print("Could not understand the audio.")
            return None
        except sr.RequestError as e:
            print(f"Error with speech recognition service: {e}")
            return None
        except sr.WaitTimeoutError:
            print("Listening timed out.")
            return None

# Parse user query
def parse_query(query):
    words = query.lower().split()
    attributes = [word for word in words if word in ["red", "blue", "green", "yellow"]]
    object_name = next((word for word in words if word not in attributes and word not in ["a", "an", "the"]), None)
    return object_name, attributes

# Initialize the text-to-speech engine
def speak(text):
    engine = pyttsx3.init()
    engine.say(text)
    engine.runAndWait()

# Load the YOLO model
model = YOLO("yolov8n.pt")

# Main function
def main():
    query = get_speech_input()
    if not query:
        print("No input detected. Exiting.")
        return

    object_name, attributes = parse_query(query)
    if not object_name:
        print("Could not parse object name from the query. Exiting.")
        return

    print(f"Looking for {object_name} with attributes {attributes}.")
    speak(f"Looking for {object_name} with attributes {', '.join(attributes)}.")

    cap = cv2.VideoCapture(0)
    if not cap.isOpened():
        print("Failed to access the camera. Exiting.")
        return

    confidence_threshold = 0.5  # Set your desired confidence threshold

    while True:
        ret, frame = cap.read()
        if not ret:
            print("Failed to read a frame. Exiting...")
            break

        results = model(frame)
        detected = False

        for detection in results[0].boxes:
            x1, y1, x2, y2 = map(int, detection.xyxy[0])  # Bounding box
            cls = int(detection.cls[0])  # Class ID
            confidence = float(detection.conf[0])  # Confidence score

            # Check if the confidence is above the threshold
            if confidence >= confidence_threshold:
                # Match class name with object_name
                detected_class = model.names[cls]
                if object_name in detected_class.lower():
                    roi = frame[y1:y2, x1:x2]
                    detected_color = detect_color(roi)

                    if detected_color in attributes:
                        message = f"Found { object_name} ({detected_color}) at ({x1}, {y1}, {x2}, {y2})."
                        print(message)
                        speak(message)  # Speak the detected object and its attributes
                        cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
                        cv2.putText(frame, f"{detected_class} ({detected_color})", (x1, y1 - 10),
                                    cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)
                        detected = True

        if not detected:
            print(f"No matching {object_name} found.")

        # Display the frame with labels
        cv2.imshow("Live Feed", frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

main()