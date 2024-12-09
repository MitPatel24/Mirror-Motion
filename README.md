# Mirror Motion: Ball Mover Game 👋🏐🪞🏐

 
**Mirror Motion**: Ball Mover Game is an interactive application that combines computer vision and Unity to create a ball movement game. The ball's motion is controlled by real-time color tracking using a webcam, with data seamlessly transferred between Python and Unity through socket communication.

---

## 📂 **Features**  
- Interactive ball motion control via webcam.
- Real-time data transfer between Python (OpenCV) and Unity (C#). 
- Adjustable color detection using HSV values. 
- Simple setup leveraging Python libraries and socket communication.  
---


## 🚀 **Getting Started**

### **Prerequisites**   
* Ensure the following libraries are installed with the specified versions: 

    ```bash
        opencv-python==4.10.0.84  
        cvzone
        socket


### **Installation**
#### 1) Python Setup:

1. Install Python dependencies:
    ```bash
    pip install opencv-python cvzone
2. Ensure Python 3.x is installed.

#### 2) Unity Setup:

1. Install Unity Editor for developing and running the C# script.

2. Create a Unity project and integrate BallMovement.cs.

### 📋 **Usage**
#### 1) Python:
1. Open main.py and execute the script to initialize webcam-based motion detection.
2. Adjust HSV values in main.py under the hsvVals dictionary to match your desired tracking color.
#### 2) Unity:
1. Load the Unity project and integrate the BallMovement.cs script.
2. Start the Unity game to observe ball movement controlled by the Python program.

#### Termination
* Press m in the Python script to exit the program.

## **Contributors**
- Mitkumar Patel -  [MitPatel24](https://github.com/MitPatel24)
