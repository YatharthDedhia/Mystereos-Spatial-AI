"""
 @Time    : 2020/3/15 20:43
 @Author  : TaylorMei
 @E-mail  : mhy666@mail.dlut.edu.cn
 
 @Project : CVPR2020_GDNet
 @File    : infer.py
 @Function:
 
"""
import os
import time

import numpy as np

import torch
from PIL import Image
from torch.autograd import Variable
from torchvision import transforms

from config import gdd_testing_root, gdd_results_root
from misc import check_mkdir, crf_refine
from gdnet import GDNet

device_ids = [0]

ckpt_path = './ckpt'
exp_name = 'GDNet'
args = {
    'snapshot': '200',
    'scale': 416,
    # 'crf': True,
    'crf': False,
}

print(torch.__version__)

img_transform = transforms.Compose([
    transforms.Resize((args['scale'], args['scale'])),
    transforms.ToTensor(),
    transforms.Normalize([0.485, 0.456, 0.406], [0.229, 0.224, 0.225])
])

to_test = {'GDD': gdd_testing_root}

to_pil = transforms.ToPILImage()


def gdnet(frame):
    net = GDNet()
    net.load_state_dict(torch.load("../Models/200.pth"))

    net.eval()
    with torch.no_grad():
        img = Image.fromarray(frame)
        w, h = img.size
        img_var = Variable(img_transform(img).unsqueeze(0))
        f1, f2, f3 = net(img_var)
        f1 = f1.data.squeeze(0).cpu()
        f2 = f2.data.squeeze(0).cpu()
        f3 = f3.data.squeeze(0).cpu()
        f1 = np.array(transforms.Resize((h, w))(to_pil(f1)))
        f2 = np.array(transforms.Resize((h, w))(to_pil(f2)))
        f3 = np.array(transforms.Resize((h, w))(to_pil(f3)))
        if args['crf']:
            # f1 = crf_refine(np.array(img.convert('RGB')), f1)
            # f2 = crf_refine(np.array(img.convert('RGB')), f2)
            f3 = crf_refine(np.array(img.convert('RGB')), f3)

        # Image.fromarray(f1).save(os.path.join(ckpt_path, exp_name, '%s_%s' % (exp_name, args['snapshot']),
        #                                       img_name[:-4] + "_h.png"))
        # Image.fromarray(f2).save(os.path.join(ckpt_path, exp_name, '%s_%s' % (exp_name, args['snapshot']),
        #                                       img_name[:-4] + "_l.png"))
        return f3
