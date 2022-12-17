import numpy as np
import os
import time
import cv2
import torch
from PIL import Image
from torch.autograd import Variable
from torchvision import transforms

from config import msd_testing_root
from misc import check_mkdir, crf_refine
from mirrornet import MirrorNet

args = {
    'snapshot': '160',
    'scale': 384,
    'crf': True
}

img_transform = transforms.Compose([
    transforms.Resize((args['scale'], args['scale'])),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

to_test = {'MSD': msd_testing_root}

to_pil = transforms.ToPILImage()

def mirror(frame):
    net = MirrorNet()

    net.load_state_dict(torch.load("../../Models/160.pth"))

    net.eval()
    # dummy_input = dummy_input = torch.randn(1, 3, 224, 224)
    # torch.onnx.export(net, (dummy_input, ), 'mirrornet.onnx')
    with torch.no_grad():
        img = Image.fromarray(frame)
        w, h = img.size
        img_var = Variable(img_transform(img).unsqueeze(0))
        f_4, f_3, f_2, f_1 = net(img_var)
        f_4 = f_4.data.squeeze(0).cpu()
        f_3 = f_3.data.squeeze(0).cpu()
        f_2 = f_2.data.squeeze(0).cpu()
        f_1 = f_1.data.squeeze(0).cpu()
        f_4 = np.array(transforms.Resize((h, w))(to_pil(f_4)))
        f_3 = np.array(transforms.Resize((h, w))(to_pil(f_3)))
        f_2 = np.array(transforms.Resize((h, w))(to_pil(f_2)))
        f_1 = np.array(transforms.Resize((h, w))(to_pil(f_1)))
        if args['crf']:
            f_4 = crf_refine(np.array(img.convert('RGB')), f_4)

        return f_4
