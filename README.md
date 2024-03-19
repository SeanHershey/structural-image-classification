# Structural Image Classification

Project for CSC 480 at Cal Poly with Professor Dr. Rodrigo Canaan.

Made by Alejandra Bravo, Nipun Das, Sean Hershey.

## Credits
1. Gao Y., & Mosalam K.M. (2018). Deep Transfer Learning for Image-based Structural Damage Recognition, Computer-Aided Civil and Infrastructure Engineering, 33(9): 748-768.
2. Gao, Y., & Mosalam, K. M. (2019). PEER Hub ImageNet (Φ-Net): A Large-Scale Multi-Attribute Benchmark Dataset of Structural Images. PEER Report No.2019/07, Pacific Earthquake Engineering Research Center, University of California, Berkeley, CA.
3. Gao, Y., & Mosalam, K. M. (2020). PEER Hub ImageNet: A Large-Scale Multiattribute Benchmark Data Set of Structural Images. Journal of Structural Engineering, 146(10), 04020198.
4. PEER Hub Image-Net. (2018). https://doi.org/10.55461/PHIN01152018
5. Wood, Luke and Tan, Zhenyu and Stenbit, Ian and Bischof, Jonathan and Zhu, Scott and Chollet, Fran\c{c}ois and Sreepathihalli, Divyashree and Sampath, Ramesh and others (2022). KerasCV. https://github.com/keras-team/keras-cv
6. Martín Abadi, Ashish Agarwal, Paul Barham, Eugene Brevdo, Zhifeng Chen, Craig Citro, Greg S. Corrado, Andy Davis, Jeffrey Dean, Matthieu Devin, Sanjay Ghemawat, Ian Goodfellow,
Andrew Harp, Geoffrey Irving, Michael Isard, Rafal Jozefowicz, Yangqing Jia, Lukasz Kaiser, Manjunath Kudlur, Josh Levenberg, Dan Mané, Mike Schuster, Rajat Monga, Sherry Moore, Derek Murray, Chris Olah, Jonathon Shlens, Benoit Steiner, Ilya Sutskever, Kunal Talwar, Paul Tucker, Vincent Vanhoucke, Vijay Vasudevan, Fernanda Viégas, Oriol Vinyals, Pete Warden, Martin Wattenberg, Martin Wicke, Yuan Yu, and Xiaoqiang Zheng (2015). TensorFlow: Large-scale machine learning on heterogeneous systems. https://tensorflow.org

## Instructions
1. Install Tensorflow and Keras.
   - pip install tensorflow keras
2. Install Gradio and Skimage for demo.
   - pip install gradio scikit-image
3. To Demo: Run demo.ipynb in the demo folder  
4. To Train: Download dataset from ImageNet 
   - Request the download for Dataset Task 7 Damage Level from ImageNet or direct download if still available.
   - Once downloaded move to dataset folder.
   -   [Task 7 Dataset Request](https://apps.peer.berkeley.edu/phi-net/download-backup/)
   -   [Task 7 Dataset Direct Download](https://apps.peer.berkeley.edu/phi-net/?ed=download&guid=sypvzr-ngymwk-qnbftk-vosygf-rvasit--cxbvin-lmxdhg-ukdzwv-xdiszp-hmszbu)
   - Run train.ipynb (the training will take around 15 minutes for the 20 epoch run, note our report and the model given is the 100 epoch run which took an hour)
   - This will produce the main graph results as well as save the model to run in the demo


## Results
![Accuracy and Loss Graph](https://i.imgur.com/aBQYitH.png)