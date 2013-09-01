#utf8     maps bytes to character code points
#unicode (is a character set) that maps integer character code points and characters

# Broken encoding:
broken = 'ETC\x85|ATTORN'
print broken    # =>  ETC?|ATTORN

# The hexadecimal \x85 has a value 133:
print 0x85   # => 133
# This is invalid for ASCII, Latin-1 and UTF-8 encoding because:
# ASCII:  133 is out of the character codepoint range.
# Latin-1:  133 is within the range but corresponds to nothing
# UTF-8 and unicode:  133 is the bit pattern bit:
bin(133)   # => 1000 0101
# Which is invalid in utf8 without a preceding character starting with 110x xxxx

# It turns out it is infact a valid character under Windows-1250—Windows-1258 and 
# in IBM/MS-DOS character encoding  where it represents an ellipsis (link to 
# wikipedia article:  http://en.wikipedia.org/wiki/Ellipsis )
