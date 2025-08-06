filename = "sample.txt"

try:
    with open(filename, 'r') as file:
        content = file.read()
        char_count = len(content)
        
    print(f"Content of {filename}:")
    print(content)
    print(f"\nTotal number of characters: {char_count}")
    
    print(f"Character count breakdown:")
    print(f"Including spaces: {char_count}")
    print(f"Excluding spaces: {len(content.replace(' ', ''))}")
    print(f"Number of words: {len(content.split())}")
    
except FileNotFoundError:
    print(f"File {filename} not found. Please run replace_file_content.py first.")
