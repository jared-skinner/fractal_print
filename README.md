# fractal_print

Creates individual iterations of fractals for use with a laser cutter



![fractal](example.png)


### Setup

You will need a copy of Python 3.x to run this script.  In addition the following modules are required:

* numpy
* matplotlib
* argparse

These can be installed with relative ease using they python pip module (this comes standard with python 3.4 and later)

```
pip install <package>
```


### Usage

mandelbrot.py does have default values to generating a plot, but you can specify the xmin, xmax, ymin, ymax and the number of iterations you wish to generate.  Images will be generated into the main folder and named i.png for the i-th iteration. 

```
python mandelbrot.py --xmin <xmin> --xmax <xmax> --ymin <ymin> --ymax <ymax> --iter <iter>
```
