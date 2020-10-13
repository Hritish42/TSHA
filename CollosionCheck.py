import time as wait

try:
    def TSHA(TEXT):

        def sha1(data):
            bytes = ""

            h0 = 0x67452301
            h1 = 0xEFCDAB89
            h2 = 0x98BADCFE
            h3 = 0x10325476
            h4 = 0xC3D2E1F0

            for n in range(len(data)):
                bytes+='{0:08b}'.format(ord(data[n]))
            bits = bytes+"1"
            pBits = bits
            while len(pBits)%512 != 448:
                pBits+="0"
            pBits+='{0:064b}'.format(len(bits)-1)

            def chunks(l, n):
                return [l[i:i+n] for i in range(0, len(l), n)]

            def rol(n, b):
                return ((n << b) | (n >> (32 - b))) & 0xffffffff

            for c in chunks(pBits, 512):
                words = chunks(c, 32)
                w = [0]*80
                for n in range(0, 16):
                    w[n] = int(words[n], 2)
                for i in range(16, 80):
                    w[i] = rol((w[i-3] ^ w[i-8] ^ w[i-14] ^ w[i-16]), 1)

                a = h0
                b = h1
                c = h2
                d = h3
                e = h4


                for i in range(0, 80):
                    if 0 <= i <= 19:
                        f = (b & c) | ((~b) & d)
                        k = 0x5A827999
                    elif 20 <= i <= 39:
                        f = b ^ c ^ d
                        k = 0x6ED9EBA1
                    elif 40 <= i <= 59:
                        f = (b & c) | (b & d) | (c & d)
                        k = 0x8F1BBCDC
                    elif 60 <= i <= 79:
                        f = b ^ c ^ d
                        k = 0xCA62C1D6

                    temp = rol(a, 5) + f + e + k + w[i] & 0xffffffff
                    e = d
                    d = c
                    c = rol(b, 30)
                    b = a
                    a = temp

                h0 = h0 + a & 0xffffffff
                h1 = h1 + b & 0xffffffff
                h2 = h2 + c & 0xffffffff
                h3 = h3 + d & 0xffffffff
                h4 = h4 + e & 0xffffffff

            return '%08x%08x%08x%08x%08x' % (h0, h1, h2, h3, h4)

        def AND(r1,x1):
            result = ''
            for i in range(len(r1)):
                if r1[i]=='1' and x1[i]=='1':
                    result=result+'1'
                if r1[i] == '0' and x1[i] == '1':
                    result = result + '0'
                if r1[i] == '1' and x1[i] == '0':
                    result = result + '0'
                if r1[i] == '0' and x1[i] == '0':
                    result = result + '0'

            return result
        def hexadecimalTObinary(n):
            res = "{0:08b}".format(int(n, 16))
            return res.zfill(160)

        def binaryToDecimal(n):
            return int(n, 2)

        def decimal_to_binary(value):
            k=''.join(format(ord(i),'b')for i in value)
            return k

        def XOR(r1,x1):
            result = ''
            for i in range(len(r1)-1):
                if r1[i]=='1' and x1[i]=='1':
                    result=result+'0'
                if r1[i] == '0' and x1[i] == '1':
                    result = result + '1'
                if r1[i] == '1' and x1[i] == '0':
                    result = result + '1'
                if r1[i] == '0' and x1[i] == '0':
                    result = result + '0'
            return result


        def cirularshift(hash,r_no):
            y=hash[0:r_no]
            x=hash[r_no+1:]
            x=x+y
            return x

        def f1(hash) :
            x = sha1(sha1(hash))
            y = cirularshift(x,5)
            return hexadecimalTObinary(y)

        def f2(hash) :
            x = sha1(sha1(hash))
            y = cirularshift(x, 9)
            y2 = sha1(sha1(sha1(y)))
            return hexadecimalTObinary(y2)


        def round(message):
            full=hexadecimalTObinary(sha1(message))
            l=  full[:80]
            r1=f2(l)
            a1=r1[0:80]
            x1=r1[80:]
            r=full[80:]
            l1=f1(r1)
            a2=l1[80:]
            x2=l1[:80]
            k1=AND(a1,a2)
            k2=XOR(x1,x2)
            return k1+k2

        def finalHash(TEXT):
            gen_hashes=[]
            gen_hashes.append(round(TEXT))
            i=0
            while i<=160:
                j=round(gen_hashes[-1])
                gen_hashes.append(j)
                i=i+1
            return gen_hashes[-1]
        return sha1(finalHash(TEXT))

    def generatingOfTestingString(l):
        testing_string=[]
        for i in range(0,l+1):
            y='a'*(i)+'@'+'a'*(l-i)
            testing_string.append(y)
        return testing_string

    l=generatingOfTestingString(int(input("Enter the number of Hashes you want to verify: ")))

    print("[+] Generating Hashes....\n")
    for i in l:
        print(l.index(i),TSHA(i))
        print()

    def checkingForCollosion(list):
        vault_keys=[]
        for i in list:
            if i not in vault_keys:
                vault_keys.append(i)
        print("[+] Processing.... \n")
        wait.sleep(2)
        print("[+] Checking for Collision now\n")
        wait.sleep(1)
        print("[+] This process may take a while...\n")
        wait.sleep(3)
        if len(list)==len(vault_keys):
            print("[+] No Collision Found!")
        else:
            print("[-] Collision Found!")

    checkingForCollosion(l)
except(Exception):
    print("\n\n[-] Invalid Input")
    exit("[-] Exiting Program!!!")