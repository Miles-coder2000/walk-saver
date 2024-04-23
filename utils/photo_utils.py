from PIL import ImageGrab
import os

def take_and_save_photo():
    # Capture the screen as an image
    photo = ImageGrab.grab()
    
    # Define the directory to save the photo
    save_dir = "C:/Projects/WalkingApp/photos"  # Change this to your desired directory
    
    # Ensure the directory exists
    if not os.path.exists(save_dir):
        os.makedirs(save_dir)
    
    # Save the photo with a unique filename
    photo_path = os.path.join(save_dir, "walking_photo.png")
    photo.save(photo_path)
    
    return photo_path
