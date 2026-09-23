# Pygame Dino Game

A Dino-style game developed using Python and Pygame. The player controls a dinosaur, jumps over cactus obstacles, and tries to avoid collisions.

## Table Of Contents

* [Table Of Contents](#table-of-contents)
* [Features](#features)
* [Project Structure](#project-structure)
* [Requirement](#requirement)
* [Installation](#installation)
* [Environment Setup](#environment-setup)
* [Usage](#usage)
* [Example Output](#example-output)

## Features

* Dino jumping
* Cactus obstacles
* Moving obstacles
* Collision detection
* Timer
* Game Over system
* Jump sound
* Background music

## Project Structure

```text
pygame-dino-game/

│   main.py
│   dino.png
│   Cactus.webp
│   music.mp3
│   jump.mp3
│   README.md
```

### File Description

* `main.py` - main file used to run the Dino game
* `dino.png` - image used for the dinosaur
* `Cactus.webp` - image used for the cactus obstacle
* `music.mp3` - background music
* `jump.mp3` - sound played when the dinosaur jumps
* `README.md` - contains the project documentation

## Requirement

Before running the project, make sure you have:

* `Python 3`
* `Pygame`

## Installation

1. Open a terminal in the project folder.

2. Check that Python is installed:

```bash
python --version
```

3. Install Pygame:

```bash
pip install pygame
```

## Environment Setup

No environment variables are required for this project.

## Usage

1. Open a terminal in the project folder.
2. Run the game:

```bash
python main.py
```

3. Press `Space` to make the dinosaur jump.
4. Avoid the cactus obstacles.
5. The game ends when the dinosaur collides with a cactus.

## Example Output

```text
Pygame Dino Game

A game window opens with:
- A dinosaur
- Cactus obstacles
- A timer
- Background music

Press Space to jump.
If the dinosaur hits a cactus, "Game Over" is displayed.
```
