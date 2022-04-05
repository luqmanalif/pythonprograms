#examine 3 variables xyz and print largest odd number among them. If none are odd, print no odd numbers.
x = int(input('please put the value of x '))
y = int(input('please put the value of y '))
z = int(input('please put the value of z '))

variables = list((x,y,z))

oddvariables = [x for x in variables if x%2 != 0]

if len(oddvariables) != 0:
  largestodd = str(max(oddvariables))
  print('the largest odd number is ' + largestodd)
else:
  print('no odd number in x, y, z.')