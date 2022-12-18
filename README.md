# File Structure:


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

## **MirrorNet**:
```
cd Mirrornet
```
### Run only MiDaS depth model 12 FPS

    python MiDaS.py

### Run Mirrornet masking on OAK-D 2 FPS

    mirrornet_OAK-D.py 

### Run MiDaS on OAK-D and Mirrornet locally simultaneously

    cd MirrorNet\ Midas/
    python main.py

### Test Mirrornet on Locally stored images

    cd MirrorNet\ Midas/
    python infer_local.py

## **GDNet**
### Run MiDaS on OAK-D and GDNet locally simultaneously

    cd GDNet
    python main.py

---

# Results:

## **MiDaS Monocular Depth Estimation:**

**FPS:** ~13-14 FPS

![MiDaS results](Assets/midas_results.gif)

## **MirrorNet**
**FPS:** ~2 FPS on OAK-D Pro

![MirrorNet Results](Assets/mirrornet_results)

## **GDNet**
**FPS:** ~2 FPS on OAK-D Pro

 ![GDNet Results](Assets/gdnet_results)

## **MiDaS and MirrorNet Masking**
**FPS:** ~1 FPS

![MirrorNet Masking Results](Assets/mirrornet_masking_results)

## **MiDaS and GDNet Masking**
**FPS:** ~1 FPS

![GDNet Masking Results](Assets/gdnet_masking_results)
