#WARNING: VERY SLOPPY CODE AHEAD 
#NEED TO ADD OPERATORS WITH OTHER REGISTERS
#Ex: AND EBX, ?
#    AND ECX, ?

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

goodchars = []
for i in range(0, 256):
    if not chr(i) in badchars:
        goodchars.append(i)

#http://ref.x86asm.net/coder32.html
basic_cmds = {
    "\x05":"ADD EAX, ?",
    "\x0D":" OR EAX, ?",
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
    "\x58":"POP ECX",
    "\x58":"POP EDX",
    "\x58":"POP EBX",
    "\x58":"POP ESP",
    "\x58":"POP EBP",
    "\x58":"POP ESI",
    "\x58":"POP EDI",
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
    "\xEB":"JMP SHORT",
    "\xFF":"CALL",
    "\xC3":"RETN"
}
bad = []
good = []
for k, v in basic_cmds.items():
    found = 0
    for i in badchars:
        if k == i:
            found = 1
            bad.append(hex(ord(k)) + " - " + v)
            break
    if found == 0:
        good.append(hex(ord(k)) + " - " + v)

def sub_encoder(max_limit, shellcode):
    print "SUB Encoder"
    subtract_term1 = []
    subtract_term2 = []
    subtract_term3 = []
    v = tohex(0 - toint(shellcode), 32)
    v = v.replace("0x", "")
    v = v.replace("L", "")
    sh = [v[j:j+2] for j in range(0, len(v), 2)]
    inner_limit = 0
    for i in range(0, 256):
        if not chr(i) in badchars:
            inner_limit = i
            break
    
    threeterms = False
    for i in sh:
        if int(i, 16) > (max_limit - inner_limit) * 2:
            threeterms = True
    
    for i in sh:
        current = int(i, 16)
        counter1 = 0
        counter2 = 0
        if threeterms:
            if current > (max_limit - inner_limit) * 2:
                current -= (max_limit - inner_limit) * 2
                counter1 = max_limit - inner_limit
                counter2 = max_limit - inner_limit
            else:
                if current > max_limit - inner_limit - inner_limit:
                    current -= max_limit 
                    counter1 = max_limit - inner_limit
                    counter2 = inner_limit
                else:
                    current -= inner_limit * 2
                    counter1 = inner_limit
                    counter2 = inner_limit
            while chr(current) in badchars:
                if current > inner_limit:
                    current -= 1
                    if counter1 + 1 <= max_limit and not chr(counter1 + 1) in badchars: 
                        counter1 += 1
                    else:
                        if counter2 + 1 <= max_limit and not chr(counter2 + 1) in badchars:
                            counter2 += 1
                        else:
                            current += 1
                            print "Couldn't switch values from here (): " + "%0.2X" % current + " | " + "%0.2X" % counter1 + " | " + "%0.2X" % counter2
                            break
            subtract_term1.append("%0.2X" % current)
            subtract_term2.append("%0.2X" % counter1)
            subtract_term3.append("%0.2X" % counter2)
        else:
            current -= 1
            counter1 += 1
            while current > (max_limit - 2) or (chr(current) in badchars and current > 0) or chr(counter1) in badchars:
                current -= 1
                counter1 += 1
            subtract_term1.append("%0.2X" % current)
            subtract_term2.append("%0.2X" % counter1)

    tmpterm1 = ""
    tmpterm2 = ""
    tmpterm3 = ""
    for i in subtract_term1:
        tmpterm1 += '\\x' + i
    for i in subtract_term2:
        tmpterm2 += '\\x' + i
    for i in subtract_term3:
        tmpterm3 += '\\x' + i
    print '"\\x2D' + tmpterm1 + '"' + " # SUB EAX, " + ''.join(list(reversed(subtract_term1))) + " # BIN => 2D" + ''.join(subtract_term1)
    print '"\\x2D' + tmpterm2 + '"' + " # SUB EAX, " + ''.join(list(reversed(subtract_term2))) + " # BIN => 2D" + ''.join(subtract_term2)
    olly = "For ollydbg binary paste: 2D" + ''.join(subtract_term1) + "2D" + ''.join(subtract_term2)
    if threeterms:
        print '"\\x2D' + tmpterm3 + '"' + " # SUB EAX, " + ''.join(list(reversed(subtract_term3))) + " # BIN => 2D" + ''.join(subtract_term3)
        olly += "2D" + ''.join(subtract_term3)
    print olly

def operator(operation, fourbytesh):
    if operation == "XOR" and "\x35" in badchars:
        return 0
    if operation == "ADD" and "\x05" in badchars:
        return 0
    if operation == "SUB" and "\x2D" in badchars:
        return 0
    
    machine_code = "\x35"
    if operation == "ADD":
        machine_code = "\x05"
    if operation == "SUB":
        machine_code = "\x2D"
    print "Encoding with " + operation
    decoder = operation + " EAX, "
    encoded = ""
    all_success = 1
    d_machine_code = ""
    for i in fourbytesh:
        success = 0
        for j in goodchars:
            if operation == "XOR":
                result = ord(i) ^ j
            elif operation == "ADD":
                result = ord(i) + j
            elif operation == "SUB":
                result = ord(i) - j
            if result in goodchars and result >= 0 and result <= 255:
                decoder += "%0.2X" % result
                d_machine_code += "%0.2X" % result
                encoded += "%0.2X" % j
                success = 1
                break
        if success == 0:
            print "Can't encode " + "%0.2X" % ord(i) + " through operator " + operation
            all_success = 0
    if all_success == 1:
        print "Encoded: " + encoded + ", Decoder: " + decoder
        print "Encoded (B): " + encoded + ", Decoder (B): " + "%0.2X" % ord(machine_code) + d_machine_code
    return all_success

def twoscomplement(val):
    v = tohex(0 - toint(val), 32)
    v = v.replace("0x", "")
    v = v.replace("L", "")
    return '"' + ''.join(['\\x' + v[j:j+2] for j in range(0, len(v), 2)]) + '"'

def toint(val):
    temp = ""
    for i in val:
        temp += "%0.2X" % ord(i)
    return int(temp, 16)   

def tohex(val, nbits):
  return hex((val + (1 << nbits)) % (1 << nbits))

def printshellcode(val):
    temp = ""
    for i in val:
        temp += "\\x%0.2X" % ord(i)
    return '"' + temp + '"'

def zero_reg(maximum):
    counter = 0
    tmpbin = ""
    if ord("\x25") in goodchars:
        for i in goodchars:
            for j in goodchars:
                if i & j == 0:
                    x = ("%02.X" % i)
                    y = ("%02.X" % j)
                    first = "AND EAX, " + x * 4
                    second = "AND EAX, " + y * 4
                    print "Can be used to clear EAX: "
                    print '"\\x25\\x' + x + '\\x' + x + '\\x' + x + '\\x' + x + '" # ' + first + " # BIN => 25" + x * 4 
                    print '"\\x25\\x' + y + '\\x' + y + '\\x' + y + '\\x' + y + '" # ' + second + " # BIN => 25" + y * 4
                    print 'For ollydbg binary paste: 25' + x * 4 + '25' + y * 4 
                    counter += 1
                    if counter == maximum:
                        print ""
                        return
    if ord("\x33") in goodchars and ord("\xC0") in goodchars:
        print "Can be used to clear EAX: "
        print '"\\x33\\xC0" # XOR EAX, EAX'

#print "Commands allowed based on bad character list:"
#for i in good:
#    print i

#print ""
#print "Commands not allowed based on bad character list:"
#for i in bad:
#    print i
#print ""

#fourbytesh = "\xaf\xea\x75\xaf"
#fourbytesh = "\x2e\xcd\x58\x02"
fourbytesh = "\x74\x5a\x05\x3c"
print "Original Shellcode: \t" + printshellcode(fourbytesh)
print ""
print "Sub Encoder"
print "Reversed: \t\t" + printshellcode(fourbytesh[::-1])
print "Two's Complement: \t" + twoscomplement(fourbytesh[::-1])
sub_encoder(0x7f, fourbytesh[::-1])
print ""
zero_reg(1)     
if operator("XOR", fourbytesh[::-1]) == 0:
    print "XOR FAILED"
    print ""
    if operator("ADD", fourbytesh[::-1]) == 0:
        print "ADD FAILED"
        print ""
        if operator("SUB", fourbytesh[::-1]) == 0:
            print "SUB FAILED"
            print ""
