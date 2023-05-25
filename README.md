# image_and_video_colourisation
This a app build in python and streamlet to colourise images and videos

To run the app please do the following imports with PIP

To include the required headers for your Streamlit script, you'll need to install the following packages via pip:

1. streamlit: The Streamlit library itself.
   pip install streamlit

2. opencv-python: The OpenCV library for image processing.
   pip install opencv-python

3. pillow: The PIL (Python Imaging Library) package for image manipulation.
   pip install pillow

After installing these packages, you should be able to import them successfully in your Streamlit script and use the necessary functions and classes.

After all this go to the curent working directory of the app and write this in the cmd/terminal

streamlit run Webb.py

****************************************************************************************************************************************************

However, if you are encountering import errors for these packages, it could be due to issues with your Python installation. In that case, you may consider reinstalling Python to ensure all standard library modules are available.

Here are the installation instructions for Python:

1. Visit the official Python website: https://www.python.org/
2. Go to the "Downloads" section.
3. Choose the appropriate version of Python for your operating system.
4. Download the installer and run it.
5. Follow the installation wizard, ensuring that you select the option to include pip, which is the package manager for Python.
6. After reinstalling Python, you should be able to import numpy and tempfile without any issues.

******************************************************************************************************************************************************

If you Have NVIDIA high End GPU you Could use this process

To install CUDA and GPU processing support via pip, you typically don't directly install them through pip. Instead, you need to install CUDA toolkit and related GPU drivers separately. Once you have CUDA installed, you can use pip to install packages that leverage GPU processing.

Here's the general process to install CUDA and set up GPU processing:

Verify GPU Compatibility: Make sure your GPU is compatible with CUDA. Check the NVIDIA CUDA website (https://developer.nvidia.com/cuda-gpus) for the list of supported GPUs.

Install CUDA Toolkit: Visit the NVIDIA CUDA Toolkit download page (https://developer.nvidia.com/cuda-toolkit-archive) and download the appropriate version for your operating system. Follow the installation instructions provided by NVIDIA to install CUDA.

Install GPU Drivers: Ensure that you have the latest GPU drivers installed on your system. You can download the drivers from the NVIDIA website (https://www.nvidia.com/Download/index.aspx).

Verify CUDA Installation: After installing CUDA, verify that it is correctly installed by checking the CUDA version and running sample programs provided by NVIDIA.

Once you have CUDA installed and verified, you can use pip to install packages that support GPU processing, such as tensorflow-gpu or pytorch.

For example, to install tensorflow-gpu:
pip install tensorflow-gpu

Please note that GPU processing requires a compatible GPU with CUDA support, appropriate GPU drivers, and the necessary dependencies specific to the library you are using (e.g., CUDA-enabled versions of libraries like TensorFlow or PyTorch).


