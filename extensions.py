# extensions.py

# Prompt the user for the name of a file
file_name = input("Enter the name of a file: ").strip().lower()

# Define a dictionary mapping file extensions to media types
extension_to_media_type = {
    ".gif": "image/gif",
    ".jpg": "image/jpeg",
    ".jpeg": "image/jpeg",
    ".png": "image/png",
    ".pdf": "application/pdf",
    ".txt": "text/plain",
    ".zip": "application/zip"
}

# Extract the file extension from the file name (if it exists)
file_extension = None
if "." in file_name:
    file_extension = "." + file_name.split(".")[-1]

# Check if the file extension exists in the dictionary
if file_extension in extension_to_media_type:
    media_type = extension_to_media_type[file_extension]
else:
    media_type = "application/octet-stream"

# Output the determined media type
print(media_type)
