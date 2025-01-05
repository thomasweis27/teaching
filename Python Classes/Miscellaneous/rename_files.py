import os

def rename_files_in_folder(folder_path):
    """
    Removes the prefixes "IMG_", "Snapchat_", "Screenshot_", and "PXL_" 
    from all file names in the specified folder.
    """
    prefixes = ["IMG_", "Snapchat_", "Snapchat-", "Screenshot_", "PXL_", "VID_", "DOWNLOAD_", "image-", "moment_", "download_", "VID-", "IMG-"]
    
    try:
        # Get the list of all files in the folder
        files = os.listdir(folder_path)
        
        # Iterate over each file
        for file_name in files:
            new_name = file_name
            
            # Check and remove any matching prefix
            for prefix in prefixes:
                if new_name.startswith(prefix):
                    new_name = new_name[len(prefix):]
                    break  # Remove only one prefix per iteration
            
            # If the name changed, rename the file
            if new_name != file_name:
                old_path = os.path.join(folder_path, file_name)
                new_path = os.path.join(folder_path, new_name)
                
                os.rename(old_path, new_path)
                print(f"Renamed: {file_name} -> {new_name}")
        
        print("Renaming complete.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    # Change this to the folder path you want to use
    folder_path = input("Enter the folder path: ").strip()
    if os.path.isdir(folder_path):
        rename_files_in_folder(folder_path)
    else:
        print("Invalid folder path. Please provide a valid directory.")
