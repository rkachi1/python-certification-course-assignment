import re
password = str(input('Enter password for booking ticket\n'))

if len(password) >12:
  print ('password is too long It must be between 6 and 12 characters')

elif len(password) <6:
  print ('password is too short It must be between 6 and 12 characters')
  
elif len(password)    >=6 and len(password) <= 12:
  print ('password ok')



  if not re.search("[a-z]", password):
        print('password must contain atleast one lowercase letter')
  elif not re.search("[A-Z]", password):
      print('password must contain atleast one upercase letter')

  elif not re.search("[0-9]", password):
      print('password must contain atleast one number')

  elif not re.search("[_@$]", password):
      print('password must contain atleast one special characater')
  
  else:
      print('password success')