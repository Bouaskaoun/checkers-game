<p align="center">
  <a href="https://github.com/Bouaskaoun">
    <img src="assets/chinese-checkers-256.png" alt="Logo" width=72 height=72>
  </a>

  <h3 align="center">Logo</h3>

  <p align="center">
    Checkers Game AI Built Using Pygame
    <br>
  </p>
</p>


## Using It
Play by selecting your piece and clicking on the tile you want to move to. Click [here](https://www.wikihow.com/Play-Checkers#Checkers-Rules-and-Gameplay) to learn how to play checkers.

1. Implemented a basic Minimax Agent with limited depth.

<table>
    <tr>
        <td><img src="assets/welcome__screen.png" alt="welcome"></td>
    </tr>
    <tr>
        <td><img src="assets/board__screen.png" alt="board"></td>
    </tr>
</table>

## Evaluation Functions

The evaluation functions have been used:
```
f(x) = white_left - red_left + (white_kings * 0.5 - red_kings * 0.5)
```

## How to run the code

Step 1: Check for Python Installation
```
python --version
```
Step 2: Check for PIP installation 
```
pip --version
```
Step 3: Install Pygame
```
pip install pygame
```

### Run the Game

```bash
python3 main.py
```

## Conclusion

1. Heuristics can be drastically improved by adding specific features.
2. The depth of the game tree has a significant influence on the quality of the computer player.
3. There's a tradeoff between calculation time and quality of the game.
4. It is not efficient to use Minimax without optimizations while with them it can be a good solution.
5. Alpha-Beta pruning is exponentially improving in comparison to Minimax as the depth grows.
6. Certain heuristics are clearly better than others but some of the “bad” ones still work well in some cases.


Enjoy :metal:

