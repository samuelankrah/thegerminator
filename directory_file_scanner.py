import os

def bytes_to_readable_size(size_in_bytes):
    """
    Convert bytes to a human-readable format.
    
    :param size_in_bytes: File size in bytes.
    :return: Human-readable file size.
    """
    # Define size units.
    units = ['bytes', 'KB', 'MB', 'GB', 'TB']

    # Calculate unit size.
    unit_index = 0
    while size_in_bytes > 1024 and unit_index < len(units) - 1:
        size_in_bytes /= 1024
        unit_index += 1

    return f"{size_in_bytes:.2f} {units[unit_index]}"


def generate_file_info(path=None):
    """
    Generates a list of dictionaries about files in a given directory (and its sub-directories).
    
    :param path: Path to the directory. Defaults to the current working directory.
    :return: List of dictionaries with file info.
    """
    # If no path is provided, default to the current working directory.
    if path is None:
        path = os.getcwd()

    # Check if the provided path exists.
    if not os.path.exists(path):
        print(f"The path '{path}' does not exist.")
        return []

    # Check if the provided path is a directory.
    if not os.path.isdir(path):
        print(f"The path '{path}' is not a directory.")
        return []

    file_info_list = []

    # Walk through the path, including its sub-directories.
    for dirpath, _, filenames in os.walk(path):
        for filename in filenames:
            file_path = os.path.join(dirpath, filename)
            
            # Gather file information.
            info = {
                'name': filename,
                'path': file_path,
                'size': bytes_to_readable_size(os.path.getsize(file_path))
            }
            file_info_list.append(info)

    return file_info_list

# Example usage
if __name__ == "__main__":
    files = generate_file_info()
    
    # Print the file details in a human-readable format.
    for file in files:
        print(f"Name: {file['name']}\nPath: {file['path']}\nSize: {file['size']}\n{'-'*60}")
