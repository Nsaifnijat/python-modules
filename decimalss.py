# -*- coding: utf-8 -*-

#decimal is used to find the precision and scale of a number
#remember variable has to be a string else floats has varying scale
#in the following number precision is 3 and scale is 4
import decimal

a='644.4545'
#changing to decimal
decimalling=decimal.Decimal(a)
print(decimalling)

floats_scale=decimalling.as_tuple().exponent
floats_precision=decimalling.as_tuple().
print(floats_scale)
print(floats_precision)
