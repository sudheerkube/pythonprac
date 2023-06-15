# msg = "hello you"
# lenth = 0 

# for i in msg:
#    lenth += 1
# print(lenth)

##############################################################

def str_length(stg):
   len_count = 0
   for i in stg:
      len_count += 1 
   return  len_count

stg = "new 0000one"

str_len = str_length(stg)
print("Len of stg: ", str_len)
