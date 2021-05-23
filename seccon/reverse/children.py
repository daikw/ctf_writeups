from pwn import *
import subprocess as sp
import re

def get_child_pid():
    pid_check_cmd = "ps aux | grep [c]hildren | grep defunct | awk '{print $2}' | tail -n 1"
    ret = sp.check_output(pid_check_cmd, shell=True)
    pid = ret.decode("utf8").strip()

    return pid

def count_children():
    cmd = "ps aux | grep [c]hildren | grep defunct | awk '{print $2}' | wc -l"
    ret = sp.check_output(cmd, shell=True)
    return ret.decode("utf8").strip()

require_pid = "Please give me my child pid!"
require_count = "How many children were born?"
delims = [require_pid, require_count]

io = process("./children")
count = 0
while True:
    ret = io.recvuntil(delims)
    msg = ret.decode("utf8")
    print(msg)

    if re.search(r'^Please', msg, re.MULTILINE):
        pid = get_child_pid()
        print(pid)
        count = count + 1
        io.sendline(pid)
    elif re.search(r'^How', msg, re.MULTILINE):
        print(count)
        count = count_children()
        print(count)
        io.sendline(str(count))
        break
    else:
        pass

print(io.recvrepeat(1000))

