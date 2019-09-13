# Blender_Library_Port_for_Lambda
This is the Blender library standalone package to go on the lambda package. It integrates with the python code nicely.
Just add the necessary code in the file lambda_function.py and use import bpy for the import to work. Uninstall any existing blender
installation so that python can recognize it. Almost all of the blender tasks can be performed by this.

Requirements:

1. Python 3.6
2. Tested remotely on Amazon linux but it will work on other linux distros too.
3. Put Bpy in the root folder of the project.
4. Tested on lambda as package and working nicely.

Sample code is provided which when executed imports libraries.
