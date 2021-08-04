'''
            disclamer!!! 

        ONLY IN PYTHON 2.7 

'''
import hashlib

#import pdb # DEBUGGER

print('''	  
 		CYPHER
	Tool for encrypt key with differts methods 
''')

print('''

''')
secHash=list(hashlib.algorithms_guaranteed)

for idxHash in range(len(secHash)):
   print('  '+str(idxHash)+')  '+ secHash[idxHash])
    
print("""
      """)

idx_chosen=input('Choose the encryption method using numbers:  ')

chosen=secHash[int(idx_chosen)]
#print(chosen)
print('''   method chosen : '''+ chosen)

word = input("     insert something to encrypt : ")
exec('hash_object =hashlib.'+chosen+"(b'"+str(word)+"')")
print( hash_object.hexdigest() )

