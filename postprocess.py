import numpy as np
from itertools import product
import cv2

CONF_THRESH = 0.5
NMS_THRESH = 0.4

def decode_bbox(anchors, raw_outputs, img_size):
    """Decode the raw bbox predictions to x,y,w,h"""
    
    # Decode bbox coordinates
    x = (raw_outputs[..., 0:1] * 2 - 0.5 + grid) * img_size
    y = (raw_outputs[..., 1:2] * 2 - 0.5 + grid) * img_size
    w = anchors * np.exp(raw_outputs[..., 2:3]) 
    h = anchors * np.exp(raw_outputs[..., 3:4])
    
    # Convert to integers
    x = x.astype(np.int32) 
    y = y.astype(np.int32)
    w = w.astype(np.int32)
    h = h.astype(np.int32) 

    return x, y, w, h

def postprocess(img, outputs, anchors, stride, num_classes):
    """Postprocess YOLOv8 outputs"""
    
    bbox_attrs = 5 + num_classes
    img_h, img_w = img.shape[:2]
    
    bboxes = []
    
    for output in outputs:
        pred = output[0]
        pred = pred.reshape(-1, bbox_attrs)

        bbox_coords = pred[:, :4] 
        bbox_scores = pred[:, 4]
        bbox_clses = pred[:, 5]
        
        idx = bbox_scores >= CONF_THRESH        
        filtered_scores = bbox_scores[idx]
        filtered_boxes = bbox_coords[idx]
        filtered_clses = bbox_clses[idx]

        for cls, (x, y, w, h) in zip(filtered_clses, filtered_boxes):
            x1 = int((x - w / 2) * stride)
            y1 = int((y - h / 2) * stride)
            x2 = int((x + w / 2) * stride) 
            y2 = int((y + h / 2) * stride)
            
            bboxes.append([x1, y1, x2, y2, cls, filtered_scores])
            
    nms_bboxes = nms(bboxes, NMS_THRESH)
            
    return nms_bboxes
        
def nms(bboxes, threshold):
   """Apply non-maximum suppression"""
   
   final_bboxes = []
   
   while bboxes:
       bbox = bboxes.pop(0)
       
       final_bboxes.append(bbox)
       
       bboxes = [ 
           box for box in bboxes 
           if box[4] != bbox[4]  
           or intersection_over_union(box, bbox) < threshold    
       ]
       
   return final_bboxes
   
# Additional utility functions   

def intersection_over_union(box1, box2):
    # Calculate IOU between two boxes
  return box1,box2
