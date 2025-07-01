# Voice-Controlled Object Detection System

A real-time computer vision application that combines YOLO object detection with voice commands and text-to-speech feedback. Simply speak the name and color of an object you're looking for, and the system will detect and highlight it in the live camera feed.

## 🎯 Features

- **Voice Command Input**: Speak naturally to specify what object you're looking for
- **Real-time Object Detection**: Uses YOLOv8 for accurate object recognition
- **Color Detection**: Identifies dominant colors (red, blue, green, yellow) in detected objects
- **Audio Feedback**: Announces when matching objects are found
- **Live Video Feed**: Real-time camera processing with visual overlays
- **Intelligent Matching**: Combines object type and color attributes for precise detection

## 🛠️ Technology Stack

- **Computer Vision**: OpenCV, YOLOv8 (Ultralytics)
- **Speech Recognition**: Google Speech Recognition API
- **Text-to-Speech**: pyttsx3
- **Image Processing**: NumPy
- **Programming Language**: Python 3.7+

## 📋 Prerequisites

- Python 3.7 or higher
- Webcam/Camera device
- Microphone for voice input
- Internet connection (for speech recognition)

## 🚀 Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/yourusername/voice-controlled-object-detection.git
   cd voice-controlled-object-detection
   ```

2. **Create a virtual environment (recommended)**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install required packages**
   ```bash
   pip install -r requirements.txt
   ```

4. **Download YOLO model (automatic on first run)**
   The YOLOv8n model will be downloaded automatically when you first run the application.

## 📦 Dependencies

```
opencv-python>=4.5.0
ultralytics>=8.0.0
speechrecognition>=3.8.0
pyttsx3>=2.90
numpy>=1.21.0
pyaudio>=0.2.11
```

## 🎮 Usage

1. **Run the application**
   ```bash
   python main.py
   ```

2. **Give voice commands**
   - Speak clearly into your microphone
   - Use format: "[color] [object]" (e.g., "red apple", "blue bottle")
   - Supported colors: red, blue, green, yellow
   - Wait for the "Listening..." prompt

3. **View results**
   - The camera feed will display with detected objects highlighted
   - Audio feedback will announce when matching objects are found
   - Press 'q' to quit the application

## 💡 Example Commands

- "red apple" - Detects red-colored apples
- "blue bottle" - Finds blue bottles
- "green book" - Looks for green books
- "yellow banana" - Identifies yellow bananas

## 🔧 Configuration

You can modify these parameters in the code:

- **Confidence Threshold**: Adjust `confidence_threshold` (default: 0.5)
- **Color Ranges**: Modify HSV ranges in `color_ranges` dictionary
- **Timeout**: Change speech recognition timeout (default: 5 seconds)

## 📁 Project Structure

```
voice-controlled-object-detection/
├── main.py                 # Main application file
├── requirements.txt        # Python dependencies
├── README.md              # Project documentation
├── LICENSE                # License file
├── .gitignore            # Git ignore rules
└── assets/               # Screenshots and demo files
    └── demo.gif          # Demo GIF (if available)
```

## 🎯 How It Works

1. **Voice Input**: Captures audio through microphone using speech recognition
2. **Query Parsing**: Extracts object name and color attributes from speech
3. **Object Detection**: Uses YOLOv8 to detect objects in real-time video
4. **Color Analysis**: Analyzes dominant colors in detected object regions
5. **Matching**: Compares detected objects with user query
6. **Feedback**: Provides visual highlighting and audio confirmation

## 🚨 Troubleshooting

**Camera Issues**
- Ensure your camera is not being used by another application
- Try changing the camera index in `cv2.VideoCapture(0)` to 1 or 2

**Speech Recognition Problems**
- Check your microphone permissions
- Ensure stable internet connection
- Speak clearly and avoid background noise

**Audio Output Issues**
- Verify your speakers/headphones are working
- Check system audio settings

## 🔮 Future Enhancements

- [ ] Support for more colors and custom color ranges
- [ ] Integration with additional object detection models
- [ ] Mobile app version
- [ ] Object tracking capabilities
- [ ] Multiple language support
- [ ] Custom object training
- [ ] Database logging of detections

## 🤝 Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👨‍💻 Author

Your Name - [@yourusername](https://github.com/yourusername)

## 🙏 Acknowledgments

- [Ultralytics](https://github.com/ultralytics/ultralytics) for YOLOv8
- [OpenCV](https://opencv.org/) for computer vision capabilities
- [SpeechRecognition](https://pypi.org/project/SpeechRecognition/) library
- [pyttsx3](https://pypi.org/project/pyttsx3/) for text-to-speech

## 📊 Performance

- **Detection Speed**: ~30 FPS on modern hardware
- **Accuracy**: Depends on YOLO model and lighting conditions
- **Supported Objects**: 80+ COCO dataset classes

---

⭐ **Star this repository if you found it helpful!**
