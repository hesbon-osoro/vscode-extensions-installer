import os
import subprocess

def execute_commands_from_file(filepath):
    """
    Reads commands from a file and executes them using subprocess.

    Args:
        filepath (str): The path to the file containing commands (e.g., cmd.txt).
    """
    try:
        with open(filepath, 'r') as f:
            commands = [line.strip() for line in f if line.strip()]

        print("Checking environment variables for VS Code path...")
        path_env = os.environ.get('PATH', '')
        vscode_bin_path = r'C:\Users\User\AppData\Local\Programs\Microsoft VS Code\bin'  # Use raw string for path

        if vscode_bin_path.lower() in path_env.lower():
            print(f"VS Code path '{vscode_bin_path}' found in environment variables.")
        else:
            print(f"Warning: VS Code path '{vscode_bin_path}' not found in environment variables. "
                  "The 'code' command might not work.")

        print("\nExecuting commands from the file:")
        for command in commands:
            print(f"\nExecuting: {command}")
            try:
                process = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
                print("Command executed successfully.")
                if process.stdout:
                    print("Output:")
                    print(process.stdout)
                if process.stderr:
                    print("Errors:")
                    print(process.stderr)
            except subprocess.CalledProcessError as e:
                print(f"Error executing command '{command}':")
                print(f"Return Code: {e.returncode}")
                print(f"Stdout: {e.stdout}")
                print(f"Stderr: {e.stderr}")
            except FileNotFoundError:
                print(f"Error: The command '{command.split()[0]}' was not found. "
                      "Make sure it's in your system's PATH.")
            except Exception as e:
                print(f"An unexpected error occurred while executing '{command}': {e}")

    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    file_path = input("Please enter the path to the file containing commands (e.g., cmd.txt): ")
    execute_commands_from_file(file_path)