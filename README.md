# Mystereos-Spatial-AI

## Aim

The aim of our project is to improve the depth estimation of Oak-D Pro and other similar camera systems by addressing various significant issues, such as occlusions, enhancing depth estimation of mirror surfaces and Long Range Depth Estimation employing stereo and monocular depth estimation approaches.

## Motivation

Using geometry-based methods for estimation, Oak-D Pro often approaches depth estimation as a geometrical problem. These approaches fall short in chaotic settings, tough unstructured environments, and produce issues like occlusions and inaccurate mirror depth. As a result, we provide CNN-based approaches to address the various depth estimation issues.


## File Structure:
```
├── Assets
├── GDNet
│   ├── backbone
│   ├── config.py
│   ├── dataset.py
│   ├── gdnet.py
│   ├── infer.py
│   ├── main.py
│   ├── misc.py
│   └── README.md
├── Mirrornet
│   ├── MiDaS.py
│   ├── MirrorNet Midas
│   │   ├── backbone
│   │   ├── config.py
│   │   ├── dataset.py
│   │   ├── infer_local.py
│   │   ├── infer.py
│   │   ├── main.py
│   │   ├── mirrornet.py
│   │   ├── misc.py
│   │   ├── README.md
│   │   └── utils
│   └── mirrornet_oakd.py
├── Models
│   ├── 160.pth
│   ├── 200.pth
│   ├── blob
│   ├── MiDaS_small.bin
│   ├── MiDaS_small.xml
│   ├── nyu_rawdata.pth
│   └── onnx
├── README.md
├── Report.md
└── requirements.txt
```

# Installation:
### 1. Create conda environment:
```
conda create -n mystereos
conda activate mystereos
```
### 2. Install Requirements
```
sudo pip install -r requirements.txt
conda install scikit-image

python3 -m pip list | grep depthai

conda install pytorch torchvision torchaudio cpuonly -c pytorch
```
<!-- pip install git+https://github.com/lucasb-eyer/pydensecrf.git
pip3 install -U scikit-learn
pip install blobconverter
pip install depthai
pip install opencv-python -->

```
cd Mirrornet
```

## A New approach

Oak-D pro camera treats the problem of Depth estimation as a StereoVision problem. StereoVision comes with its own drawbacks a major one being the problem of Occlusion and the problem of Incorrect depth estimation in case of mirror scene. Hence we propose to run a neural network model that generates superior quality depth maps namely MiDas. Having been trained on multiple datasets like ReDWeb, DIML, Movies, MegaDepth, WSVD abd IRS, this approach clearly outperforms competing methods across diverse datasets, setting a new state of the art for monocular depth estimation. The experiments confirm that mixing data from complementary sources greatly improves monocular depth estimation.

### Run only MiDaS depth model 12 FPS

    python MiDaS.py

## **MirrorNet**:

## Improving depth estimation of **Lambertian** surfaces

Existing computer vision systems do not consider lambertian surfaces such as mirrors, and may get confused by the reflected content inside a mirror and hence we get the depth of objects reflected inside the mirror while using the Oak-D camera. The RGB input images from the camera are passed to Mirror Detection Networks- MirrorNet and GDNet and we use opencv techniques on the resultant images obtained a superior depth estimation. 

### Run Mirrornet masking on OAK-D 2 FPS

    mirrornet_OAK-D.py 

### Run MiDaS on OAK-D and Mirrornet locally simultaneously

We run both the Mirrornet and the MiDas network simultaneously on the Oak-D pro. Mirrornet is used to generate a real time mirror segmented mask of the real world scene observed through the Oak-D pro camera. Simultaneously the novel MiDas network generates a depth map f the very same scene. Now the mirror mask is applied on this depth map and the depth of the mirror surroundings is given to the plane mirror segment using principles of OpenCv like infilling , etc.

    cd MirrorNet\ Midas/
    python main.py

### Test Mirrornet on Locally stored images

    cd MirrorNet\ Midas/
    python infer_local.py

## **GDNet**

GDNet is a upgrade over MirrorNet which outperforms it in Mirror and glass scenes. Extensive experiments demonstrate the proposed method achieves superior glass detection results on the GDD test set. Particularly, it outperforms state-of-the-art methods that is fine-tuned for glass detection. Running GDNet simultaneously with MiDas to obtain the mirror mask using which infilling is performed on the depth estimate gives a better result than mirrornet in mirror scenes but in case of no mirror or gls produces faulty mask whick might not be very accursate. Hence , GDNet is currently limited to only mirror or glass scenes.

### Run MiDaS on OAK-D and GDNet locally simultaneously

    cd GDNet
    python main.py

---

# Results:

## **MiDaS Monocular Depth Estimation:**

**FPS:** 13-14 FPS on OAK-D Pro

![Midas Output](https://scontent.xx.fbcdn.net/v/t1.15752-9/319750872_2405478366282664_522612049283482844_n.png?stp=dst-png_s370x247&_nc_cat=102&ccb=1-7&_nc_sid=aee45a&_nc_ohc=f1iaJ7AiVl8AX82yTum&_nc_oc=AQlO6qB2zG8u4Cx5v65Nsv0yWPFrjlRhsetqjkg1FFMWyq4C2xrxb9qOeni3l2nm5NlVq9C-5j1LenzSHwGkhia8&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdRwujOTokiillGEwNorAmzvoJyvhQafx11URKFJ3mabqQ&oe=63C71689)

Flase Depth is being calculated for the virtual background on the laptop screen.

---

![MiDaS results](Assets/midas.gif)

The above video shows accurate depth estimation on non reflective surfaces, but incorrect depth on reflective surfaces (mirror), as the person is clearly visible in the depth map of the mirror, which should ideally be a flat surface.

---

## **MiDaS and MirrorNet Masking**

**FPS:** ~1 FPS

![Mirrornet](https://scontent.xx.fbcdn.net/v/t1.15752-9/319788488_1749194355452558_8809600691224987451_n.png?stp=dst-png_p206x206&_nc_cat=108&ccb=1-7&_nc_sid=aee45a&_nc_ohc=4bStDqMnt2kAX-FpiL9&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdRFw4RKrgP60YEpYIolnxpEaYcVFoMyHO6_1-5XCXEHXA&oe=63C71316)

![Mirrornet](https://scontent.xx.fbcdn.net/v/t1.15752-9/319788488_1749194355452558_8809600691224987451_n.png?stp=dst-png_p206x206&_nc_cat=108&ccb=1-7&_nc_sid=aee45a&_nc_ohc=4bStDqMnt2kAX-FpiL9&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdRFw4RKrgP60YEpYIolnxpEaYcVFoMyHO6_1-5XCXEHXA&oe=63C71316)

**Leftmost image**: RGB image

**2nd from left image**: inaccurate depth map for lambertian surfaces

**3rd from left image:** mask created by mirrornet for reflective surface detected 

**Rightmost image:** Depth Map output after applying mask and post processing

---
![MirrorNet Masking Results](Assets/mirrornet.gif)

The above video shows that the model accurately removes the false depth from the mirror, tho the FPS takes a significant hit.

---
## **MiDaS and GDNet Masking**

**FPS:** ~1 FPS

![Mirrornet](https://scontent.xx.fbcdn.net/v/t1.15752-9/320231601_1583740212066521_7619536432638194861_n.png?stp=dst-png_s350x350&_nc_cat=102&ccb=1-7&_nc_sid=aee45a&_nc_ohc=bBCIucJFGHkAX-HyJbL&_nc_ad=z-m&_nc_cid=0&_nc_ht=scontent.xx&oh=03_AdRyNjFAIMW167cvPX5vKsDscPDQfYmT9xrhUNkHPejTAQ&oe=63C6EC3D)

**Leftmost image**: RGB image

**2nd from left image**: inaccurate depth map for lambertian surfaces

**3rd from left image:** mask created by mirrornet for reflective surface detected 

**Rightmost image:** Depth Map output after applying mask and post processing

---
![GDNet Masking Results](Assets/gdnet.gif)

The above video shows that the model accurately removes the false depth from the mirror, but also creates false depth maps in the absence of a mirror. 

---
