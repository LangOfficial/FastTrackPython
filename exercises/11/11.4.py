# 11-4. Is the Word Short or Long?

def is_short_or_long(s):
  if len(s) >= 10: # or > 9
    return f"'{s}' is long"
  else:
    return f"'{s}' is short"
  
# with ternary
def is_short_or_long_2(s):
  # return f"'{s}' is long" if len(s) >= 10 else f"'{s}' is short"
  # Commented ternary might be a little repetitive to some but there's nothing inherently wrong.

  s_length = 'long' if len(s) >= 10 else 'short'
  return f"'{s}' is {s_length}"

long_string = 'This is long I hope.'
print(is_short_or_long(long_string))

short_string = 'short'
print(is_short_or_long(short_string))