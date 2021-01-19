# screenshotter python utility

## USAGE

conf.json can contain up to 4 variables :
 - `x`: left-most pixel at which to start the capture. Default value : 0.
 - `y`: up-most pixel at which to start the capture. Default value : 0.
 - `width`: right-most pixel at which to STOP the capture. Must be provided.
 - `heigth`: bot-most pixel at which to STOP the capture. Must be provided.

It follows that `width` and `heigth` must be GREATER than `x`, `y`, respectively.

Execute the program by double clicking on `screenshotter.bat`.
The output image will always be located in the local folder and be named `img.png`.
Hence, images to be saved MUST BE backed up before re-capturing.
