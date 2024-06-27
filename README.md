# Inactivity Logger and Auto-Logout

## Overview

This Python script monitors user activity (keyboard and mouse) and logs out the user after a specified period of inactivity. It shows a warning message before logging out.

## Features

- Monitors keyboard and mouse activity.
- Warns the user with a popup message 2 minutes before logging out.
- Logs out the user after 15 minutes of inactivity.

## Requirements

- Python 3.x
- `pynput` library
- `tkinter` library (included with Python standard library)

## Installation

1. **Clone the Repository:**

    ```sh
    git clone https://github.com/csusbMLC/idleChecker.git
    cd idleChecker
    ```

2. **Install the Required Libraries:**

    ```sh
    pip install -r requirements.txt
    ```

3. **Convert the Script to an Executable Using PyInstaller:**

    ```sh
    pyinstaller --onefile --noconsole your_script_name.py
    ```

## Usage

1. **Run the Executable:**

    - For Windows:
        ```sh
        your_script_name.exe
        ```

    - For Linux:
        ```sh
        ./your_script_name
        ```

2. **Behavior:**

    - The script will run in the background, monitoring keyboard and mouse activity.
    - If no activity is detected for 13 minutes, a warning popup will appear.
    - If no activity is detected for 15 minutes, the user will be logged out.

## Script Details

- **Idle Threshold:** 15 minutes
- **Warning Threshold:** 13 minutes

### Functions

- `on_activity()`: Updates the last activity time and resets the warning flag.
- `on_press(key)`: Detects keyboard press and calls `on_activity()`.
- `on_move(x, y)`: Detects mouse movement and calls `on_activity()`.
- `on_click(x, y, button, pressed)`: Detects mouse clicks and calls `on_activity()`.
- `show_warning_popup()`: Displays a warning message using Tkinter.
- `log_out_user()`: Logs out the user (different commands for Windows and Linux).
- `check_idle()`: Continuously checks for user inactivity and takes appropriate actions.

## Notes

- Ensure you have the necessary permissions to log out the user.
- The logout command may vary depending on the operating system and environment.

## License

This project is licensed under the MIT License. See the LICENSE file for details.

---

Feel free to modify the content as needed to better suit your project.