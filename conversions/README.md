## OTF Output

This directory contains `.otf` generated files from the `legacy-soruces/mf-ethiop` folders, the subdirectories here
mirror the directories from source folder.

### convert-mf.sh
This is a batch file which takes the source directory as an argument and converts `.mf`
files in subdirectories thereof.  `convert-mf.sh` passes the `.mf` files it finds to the
`mf2ff.py` script.  Output files are then copied over locally and the `.log` files that
get created are deleted. 

### mf2ff.py
This is a slightly modified version of the original that avoids failing when irregular
responses come back from an API that handles the `fontdimen` metafont command.  The
numbers being returned contain a `:` only, or also with a number like `:5` .  Why this
happens is unknown, it is likely to do with the age of the source metafont files (possible
syntaax errors) or with limitations in the mf2ff.py fascility.

The original source can be found at [https://github.com/mf2vec-dev/mf2ff](https://github.com/mf2vec-dev/mf2ff)
