# Land Scanning "App"

There are the following components to the land scanning "application"
that we used to make a Blender surface:

1. Elsa Landcaster. This script scans the land at intervals of 2
   meters, starting with (1,1). It serves HTTP requests for specific
   scan lines.
2. URL-4. A python script that, given the URL of the landcaster, scans
   all 128 lines and writes a file with the result.
3. graymap.main, a python script that reads a scan file and draws a
   gray-scale map of the height values.
4. land_script.py, a python script for Blender, that creates a mesh
   whose x,y,z are those in a scan file.

## Elsa Landcaster (landcaster.lsl)

This LSL script provides an HTTP address that receives GET requests
including an integer parameter that selects the line to be scanned,
`URL/?3` scans a line with x = 3, y = 1, 3, 5, ..., 255. The line is
returned as the body of the response, lightly formatted with the line
number on the front and // on the back.

## URL-4

This Python script just opens a specified output file and reads lines
1,3,5,...,255 from a specified URL, saving the lines into its output
file. This script was typically run under Pythonista on the iPad.

The file was moved manually, via Dropbox, to my desktop.

## graymap

The main program provided here mangles the z values a bit and draws a
gray-scale map of the data from a landcaster file. It was just used as
a visualization tool, although it has alwo been used to build a
surface in Blender.

## land_script.py

This script, executed in blender, will read the specified file and
produce a mesh object whose x,y,z values are those in the file, with a
face in each quad, facing toward positive z. 


