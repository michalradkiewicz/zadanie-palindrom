def is_palindromy(palindrom):
    if palindrom == palindrom[::-1]:
            return(True)
    else:
          return(False)
palindrom_list = ['kajak', 'jaka', 'arka', 'potop', 'kokot']
for name in palindrom_list:
     print(is_palindromy(name))