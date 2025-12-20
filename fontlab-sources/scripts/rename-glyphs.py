#
# Rename the glyphs to uniWXYZ convetion
#
for glyph in cf.values():
  unicode = glyph.unicode
  if( (unicode != None) and (unicode >= 0x1200) ):
    newName = "uni%X" % unicode
    print( glyph.name , " => ", newName )
    glyph.name = newName
