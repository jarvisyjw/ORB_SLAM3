# ORB-SLAM3

## This repo serves for the installation with Ubuntu20.04 and ROS1-noetic [[Original README]](./README_old.md)

First of all, if you are using anaconda to manage your python environment, please be careful, there might be fuzzy bugs. The vanilla ORB_SLAM3 can successfully complied by the original python environment came with the Ubuntu20.04.

# Installation
## Step1: Install Pangolin
```bash
# Get Pangolin
cd ~/your_fav_code_directory
git clone --recursive https://github.com/stevenlovegrove/Pangolin.git
cd Pangolin
git checkout v0.6 # use this version might save you a lot of trouble

# Install dependencies (as described above, or your preferred method)
# remove catch2 if installing on Ubuntu 20.04
./scripts/install_prerequisites.sh recommended

# Configure and build
cmake -B build -DPython_EXECUTABLE='path/to/desired/python/interpreter'
cmake --build build

# with Ninja for faster builds (sudo apt install ninja-build)
cmake -B build -GNinja
cmake --build build

# GIVEME THE PYTHON STUFF!!!! (Check the output to verify selected python version)
cmake --build build -t pypangolin_pip_install
```
Quick install of Pangolin with v0.6
```bash
cd opt/ && \
git clone https://github.com/stevenlovegrove/Pangolin.git Pangolin && \
cd Pangolin/ && \
git checkout v0.6 && \
mkdir build && \
cd build/ && \
cmake -D CMAKE_BUILD_TYPE=RELEASE -D CPP11_NO_BOOST=1 .. && \
make -j$(nproc) && \
make install
```

## Step2: Install OpenCV
```bash
# Check the system's OpenCV
pkg-config --modversion opencv4
# or older version 
pkg-config --modversion opencv

# OpenCV 4.4 is recommended
# Install OpenCV 4.4 mannually
# Get the opencv and opencv_contrib source
wget https://github.com/opencv/opencv/archive/4.4.0.zip
wget https://github.com/opencv/opencv_contrib/archive/4.4.0.zip
# unzip both
unzip xxx.zip
# build & configure
cd opencv-4.4.0
mkdir build && cd build

# remember to use proxy to download required cache for opencv_contrib xfeatures2d
cmake -D CMAKE_BUILD_TYPE=RELEASE \
-D BUILD_TIFF=ON \
-D WITH_CUDA=OFF \
-D ENABLE_AVX=OFF \
-D WITH_OPENGL=OFF \
-D WITH_OPENCL=OFF \
-D WITH_IPP=OFF \
-D WITH_TBB=ON \
-D BUILD_TBB=ON \
-D WITH_EIGEN=ON \
-D WITH_V4L=OFF \
-D WITH_VTK=OFF \
-D BUILD_TESTS=OFF \
-D BUILD_PERF_TESTS=OFF \
-D OPENCV_GENERATE_PKGCONFIG=ON \
-D OPENCV_EXTRA_MODULES_PATH=../../opencv_contrib-4.4.0/modules \
..

make
sudo make install
ldconfig
```

## Step3: Install Eigen3
Required by g2o (see below). Download and install instructions can be found at: http://eigen.tuxfamily.org. Required at least 3.1.0.
```bash
# Check the system's Eigen version
apt list -a libeigen3-dev
```

## Step4: Build
```bash
chmod +x build.sh
./build.sh
```

## Step5: Build for ROS (Optional)
```bash
# export in current terminal or edit in bash/zsh for good.
export ROS_PACKAGE_PATH=${ROS_PACKAGE_PATH}:PATH/ORB_SLAM3/Examples_old/ROS
# build
chmod +x build_ros.sh
./build_ros.sh
```

## Notes
- **rosdep2.rospak**
  
  If you encounter the following error and found that you are using a Anaconda python environment or there exist multiple python environment in your system.
  ```bash
  [rospack] Error: could not find python module 'rosdep2.rospack'. is rosdep up-to-date (at least 0.10.4)?
  ```
  There are two ways that might solve it:
  1. `conda deactivate`
  2. `pip install rosdep` in your anaconda env
  3. Delete python environment that may cause confusion

- **Minor Modification**
  
  If you encounter error compiling the MonoAR node:
  The minor modification mentions in issue [#479](https://github.com/UZ-SLAMLab/ORB_SLAM3/issues/479) might solve this problem. Or you can directly clone from this repo.

- **Useful Forks**
  
  - [This fork](https://github.com/shashankyld/orbslam3_ROS.git) provide docker support. I might look into it later.
  - [This fork](https://github.com/shanpenghui/ORB_SLAM3_Fixed.git) provides detailed tutorial of runnning on cutomized sensors.

# Running Experiments
