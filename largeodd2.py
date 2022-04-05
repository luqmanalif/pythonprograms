iteration = 10
variables = []

while iteration != 0:
    values = int(input('please input a number (' + str(iteration) + ' more times)'))
    variables.append(values)
    iteration = iteration - 1

oddvariables = [x for x in variables if x%2 != 0]

if len(oddvariables) != 0:
  largestodd = str(max(oddvariables))
  print('the largest odd number is ' + largestodd)
else:
  print('no odd number in x, y, z.')