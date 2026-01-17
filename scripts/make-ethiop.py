#
# This script will generate OpenType and TrueType font files from a UFO
# source and removes contour overlaps in the process. The resulting
# outlines appear superior to those created from a TrueType/OpenType
# exports from FontLab Studio 8.4 or from Google's "fontmake" utility
# run as per:
#
#   fontmake -u Ethiop_main.ufo --overlaps-backend pathops -o ttf
#
#
from datetime import datetime
from defcon import Font
from ufo2ft import compileOTF, compileTTF
import os

prfx = str(datetime.now()).split('.')[0].replace(":", "-").replace(" ", "_")

# create output dir if it doesn't exist:
if not os.path.exists('test-fonts'):
    os.makedirs('test-fonts')

ufo = Font('Source-UFO/Ethiop_main.ufo')

otf = compileOTF(ufo, removeOverlaps=True)
otf.save('test-fonts/%s_Ethiop_main.otf' % prfx)

ttf = compileTTF(ufo, removeOverlaps=True)
ttf.save('test-fonts/%s_Ethiop_main.ttf' % prfx)
