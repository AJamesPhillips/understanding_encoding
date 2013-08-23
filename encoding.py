# -*- coding: utf-8 -*-


def binStr(i):
  return bin(i).replace('0b', '')

def bin2hex(b):
  return hex(int(b, 2))


# we want 怯  but let's say it's been incorrectly decoded into latin-1

bad = '怯'.decode('latin1')

# now it's a series of bytes like:
st = u'\xe6\x80\xaf'
print st == bad

# These come from the fact that 怯 has a unicode character point of: 0x602f  (and as an base 10 integer of: 24623 )

print binStr(24623)  # => 110 000000 101111
# as utf-8 this would then be (we've put a 0 as padding)
# 1110 0 110    10 000000    10 101111

# which in hex this bit string would be represented as:
# 11100110 10000000 10101111  # =>  '\xc6\x80\xaf'
# e.g.:
print bin2hex('11100110') == '0xe6'

# Now if you just printed the string:
print st # => æ¯
# this happens because those bytes are those latin-1, e.g.:
# 11100110 == 230 == latin-1 character of æ  (See: http://en.wikipedia.org/wiki/ISO/IEC_8859-1 )

# Now if we choose the correct encoding for the previously incorrectly encoded character and you're there!
print st.encode('latin1') # => 怯

#and to store this correctly as utf8 it's:
correct = st.encode('latin1').decode('utf8')
