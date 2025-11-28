#!/bin/bash

# /usr/local/opt/python\@3.14/libexec/bin/python mf2ff.py

export PYTHONPATH="/usr/local/Cellar/fontforge/20251009_1/lib/python3.14/site-packages/"

ffpython=/usr/local/opt/python\@3.14/libexec/bin/python


echo "ARG: $1"
ls -d $1/* |
while read dir
do
	if [ -d $dir ] ; then
		echo "DIR: $dir"
		ls $dir/*.mf  |
		while read file
		do
			echo "    FILE: $file"
			outfile=`echo $file | cut -d. -f3`
			outfile="..$outfile.otf"
			logfile=`echo $file | cut -d. -f3`
			logfile="..$logfile.log"
			# echo "    OUTFILE: $outfile"
			# echo "    LOGFILE: $logfile"
			$ffpython mf2ff.py -otf $file
			rm $logfile
			mv $outfile .
		done
	fi
done


