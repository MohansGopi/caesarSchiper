#############Welcome to the encryption and decryption portal#####################
#############by -  payakan##################


# list of albhabets and number
list = [' ','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','_','+','=','`','~','<','>',',','.','/','?','|','[','}',']','{','-',"'",'.',' ','q','w','e','r','t','y','u','i','o','p','a','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','^','&','*','(',')','_','+','=','`','~','<','>',',','.','/','?','|','[','}',']','{','-',"'",'.']
# loop the function 
while True:
  en_de = input('What you want to do Encrypt or Decrypt : \n type encode for encryption \n type decode for decryption : \n type no to exit : ')
  en_de = en_de.lower()
  #encrytion method
  def encrypt():
    user_text = input('\nEnter the text : ')
    shift_no = int(input('\nEnter the shift number between 1 - 10: '))
    if 1>shift_no>10:
      print('The shift range will be in 1 - 10')
      exit()
    encrypt_text = ''
    for letter in user_text:
      position = list.index(letter)
      new_position = position + shift_no
      encrypt_text += list[new_position]
    print(f'\nYour encrypted text is {encrypt_text}\n')
  
  #decryption methon
  def decrypt():
    user_text = input('\nEnter the text : ')
    shift_no = int(input('\nEnter the shift number between 1 - 10: '))
    if 1>shift_no>10:
      print('The shift range will be in 1 - 10')
      exit()
    decrypt_text = ''
    for letter in user_text:
      position = list.index(letter)
      new_position = position - shift_no
      decrypt_text += list[new_position]
    print(f'\nYour decrypted text is {decrypt_text}\n')
  
  
  #user's input taking
  if en_de == 'encode':
    encrypt()
  elif en_de == 'decode':
    decrypt()
  elif en_de == 'no' or en_de == 'NO' or en_de == 'No' or en_de == 'nO':
    exit()
  else:
    print('you enter the wrong key')
    exit()