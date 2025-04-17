import os
import time

input_folder = 'ascii/ 
frame_count = 384  

def show_frame(frame_number):
    file_path = os.path.join(input_folder, f"{frame_number}.txt")
    if os.path.exists(file_path):
        with open(file_path, 'r') as f:
            ascii_art = f.read()
            print(ascii_art)
    else:
        print(f"clip {frame_number} not found.")

for frame in range(1, frame_count + 1):
    os.system('cls' if os.name == 'nt' else 'clear')
    
    show_frame(frame)
    time.sleep(0.05)  
