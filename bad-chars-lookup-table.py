badchars = (
    "\x00"
    "\x80\x81\x82\x83\x84\x85\x86\x87\x88\x89\x8A\x8B\x8C\x8D\x8E\x8F"
    "\x90\x91\x92\x93\x94\x95\x96\x97\x98\x99\x9A\x9B\x9C\x9D\x9E\x9F"
    "\xA0\xA1\xA2\xA3\xA4\xA5\xA6\xA7\xA8\xA9\xAA\xAB\xAC\xAD\xAE\xAF"
    "\xB0\xB1\xB2\xB3\xB4\xB5\xB6\xB7\xB8\xB9\xBA\xBB\xBC\xBD\xBE\xBF"
    "\xC0\xC1\xC2\xC3\xC4\xC5\xC6\xC7\xC8\xC9\xCA\xCB\xCC\xCD\xCE\xCF"
    "\xD0\xD1\xD2\xD3\xD4\xD5\xD6\xD7\xD8\xD9\xDA\xDB\xDC\xDD\xDE\xDF"
    "\xE0\xE1\xE2\xE3\xE4\xE5\xE6\xE7\xE8\xE9\xEA\xEB\xEC\xED\xEE\xEF"
    "\xF0\xF1\xF2\xF3\xF4\xF5\xF6\xF7\xF8\xF9\xFA\xFB\xFC\xFD\xFE\xFF"
)

goodchars = ""
for i in range(0, 256):
    if not chr(i) in badchars:
        goodchars += chr(i)

#char mangled to x
#Ex. 0x00 becomes 0xEB, making 0x00 a bad char
#If the outcome is found in the bad char list,
#Use the bad char to generate the required instruction.
#Ex. 0xEB = jmp short 
#    0xEB (If this is part of the bad chars, use \x00 instead)
badchars_lookup = {
    "\x80":"\x01",
    "\x00":"\xEB",
    "\x81":"\x81\xea"
}

#http://ref.x86asm.net/coder32.html
basic_cmds = {
    "\x05":"ADD EAX, ?",
    "\x0D":"OR EAX, ?",
    "\x25":"AND EAX, ?",
    "\x2D":"SUB EAX, ?",
    "\x35":"XOR EAX, ?",
    "\x50":"PUSH EAX",
    "\x51":"PUSH ECX",
    "\x52":"PUSH EDX",
    "\x53":"PUSH EBX",
    "\x54":"PUSH ESP",
    "\x55":"PUSH EBP",
    "\x56":"PUSH ESI",
    "\x57":"PUSH EDI",
    "\x58":"POP EAX",
    "\x59":"POP ECX",
    "\x5A":"POP EDX",
    "\x5B":"POP EBX",
    "\x5C":"POP ESP",
    "\x5D":"POP EBP",
    "\x5E":"POP ESI",
    "\x5F":"POP EDI",
    "\x60":"PUSHAD",
    "\x61":"POPAD",
    "\x70":"JMP SHORT (JO) OF=1",
    "\x71":"JMP SHORT (JNO) OF=0",
    "\x72":"JMP SHORT (JB/JNAE/JC) CF=1",
    "\x73":"JMP SHORT (JNB/JAE/JNC) CF=0",
    "\x74":"JMP SHORT (JZ/JE) ZF=1",
    "\x75":"JMP SHORT (JNZ/JNE) ZF=0",
    "\x76":"JMP SHORT (JBE/JNA) CF=1 or ZF=1",
    "\x77":"JMP SHORT (JNB/JA) CF=0 and ZF=0",
    "\x78":"JMP SHORT (JS) SF=1",
    "\x79":"JMP SHORT (JNS) SF=0",
    "\x7A":"JMP SHORT (JP/JPE) PF=1",
    "\x7B":"JMP SHORT (JNP/JPO) PF=0",
    "\x7C":"JMP SHORT (JL/JNGE) SF!=OF",
    "\x7D":"JMP SHORT (JNL/JGE) SF=OF",
    "\x7E":"JMP SHORT (JLE/JNG) ZF=1 OR SF!=OF",
    "\x7F":"JMP SHORT (JNLE/JG) ZF=0 AND SF=OF",
    "\x81\xC1":"ADD ECX, ?",
    "\x81\xC2":"ADD EDX, ?",
    "\x81\xC3":"ADD EBX, ?",
    "\x81\xC4":"ADD ESP, ?",
    "\x81\xC5":"ADD EBP, ?",
    "\x81\xC6":"ADD ESI, ?",
    "\x81\xC7":"ADD EDI, ?",
    "\x81\xC8":"OR EAX, ?",
    "\x81\xC9":"OR ECX, ?",
    "\x81\xCA":"OR EDX, ?",
    "\x81\xCB":"OR EBX, ?",
    "\x81\xCC":"OR ESP, ?",
    "\x81\xCD":"OR EBP, ?",
    "\x81\xCE":"OR ESI, ?",
    "\x81\xCF":"OR EDI, ?",
    "\x81\xE1":"AND ECX, ?",
    "\x81\xE2":"AND EDX, ?",
    "\x81\xE3":"AND EBX, ?",
    "\x81\xE4":"AND ESP, ?",
    "\x81\xE5":"AND EBP, ?",
    "\x81\xE6":"AND ESI, ?",
    "\x81\xE7":"AND EDI, ?",
    "\x81\xE8":"SUB EAX, ?",
    "\x81\xE9":"SUB ECX, ?",
    "\x81\xEA":"SUB EDX, ?",
    "\x81\xEB":"SUB EBX, ?",
    "\x81\xEC":"SUB ESP, ?",
    "\x81\xED":"SUB EBP, ?",
    "\x81\xEE":"SUB ESI, ?",
    "\x81\xEF":"SUB EDI, ?",
    "\x81\xF1":"XOR ECX, ?",
    "\x81\xF2":"XOR EDX, ?",
    "\x81\xF3":"XOR EBX, ?",
    "\x81\xF4":"XOR ESP, ?",
    "\x81\xF5":"XOR EBP, ?",
    "\x81\xF6":"XOR ESI, ?",
    "\x81\xF7":"XOR EDI, ?",
    "\x9C":"PUSHFD",
    "\x9D":"POPFD",
    "\xEB":"JMP SHORT",
    "\xFF":"CALL",
    "\xC3":"RETN"
}

bad = []
good = []
for k, v in basic_cmds.items():
    found = 0
    for i in badchars:
        temp = ""
        for c in k:
            if c == i:
                found = 1
            temp += hex(ord(c)) + " "
    if found == 0:
        good.append(temp + "- " + v)
    else:
        bad.append(temp + "- " + v)

print "Instructions allowed:"
for i in good:
    print i
print ""
print "Instructions not allowed:"
for i in bad:
    print i
print ""
print "Instruction substitution:"
for k, v in badchars_lookup.items():
    temp1 = ""
    temp2 = ""
    for i in v:
        temp1 += hex(ord(i)) + " "
    temp1 = temp1[:-1]
    for i in k:
        temp2 += hex(ord(i)) + " "
    if v in basic_cmds:
        print "I can use " + basic_cmds[v] + " (" + temp1 + ") by entering " + temp2
