

# add fuction

def add_chocolates(chocolates):
  name=input("Enter name of the chocolates: ")
  amount=int(input("Enter the amount: "))
  stock=int(input("Enter the stocks: "))
  chocolate={'name':name,'amount':amount,'stock':stock}
  chocolates.append(chocolate)
  return chocolates

#remove fuction

def remove_chocolates(chocolates):
  name=input("Enter name of chocolate: ")
  for chocolate in chocolates:
    if chocolate['name'] == name:
      chocolates.remove(chocolate)
  return chocolates

#update amount funtion

def update_amount(chocolates):
  name=input("Enter name of chocolate: ")
  amount=int(input("Enter the amount: "))
  for chocolate in chocolates:
    if chocolate['name'] == name:
      chocolate['amount']=amount
  return chocolates

#update stock fuction

def update_stock(chocolates):
  name=input("Enter name of chocolate: ")
  stock=int(input("Enter the stock: "))
  for chocolate in chocolates:
    if chocolate['name'] == name:
      chocolate['stock']=stock
  return chocolates