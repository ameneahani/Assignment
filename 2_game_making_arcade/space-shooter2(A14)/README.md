# 🚀 Spaceships War  

A **2D arcade-style space shooter game** built with [Python Arcade](https://api.arcade.academy/).  
Control your spaceship, shoot enemies, survive as long as possible, and keep your hearts alive!  

---

## 🎮 Features
- Move spaceship left/right using **arrow keys (← →)**  
- Shoot bullets with **SPACE key**  
- Enemies spawn every 3 seconds and move down the screen  
- Health system with **3 hearts**  
- **Score system**: +1 for each enemy destroyed  
- Explosion sound effects  
- Game Over screen (auto-exits after 3 seconds)  

---


## 📂 Project Structure
.
├── main.py # Main game loop
├── spaceship.py # Spaceship class
├── enemy.py # Enemy class
├── bullet.py # Bullet class
├── heart.py # Heart (life/health) class
├── gameover.png # Game Over screen image

yaml
Copy code

---

## ▶️ How to Run
1. Install [Python 3.x](https://www.python.org/downloads/).  
2. Install the **arcade** library:  
   ```bash
   pip install arcade
Run the game:

bash
Copy code
python main.py
📝 Controls
← / → : Move spaceship

SPACE : Fire bullets

🔮 Possible Improvements
Add multiple types of enemies

Add power-ups (extra hearts, faster bullets, etc.)

Add levels or waves of difficulty

Save high scores