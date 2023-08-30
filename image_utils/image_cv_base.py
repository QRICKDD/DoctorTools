import cv2
import torch
from torchvision import transforms
#return (1,h,w,c)
def img_read(path)->torch.Tensor:
    transform = transforms.ToTensor()
    im = cv2.imread(path, 1)
    im = cv2.cvtColor(im, cv2.COLOR_BGR2RGB)
    img = transform(im)
    img = img.unsqueeze_(0)
    return img
