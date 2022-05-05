from pwn import *

r = remote("mercury.picoctf.net", 20266)
r.recvline()
