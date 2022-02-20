# AIS-LBS-model
-data.py file:
  
This program is made to capture the images we will use for our Machine Learning Model.  
This is accomplished by using screen capture technology but for this to work for your computer there  
may be extra steps required.  
  
Make sure your M64PY file is open when the program is started and that the edges are exposed. 
the program will let you know if the images you are using to find the emulator screen is not  
working. In that case you may need to screenshot the edges of the M64PY emularator on your computer and replace  
them manually.  

in the emulator itself make sure the controls are configured correctly.  
this can be found in the emulator itself under  settings>plugins  
then press the configure button in the input box.

the controller configuration should look like this.
!('readme_imgs\controllerConfig.png')

currently the data automaticly splits into an 80/20 training/testing split  
in the future we may change that into a training/validation split but currently  
this works for the program
  
to be clear the data.py file is what is working at the moment. the model still needs a little work.

if the automatic open function is not working feel free to comment out the line its called on.