import hashlib
sha1 = open("sha1.txt","w")
sha256 = open("sha256.txt","w")
md5 = open("md5.txt","w")

#print(hashlib.algorithms_available)
#print(hashlib.algorithms_guaranteed)

with open("numb.txt") as f:
    for line in f:
        line = line[:-1]
        sha1.write(str(hashlib.sha1(line.encode()).hexdigest())+"\n")
        sha256.write(str(hashlib.sha256(line.encode()).hexdigest())+"\n")
        md5.write(str(hashlib.md5(line.encode()).hexdigest()))
