# Cyrus Smith (https://github.com/smithcyr/project_euler)
# 
# http://projecteuler.net/problem=33
import string
import re
import fractions
prod = 1
for y in range(10,99):
  # fractions must evaluate to be less than 1
  for x in range(10,y):
    # canceling zero's is trivial
    if x%10==0 and y%10==0:
      continue
    # take the intersection of the sets of digits that make up x and y 
    # and combine those numbers in a list
    similar = "".join(list(set(str(x))&set(str(y))))
    # only if the number of shared characters is 1
    if len(similar)==1:
      # and the canceling doesn't leave the denominator 0 or either
      # the numerator or denominator NULL 
      if re.sub(similar,"",str(x)) != "" and \
         re.sub(similar,"",str(y)) != "" and \
         re.sub(similar,"",str(y)) != "0": 
        # and the value of the original fraction is equal to the new canceled fraction
        if float(x)/y == float(re.sub(similar,"",str(x)))/float(re.sub(similar,"",str(y))):
          # then continue the multiplication AND assignment
          prod *= (float(x)/y)
# limit_denominator() reduces the fraction
print fractions.Fraction(prod).limit_denominator().denominator
