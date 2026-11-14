import os


base_dir = r"Directory address"


for i in range(4, 71):
   
    folder_name = f"Patient {i}"
    
    
    folder_path = os.path.join(base_dir, folder_name)
    
    
    os.makedirs(folder_path, exist_ok=True)

print("Completed creating folders.")
