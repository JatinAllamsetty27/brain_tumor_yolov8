import cv2
import numpy as np

IMG_WIDTH = 256
IMG_HEIGHT = 256

def preprocess_image(img_path):
    """Preprocess the image before passing to model"""
    
    img = cv2.imread(img_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Resize the image
    img = cv2.resize(img, (IMG_WIDTH, IMG_HEIGHT)) 
    
    # Normalize the pixel values 
    img = img/255.0
    
    return img

def preprocess_batch(img_batch):
    """Preprocess a batch of images"""
    
    processed_imgs = []
    
    for img_path in img_batch:
        img = preprocess_image(img_path)
        processed_imgs.append(img)
        
    return np.array(processed_imgs)
