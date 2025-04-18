# VS Code Extension Automation Scripts

This repository contains scripts to automate the installation of VS Code extensions, particularly useful when migrating or setting up new environments.

## Files

* **`get_installed_extensions.py`**: A Python script that reads a VS Code `extensions.json` file (in list format) and generates `code --install-extension` commands.
* **`generate_commands_file.py`**: A Python script that reads a VS Code `extensions.json` file (in list format) and writes the `code --install-extension` commands to a `cmd.txt` file.
* **`execute_commands.py`**: A Python script that reads commands from a text file (e.g., `cmd.txt`) and executes them using Python's `subprocess` module, with a check for the VS Code path in environment variables.

## Usage

### Cloning the Repository

First, clone this repository to your local machine using Git:

```bash
git clone https://github.com/hesbon-osoro/vscode-extensions-installer.git
cd vscode-extensions-installer
```

1.  **Obtain your `extensions.json` file:** This file can usually be found in your VS Code user settings directory (e.g., `~/.vscode/extensions/` on Linux/macOS or `C:\Users\<Your Username>\.vscode\extensions\` on Windows - though you manually obtained yours).
2.  **Run the appropriate Python script:**
    * `python get_installed_extensions.py`: To directly see the list of extensions and their install commands in your terminal.
    * `python generate_commands_file.py`: To save the install commands to `cmd.txt`.
    * `python execute_commands.py`: To read and execute the commands from `cmd.txt`.
3.  **Execute the commands:** For `get_installed_extensions.py`, copy and paste the commands into your terminal. For `generate_commands_file.py`, you can either copy and paste from `cmd.txt` or use the `execute_commands.py` script.

## Note

* These scripts assume you have the VS Code command-line interface (`code`) available in your system's PATH environment variable.
* The scripts do not automatically identify or handle deprecated extensions. Manual review of extensions is recommended.

## Author

[Hesbon Osoro](https://github.com/hesbon-osoro)