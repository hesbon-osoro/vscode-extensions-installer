import json
import os

def generate_install_commands_to_file(filepath, output_filename="cmd.txt"):
    """
    Reads a VS Code extensions.json file (list format) and writes installation
    commands to a specified output file.

    Args:
        filepath (str): The path to the extensions.json file.
        output_filename (str, optional): The name of the file to write commands to.
                                         Defaults to "cmd.txt".

    Returns:
        bool: True if the commands were written successfully, False otherwise.
    """
    try:
        with open(filepath, 'r') as f:
            data = json.load(f)
            if isinstance(data, list):
                commands = []
                for extension_info in data:
                    if 'identifier' in extension_info and 'id' in extension_info['identifier']:
                        extension_id = extension_info['identifier']['id']
                        command = f"code --install-extension {extension_id}"
                        commands.append(command)

                if commands:
                    with open(output_filename, 'w') as outfile:
                        for command in commands:
                            outfile.write(command + os.linesep)
                    print(f"\nInstallation commands have been written to '{output_filename}'.")
                    return True
                else:
                    print("No extension IDs found in the JSON file.")
                    return False
            else:
                print("Warning: The JSON file does not contain a list of extension objects.")
                return False
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return False
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filepath}. Please ensure it's a valid JSON file.")
        return False

if __name__ == "__main__":
    file_path = input("Please enter the path to your extensions.json file: ")
    output_file = "cmd.txt"
    if generate_install_commands_to_file(file_path, output_file):
        print(f"You can now open '{output_file}' and copy the commands to your terminal.")