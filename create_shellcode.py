import sys, re

if not sys.stdin.isatty():
    try:
        shellcode = ""
        lenght = 0
        while True:
            item = sys.stdin.readline()
            if item:
                if re.match("^[ ]*[0-9a-f]*:.*$",item):
                    item =item.split(":")[1].lstrip()
                    x = item.split("\t")
                    opcode = re.findall("[0-9a-f][0-9a-f]",x[0])
                    for i in opcode:
                        shellcode += "\\x" + i
                        lenght += 1
            else:
                break
        if shellcode == "":
            print("Nothing to extract")
        else:
            print("\n" + shellcode)
            print("\nLenght: " + str(lenght) + "\n")
    except:
        print("\nError! \n Usage:  objdump -d example.o | python shellcode_extractor.py")
        pass
else:
    print("\nError! \n Usage:  objdump -d example.o | python shellcode_extractor.py \n")
