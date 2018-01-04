# Tron-Simulator

Simulator of an old Arcade game in Python.

## Rules of game

The more points you get, the better!

* Every orange box is 5 points.
* Every grey box is Crossover. Each of them lets you go once throw the enemy.
It resets every round.
* Every time you cross the enemy, yourself or the wall
all of the players except you get 10 points.

There are following control keys:
* Player 1:
    ```
    Up Down Left Right
    ```
* Player 2:
    ```
    W S A D
    ```
* Player 3:
    ```
    F V C B
    ```
* Player 4:
    ```
    i k j l
    ```

## Getting Started

### Prerequisites

Python with "pygames" library needs to be installed.
You can change the number of players by setting the variable in params.py:
```
NUMBER_OF_PLAYERS
```

### Installing

To install simply download the project from github.

### Running

To run use command in the project directory:
```
python main.py
```

## Authors

* **Dawid Pyczek**

## License

This project is licensed under the MIT License.
