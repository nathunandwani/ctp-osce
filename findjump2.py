import subprocess
import os
import re

badchars = (
    "\x00\x0A\x0D"
    "\x2F"
    "\x3A\x3F"
    "\x40"
    "\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8A\x8B\x8C\x8D\x8E\x8F"
    "\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9A\x9B\x9C\x9D\x9E\x9F"
    "\xA0\xA1\xA2\xA3\xA4\xA5\xA6\xA7\xA8\xA9\xAA\xAB\xAC\xAD\xAE\xAF"
    "\xB0\xB1\xB2\xB3\xB4\xB5\xB6\xB7\xB8\xB9\xBA\xBB\xBC\xBD\xBE\xBF"
    "\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF"
    "\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF"
    "\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF"
    "\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF"
)

def getaddresses_pop_pop_ret(library, register):
    p1 = subprocess.Popen(["findjump2", library, register], stdout=subprocess.PIPE)
    ret_val = p1.communicate()[0]
    lines = ret_val.split("\n")
    addr_dict = {}
    for i in lines:
        if i.count("pop") > 1:
            addr = i.split(" ")[0]
            extracted = re.findall(r'0x[0-9A-F]+', addr, re.I)
            for j in extracted:
                if not j in addr_dict:
                    if checkbadchars(j, False) == 0:
                        addr_dict[j] = i.strip()
    return addr_dict

def checkbadchars(addr, exclude_null=True):
    addr = addr.replace("0x", "")
    tmp_addr = [addr[j:j+2] for j in range(0, len(addr), 2)]
    bad = 0
    for j in tmp_addr:
        addr_byte = int(j, 16)
        if exclude_null:
            if addr_byte == 0:
                continue
        for k in badchars:
            if addr_byte == ord(k):
                bad = 1
                break
    return bad

def print_dict(dictionary):
    for k, v in dictionary.items():
        print v.replace("\t", " ")

contents = ""
rop_commands = ""
with open("mona-modules.txt", "r") as f:
    contents = f.read()
lines = contents.split("\n")
print "\nPotential Candidates without Bad Characters\n"
for i in lines:
    arr = i.split("|")
    if ".dll" in i or ".exe" in i:
        os_dll = arr[7]
        if "False" in os_dll:
            base_addr = arr[0].split(" ")[3].replace(" ", "")
            bad = checkbadchars(base_addr)
            if bad == 0:
                pe = arr[8].split("[")[1].split("]")[0]
                temp = "---------------------------[" + pe + "]---------------------------\n"
                temp += "!mona rop -m " + pe + "\n"
                temp += i + "\n"
                eax = getaddresses_pop_pop_ret(pe, "eax")
                ebx = getaddresses_pop_pop_ret(pe, "ebx")
                ecx = getaddresses_pop_pop_ret(pe, "ecx")
                edx = getaddresses_pop_pop_ret(pe, "edx")
                esi = getaddresses_pop_pop_ret(pe, "esi")
                edi = getaddresses_pop_pop_ret(pe, "edi")
                esp = getaddresses_pop_pop_ret(pe, "esp")
                ebp = getaddresses_pop_pop_ret(pe, "ebp")
                if len(eax) > 0 or len(ebx) > 0 or len(ecx) > 0 or len(edx) > 0 or len(esi) > 0 or len(edi) > 0 or len(esp) > 0 or len(ebp) > 0:
                    print temp
                    print_dict(eax)
                    print_dict(ebx)
                    print_dict(ecx)
                    print_dict(edx)
                    print_dict(esi)
                    print_dict(edi)
                    print_dict(esp)
                    print_dict(ebp)
                    print ""

