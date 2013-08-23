#utf8     maps bytes to character code points
#unicode (is a character set) that maps integer character code points and characters

# Broken encoding:
broken = 'ETC\x85|ATTORN'
print broken    # =>  ETC?|ATTORN

# The hexadecimal \x85 has a value 133:
print 0x85   # => 133
# This is invalid for ASCII, Latin-1 and UTF-8 encoding because:
# ASCII:  133 is out character codepoint range.
# Latin-1:  133 is within the range but corresponds to nothing
# UTF-8 and unicode:  133 is the bit pattern bit:
bin(133)   # => 1000 0101
# Which is invalid in utf8 without a preceding character starting with 110x xxxx
