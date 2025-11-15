# Simple Snake Game (Python + Arcade)

A basic but fun implementation of the classic Snake game built using Python and the [Arcade](https://arcade.academy/) library.

---

## Features

- Move the snake using the arrow keys (`↑`, `↓`, `←`, `→`).
- Eat different items:
  - **Apple**: +1 score
  - **Pear**: +2 score
  - **Shit**: −1 score (if score drops to zero, game over)
- Game over when:
  - Snake hits the window boundaries
  - Score falls to zero (due to consuming the negative item)
- Displays a game over image (`gameover.png`) for 3 seconds before exiting automatically.

---

## Installation & Setup

1. **Install Arcade**  
   ```bash
   pip install arcade
Clone the repository

bash
Copy code
git clone https://github.com/yourusername/your-repo-name.git
cd your-repo-name
Run the game

bash
Copy code
python main.py
Project Structure
bash
Copy code
├── main.py             # Contains the Game class and main loop
├── snake.py            # Snake class and movement logic
├── apple.py            # Apple item class
├── pear.py             # Pear item class
├── shit.py             # Negative item class (reduces score)
├── gameover.png        # Image shown when the game ends
└──