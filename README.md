# Sudoku Project

## Description
This project is a command-line interface (CLI) based Sudoku game. It allows users to play Sudoku, manage players, and interact with the game through a CLI.

## Features
- Create and manage Sudoku tables
- Create and manage player profiles
- Play Sudoku through a CLI

## Installation
1. Clone the repository:
    ```sh
    git clone <repository-url>
    cd <repository-directory>
    ```

2. Install the required dependencies:
    ```sh
    pip install -r requirements.txt
    ```

## Usage
1. Run the game:
    ```sh
    python run.py
    ```

2. Follow the CLI prompts to interact with the game.

## Project Structure
- `run.py`: The main entry point of the application.
- `cli.py`: Contains the `Cli` class which handles the command-line interface.
- `sudoku.py`: Contains the `Sudoku` class which manages the Sudoku game logic.
- `player.py`: Contains the `Player` class which manages player profiles.

## Dependencies
- `ipdb`: Used for debugging.
- Other dependencies as listed in `requirements.txt`.

## Contributing
1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -am 'Add new feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Create a new Pull Request.

## License
This project is licensed under the MIT License. See the `LICENSE` file for details.