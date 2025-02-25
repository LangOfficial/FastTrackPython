# 14-6. Alternate Casing

def alternate_case(s):
  alt_case = [char.upper() if index % 2 == 0 else char.lower() for index, char in enumerate(s)]
  return ''.join(alt_case)

print(alternate_case("Hello guys!"))