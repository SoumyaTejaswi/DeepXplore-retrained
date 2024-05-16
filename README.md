# DeepXplore-retrained
DeepXplore is an automated testing tool for deep learning systems, designed to expose vulnerabilities and improve their robustness. By systematically generating diverse inputs and analyzing model behaviors, it aims to detect bugs, adversarial examples, and corner cases, enhancing the reliability and security of AI applications.
--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

1. Requirements - (we used both google colab and vs code for this)
        Python version: 3.10.12 (main, Nov 20 2023, 15:14:05) [GCC 11.4.0]
        TensorFlow version: 2.15.0
        Keras version: 2.15.0
        h5py version: 3.9.0
        Pillow version: 9.4.0
        OpenCV version: 4.8.0

   (use "pip install" to install all the requirements or use google colab)

2. Dataset - We use MNIST dataset which contains handwritten images of number, The dataset has been directly imported keras, then loaded and preprocessed.
   
3. Code - Result.ipynb is the main code file where two models (LENET - 1 and LENET - 4) are used and three transformations are used (Blackout, light and Occulsion).
          parameter.py is the code file that just contains the parameters used for diffferent transformation.
   
4. Result.ipynb and result 1.py are the main code files, if using google colab use Result.ipynb directly and run each cell one by one in sequence.

5. You will be prompted to mount your google drive as it is important.
   
6. generated_input_test, generated_input_train, lenet1.best.hdf5 and lenet4.best.hdf5 these are the required files to run the code. Unzip and upload the files to google drive nad mount the drive. You might also have to change the path whereever required accordingly while running each cell.

7. Generating inputs for train and test takes alot of time approx. 5 hrs each hence already generated inputs are used to train the models.

8. Accuracy and loss will be shown with the help of a plot to make it easy to understand.

