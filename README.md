# Asteroids (Pygame)

A simple Asteroids-style game built with [Pygame](https://www.pygame.org/).  
The player controls a triangular ship, dodges incoming asteroids, and shoots them to split or destroy them.  

---

## Requirements
- **Python 3.9+**  
- **Pygame** (`pip install pygame`)  
- (Optional) [**uv**](https://github.com/astral-sh/uv) for fast virtual environment management  

---

## Project Structure
```
.
├── main.py            # Entry point: game loop and event handling
├── constants.py       # Screen size, speeds, spawn rates, etc.
├── player.py          # Player ship class (inherits CircleShape)
├── asteroid.py        # Asteroid class and splitting logic
├── asteroidfield.py   # Spawner for new asteroids
├── shot.py            # Bullet class
└── README.md
```

---

## Running the Game

### **1. Using uv (Recommended)**
[uv](https://github.com/astral-sh/uv) provides fast virtual environment creation and dependency installation.

```bash
# Install uv if not already installed
pip install uv

# Create and activate a virtual environment
uv venv

# Activate the environment (Linux/macOS)
source .venv/bin/activate

# Or on Windows
.venv\Scripts\activate

# Install pygame inside the environment
pip install pygame

# Run the game
python main.py
```

### **2. Using Standard venv**
```bash
python -m venv .venv
source .venv/bin/activate   # or .venv\Scripts\activate on Windows
pip install pygame
python main.py
```

---

## Controls
| Key      | Action              |
|----------|-------------------|
| **W**    | Thrust forward     |
| **S**    | Thrust backward    |
| **A**    | Rotate left        |
| **D**    | Rotate right       |
| **Space**| Shoot              |
| **Esc / Close Window** | Quit |

---

## Gameplay
- Asteroids drift onto the screen from random positions.  
- Hitting an asteroid with a shot causes it to **split** or be destroyed if already small.  
- Colliding with an asteroid ends the game (**Game Over!**).  

---

## Development Notes
- Uses **`pygame.sprite.Group`** for efficient update and draw calls:
  - `updatable` for all sprites with `update()`.
  - `drawable` for all sprites with `draw()`.
  - `asteroids` and `shots` for collision checks.  
- `containers` tuples in each class automatically add new objects to the proper groups.  
- Frame timing (`dt`) is managed with `Clock.tick()` for smooth movement.  



