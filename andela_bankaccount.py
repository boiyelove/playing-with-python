import unittest

class CurrentAccountTestCases(unittest.TestCase):
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

class SavingsAccountTestCases(unittest.TestCase):
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

class BankAccount(object):
  def withdraw(self):
    pass

  def deposit(self):
    pass


class SavingsAccount(BankAccount):

  def __init__(self):
    self.balance = 500


  def deposit(self, amount):
    if amount < 0:
      return "Invalid deposit amount"
    self.balance += amount
    return self.balance

  def withdraw(self, amount):
    if self.balance <= amount:
      return "Cannot withdraw beyond the current account balance"
    elif amount < 0:
      return "Invalid withdrawal amount"
    else:
      self.balance -= amount
    return self.balance

class CurrentAccount(BankAccount):
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
