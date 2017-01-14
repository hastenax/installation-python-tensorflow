Installing tensorflow/tensorflow-gpu on Ubuntu 14.04 LTS
=============

Install JDK 8
---

- `sudo add-apt-repository ppa:webupd8team/java`
- `sudo apt-get update`
- `sudo apt-get install oracle-java8-installer`

Install Bazel
---

Add Bazel package source
- `echo "deb [arch=amd64] http://storage.googleapis.com/bazel-apt stable jdk1.8" | sudo tee /etc/apt/sources.list.d/bazel.list`
- `curl https://bazel.build/bazel-release.pub.gpg | sudo apt-key add`

Install and update Bazel
- `sudo apt-get update && sudo apt-get install bazel`
- `sudo apt-get upgrade bazel`

CUDA 8.0 and cuDNN 5.1
---

Go to https://developer.nvidia.com/cuda-downloads and get appropriate cuda deb installer file

- `sudo dpkg -i cuda-repo-ubuntu1404-8-0-local_8.0.44-1_amd64.deb`
- `sudo apt-get update`
- `sudo apt-get install cuda`

Toggle Secure Boot by choosing password and reboot
SET PATH and LD_LIBRARY_PATH

Set up development path wherever in /etc/profile
- `sudo vim /etc/profile`
> PATH=$PATH:/usr/local/cuda-8.0/bin
> export PATH
> LD_LIBRARY_PATH=$LD_LIBRARY_PATH:/usr/local/cuda-8.0/lib64
> export LD_LIBRARY_PATH

Download and Unpack cuDNN 5.1 from https://developer.nvidia.com/cudnn (registration required), move headers and libs to approriate place

- `tar zxvf`
- `sudo cp cuda/include/* /usr/local/cuda-8.0/include/`
- `sudo cp cuda/lib64/* /usr/local/cuda-8.0/lib64/`

Python PIP Installation
---

For Python 2.7
- `sudo apt-get install python-dev`
- `sudo apt-get install python-pip`
- `sudo -H pip install --upgrade pip`

For Python 3.x
- `sudo apt-get install python3-dev`
- `sudo apt-get install python3-pip`
- `sudo -H pip3 install --upgrade pip`

Install tensorflow or tensorflow-gpu
---
- `sudo -H pip install tensorflow`
or
- `sudo -H pip install tensorflow-gpu`
