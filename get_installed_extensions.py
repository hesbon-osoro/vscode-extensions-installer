import json

def generate_install_commands_from_list(filepath):
    """
    Reads a VS Code extensions.json file (list format) and generates installation commands.

    Args:
        filepath (str): The path to the extensions.json file.

    Returns:
        list: A list of tuples, where each tuple contains the extension ID
              and the corresponding 'code --install-extension' command.
              Returns an empty list if the file is not found or has issues.
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
                        commands.append((extension_id, command))
                return commands
            else:
                print("Warning: The JSON file does not contain a list of extension objects.")
                return []
    except FileNotFoundError:
        print(f"Error: File not found at {filepath}")
        return []
    except json.JSONDecodeError:
        print(f"Error: Could not decode JSON from {filepath}. Please ensure it's a valid JSON file.")
        return []

if __name__ == "__main__":
    file_path = input("Please enter the path to your extensions.json file: ")
    extension_commands = generate_install_commands_from_list(file_path)

    if extension_commands:
        print("\nExtensions and their installation commands:")
        for name, command in extension_commands:
            print(f"- ID: {name}")
            print(f"  Command: {command}")
        print("\nTo install all these extensions, you can copy and paste these commands into your terminal.")