Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> l = [10,2,3]
>>> sorted(l, reverse=True)
[10, 3, 2]
>>> list(reveresed([2,4,5,6]))
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    list(reveresed([2,4,5,6]))
NameError: name 'reveresed' is not defined
>>> list(reversed([2,4,5,6]))
[6, 5, 4, 2]
>>> if (value=2.1)
SyntaxError: invalid syntax
>>> counter = 0
>>> while checkpositive(salary)
SyntaxError: invalid syntax
>>> while checkpositive(salary):
	if counter == 0:
		taxrate = 0%
		
SyntaxError: invalid syntax
>>> while checkpositive(salary):
	if counter == 0:
		taxrate = 0
	elif counter == 1:
		taxrate = 0.1
	elif counter == 2:
		raxrate = 0.15
	elif counter == 3:
		taxrate = 0.2
	elif counter == 4:
		taxrate = 0.25
	else:
		taxrate = 0.3%
		
SyntaxError: invalid syntax
>>> def salarydecuct(salary):
	if salary <= 1000:
		remainder = salary - 1000
		salarydecuct(remainder)
	elif salary >=1000 and salary >= 1001:
		%
		
SyntaxError: invalid syntax
>>> def calculate_tax(dict x ={}):
	
SyntaxError: invalid syntax
>>> def calculate_tax(dict x):
	
SyntaxError: invalid syntax
>>> def calculate_tax(x = dict{}):
	
SyntaxError: invalid syntax
>>> def calculate_tax(x =dict()):
	for key, value in x.iteritems():
		name = key
		value = x[key]
		%
		
SyntaxError: invalid syntax
>>> def cutsalary(salary, cutlevel):
	if  cutlevel = 1:
		
SyntaxError: invalid syntax
>>> def cutsalary(salary, cutlevel):
	if  cutlevel == 1:
		remainder = salary - 1000
		*
		
SyntaxError: invalid syntax
>>> level = 1
>>> level += 1
>>> level
2
>>> def get_tax(salary, remainder, level = 1, deducted = 0, total = 0):
  if remainder == 0 or salary < 1000 or level > 6:
      return total
  else:
    if level ==  1:
      total += 1000 * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if salary >= 10000:
        taxval = 10000 - deducted
      else:
        taxval = salary -deducted
      total += taxval * 0.10
      deducted = 10000
      remainder = salary - deducted
    elif level == 3:
      if salary <= 20200
        taxval = 20200 - deducted
      else:
        taxval = salary -deducted
      total += taxval * 0.15
      deducted = 20200
    elif level == 4:
      if salary <= 30750:
        taxval = 30750 - deducted
      else:
        taxval = salary -deducted
      total += taxval * 0.20
      deducted = 30750
    elif level == 5:
      if salary <= 50000:
        taxval = 50000 - deducted
      else:
        taxval = salary - deducted
      remainder = salary - 50000
      total += taxval * 0.25
      deducted = 50000
    elif level == 6:
      if salary > 50000:
        taxval = 50000 - deducted
      remainder = 0
      total  += taxval * 0.3
      deducted = 50000
    level += 1
    return get_tax(salary, remainder, level, deducted, total)
SyntaxError: invalid syntax
>>> def get_tax(salary, remainder, level = 1, deducted = 0, total = 0):
  if remainder == 0 or salary < 1000 or level > 6:
      return total
  else:
    if level ==  1:
      total += 1000 * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if salary >= 10000:
        taxval = 10000 - deducted
      else:
        taxval = salary -deducted
      total += taxval * 0.10
      deducted = 10000
      remainder = salary - deducted
    elif level == 3:
      if salary <= 20200:
        taxval = 20200 - deducted
      else:
        taxval = salary -deducted
      total += taxval * 0.15
      deducted = 20200
    elif level == 4:
      if salary <= 30750:
        taxval = 30750 - deducted
      else:
        taxval = salary -deducted
      total += taxval * 0.20
      deducted = 30750
    elif level == 5:
      if salary <= 50000:
        taxval = 50000 - deducted
      else:
        taxval = salary - deducted
      remainder = salary - 50000
      total += taxval * 0.25
      deducted = 50000
    elif level == 6:
      if salary > 50000:
        taxval = 50000 - deducted
      remainder = 0
      total  += taxval * 0.3
      deducted = 50000
    level += 1
    return get_tax(salary, remainder, level, deducted, total)

>>> get_tax(20500, 0, 1, 0, 0)
0
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0):
  if ((remainder == 0) and (level > 1)) or (salary < 1000) or (level > 6):
      return total
  else:
    if level ==  1:
      total += 1000 * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if salary >= 10000:
        taxval = 10000 - deducted
      else:
        taxval = salary -deducted
      total += taxval * 0.10
      deducted = 10000
      remainder = salary - deducted
    elif level == 3:
      if salary <= 20200:
        taxval = 20200 - deducted
      else:
        taxval = salary -deducted
      total += taxval * 0.15
      deducted = 20200
    elif level == 4:
      if salary <= 30750:
        taxval = 30750 - deducted
      else:
        taxval = salary -deducted
      total += taxval * 0.20
      deducted = 30750
    elif level == 5:
      if salary <= 50000:
        taxval = 50000 - deducted
      else:
        taxval = salary - deducted
      remainder = salary - 50000
      total += taxval * 0.25
      deducted = 50000
    elif level == 6:
      if salary > 50000:
        taxval = 50000 - deducted
      remainder = 0
      total  += taxval * 0.3
      deducted = 50000
    level += 1
    return get_tax(salary, remainder, level, deducted, total)

>>> get_tax(20500)
Traceback (most recent call last):
  File "<pyshell#56>", line 1, in <module>
    get_tax(20500)
  File "<pyshell#55>", line 46, in get_tax
    return get_tax(salary, remainder, level, deducted, total)
  File "<pyshell#55>", line 46, in get_tax
    return get_tax(salary, remainder, level, deducted, total)
  File "<pyshell#55>", line 46, in get_tax
    return get_tax(salary, remainder, level, deducted, total)
  File "<pyshell#55>", line 46, in get_tax
    return get_tax(salary, remainder, level, deducted, total)
  File "<pyshell#55>", line 46, in get_tax
    return get_tax(salary, remainder, level, deducted, total)
  File "<pyshell#55>", line 43, in get_tax
    total  += taxval * 0.3
UnboundLocalError: local variable 'taxval' referenced before assignment
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0):
  if ((remainder == 0) and (level > 1)) or (salary < 1000) or (level > 6):
      return total
  else:
    taxval = salary - deducted
    if level ==  1:
      total += 1000 * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if salary >= 10000:
        taxval = 10000 - deducted
      total += taxval * 0.10
      deducted = 10000
      remainder = salary - deducted
    elif level == 3:
      if salary <= 20200:
        taxval = 20200 - deducted
      total += taxval * 0.15
      deducted = 20200
    elif level == 4:
      if salary <= 30750:
        taxval = 30750 - deducted
      total += taxval * 0.20
      deducted = 30750
    elif level == 5:
      if salary <= 50000:
        taxval = 50000 - deducted
      remainder = salary - 50000
      total += taxval * 0.25
      deducted = 50000
    elif level == 6:
      if salary > 50000:
        taxval = 50000 - deducted
        total  += taxval * 0.3
        deducted = 50000
      remainder = 0
    level += 1
    return get_tax(salary, remainder, level, deducted, total)

>>> get_tax(20500)
9397.5
>>> get_tax(500)
0
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0):
  if ((remainder == 0) and (level > 1)) or (salary < 1000) or (level > 6):
      return total
  else:
    taxval = salary - deducted
    if level ==  1:
      taxval = 1000
      total += taxval * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if salary <= 10000:
        taxval = 9000
      total += taxval * 0.10
      deducted = 10000
      remainder = salary - deducted
    elif level == 3:
      if salary <= 20200:
        taxval = 20200 - deducted
      total += taxval * 0.15
      deducted = 20200
    elif level == 4:
      if salary <= 30750:
        taxval = 30750 - deducted
      total += taxval * 0.20
      deducted = 30750
    elif level == 5:
      if salary <= 50000:
        taxval = 50000 - deducted
      remainder = salary - 50000
      total += taxval * 0.25
      deducted = 50000
    elif level == 6:
      if salary > 50000:
        taxval = 50000 - deducted
        total  += taxval * 0.3
        deducted = 50000
      remainder = 0
    level += 1
    return get_tax(salary, remainder, level, deducted, total)

>>> get_tax(20500)
10447.5
>>> get_tax(20500)
10447.5
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0):
  if ((remainder == 0) and (level > 1)) or (salary < 1000) or (level > 6):
      return total
  else:
    taxval = salary - deducted
    if level ==  1:
      taxval = 1000
      total += taxval * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if salary <= 10000:
        taxval = 9000
      total += taxval * 0.10
      deducted = 10000
      remainder = salary - deducted
    elif level == 3:
      if salary <= 20200:
        taxval = 20200 - deducted
      total += taxval * 0.15
      deducted = 20200
    elif level == 4:
      if salary <= 30750:
        taxval = 30750 - deducted
      total += taxval * 0.20
      deducted = 30750
    elif level == 5:
      if salary <= 50000:
        taxval = 50000 - deducted
      remainder = salary - 50000
      total += taxval * 0.25
      deducted = 50000
    elif level == 6:
      if salary > 50000:
        taxval = 50000 - deducted
        total  += taxval * 0.3
        deducted = 50000
      remainder = 0
    level += 1
    print(salary, level, deduction, total, taxval)
    return get_tax(salary, remainder, level, deducted, total)

>>> get_tax(20500)
Traceback (most recent call last):
  File "<pyshell#67>", line 1, in <module>
    get_tax(20500)
  File "<pyshell#66>", line 40, in get_tax
    print(salary, level, deduction, total, taxval)
NameError: name 'deduction' is not defined
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0)
  if ((remainder == 0) and (level > 1)) or (salary < 1000) or (level > 6):
      return total
  else:
    taxval = salary - deducted
    print('Begining: ', salary, level, deducted, total, taxval, remainder)
    if level ==  1:
      taxval = 1000
      total += taxval * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if salary <= 10000:
        taxval = 9000
      total += taxval * 0.10
      deducted = 10000
      remainder = salary - deducted
    elif level == 3:
      if salary <= 20200:
        taxval = 20200 - deducted
      total += taxval * 0.15
      deducted = 20200
    elif level == 4:
      if salary <= 30750:
        taxval = 30750 - deducted
      total += taxval * 0.20
      deducted = 30750
    elif level == 5:
      if salary <= 50000:
        taxval = 50000 - deducted
      remainder = salary - 50000
      total += taxval * 0.25
      deducted = 50000
    elif level == 6:
      if salary > 50000:
        taxval = 50000 - deducted
        total  += taxval * 0.3
        deducted = 50000
      remainder = 0
    level += 1
    print('End: ',salary, level, deducted, total, taxval)
    print('')
    return get_tax(salary, remainder, level, deducted, total)
SyntaxError: invalid syntax
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0):
  if ((remainder == 0) and (level > 1)) or (salary < 1000) or (level > 6):
      return total
  else:
    taxval = salary - deducted
    print('Begining: ', salary, level, deducted, total, taxval, remainder)
    if level ==  1:
      taxval = 1000
      total += taxval * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if salary <= 10000:
        taxval = 9000
      total += taxval * 0.10
      deducted = 10000
      remainder = salary - deducted
    elif level == 3:
      if salary <= 20200:
        taxval = 20200 - deducted
      total += taxval * 0.15
      deducted = 20200
    elif level == 4:
      if salary <= 30750:
        taxval = 30750 - deducted
      total += taxval * 0.20
      deducted = 30750
    elif level == 5:
      if salary <= 50000:
        taxval = 50000 - deducted
      remainder = salary - 50000
      total += taxval * 0.25
      deducted = 50000
    elif level == 6:
      if salary > 50000:
        taxval = 50000 - deducted
        total  += taxval * 0.3
        deducted = 50000
      remainder = 0
    level += 1
    print('End: ',salary, level, deducted, total, taxval)
    print('')
    return get_tax(salary, remainder, level, deducted, total)

>>> get_tax(20500)
Begining:  20500 1 0 0 20500 0
End:  20500 2 1000 0 1000

Begining:  20500 2 1000 0 19500 19500
End:  20500 3 10000 1950.0 19500

Begining:  20500 3 10000 1950.0 10500 10500
End:  20500 4 20200 3525.0 10500

Begining:  20500 4 20200 3525.0 300 10500
End:  20500 5 30750 5635.0 10550

Begining:  20500 5 30750 5635.0 -10250 10500
End:  20500 6 50000 10447.5 19250

Begining:  20500 6 50000 10447.5 -29500 -29500
End:  20500 7 50000 10447.5 -29500

10447.5
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0)
  if ((remainder == 0) and (level > 1)) or (salary < 1000) or (level > 6):
      return total
  else:
    taxval = salary - deducted
    print('Begin: ','salary:',salary,' level:', level, ' deducted:',deducted,' taxval:',taxval,' remainder:',remainder,' total:',total)
    if level ==  1:
      taxval = 1000
      total += taxval * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if salary <= 10000:
        taxval = 9000
      total += taxval * 0.10
      deducted = 10000
      remainder = salary - deducted
    elif level == 3:
      if salary <= 20200:
        taxval = 20200 - deducted
      total += taxval * 0.15
      deducted = 20200
    elif level == 4:
      if salary <= 30750:
        taxval = 30750 - deducted
      total += taxval * 0.20
      deducted = 30750
    elif level == 5:
      if salary <= 50000:
        taxval = 50000 - deducted
      remainder = salary - 50000
      total += taxval * 0.25
      deducted = 50000
    elif level == 6:
      if salary > 50000:
        taxval = 50000 - deducted
        total  += taxval * 0.3
        deducted = 50000
      remainder = 0
    level += 1
    print('End: ','salary:',salary,' level:', level, ' deducted:',deducted,' taxval:',taxval,' remainder:',remainder,' total:',total)
    print('')
    return get_tax(salary, remainder, level, deducted, total)
SyntaxError: invalid syntax
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0):
  if ((remainder == 0) and (level > 1)) or (salary < 1000) or (level > 6):
      return total
  else:
    taxval = salary - deducted
    print('Begin: ','salary:',salary,' level:', level, ' deducted:',deducted,' taxval:',taxval,' remainder:',remainder,' total:',total)
    if level ==  1:
      taxval = 1000
      total += taxval * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if salary <= 10000:
        taxval = 9000
      total += taxval * 0.10
      deducted = 10000
      remainder = salary - deducted
    elif level == 3:
      if salary <= 20200:
        taxval = 20200 - deducted
      total += taxval * 0.15
      deducted = 20200
    elif level == 4:
      if salary <= 30750:
        taxval = 30750 - deducted
      total += taxval * 0.20
      deducted = 30750
    elif level == 5:
      if salary <= 50000:
        taxval = 50000 - deducted
      remainder = salary - 50000
      total += taxval * 0.25
      deducted = 50000
    elif level == 6:
      if salary > 50000:
        taxval = 50000 - deducted
        total  += taxval * 0.3
        deducted = 50000
      remainder = 0
    level += 1
    print('End: ','salary:',salary,' level:', level, ' deducted:',deducted,' taxval:',taxval,' remainder:',remainder,' total:',total)
    print('')
    return get_tax(salary, remainder, level, deducted, total)

>>> get_tax(20500)
Begin:  salary: 20500  level: 1  deducted: 0  taxval: 20500  remainder: 0  total: 0
End:  salary: 20500  level: 2  deducted: 1000  taxval: 1000  remainder: 19500  total: 0

Begin:  salary: 20500  level: 2  deducted: 1000  taxval: 19500  remainder: 19500  total: 0
End:  salary: 20500  level: 3  deducted: 10000  taxval: 19500  remainder: 10500  total: 1950.0

Begin:  salary: 20500  level: 3  deducted: 10000  taxval: 10500  remainder: 10500  total: 1950.0
End:  salary: 20500  level: 4  deducted: 20200  taxval: 10500  remainder: 10500  total: 3525.0

Begin:  salary: 20500  level: 4  deducted: 20200  taxval: 300  remainder: 10500  total: 3525.0
End:  salary: 20500  level: 5  deducted: 30750  taxval: 10550  remainder: 10500  total: 5635.0

Begin:  salary: 20500  level: 5  deducted: 30750  taxval: -10250  remainder: 10500  total: 5635.0
End:  salary: 20500  level: 6  deducted: 50000  taxval: 19250  remainder: -29500  total: 10447.5

Begin:  salary: 20500  level: 6  deducted: 50000  taxval: -29500  remainder: -29500  total: 10447.5
End:  salary: 20500  level: 7  deducted: 50000  taxval: -29500  remainder: 0  total: 10447.5

10447.5
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0):
  if (level > 6) or ((remainder == 0) and (level > 1)) or (salary < 1000):
      return total
  else:
    taxval = remainder
    if level ==  1:
      taxval = 1000
      total += taxval * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if (10000 - deducted) >= 0:
        taxval = 9000
      total += taxval * 0.1
      deducted = 10000
      remainder = salary - 10000
    elif level == 3:
      if (20200 - deducted) >= 0:
        taxval = 10200
      total += taxval * 0.15
      deducted = 20200
      remainder = salary - 20200
    elif level == 4:
      if (30750 - deducted) >= 0:
        taxval = 10550
      total += taxval * 0.20
      deducted = 30750
      remainder = salary - 30750
    elif level == 5:
      if salary <= 50000:
        taxval = 19250
      total += taxval * 0.25
      deducted = 50000
      remainder = salary - 50000
    elif level == 6:
      if salary > 50000:
        taxval = 50000 - deducted
        total  += taxval * 0.3
        deducted = 50000
        remainder = 0
    level += 1
    return get_tax(salary, remainder, level, deducted, total)

>>> get_tax(20500)
9352.5
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0):
  if (level > 6) or ((remainder == 0) and (level > 1)) or (salary < 1000):
      return total
  else:
    taxval = remainder
    print('Begin: ','salary:',salary,' level:', level, ' deducted:',deducted,' taxval:',taxval,' remainder:',remainder,' total:',total)
    if level ==  1:
      taxval = 1000
      total += taxval * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if (10000 - deducted) >= 0:
        taxval = 9000
      total += taxval * 0.1
      deducted = 10000
      remainder = salary - 10000
    elif level == 3:
      if (20200 - deducted) >= 0:
        taxval = 10200
      total += taxval * 0.15
      deducted = 20200
      remainder = salary - 20200
    elif level == 4:
      if (30750 - deducted) >= 0:
        taxval = 10550
      total += taxval * 0.20
      deducted = 30750
      remainder = salary - 30750
    elif level == 5:
      if salary <= 50000:
        taxval = 19250
      total += taxval * 0.25
      deducted = 50000
      remainder = salary - 50000
    elif level == 6:
      if salary > 50000:
        taxval = 50000 - deducted
        total  += taxval * 0.3
        deducted = 50000
        remainder = 0
    level += 1
    print('End: ','salary:',salary,' level:', level, ' deducted:',deducted,' taxval:',taxval,' remainder:',remainder,' total:',total)
    print('')
    return get_tax(salary, remainder, level, deducted, total)

>>> get_tax(20500)
Begin:  salary: 20500  level: 1  deducted: 0  taxval: 0  remainder: 0  total: 0
End:  salary: 20500  level: 2  deducted: 1000  taxval: 1000  remainder: 19500  total: 0

Begin:  salary: 20500  level: 2  deducted: 1000  taxval: 19500  remainder: 19500  total: 0
End:  salary: 20500  level: 3  deducted: 10000  taxval: 9000  remainder: 10500  total: 900.0

Begin:  salary: 20500  level: 3  deducted: 10000  taxval: 10500  remainder: 10500  total: 900.0
End:  salary: 20500  level: 4  deducted: 20200  taxval: 10200  remainder: 300  total: 2430.0

Begin:  salary: 20500  level: 4  deducted: 20200  taxval: 300  remainder: 300  total: 2430.0
End:  salary: 20500  level: 5  deducted: 30750  taxval: 10550  remainder: -10250  total: 4540.0

Begin:  salary: 20500  level: 5  deducted: 30750  taxval: -10250  remainder: -10250  total: 4540.0
End:  salary: 20500  level: 6  deducted: 50000  taxval: 19250  remainder: -29500  total: 9352.5

Begin:  salary: 20500  level: 6  deducted: 50000  taxval: -29500  remainder: -29500  total: 9352.5
End:  salary: 20500  level: 7  deducted: 50000  taxval: -29500  remainder: -29500  total: 9352.5

9352.5
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0):
  if (level > 6) or ((remainder == 0) and (level > 1)) or (salary < 1000):
      return total
  else:
    taxval = remainder
    print('Begin: ','salary:',salary,' level:', level, ' deducted:',deducted,' taxval:',taxval,' remainder:',remainder,' total:',total)
    if level ==  1:
      taxval = 1000
      total += taxval * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if (10000 - deducted) >= 0:
        taxval = 9000
      total += taxval * 0.1
      deducted = 10000
      remainder = salary - 10000
    elif level == 3:
      if (20200 - deducted) >= 0:
        taxval = 10200
      total += taxval * 0.15
      deducted = 20200
      remainder = salary - 20200
    elif level == 4:
      if (30750 - deducted) >= 0:
        taxval = 10550
      total += taxval * 0.20
      deducted = 30750
      remainder = salary - 30750
    elif level == 5:
      if salary <= 50000:
        taxval = 19250
      total += taxval * 0.25
      deducted = 50000
      remainder = salary - 50000
    elif level == 6:
      if salary > 50000:
        taxval = 50000 - deducted
        total  += taxval * 0.3
        deducted = 50000
        remainder = 0
    level += 1
    print('End: ','salary:',salary, ' deducted:',deducted,' taxval:',taxval,' remainder:',remainder,' total:',total)
    print('')
    return get_tax(salary, remainder, level, deducted, total)

>>> get_tax(20500)
Begin:  salary: 20500  level: 1  deducted: 0  taxval: 0  remainder: 0  total: 0
End:  salary: 20500  deducted: 1000  taxval: 1000  remainder: 19500  total: 0

Begin:  salary: 20500  level: 2  deducted: 1000  taxval: 19500  remainder: 19500  total: 0
End:  salary: 20500  deducted: 10000  taxval: 9000  remainder: 10500  total: 900.0

Begin:  salary: 20500  level: 3  deducted: 10000  taxval: 10500  remainder: 10500  total: 900.0
End:  salary: 20500  deducted: 20200  taxval: 10200  remainder: 300  total: 2430.0

Begin:  salary: 20500  level: 4  deducted: 20200  taxval: 300  remainder: 300  total: 2430.0
End:  salary: 20500  deducted: 30750  taxval: 10550  remainder: -10250  total: 4540.0

Begin:  salary: 20500  level: 5  deducted: 30750  taxval: -10250  remainder: -10250  total: 4540.0
End:  salary: 20500  deducted: 50000  taxval: 19250  remainder: -29500  total: 9352.5

Begin:  salary: 20500  level: 6  deducted: 50000  taxval: -29500  remainder: -29500  total: 9352.5
End:  salary: 20500  deducted: 50000  taxval: -29500  remainder: -29500  total: 9352.5

9352.5
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0):
  if (level > 6) or ((remainder == 0) and (level > 1)) or (salary < 1000):
      return total
  else:
    taxval = remainder
    print('Begin: ','salary:',salary,' level:', level, ' deducted:',deducted,' taxval:',taxval,' remainder:',remainder,' total:',total)
    if level ==  1:
      taxval = 1000
      total += taxval * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if 9000 < remainder:
        taxval = 9000
      total += taxval * 0.1
      deducted = 10000
      remainder = salary - 10000
    elif level == 3:
      if 20200 < remainder:
        taxval = 10200
      total += taxval * 0.15
      deducted = 20200
      remainder = salary - 20200
    elif level == 4:
      if 30750 < remainder:
        taxval = 10550
      total += taxval * 0.2
      deducted = 30750
      remainder = salary - 30750
    elif level == 5:
      if 19250 < remainder:
        taxval = 19250
      total += taxval * 0.25
      deducted = 50000
      remainder = salary - 50000
    elif level == 6:
      if salary > 50000:
        taxval = 50000 - deducted
        total  += taxval * 0.3
        deducted = 50000
        remainder = 0
    level += 1
    print('End: ','salary:',salary, ' deducted:',deducted,' taxval:',taxval,' remainder:',remainder,' total:',total)
    print('')
    return get_tax(salary, remainder, level, deducted, total)

>>> get_tax(20500)
Begin:  salary: 20500  level: 1  deducted: 0  taxval: 0  remainder: 0  total: 0
End:  salary: 20500  deducted: 1000  taxval: 1000  remainder: 19500  total: 0

Begin:  salary: 20500  level: 2  deducted: 1000  taxval: 19500  remainder: 19500  total: 0
End:  salary: 20500  deducted: 10000  taxval: 9000  remainder: 10500  total: 900.0

Begin:  salary: 20500  level: 3  deducted: 10000  taxval: 10500  remainder: 10500  total: 900.0
End:  salary: 20500  deducted: 20200  taxval: 10500  remainder: 300  total: 2475.0

Begin:  salary: 20500  level: 4  deducted: 20200  taxval: 300  remainder: 300  total: 2475.0
End:  salary: 20500  deducted: 30750  taxval: 300  remainder: -10250  total: 2535.0

Begin:  salary: 20500  level: 5  deducted: 30750  taxval: -10250  remainder: -10250  total: 2535.0
End:  salary: 20500  deducted: 50000  taxval: -10250  remainder: -29500  total: -27.5

Begin:  salary: 20500  level: 6  deducted: 50000  taxval: -29500  remainder: -29500  total: -27.5
End:  salary: 20500  deducted: 50000  taxval: -29500  remainder: -29500  total: -27.5

-27.5
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0):
  if (level > 6) or ((remainder <= 0) and (level > 1)) or (salary < 1000):
      return total
  else:
    taxval = remainder
    print('Begin: ','salary:',salary,' level:', level, ' deducted:',deducted,' taxval:',taxval,' remainder:',remainder,' total:',total)
    if level ==  1:
      taxval = 1000
      total += taxval * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if 9000 < remainder:
        taxval = 9000
      total += taxval * 0.1
      deducted = 10000
      remainder = salary - 10000
    elif level == 3:
      if 20200 < remainder:
        taxval = 10200
      total += taxval * 0.15
      deducted = 20200
      remainder = salary - 20200
    elif level == 4:
      if 30750 < remainder:
        taxval = 10550
      total += taxval * 0.2
      deducted = 30750
      remainder = salary - 30750
    elif level == 5:
      if 19250 < remainder:
        taxval = 19250
      total += taxval * 0.25
      deducted = 50000
      remainder = salary - 50000
    elif level == 6:
      if salary > 50000:
        taxval = 50000 - deducted
        total  += taxval * 0.3
        deducted = 50000
        remainder = 0
    level += 1
    print('End: ','salary:',salary, ' deducted:',deducted,' taxval:',taxval,' remainder:',remainder,' total:',total)
    print('')
    return get_tax(salary, remainder, level, deducted, total)

>>> get_tax(20500)
Begin:  salary: 20500  level: 1  deducted: 0  taxval: 0  remainder: 0  total: 0
End:  salary: 20500  deducted: 1000  taxval: 1000  remainder: 19500  total: 0

Begin:  salary: 20500  level: 2  deducted: 1000  taxval: 19500  remainder: 19500  total: 0
End:  salary: 20500  deducted: 10000  taxval: 9000  remainder: 10500  total: 900.0

Begin:  salary: 20500  level: 3  deducted: 10000  taxval: 10500  remainder: 10500  total: 900.0
End:  salary: 20500  deducted: 20200  taxval: 10500  remainder: 300  total: 2475.0

Begin:  salary: 20500  level: 4  deducted: 20200  taxval: 300  remainder: 300  total: 2475.0
End:  salary: 20500  deducted: 30750  taxval: 300  remainder: -10250  total: 2535.0

2535.0
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0):
  if (level > 6) or ((remainder <= 0) and (level > 1)) or (salary < 1000):
      return total
  else:
    taxval = remainder
    print('Begin: ','salary:',salary,' level:', level, ' deducted:',deducted,' taxval:',taxval,' remainder:',remainder,' total:',total)
    if level ==  1:
      taxval = 1000
      total += taxval * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if 9000 < remainder:
        taxval = 9000
      total += taxval * 0.1
      deducted = 10000
      remainder = salary - 10000
    elif level == 3:
      if 10200 < remainder:
        taxval = 10200
      total += taxval * 0.15
      deducted = 20200
      remainder = salary - 20200
    elif level == 4:
      if 10550 < remainder:
        taxval = 10550
      total += taxval * 0.2
      deducted = 30750
      remainder = salary - 30750
    elif level == 5:
      if 19250 < remainder:
        taxval = 19250
      total += taxval * 0.25
      deducted = 50000
      remainder = salary - 50000
    elif level == 6:
      if salary > 50000:
        taxval = 50000 - deducted
        total  += taxval * 0.3
        deducted = 50000
        remainder = 0
    level += 1
    print('End: ','salary:',salary, ' deducted:',deducted,' taxval:',taxval,' remainder:',remainder,' total:',total)
    print('')
    return get_tax(salary, remainder, level, deducted, total)

>>> get_tax(20500)
Begin:  salary: 20500  level: 1  deducted: 0  taxval: 0  remainder: 0  total: 0
End:  salary: 20500  deducted: 1000  taxval: 1000  remainder: 19500  total: 0

Begin:  salary: 20500  level: 2  deducted: 1000  taxval: 19500  remainder: 19500  total: 0
End:  salary: 20500  deducted: 10000  taxval: 9000  remainder: 10500  total: 900.0

Begin:  salary: 20500  level: 3  deducted: 10000  taxval: 10500  remainder: 10500  total: 900.0
End:  salary: 20500  deducted: 20200  taxval: 10200  remainder: 300  total: 2430.0

Begin:  salary: 20500  level: 4  deducted: 20200  taxval: 300  remainder: 300  total: 2430.0
End:  salary: 20500  deducted: 30750  taxval: 300  remainder: -10250  total: 2490.0

2490.0
>>> get_tax(70000)
Begin:  salary: 70000  level: 1  deducted: 0  taxval: 0  remainder: 0  total: 0
End:  salary: 70000  deducted: 1000  taxval: 1000  remainder: 69000  total: 0

Begin:  salary: 70000  level: 2  deducted: 1000  taxval: 69000  remainder: 69000  total: 0
End:  salary: 70000  deducted: 10000  taxval: 9000  remainder: 60000  total: 900.0

Begin:  salary: 70000  level: 3  deducted: 10000  taxval: 60000  remainder: 60000  total: 900.0
End:  salary: 70000  deducted: 20200  taxval: 10200  remainder: 49800  total: 2430.0

Begin:  salary: 70000  level: 4  deducted: 20200  taxval: 49800  remainder: 49800  total: 2430.0
End:  salary: 70000  deducted: 30750  taxval: 10550  remainder: 39250  total: 4540.0

Begin:  salary: 70000  level: 5  deducted: 30750  taxval: 39250  remainder: 39250  total: 4540.0
End:  salary: 70000  deducted: 50000  taxval: 19250  remainder: 20000  total: 9352.5

Begin:  salary: 70000  level: 6  deducted: 50000  taxval: 20000  remainder: 20000  total: 9352.5
End:  salary: 70000  deducted: 50000  taxval: 0  remainder: 0  total: 9352.5

9352.5
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0):
  if (level > 6) or ((remainder == 0) and (level > 1)) or (salary < 1000):
      return total
  else:
    taxval = remainder
    if level ==  1:
      taxval = 1000
      total += taxval * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if 9000 < remainder:
        taxval = 9000
      total += taxval * 0.1
      deducted = 10000
      remainder = salary - 10000
    elif level == 3:
      if 20200 < remainder:
        taxval = 10200
      total += taxval * 0.15
      deducted = 20200
      remainder = salary - 20200
    elif level == 4:
      if 30750 < remainder:
        taxval = 10550
      total += taxval * 0.2
      deducted = 30750
      remainder = salary - 30750
    elif level == 5:
      if 19250 < remainder:
        taxval = 19250
      total += taxval * 0.25
      deducted = 50000
      remainder = salary - 50000
    elif level == 6:
      if remainder > 0:
        total  += taxval * 0.3
        deducted = 50000
        remainder = 0
    level += 1
    return get_tax(salary, remainder, level, deducted, total)

>>> get_tax(70000)
15352.5
>>> get_tax(20500)
-27.5
>>> get_tax(20500)
-27.5
>>> get_tax(70000)
15352.5
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0):
  if (level > 6) or ((remainder <= 0) and (level > 1)) or (salary < 1000):
      return total
  else:
    taxval = remainder
    if level ==  1:
      taxval = 1000
      total += taxval * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if 9000 < remainder:
        taxval = 9000
      total += taxval * 0.1
      deducted = 10000
      remainder = salary - 10000
    elif level == 3:
      if 20200 < remainder:
        taxval = 10200
      total += taxval * 0.15
      deducted = 20200
      remainder = salary - 20200
    elif level == 4:
      if 30750 < remainder:
        taxval = 10550
      total += taxval * 0.2
      deducted = 30750
      remainder = salary - 30750
    elif level == 5:
      if 19250 < remainder:
        taxval = 19250
      total += taxval * 0.25
      deducted = 50000
      remainder = salary - 50000
    elif level == 6:
      if remainder > 0:
        total  += taxval * 0.3
        deducted = 50000
        remainder = 0
    level += 1
    return get_tax(salary, remainder, level, deducted, total)

>>> get_tax(20500)
2535.0
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0):
  if (level > 6) or ((remainder <= 0) and (level > 1)) or (salary < 1000):
      return total
  else:
    taxval = remainder
    print('Begin: ','salary:',salary,' level:', level, ' deducted:',deducted,' taxval:',taxval,' remainder:',remainder,' total:',total)
    if level ==  1:
      taxval = 1000
      total += taxval * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if 9000 < remainder:
        taxval = 9000
      total += taxval * 0.1
      deducted = 10000
      remainder = salary - 10000
    elif level == 3:
      if 10200 < remainder:
        taxval = 10200
      total += taxval * 0.15
      deducted = 20200
      remainder = salary - 20200
    elif level == 4:
      if 10550 < remainder:
        taxval = 10550
      total += taxval * 0.2
      deducted = 30750
      remainder = salary - 30750
    elif level == 5:
      if 19250 < remainder:
        taxval = 19250
      total += taxval * 0.25
      deducted = 50000
      remainder = salary - 50000
    elif level == 6:
      if remainder > 0:
        total  += taxval * 0.3
        deducted = 50000
        remainder = 0
    level += 1
    print('End: ','salary:',salary, ' deducted:',deducted,' taxval:',taxval,' remainder:',remainder,' total:',total)
    print('')
    return get_tax(salary, remainder, level, deducted, total)

>>> get
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    get
NameError: name 'get' is not defined
>>> get_tax(2500)
Begin:  salary: 2500  level: 1  deducted: 0  taxval: 0  remainder: 0  total: 0
End:  salary: 2500  deducted: 1000  taxval: 1000  remainder: 1500  total: 0

Begin:  salary: 2500  level: 2  deducted: 1000  taxval: 1500  remainder: 1500  total: 0
End:  salary: 2500  deducted: 10000  taxval: 1500  remainder: -7500  total: 150.0

150.0
>>> get_tax(20500)
Begin:  salary: 20500  level: 1  deducted: 0  taxval: 0  remainder: 0  total: 0
End:  salary: 20500  deducted: 1000  taxval: 1000  remainder: 19500  total: 0

Begin:  salary: 20500  level: 2  deducted: 1000  taxval: 19500  remainder: 19500  total: 0
End:  salary: 20500  deducted: 10000  taxval: 9000  remainder: 10500  total: 900.0

Begin:  salary: 20500  level: 3  deducted: 10000  taxval: 10500  remainder: 10500  total: 900.0
End:  salary: 20500  deducted: 20200  taxval: 10200  remainder: 300  total: 2430.0

Begin:  salary: 20500  level: 4  deducted: 20200  taxval: 300  remainder: 300  total: 2430.0
End:  salary: 20500  deducted: 30750  taxval: 300  remainder: -10250  total: 2490.0

2490.0
>>> get_tax(70000)
Begin:  salary: 70000  level: 1  deducted: 0  taxval: 0  remainder: 0  total: 0
End:  salary: 70000  deducted: 1000  taxval: 1000  remainder: 69000  total: 0

Begin:  salary: 70000  level: 2  deducted: 1000  taxval: 69000  remainder: 69000  total: 0
End:  salary: 70000  deducted: 10000  taxval: 9000  remainder: 60000  total: 900.0

Begin:  salary: 70000  level: 3  deducted: 10000  taxval: 60000  remainder: 60000  total: 900.0
End:  salary: 70000  deducted: 20200  taxval: 10200  remainder: 49800  total: 2430.0

Begin:  salary: 70000  level: 4  deducted: 20200  taxval: 49800  remainder: 49800  total: 2430.0
End:  salary: 70000  deducted: 30750  taxval: 10550  remainder: 39250  total: 4540.0

Begin:  salary: 70000  level: 5  deducted: 30750  taxval: 39250  remainder: 39250  total: 4540.0
End:  salary: 70000  deducted: 50000  taxval: 19250  remainder: 20000  total: 9352.5

Begin:  salary: 70000  level: 6  deducted: 50000  taxval: 20000  remainder: 20000  total: 9352.5
End:  salary: 70000  deducted: 50000  taxval: 20000  remainder: 0  total: 15352.5

15352.5
>>> get_tax(1000)
Begin:  salary: 1000  level: 1  deducted: 0  taxval: 0  remainder: 0  total: 0
End:  salary: 1000  deducted: 1000  taxval: 1000  remainder: 0  total: 0

0
>>> get_tax(500)
0
>>> get_tax(0)
0
>>> get_tax(-5)
0
>>> get(1000000)
Traceback (most recent call last):
  File "<pyshell#114>", line 1, in <module>
    get(1000000)
NameError: name 'get' is not defined
>>> get_tax(20500)
Begin:  salary: 20500  level: 1  deducted: 0  taxval: 0  remainder: 0  total: 0
End:  salary: 20500  deducted: 1000  taxval: 1000  remainder: 19500  total: 0

Begin:  salary: 20500  level: 2  deducted: 1000  taxval: 19500  remainder: 19500  total: 0
End:  salary: 20500  deducted: 10000  taxval: 9000  remainder: 10500  total: 900.0

Begin:  salary: 20500  level: 3  deducted: 10000  taxval: 10500  remainder: 10500  total: 900.0
End:  salary: 20500  deducted: 20200  taxval: 10200  remainder: 300  total: 2430.0

Begin:  salary: 20500  level: 4  deducted: 20200  taxval: 300  remainder: 300  total: 2430.0
End:  salary: 20500  deducted: 30750  taxval: 300  remainder: -10250  total: 2490.0

2490.0
>>> get_tax(70000)
Begin:  salary: 70000  level: 1  deducted: 0  taxval: 0  remainder: 0  total: 0
End:  salary: 70000  deducted: 1000  taxval: 1000  remainder: 69000  total: 0

Begin:  salary: 70000  level: 2  deducted: 1000  taxval: 69000  remainder: 69000  total: 0
End:  salary: 70000  deducted: 10000  taxval: 9000  remainder: 60000  total: 900.0

Begin:  salary: 70000  level: 3  deducted: 10000  taxval: 60000  remainder: 60000  total: 900.0
End:  salary: 70000  deducted: 20200  taxval: 10200  remainder: 49800  total: 2430.0

Begin:  salary: 70000  level: 4  deducted: 20200  taxval: 49800  remainder: 49800  total: 2430.0
End:  salary: 70000  deducted: 30750  taxval: 10550  remainder: 39250  total: 4540.0

Begin:  salary: 70000  level: 5  deducted: 30750  taxval: 39250  remainder: 39250  total: 4540.0
End:  salary: 70000  deducted: 50000  taxval: 19250  remainder: 20000  total: 9352.5

Begin:  salary: 70000  level: 6  deducted: 50000  taxval: 20000  remainder: 20000  total: 9352.5
End:  salary: 70000  deducted: 50000  taxval: 20000  remainder: 0  total: 15352.5

15352.5
>>> get_tax(30500)
Begin:  salary: 30500  level: 1  deducted: 0  taxval: 0  remainder: 0  total: 0
End:  salary: 30500  deducted: 1000  taxval: 1000  remainder: 29500  total: 0

Begin:  salary: 30500  level: 2  deducted: 1000  taxval: 29500  remainder: 29500  total: 0
End:  salary: 30500  deducted: 10000  taxval: 9000  remainder: 20500  total: 900.0

Begin:  salary: 30500  level: 3  deducted: 10000  taxval: 20500  remainder: 20500  total: 900.0
End:  salary: 30500  deducted: 20200  taxval: 10200  remainder: 10300  total: 2430.0

Begin:  salary: 30500  level: 4  deducted: 20200  taxval: 10300  remainder: 10300  total: 2430.0
End:  salary: 30500  deducted: 30750  taxval: 10300  remainder: -250  total: 4490.0

4490.0
>>> def calculate_tax(x = dict{}):
  if not x:
    return x
  else:
    newdict = dict()
    for key, value in x.iteritems():
      salary = x[key]
      newdict[key] = get_tax(salary)
  return newdict
SyntaxError: invalid syntax
>>> def calculate_tax(x = dict()):
  if not x:
    return x
  else:
    newdict = dict()
    for key, value in x.iteritems():
      salary = x[key]
      newdict[key] = get_tax(salary)
  return newdict

>>> calculate_tax({
    ‘Alex’: 500,
    ‘James’: 20500,
    ‘Kinuthia’: 70000
})
SyntaxError: invalid character in identifier
>>> calculate_tax({‘Alex’: 500,‘James’: 20500,‘Kinuthia’: 70000})
SyntaxError: invalid character in identifier
>>> calculate_tax({"Alex": 500,"James": 20500,"Kinuthia": 70000})
Traceback (most recent call last):
  File "<pyshell#123>", line 1, in <module>
    calculate_tax({"Alex": 500,"James": 20500,"Kinuthia": 70000})
  File "<pyshell#120>", line 6, in calculate_tax
    for key, value in x.iteritems():
AttributeError: 'dict' object has no attribute 'iteritems'
>>> def calculate_tax(x = dict()):
  if not x:
    return x
  else:
    newdict = dict()
    for key, value in x.iter_items():
      salary = x[key]
      newdict[key] = get_tax(salary)
  return newdict

>>> calculate_tax({‘Alex’: 500,‘James’: 20500,‘Kinuthia’: 70000})
SyntaxError: invalid character in identifier
>>> calculate_tax({"Alex": 500,"James": 20500,"Kinuthia": 70000})
Traceback (most recent call last):
  File "<pyshell#127>", line 1, in <module>
    calculate_tax({"Alex": 500,"James": 20500,"Kinuthia": 70000})
  File "<pyshell#125>", line 6, in calculate_tax
    for key, value in x.iter_items():
AttributeError: 'dict' object has no attribute 'iter_items'
>>> a = {"Alex": 500,"James": 20500,"Kinuthia": 70000}
>>> a.items()
dict_items([('Alex', 500), ('Kinuthia', 70000), ('James', 20500)])
>>> for key, value in a.items():
	print(key, value)

	
Alex 500
Kinuthia 70000
James 20500
>>> def calculate_tax(x = dict()):
  if not x:
    return x
  else:
    newdict = dict()
    for key, value in x.items():
      salary = x[key]
      newdict[key] = get_tax(salary)
  return newdict

>>> calculate_tax({"Alex": 500,"James": 20500,"Kinuthia": 70000})
Begin:  salary: 70000  level: 1  deducted: 0  taxval: 0  remainder: 0  total: 0
End:  salary: 70000  deducted: 1000  taxval: 1000  remainder: 69000  total: 0

Begin:  salary: 70000  level: 2  deducted: 1000  taxval: 69000  remainder: 69000  total: 0
End:  salary: 70000  deducted: 10000  taxval: 9000  remainder: 60000  total: 900.0

Begin:  salary: 70000  level: 3  deducted: 10000  taxval: 60000  remainder: 60000  total: 900.0
End:  salary: 70000  deducted: 20200  taxval: 10200  remainder: 49800  total: 2430.0

Begin:  salary: 70000  level: 4  deducted: 20200  taxval: 49800  remainder: 49800  total: 2430.0
End:  salary: 70000  deducted: 30750  taxval: 10550  remainder: 39250  total: 4540.0

Begin:  salary: 70000  level: 5  deducted: 30750  taxval: 39250  remainder: 39250  total: 4540.0
End:  salary: 70000  deducted: 50000  taxval: 19250  remainder: 20000  total: 9352.5

Begin:  salary: 70000  level: 6  deducted: 50000  taxval: 20000  remainder: 20000  total: 9352.5
End:  salary: 70000  deducted: 50000  taxval: 20000  remainder: 0  total: 15352.5

Begin:  salary: 20500  level: 1  deducted: 0  taxval: 0  remainder: 0  total: 0
End:  salary: 20500  deducted: 1000  taxval: 1000  remainder: 19500  total: 0

Begin:  salary: 20500  level: 2  deducted: 1000  taxval: 19500  remainder: 19500  total: 0
End:  salary: 20500  deducted: 10000  taxval: 9000  remainder: 10500  total: 900.0

Begin:  salary: 20500  level: 3  deducted: 10000  taxval: 10500  remainder: 10500  total: 900.0
End:  salary: 20500  deducted: 20200  taxval: 10200  remainder: 300  total: 2430.0

Begin:  salary: 20500  level: 4  deducted: 20200  taxval: 300  remainder: 300  total: 2430.0
End:  salary: 20500  deducted: 30750  taxval: 300  remainder: -10250  total: 2490.0

{'Alex': 0, 'Kinuthia': 15352.5, 'James': 2490.0}
>>> def get_tax(salary, remainder=0, level = 1, deducted = 0, total = 0):
  if (level > 6) or ((remainder <= 0) and (level > 1)) or (salary < 1000):
      return total
  else:
    taxval = remainder
    if level ==  1:
      taxval = 1000
      total += taxval * 0
      remainder = salary - 1000
      deducted = 1000
    elif level == 2:
      if 9000 < remainder:
        taxval = 9000
      total += taxval * 0.1
      deducted = 10000
      remainder = salary - 10000
    elif level == 3:
      if 10200 < remainder:
        taxval = 10200
      total += taxval * 0.15
      deducted = 20200
      remainder = salary - 20200
    elif level == 4:
      if 10550 < remainder:
        taxval = 10550
      total += taxval * 0.2
      deducted = 30750
      remainder = salary - 30750
    elif level == 5:
      if 19250 < remainder:
        taxval = 19250
      total += taxval * 0.25
      deducted = 50000
      remainder = salary - 50000
    elif level == 6:
      if remainder > 0:
        total  += taxval * 0.3
        deducted = 50000
        remainder = 0
    level += 1
    return get_tax(salary, remainder, level, deducted, total)

>>> 
>>> get_tax(70000)
15352.5
>>> get_tax(500)
0
>>> get_tax(20500)
2490.0
>>> from unittest import TestCase

class CalculateTaxTests(TestCase):
  def test_it_calculates_tax_for_one_person(self):
    result = calculate_tax({"James": 20500})
    self.assertEqual(result, {"James": 2490.0}, msg="Should return {'James': 2490.0} for the input {'James': 20500}")

  def test_it_calculates_tax_for_several_people(self):
    income_input = {"James": 20500, "Mary": 500, "Evan": 70000}
    result = calculate_tax(income_input)
    self.assertEqual({"James": 2490.0, "Mary": 0, "Evan": 15352.5}, result,
      msg="Should return {} for the input {}".format(
            {"James": 2490.0, "Mary": 0, "Evan": 15352.5},
            {"James": 20500, "Mary": 500, "Evan": 70000}
      )
    )

  def test_it_does_not_accept_integers(self):
    with self.assertRaises(ValueError) as context:
      calculate_tax(1)
      self.assertEqual(
        "The provided input is not a dictionary.",
        context.exception.message, "Invalid input of type int not allowed"
      )
        
  def test_calculated_tax_is_a_float(self):
    result = calculate_tax({"Jane": 20500})
    self.assertIsInstance(
      calculate_tax({"Jane": 20500}), dict, msg="Should return a result of data type dict")
    self.assertIsInstance(result["Jane"], float, msg="Tax returned should be an float.")

  def test_it_returns_zero_tax_for_income_less_than_1000(self):
    result = calculate_tax({"Jake": 100})
    self.assertEqual(result, {"Jake": 0}, msg="Should return zero tax for incomes less than 1000")

  def test_it_throws_an_error_if_any_of_the_inputs_is_non_numeric(self):
    with self.assertRaises(ValueError, msg='Allow only numeric input'):
      calculate_tax({"James": 2490.0, "Kiura": '200', "Kinuthia": 15352.5})

  def test_it_return_an_empty_dict_for_an_empty_dict_input(self):
    result = calculate_tax({})
    self.assertEqual(result, {}, msg='Should return an empty dict if the input was an empty dict')

SyntaxError: multiple statements found while compiling a single statement
>>> from unittest import TestCase
>>> class CalculateTaxTests(TestCase):
  def test_it_calculates_tax_for_one_person(self):
    result = calculate_tax({"James": 20500})
    self.assertEqual(result, {"James": 2490.0}, msg="Should return {'James': 2490.0} for the input {'James': 20500}")

  def test_it_calculates_tax_for_several_people(self):
    income_input = {"James": 20500, "Mary": 500, "Evan": 70000}
    result = calculate_tax(income_input)
    self.assertEqual({"James": 2490.0, "Mary": 0, "Evan": 15352.5}, result,
      msg="Should return {} for the input {}".format(
            {"James": 2490.0, "Mary": 0, "Evan": 15352.5},
            {"James": 20500, "Mary": 500, "Evan": 70000}
      )
    )

  def test_it_does_not_accept_integers(self):
    with self.assertRaises(ValueError) as context:
      calculate_tax(1)
      self.assertEqual(
        "The provided input is not a dictionary.",
        context.exception.message, "Invalid input of type int not allowed"
      )
        
  def test_calculated_tax_is_a_float(self):
    result = calculate_tax({"Jane": 20500})
    self.assertIsInstance(
      calculate_tax({"Jane": 20500}), dict, msg="Should return a result of data type dict")
    self.assertIsInstance(result["Jane"], float, msg="Tax returned should be an float.")

  def test_it_returns_zero_tax_for_income_less_than_1000(self):
    result = calculate_tax({"Jake": 100})
    self.assertEqual(result, {"Jake": 0}, msg="Should return zero tax for incomes less than 1000")

  def test_it_throws_an_error_if_any_of_the_inputs_is_non_numeric(self):
    with self.assertRaises(ValueError, msg='Allow only numeric input'):
      calculate_tax({"James": 2490.0, "Kiura": '200', "Kinuthia": 15352.5})

  def test_it_return_an_empty_dict_for_an_empty_dict_input(self):
    result = calculate_tax({})
    self.assertEqual(result, {}, msg='Should return an empty dict if the input was an empty dict')

    
>>> 
>>> CalculateTaxTests()
<__main__.CalculateTaxTests testMethod=runTest>
>>> aerr = CalculatetaxTests()
Traceback (most recent call last):
  File "<pyshell#147>", line 1, in <module>
    aerr = CalculatetaxTests()
NameError: name 'CalculatetaxTests' is not defined
>>> aerrr = CalculateTaxTests()
>>> aerrr
<__main__.CalculateTaxTests testMethod=runTest>
>>> aerrr.test_it_throws_an_error_if_any_of_the_inputs_is_non_numeric()
Traceback (most recent call last):
  File "<pyshell#150>", line 1, in <module>
    aerrr.test_it_throws_an_error_if_any_of_the_inputs_is_non_numeric()
  File "<pyshell#144>", line 36, in test_it_throws_an_error_if_any_of_the_inputs_is_non_numeric
    calculate_tax({"James": 2490.0, "Kiura": '200', "Kinuthia": 15352.5})
  File "<pyshell#134>", line 8, in calculate_tax
    newdict[key] = get_tax(salary)
  File "<pyshell#136>", line 2, in get_tax
    if (level > 6) or ((remainder <= 0) and (level > 1)) or (salary < 1000):
TypeError: unorderable types: str() < int()
>>> aerrr.test_it_calculates_tax_for_one_person
<bound method CalculateTaxTests.test_it_calculates_tax_for_one_person of <__main__.CalculateTaxTests testMethod=runTest>>
>>> aerrr.test_it_calculates_tax_for_one_person()
>>> aerrr.test_it_calculates_tax_for_several_people()
>>> aerrr.test_it_does_not_accept_integers()
Traceback (most recent call last):
  File "<pyshell#154>", line 1, in <module>
    aerrr.test_it_does_not_accept_integers()
  File "<pyshell#144>", line 18, in test_it_does_not_accept_integers
    calculate_tax(1)
  File "<pyshell#134>", line 6, in calculate_tax
    for key, value in x.items():
AttributeError: 'int' object has no attribute 'items'
>>> def calculate_tax(x = dict()):
  if not x:
    return x
  elif type(x) not type(dict()):
	  raise ValueError("The provided input is not a dictionary.")
  else:
    newdict = dict()
    for key, value in x.items():
      salary = x[key]
      newdict[key] = get_tax(salary)
  return newdict
SyntaxError: invalid syntax
>>> def calculate_tax(x = dict()):
  if not x:
    return x
  elif type(x) not type(dict()):
	  raise ValueError("The provided input is not a dictionary.")
  else:
    newdict = dict()
    for key, value in x.items():
      salary = x[key]
      newdict[key] = get_tax(salary)
  return newdict
SyntaxError: invalid syntax
>>> def calculate_tax(x = dict()):
  if not x:
    return x
  elif type(x) not type(dict()):
    raise ValueError("The provided input is not a dictionary.")
  else:
    newdict = dict()
    for key, value in x.items():
      salary = x[key]
      newdict[key] = get_tax(salary)
  return newdict
SyntaxError: invalid syntax
>>> def calculate_tax(x = dict()):
  if not x:
    return x
  elif x not dict():
	  raise ValueError('The provided input is not a dictionary.')
  else:
    newdict = dict()
    for key, value in x.items():
      salary = x[key]
      newdict[key] = get_tax(salary)
  return newdict
SyntaxError: invalid syntax
>>> def calculate_tax(x = dict()):
  if not x:
    return x
  elif x:
    raise ValueError("The provided input is not a dictionary.")
  else:
    newdict = dict()
    for key, value in x.items():
      salary = x[key]
      newdict[key] = get_tax(salary)
  return newdict

>>> type(a)
<class 'dict'>
>>> def calculate_tax(x = dict()):
  if not x:
    return x
  elif type(x) is not dict:
    raise ValueError("The provided input is not a dictionary.")
  else:
    newdict = dict()
    for key, value in x.items():
      salary = x[key]
      newdict[key] = get_tax(salary)
  return newdict

>>> aerrr.test_it_does_not_accept_integers()
>>> aerrr.test_calculated_tax_is_a_float()
>>> aerr.test_it_returns_zero_tax_for_income_less_than_1000()
Traceback (most recent call last):
  File "<pyshell#166>", line 1, in <module>
    aerr.test_it_returns_zero_tax_for_income_less_than_1000()
NameError: name 'aerr' is not defined
>>> aerrr.test_it_returns_zero_tax_for_income_less_than_1000()
>>> aerrr.test_it_throws_an_error_if_any_of_the_inputs_is_non_numeric()
Traceback (most recent call last):
  File "<pyshell#168>", line 1, in <module>
    aerrr.test_it_throws_an_error_if_any_of_the_inputs_is_non_numeric()
  File "<pyshell#144>", line 36, in test_it_throws_an_error_if_any_of_the_inputs_is_non_numeric
    calculate_tax({"James": 2490.0, "Kiura": '200', "Kinuthia": 15352.5})
  File "<pyshell#163>", line 10, in calculate_tax
    newdict[key] = get_tax(salary)
  File "<pyshell#136>", line 2, in get_tax
    if (level > 6) or ((remainder <= 0) and (level > 1)) or (salary < 1000):
TypeError: unorderable types: str() < int()
>>> def calculate_tax(x = dict()):
  if not x:
    return x
  elif type(x) is not dict:
    raise ValueError("The provided input is not a dictionary.")
  else:
    newdict = dict()
    for key, value in x.items():
      salary = x[key]
      if type(salary) is not int:
        raise ValueError("Allow only numeric input")
      newdict[key] = get_tax(salary)
  return newdict

>>> aerrr.test_it_throws_an_error_if_any_of_the_inputs_is_non_numeric()
>>> aerrr.test_it_return_an_empty_dict_for_an_empty_dict_input()
>>> from abc import ABCMeta
>>> class MyABC(metaclass=ABCMeta):
	pass

>>> MyABC.register(tuple)
<class 'tuple'>
>>> assert issubclass(tuble, MyABC)
Traceback (most recent call last):
  File "<pyshell#178>", line 1, in <module>
    assert issubclass(tuble, MyABC)
NameError: name 'tuble' is not defined
>>> assert issubclass(tuple, MyABC)
>>> asserr isinstance((), MyABC)
SyntaxError: invalid syntax
>>> assert isinstance((), MyABC)
>>> from abc import ABC abstractmethod
SyntaxError: invalid syntax
>>> from abc import ABCMeta, abstractmethod
>>> class BankAccount(ABCMeta):
  
  
  @abstractmethod
  def withdraw(self):
    pass
  
  
  @abstractmethod
  def deposit(self):
    pass

>>> class SavingsAccount(BankAccount):
  
  __init__(self):
    self.balance = 500
  
  
  def deposit(self, amount):
    if amount < 0:
      raise ValueError("Invalid deposit amount")
    self.balance += amount
    return self.balance
    
  def withdraw(self, amount):
    if (self.balance - amount) < 500:
      raise ValueError("Cannot withdraw beyond the minimum account balance")
    elif amount < 0:
      raise ValueError("Invalid withdrawal amount")
    else:
      self.amount -= amount
    return self.balance
SyntaxError: invalid syntax
>>> class SavingsAccount(BankAccount):
  
  def __init__(self):
    self.balance = 500
  
  
  def deposit(self, amount):
    if amount < 0:
      raise ValueError("Invalid deposit amount")
    self.balance += amount
    return self.balance
    
  def withdraw(self, amount):
    if (self.balance - amount) < 500:
      raise ValueError("Cannot withdraw beyond the minimum account balance")
    elif amount < 0:
      raise ValueError("Invalid withdrawal amount")
    else:
      self.amount -= amount
    return self.balance

>>> class CurrentAccount(BankAccount):
  def __init__(self):
    self.balance =  0

  def deposit(self, amount):
    if amount < 0:
      raise ValueError("Invalid deposit amount")
    self.balance += amount
  return self.balance
  
  def withdraw(self, amount):
    if (self.balance - amount) < 500:
      raise ValueError("Cannot withdraw beyond the current account balance")
    elif amount < 0:
      raise ValueError("Invalid withdrawal amount")
    else:
      self.amount -= amount
  return self.balance
SyntaxError: 'return' outside function
>>> class CurrentAccount(BankAccount):
  def __init__(self):
    self.balance =  0

  def deposit(self, amount):
    if amount < 0:
      raise ValueError("Invalid deposit amount")
    self.balance += amount
    return self.balance
  
  def withdraw(self, amount):
    if (self.balance - amount) < 500:
      raise ValueError("Cannot withdraw beyond the current account balance")
    elif amount < 0:
      raise ValueError("Invalid withdrawal amount")
    else:
      self.amount -= amount
    return self.balance

>>> import unittest
>>> class CurrentAccountTestCases(unittest.TestCase):
  def setUp(self):
    self.ca = CurrentAccount()
    
  def tearDown(self):
    del self.ca

  def test_current_account_is_instance_of_bank_account(self):
    self.assertTrue(isinstance(self.ca, BankAccount), msg='CurrentAccount is not a subclass of BankAccount')
  
  def test_current_account_can_deposit_valid_amounts(self):
    balance = self.ca.deposit(1500)
    self.assertEquals(balance, 1500)
  
  def test_current_account_cannot_withdraw_more_than_current_balance(self):
    message = self.ca.withdraw(1500)
    self.assertEquals(message, 'Cannot withdraw beyond the current account balance', msg='No overdrafts')
  
  def test_current_account_can_withdraw_valid_cash_amounts(self):
    self.ca.deposit(23001)
    self.ca.withdraw(437)
    self.assertEquals(self.ca.balance, 22564, msg='Incorrect balance after withdrawal')

    
>>> class SavingsAccountTestCases(unittest.TestCase):
  def setUp(self):
    self.sa = SavingsAccount()
    
  def tearDown(self):
    del self.sa
  
  def test_savings_account_is_instance_of_bank_account(self):
    self.assertTrue(isinstance(self.sa, BankAccount), msg='SavingsAccount is not a subclass of BankAccount')

  def test_savings_account_can_deposit_valid_amounts(self):
    init_balance = self.sa.balance
    balance = self.sa.deposit(1500)
    self.assertEquals(balance, (1500 + init_balance), msg='Balance does not match deposit')

  def test_savings_account_cannot_withdraw_more_than_current_balance(self):
    message = self.sa.withdraw(1500)
    self.assertEquals(message, 'Cannot withdraw beyond the current account balance', msg='No overdrafts')

  def test_savings_account_can_withdraw_valid_amounts_successfully(self):
    self.sa.deposit(2300)
    self.sa.withdraw(543)
    self.assertEquals(2257, self.sa.balance, msg="Incorrect balance after withdrawal")

    
>>> aeee = SavingsAccountTestCases()
>>> aeee.test_savings_account_is_instance_of_bank_account()
Traceback (most recent call last):
  File "<pyshell#198>", line 1, in <module>
    aeee.test_savings_account_is_instance_of_bank_account()
  File "<pyshell#196>", line 9, in test_savings_account_is_instance_of_bank_account
    self.assertTrue(isinstance(self.sa, BankAccount), msg='SavingsAccount is not a subclass of BankAccount')
AttributeError: 'SavingsAccountTestCases' object has no attribute 'sa'
>>> aeee = SavingsAccountTestCases()
>>> aeee.serUp()
Traceback (most recent call last):
  File "<pyshell#200>", line 1, in <module>
    aeee.serUp()
AttributeError: 'SavingsAccountTestCases' object has no attribute 'serUp'
>>> aeee.setUp()
Traceback (most recent call last):
  File "<pyshell#201>", line 1, in <module>
    aeee.setUp()
  File "<pyshell#196>", line 3, in setUp
    self.sa = SavingsAccount()
TypeError: __new__() missing 3 required positional arguments: 'name', 'bases', and 'namespace'
>>> class CurrentAccountTestCases(TestCase):
  def setUp(self):
    self.ca = CurrentAccount()
    
  def tearDown(self):
    del self.ca

  def test_current_account_is_instance_of_bank_account(self):
    self.assertTrue(isinstance(self.ca, BankAccount), msg='CurrentAccount is not a subclass of BankAccount')
  
  def test_current_account_can_deposit_valid_amounts(self):
    balance = self.ca.deposit(1500)
    self.assertEquals(balance, 1500)
  
  def test_current_account_cannot_withdraw_more_than_current_balance(self):
    message = self.ca.withdraw(1500)
    self.assertEquals(message, 'Cannot withdraw beyond the current account balance', msg='No overdrafts')
  
  def test_current_account_can_withdraw_valid_cash_amounts(self):
    self.ca.deposit(23001)
    self.ca.withdraw(437)
    self.assertEquals(self.ca.balance, 22564, msg='Incorrect balance after withdrawal')

    
>>> ael = CurrentAccountTestCases()
>>> ael.test_current_account_can_deposit_valid_amounts
<bound method CurrentAccountTestCases.test_current_account_can_deposit_valid_amounts of <__main__.CurrentAccountTestCases testMethod=runTest>>
>>> ael.test_current_account_can_deposit_valid_amounts()
Traceback (most recent call last):
  File "<pyshell#206>", line 1, in <module>
    ael.test_current_account_can_deposit_valid_amounts()
  File "<pyshell#203>", line 12, in test_current_account_can_deposit_valid_amounts
    balance = self.ca.deposit(1500)
AttributeError: 'CurrentAccountTestCases' object has no attribute 'ca'
>>> ael.setUp()
Traceback (most recent call last):
  File "<pyshell#207>", line 1, in <module>
    ael.setUp()
  File "<pyshell#203>", line 3, in setUp
    self.ca = CurrentAccount()
TypeError: __new__() missing 3 required positional arguments: 'name', 'bases', and 'namespace'
>>> ael
<__main__.CurrentAccountTestCases testMethod=runTest>
>>> ael.ca
Traceback (most recent call last):
  File "<pyshell#209>", line 1, in <module>
    ael.ca
AttributeError: 'CurrentAccountTestCases' object has no attribute 'ca'
>>> ael.ca = CurrentAccount()
Traceback (most recent call last):
  File "<pyshell#210>", line 1, in <module>
    ael.ca = CurrentAccount()
TypeError: __new__() missing 3 required positional arguments: 'name', 'bases', and 'namespace'
>>> aela = SavingsAccountTestCases()
>>> aela
<__main__.SavingsAccountTestCases testMethod=runTest>
>>> aela.setUp()
Traceback (most recent call last):
  File "<pyshell#213>", line 1, in <module>
    aela.setUp()
  File "<pyshell#196>", line 3, in setUp
    self.sa = SavingsAccount()
TypeError: __new__() missing 3 required positional arguments: 'name', 'bases', and 'namespace'
>>> aela()
Traceback (most recent call last):
  File "<pyshell#214>", line 1, in <module>
    aela()
  File "C:\Users\Boiyelove\AppData\Local\Programs\Python\Python35-32\lib\unittest\case.py", line 648, in __call__
    return self.run(*args, **kwds)
  File "C:\Users\Boiyelove\AppData\Local\Programs\Python\Python35-32\lib\unittest\case.py", line 575, in run
    testMethod = getattr(self, self._testMethodName)
AttributeError: 'SavingsAccountTestCases' object has no attribute 'runTest'
>>> class BankAccount(metaclass=ABCMeta):
  
  
  @abstractmethod
  def withdraw(self):
    pass
  
  
  @abstractmethod
  def deposit(self):
    pass

>>> aela = SavingsAccountTestCases()
>>> ael = CurrentAccountTestCases()
>>> ael.test_current_account_can_deposit_valid_amounts()
Traceback (most recent call last):
  File "<pyshell#219>", line 1, in <module>
    ael.test_current_account_can_deposit_valid_amounts()
  File "<pyshell#203>", line 12, in test_current_account_can_deposit_valid_amounts
    balance = self.ca.deposit(1500)
AttributeError: 'CurrentAccountTestCases' object has no attribute 'ca'
>>> aela.setUp()
Traceback (most recent call last):
  File "<pyshell#221>", line 1, in <module>
    aela.setUp()
  File "<pyshell#196>", line 3, in setUp
    self.sa = SavingsAccount()
TypeError: __new__() missing 3 required positional arguments: 'name', 'bases', and 'namespace'
>>> class BankAccount:
  def withdraw(self):
    pass
  
  def deposit(self):
    pass


class SavingsAccount(BankAccount):
  
  def __init__(self):
    self.balance = 500
  
  
  def deposit(self, amount):
    if amount < 0:
      raise ValueError("Invalid deposit amount")
    self.balance += amount
    return self.balance
    
  def withdraw(self, amount):
    if (self.balance - amount) < 500:
      raise ValueError("Cannot withdraw beyond the minimum account balance")
    elif amount < 0:
      raise ValueError("Invalid withdrawal amount")
    else:
      self.amount -= amount
    return self.balance
SyntaxError: invalid syntax
>>> class BankAccount:
  def withdraw(self):
    pass
  
  def deposit(self):
    pass

>>> class SavingsAccount(BankAccount):
  
  def __init__(self):
    self.balance = 500
  
  
  def deposit(self, amount):
    if amount < 0:
      raise ValueError("Invalid deposit amount")
    self.balance += amount
    return self.balance
    
  def withdraw(self, amount):
    if (self.balance - amount) < 500:
      raise ValueError("Cannot withdraw beyond the minimum account balance")
    elif amount < 0:
      raise ValueError("Invalid withdrawal amount")
    else:
      self.amount -= amount
    return self.balance

>>> aela = SavingsAccountTestCases()
>>> aela.test_savings_account_can_deposit_valid_amounts()
Traceback (most recent call last):
  File "<pyshell#228>", line 1, in <module>
    aela.test_savings_account_can_deposit_valid_amounts()
  File "<pyshell#196>", line 12, in test_savings_account_can_deposit_valid_amounts
    init_balance = self.sa.balance
AttributeError: 'SavingsAccountTestCases' object has no attribute 'sa'
>>> me = SavingsAccount()
>>> me.deposit(50)
550
>>> me.withdraw(500)
Traceback (most recent call last):
  File "<pyshell#231>", line 1, in <module>
    me.withdraw(500)
  File "<pyshell#226>", line 15, in withdraw
    raise ValueError("Cannot withdraw beyond the minimum account balance")
ValueError: Cannot withdraw beyond the minimum account balance
>>> class CurrentAccountTestCases(unittest.TestCase):
  def setUp(self):
    self.ca = CurrentAccount()
    
  def tearDown(self):
    del self.ca

  def test_current_account_is_instance_of_bank_account(self):
    self.assertTrue(isinstance(self.ca, BankAccount), msg='CurrentAccount is not a subclass of BankAccount')
  
  def test_current_account_can_deposit_valid_amounts(self):
    balance = self.ca.deposit(1500)
    self.assertEquals(balance, 1500)
  
  def test_current_account_cannot_withdraw_more_than_current_balance(self):
    message = self.ca.withdraw(1500)
    self.assertEquals(message, 'Cannot withdraw beyond the current account balance', msg='No overdrafts')
  
  def test_current_account_can_withdraw_valid_cash_amounts(self):
    self.ca.deposit(23001)
    self.ca.withdraw(437)
    self.assertEquals(self.ca.balance, 22564, msg='Incorrect balance after withdrawal')

    
>>> class SavingsAccountTestCases(unittest.TestCase):
  def setUp(self):
    self.sa = SavingsAccount()
    
  def tearDown(self):
    del self.sa
  
  def test_savings_account_is_instance_of_bank_account(self):
    self.assertTrue(isinstance(self.sa, BankAccount), msg='SavingsAccount is not a subclass of BankAccount')

  def test_savings_account_can_deposit_valid_amounts(self):
    init_balance = self.sa.balance
    balance = self.sa.deposit(1500)
    self.assertEquals(balance, (1500 + init_balance), msg='Balance does not match deposit')

  def test_savings_account_cannot_withdraw_more_than_current_balance(self):
    message = self.sa.withdraw(1500)
    self.assertEquals(message, 'Cannot withdraw beyond the current account balance', msg='No overdrafts')

  def test_savings_account_can_withdraw_valid_amounts_successfully(self):
    self.sa.deposit(2300)
    self.sa.withdraw(543)
    self.assertEquals(2257, self.sa.balance, msg="Incorrect balance after withdrawal")

    
>>> class BankAccount(object):
  def withdraw(self):
    pass
  
  def deposit(self):
    pass

>>> class SavingsAccount(BankAccount):
  
  def __init__(self):
    self.balance = 500
  
  
  def deposit(self, amount):
    if amount < 0:
      return "Invalid deposit amount"
    self.balance += amount
    return self.balance
    
  def withdraw(self, amount):
    if (self.balance - amount) < 500:
      return "Cannot withdraw beyond the current account balance"
    elif amount < 0:
      return "Invalid withdrawal amount"
    else:
      self.balance -= amount
    return self.balance

>>> class CurrentAccount(BankAccount):
  def __init__(self):
    self.balance =  0

  def deposit(self, amount):
    if amount <= 0:
      return "Invalid deposit amount"
    self.balance += amount
    return self.balance
  
  def withdraw(self, amount):
    if (self.balance - amount) < 500:
      return "Cannot withdraw beyond the current account balance"
    elif amount < 0:
      return "Invalid withdrawal amount"
    else:
      self.balance -= amount
    return self.balance

>>> SavingsAccountTestCases()
<__main__.SavingsAccountTestCases testMethod=runTest>
>>> aeol = SavingsAccountTestCases()
>>> aeol.test_savings_account_is_instance_of_bank_account()
Traceback (most recent call last):
  File "<pyshell#244>", line 1, in <module>
    aeol.test_savings_account_is_instance_of_bank_account()
  File "<pyshell#235>", line 9, in test_savings_account_is_instance_of_bank_account
    self.assertTrue(isinstance(self.sa, BankAccount), msg='SavingsAccount is not a subclass of BankAccount')
AttributeError: 'SavingsAccountTestCases' object has no attribute 'sa'
>>> test_savings_account_can_deposit_valid_amounts()
Traceback (most recent call last):
  File "<pyshell#245>", line 1, in <module>
    test_savings_account_can_deposit_valid_amounts()
NameError: name 'test_savings_account_can_deposit_valid_amounts' is not defined
>>> aeol.test_savings_account_can_deposit_valid_amounts()
Traceback (most recent call last):
  File "<pyshell#246>", line 1, in <module>
    aeol.test_savings_account_can_deposit_valid_amounts()
  File "<pyshell#235>", line 12, in test_savings_account_can_deposit_valid_amounts
    init_balance = self.sa.balance
AttributeError: 'SavingsAccountTestCases' object has no attribute 'sa'
>>> 
