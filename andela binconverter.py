Python 3.5.1 (v3.5.1:37a07cee5969, Dec  6 2015, 01:38:48) [MSC v.1900 32 bit (Intel)] on win32
Type "copyright", "credits" or "license()" for more information.
>>> 
======== RESTART: C:/Users/Boiyelove/Desktop/-/andela_bankaccount.py ========
>>> aeol = CurrentAccountTestCases()
>>> aeol.balance()
Traceback (most recent call last):
  File "<pyshell#1>", line 1, in <module>
    aeol.balance()
AttributeError: 'CurrentAccountTestCases' object has no attribute 'balance'
>>> aeol.balance
Traceback (most recent call last):
  File "<pyshell#2>", line 1, in <module>
    aeol.balance
AttributeError: 'CurrentAccountTestCases' object has no attribute 'balance'
>>> aeol.test_current_account_can_withdraw_valid_cash_amounts()
Traceback (most recent call last):
  File "<pyshell#3>", line 1, in <module>
    aeol.test_current_account_can_withdraw_valid_cash_amounts()
  File "C:/Users/Boiyelove/Desktop/-/andela_bankaccount.py", line 22, in test_current_account_can_withdraw_valid_cash_amounts
    self.ca.deposit(23001)
AttributeError: 'CurrentAccountTestCases' object has no attribute 'ca'
>>> aeol.setUp()
>>> aeol.test_current_account_can_withdraw_valid_cash_amounts()
amount is: 437
balance is:  23001
>>> 
======== RESTART: C:/Users/Boiyelove/Desktop/-/andela_bankaccount.py ========
>>> aeol = CurrentAccountTestCases()
>>> aeol.test_current_account_can_withdraw_valid_cash_amounts()
Traceback (most recent call last):
  File "<pyshell#7>", line 1, in <module>
    aeol.test_current_account_can_withdraw_valid_cash_amounts()
  File "C:/Users/Boiyelove/Desktop/-/andela_bankaccount.py", line 22, in test_current_account_can_withdraw_valid_cash_amounts
    self.ca.deposit(23001)
AttributeError: 'CurrentAccountTestCases' object has no attribute 'ca'
>>> aeol.setUp()
>>> aeol.test_current_account_can_withdraw_valid_cash_amounts()
amount is: 437
balance is:  23001
After amount is: 437
After balance is:  22564
>>> aeol.t
Traceback (most recent call last):
  File "<pyshell#10>", line 1, in <module>
    aeol.t
AttributeError: 'CurrentAccountTestCases' object has no attribute 't'
>>> aeol.tearDown()
>>> aeol
<__main__.CurrentAccountTestCases testMethod=runTest>
>>> aeol.deposit(33)
Traceback (most recent call last):
  File "<pyshell#13>", line 1, in <module>
    aeol.deposit(33)
AttributeError: 'CurrentAccountTestCases' object has no attribute 'deposit'
>>> SavingsAccountTestCases()
<__main__.SavingsAccountTestCases testMethod=runTest>
>>> aeol = SavingsAccountTestCases()
>>> aeol.test_savings_account_is_instance_of_bank_account()
Traceback (most recent call last):
  File "<pyshell#16>", line 1, in <module>
    aeol.test_savings_account_is_instance_of_bank_account()
  File "C:/Users/Boiyelove/Desktop/-/andela_bankaccount.py", line 34, in test_savings_account_is_instance_of_bank_account
    self.assertTrue(isinstance(self.sa, BankAccount), msg='SavingsAccount is not a subclass of BankAccount')
AttributeError: 'SavingsAccountTestCases' object has no attribute 'sa'
>>> aeol.setUp()
>>> aeol.test_savings_account_is_instance_of_bank_account()
>>> aeol.test_savings_account_can_deposit_valid_amounts()
>>> aeol.test_savings_account_cannot_withdraw_more_than_current_balance()
Traceback (most recent call last):
  File "<pyshell#20>", line 1, in <module>
    aeol.test_savings_account_cannot_withdraw_more_than_current_balance()
  File "C:/Users/Boiyelove/Desktop/-/andela_bankaccount.py", line 43, in test_savings_account_cannot_withdraw_more_than_current_balance
    self.assertEquals(message, 'Cannot withdraw beyond the current account balance', msg='No overdrafts')
  File "C:\Users\Boiyelove\AppData\Local\Programs\Python\Python35-32\lib\unittest\case.py", line 1311, in deprecated_func
    return original_func(*args, **kwargs)
  File "C:\Users\Boiyelove\AppData\Local\Programs\Python\Python35-32\lib\unittest\case.py", line 820, in assertEqual
    assertion_func(first, second, msg=msg)
  File "C:\Users\Boiyelove\AppData\Local\Programs\Python\Python35-32\lib\unittest\case.py", line 813, in _baseAssertEqual
    raise self.failureException(msg)
AssertionError: 500 != 'Cannot withdraw beyond the current account balance' : No overdrafts
>>> 
======== RESTART: C:/Users/Boiyelove/Desktop/-/andela_bankaccount.py ========
>>> aeol = SavingsAccountTestCases()
>>> aeol.setUp()
>>> aeol.test_savings_account_cannot_withdraw_more_than_current_balance()
>>> aeol.test_savings_account_can_withdraw_valid_amounts_successfully()
>>> a = []
>>> type(a)
<class 'list'>
>>> import unittest
>>> class ManipulateDataTestCases(unittest.TestCase):
  def test_only_lists_allowed(self):
    result = manipulate_data({})
    self.assertEqual(result, 'Only lists allowed', msg='Invalid argument')

  def test_it_returns_correct_output_with_positives(self):
    result = manipulate_data([1, 2, 3, 4])
    self.assertEqual(result, [4, 0], msg='Invalid output')
    
  def test_returns_correct_ouptut_with_negatives(self):
    result = manipulate_data([1, -9, 2, 3, 4, -5]);
    self.assertEqual(result, [4, -14], msg='Invalid output')

    
>>> def manipulate_data(list_item=[]):
    count_list = [0,0]
    if type(list_item) is list:
      for x in list_item:
        if x < 0:
          count_list[0] += 1
        else:
          count_list[1] += x
      return count_list
    else:
      return "Only lists allowed"

>>> aeol = ManipulateDataTestCases()
>>> aeol.test_only_lists_allowed()
>>> test_it_returns_correct_output_with_positives()
Traceback (most recent call last):
  File "<pyshell#34>", line 1, in <module>
    test_it_returns_correct_output_with_positives()
NameError: name 'test_it_returns_correct_output_with_positives' is not defined
>>> aeol.test_it_returns_correct_output_with_positives()
Traceback (most recent call last):
  File "<pyshell#35>", line 1, in <module>
    aeol.test_it_returns_correct_output_with_positives()
  File "<pyshell#29>", line 8, in test_it_returns_correct_output_with_positives
    self.assertEqual(result, [4, 0], msg='Invalid output')
  File "C:\Users\Boiyelove\AppData\Local\Programs\Python\Python35-32\lib\unittest\case.py", line 820, in assertEqual
    assertion_func(first, second, msg=msg)
  File "C:\Users\Boiyelove\AppData\Local\Programs\Python\Python35-32\lib\unittest\case.py", line 1018, in assertListEqual
    self.assertSequenceEqual(list1, list2, msg, seq_type=list)
  File "C:\Users\Boiyelove\AppData\Local\Programs\Python\Python35-32\lib\unittest\case.py", line 1000, in assertSequenceEqual
    self.fail(msg)
  File "C:\Users\Boiyelove\AppData\Local\Programs\Python\Python35-32\lib\unittest\case.py", line 665, in fail
    raise self.failureException(msg)
AssertionError: Lists differ: [0, 10] != [4, 0]

First differing element 0:
0
4

- [0, 10]
?  ^  -

+ [4, 0]
?  ^
 : Invalid output
>>> def manipulate_data(list_item=[]):
    count_list = [0,0]
    if type(list_item) is list:
      for x in list_item:
        if x > 0:
          count_list[0] += 1
        else:
          count_list[1] += x
      return count_list
    else:
      return "Only lists allowed"

>>> aeol.test_it_returns_correct_output_with_positives()
>>> aeol.test_returns_correct_ouptut_with_negatives()
>>> def bubblesort( A ):
  for i in range( len( A ) ):
    for k in range( len( A ) - 1, i, -1 ):
      if ( A[k] < A[k - 1] ):
        swap( A, k, k - 1 )

def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp
  
SyntaxError: invalid syntax
>>> def bubblesort( A ):
  for i in range( len( A ) ):
    for k in range( len( A ) - 1, i, -1 ):
      if ( A[k] < A[k - 1] ):
        swap( A, k, k - 1 )

        
>>> def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp

  
>>> def bubblesort( A ):
  for i in range( len( A ) ):
    for k in range( len( A ) - 1, i, -1 ):
      if ( A[k] < A[k - 1] ):
        swap( A, k, k - 1 )
  return A

>>> def swap( A, x, y ):
  tmp = A[x]
  A[x] = A[y]
  A[y] = tmp
  return A

>>> def insertionSort(alist):
   for index in range(1,3):

     currentvalue = alist[index]
     position = index

     while position>0 and alist[position-1]>currentvalue:
         alist[position]=alist[position-1]
         position = position-1

     alist[position]=currentvalue

     
>>> alist =[15, 5, 4, 18, 12, 19, 14, 10, 8, 20]
>>> insertionSort(alist)
>>> print(alist)
[4, 5, 15, 18, 12, 19, 14, 10, 8, 20]
>>> def selectionSort(alist):
   for fillslot in range(2,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

       
>>> alist =  [11, 7, 12, 14, 19, 1, 6, 18, 8, 20]
>>> selectionSort(alist)
>>> print(alist)
[7, 11, 12, 14, 19, 1, 6, 18, 8, 20]
>>> alist =  [11, 7, 12, 14, 19, 1, 6, 18, 8, 20]
>>> def selectionSort(alist):
   for fillslot in range(2,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]<alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

       
>>> selectionSort(alist)
>>> print(alist)
[12, 11, 7, 14, 19, 1, 6, 18, 8, 20]
>>> def selectionSort(alist):
   for fillslot in range(3,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]<alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

       
>>> alist =  [11, 7, 12, 14, 19, 1, 6, 18, 8, 20]
>>> selectionSort(alist)
>>> print(alist)
[14, 12, 11, 7, 19, 1, 6, 18, 8, 20]
>>> def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp

       
>>> def selectionSort(alist):
   for fillslot in range(len(alist)-1,0,-1):
       positionOfMax=0
       for location in range(1,fillslot+1):
           if alist[location]>alist[positionOfMax]:
               positionOfMax = location

       temp = alist[fillslot]
       alist[fillslot] = alist[positionOfMax]
       alist[positionOfMax] = temp
       print(alist)

       
>>> alist =  [11, 7, 12, 14, 19, 1, 6, 18, 8, 20]
>>> selectionSort(alist)
[11, 7, 12, 14, 19, 1, 6, 18, 8, 20]
[11, 7, 12, 14, 8, 1, 6, 18, 19, 20]
[11, 7, 12, 14, 8, 1, 6, 18, 19, 20]
[11, 7, 12, 6, 8, 1, 14, 18, 19, 20]
[11, 7, 1, 6, 8, 12, 14, 18, 19, 20]
[8, 7, 1, 6, 11, 12, 14, 18, 19, 20]
[6, 7, 1, 8, 11, 12, 14, 18, 19, 20]
[6, 1, 7, 8, 11, 12, 14, 18, 19, 20]
[1, 6, 7, 8, 11, 12, 14, 18, 19, 20]
>>> def factorial(number):
    if number == 0 :
        return 1;
    print('call: ', count + 1)
    return number * factorial(number-1)

>>> factorial(5)
Traceback (most recent call last):
  File "<pyshell#84>", line 1, in <module>
    factorial(5)
  File "<pyshell#83>", line 4, in factorial
    print('call: ', count + 1)
NameError: name 'count' is not defined
>>> count = 0
>>> factorial(5)
call:  1
call:  1
call:  1
call:  1
call:  1
120
>>> bin(10)
'0b1010'
>>> str(bin(10))
'0b1010'
>>> str(bin(10)).encode()
b'0b1010'
>>> bin(10).decode()
Traceback (most recent call last):
  File "<pyshell#90>", line 1, in <module>
    bin(10).decode()
AttributeError: 'str' object has no attribute 'decode'
>>> 0b1010
10
>>> type(bin(10))
<class 'str'>
>>> bin(10)
'0b1010'
>>> bin(25)
'0b11001'
>>> bin.__call__(10)[-2]
'1'
>>> bin.(10)[:-2]
SyntaxError: invalid syntax
>>> bin(10)[:-2]
'0b10'
>>> bin(10)[:2]
'0b'
>>> bin(10)[2:]
'1010'
>>> bin(0)[:2]
'0b'
>>> bin(0)[2:]
'0'
>>> def binary_converter(number = 0):
  if ((number >= 5) and (number<=255)) or number == 0:
    return bin(number)[2:]
  else:
    return "Invalid input"

>>> class BinaryConverterTestCases(unittest.TestCase):
  def test_conversion_one(self):
    result = binary_converter(0)
    self.assertEqual(result, '0', msg='Invalid conversion')

  def test_conversion_two(self):
    result = binary_converter(62)
    self.assertEqual(result, '111110', msg='Invalid conversion')

  def test_no_negative_numbers(self):
    result = binary_converter(-1)
    self.assertEqual(result, 'Invalid input', msg='Input below 0 not allowed')

  def test_no_numbers_above_255(self):
    result = binary_converter(300)
    self.assertEqual(result, 'Invalid input', msg='Input above 255 not allowed')

    
>>> aeol = BinaryConverterTestCase()
Traceback (most recent call last):
  File "<pyshell#106>", line 1, in <module>
    aeol = BinaryConverterTestCase()
NameError: name 'BinaryConverterTestCase' is not defined
>>> aeol = BinaryConverterTestCases()
>>> aeol.test_conversion_one()
>>> aeol.test_conversion_two()
>>> aeol.test_no_negative_numbers()
>>> aeol.test_no_numbers_above_255()
>>> def check_type(val):
  if type(val) is not (int or str):
    raise ValueError()
  else:
    return True

>>> check_type(56)
True
>>> check_type(uu)
Traceback (most recent call last):
  File "<pyshell#115>", line 1, in <module>
    check_type(uu)
NameError: name 'uu' is not defined
>>> type(11)
<class 'int'>
>>> check_type('srr')
Traceback (most recent call last):
  File "<pyshell#117>", line 1, in <module>
    check_type('srr')
  File "<pyshell#113>", line 3, in check_type
    raise ValueError()
ValueError
>>> def check_type(val):
  if (type(val) is not int) or (type(val) is not str):
    raise ValueError()
  else:
    return True

>>> check_type('sdffr')
Traceback (most recent call last):
  File "<pyshell#120>", line 1, in <module>
    check_type('sdffr')
  File "<pyshell#119>", line 3, in check_type
    raise ValueError()
ValueError
>>> def check_type(val):
  if (type(val) is not int) and (type(val) is not str):
    raise ValueError()
  else:
    return True

>>> check_type('strrr')
True
>>> check_type(56)
True
>>> check_type([])
Traceback (most recent call last):
  File "<pyshell#125>", line 1, in <module>
    check_type([])
  File "<pyshell#122>", line 3, in check_type
    raise ValueError()
ValueError
>>> def check_type(val):
  if type(val) is not (int and str):
    raise ValueError()
  else:
    return True

>>> check_type(56)
Traceback (most recent call last):
  File "<pyshell#128>", line 1, in <module>
    check_type(56)
  File "<pyshell#127>", line 3, in check_type
    raise ValueError()
ValueError
>>> 
