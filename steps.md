## Download YOLO
`git clone https://github.com/pjreddie/darknet`

## Modify Makefile

## Install cuda
https://gist.github.com/Brainiarc7/470a57e5c9fc9ab9f9c4e042d5941a40

```
# first get the PPA repository driver
sudo add-apt-repository ppa:graphics-drivers/ppa

# install nvidai driver 
sudo apt install nvidia-384 nvidia-384-dev

# install other import packages
sudo apt-get install g++ freeglut3-dev build-essential libx11-dev libxmu-dev libxi-dev libglu1-mesa libglu1-mesa-dev

# CUDA 9 requires gcc 6
sudo apt install gcc-6
sudo apt install g++-6

# downoad one of the "runfile (local)" installation packages from cuda toolkit archive 
wget https://developer.nvidia.com/compute/cuda/9.0/Prod/local_installers/cuda_9.0.176_384.81_linux-run

# make the download file executable
chmod +x cuda_9.0.176_384.81_linux-run 
sudo ./cuda_9.0.176_384.81_linux-run --override

# Answer questions following while installation begin
# You are attempting to install on an unsupported configuration. Do you wish to continue? y
# Install NVIDIA Accelerated Graphics Driver for Linux-x86_64 384.81? n
# Install the CUDA 9.0 Toolkit? y

# set up symlinks for gcc/g++
sudo ln -s /usr/bin/gcc-6 /usr/local/cuda/bin/gcc
sudo ln -s /usr/bin/g++-6 /usr/local/cuda/bin/g++

# setup your paths
echo 'export PATH=/usr/local/cuda-9.0/bin:$PATH' >> ~/.bashrc
echo 'export LD_LIBRARY_PATH=/usr/local/cuda-9.0/lib64:$LD_LIBRARY_PATH' >> ~/.bashrc
source ~/.bashrc

# install cuDNN v7.1
# in order to download cuDNN you have to regeistered here https://developer.nvidia.com/developer-program/signup
# then download cuDNN v7.1 form https://developer.nvidia.com/cudnn
CUDNN_TAR_FILE="cudnn-9.0-linux-x64-v7.1"
wget http://developer.download.nvidia.com/compute/redist/cudnn/v7.1/${CUDNN_TAR_FILE}
tar -xzvf ${CUDNN_TAR_FILE}

#copy the following files into the cuda toolkit directory.
sudo cp -P cuda/include/cudnn.h /usr/local/cuda-9.0/include
sudo cp -P cuda/lib64/libcudnn* /usr/local/cuda-9.0/lib64/
sudo chmod a+r /usr/local/cuda-9.0/lib64/libcudnn*
```
You might need to change `cuda_9.0.176_384.81_linux-run` to `cuda_9.0.176_384.81_linux.run`
If you see bad configuration message, continue anyways.
`http://developer.download.nvidia.com/compute/redist/cudnn/v7.1/${CUDNN_TAR_FILE}`
This link is dead, download it manually

## Install Opencv
https://github.com/jayrambhia/Install-OpenCV/blob/master/Ubuntu/2.4/opencv2_4_9.sh

```
wget https://raw.githubusercontent.com/jayrambhia/Install-OpenCV/master/Ubuntu/2.4/opencv2_4_9.sh
chmod +x opencv2_4_9.sh
./opencv2_4_9.sh
```

## Install gcc 6
cuda library complains about gcc version.
```
In file included from /usr/local/cuda/include/host_config.h:50,
                 from /usr/local/cuda/include/cuda_runtime.h:78,
                 from <command-line>:
/usr/local/cuda/include/crt/host_config.h:119:2: error: #error -- unsupported GNU version! gcc versions later than 6 are not supported!
  119 | #error -- unsupported GNU version! gcc versions later than 6 are not supported!
      |  ^~~~~
compilation terminated due to -Wfatal-errors.
make: *** [Makefile:92: obj/convolutional_kernels.o] Error 1
```

https://gist.github.com/zuyu/7d5682a5c75282c596449758d21db5ed

```
sudo apt-get update && \
sudo apt-get install build-essential software-properties-common -y && \
sudo add-apt-repository ppa:ubuntu-toolchain-r/test -y && \
sudo apt-get update && \
sudo apt-get install gcc-6 g++-6 -y && \
sudo update-alternatives --install /usr/bin/gcc gcc /usr/bin/gcc-6 60 --slave /usr/bin/g++ g++ /usr/bin/g++-6 && \
gcc -v
```
```
wget https://gist.githubusercontent.com/zuyu/7d5682a5c75282c596449758d21db5ed/raw/8ef3b032797b03dec824707ad6294aa43301ab8d/ubuntu-install-gcc-6
sh ubuntu-install-gcc-6
```


https://github.com/YunYang1994/tensorflow-yolov3