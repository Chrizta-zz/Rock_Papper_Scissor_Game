🎮 Rock Paper Scissors Game Using Hand Tracking

📌 Description

This project is a computer vision-based implementation of the classic Rock Paper Scissors game. Instead of using traditional inputs, players use hand gestures captured through a webcam to play against an AI opponent.

The project utilizes OpenCV, MediaPipe, and CVZone to detect and recognize hand gestures in real time. The system identifies Rock, Paper, and Scissors gestures, generates a random move for the computer, determines the winner, and updates the scores automatically.



🚀 Features

* Real-time hand gesture recognition
* Rock, Paper, and Scissors detection
* AI-generated opponent moves
* Automatic score calculation
* Countdown timer before each round
* Interactive graphical user interface
* Live score display



🛠 Technologies Used

* Python
* OpenCV
* MediaPipe
* CVZone



 📂 Project Structure
 
Rock_Paper_Scissors/
│
├── Resources/
│   ├── BG.png
│   ├── 1.png
│   ├── 2.png
│   └── 3.png
│
├── main.py
└── README.md




 ▶️ How to Run

Install Required Libraries


pip install opencv-python
pip install cvzone
pip install mediapipe


Run the Project

python main.py




 🎯 Game Controls

* Press **S** to start a round.
* Show one of the following gestures:

  * ✊ Rock
  * ✋ Paper
  * ✌️ Scissors
* Wait for the countdown to finish.
* The computer generates a move automatically.
* Scores are updated based on the winner.



📖 Working Principle

1. Webcam captures the player's hand.
2. Hand landmarks are detected using MediaPipe.
3. Finger positions are analyzed to identify the gesture.
4. The computer randomly selects Rock, Paper, or Scissors.
5. The game compares both moves.
6. The winner is determined and scores are updated. 



🌟 Future Improvements

* Multiplayer mode
* Sound effects and animations
* Improved gesture recognition
* Game history and statistics
* Difficulty levels



Author

Christa Eldo
