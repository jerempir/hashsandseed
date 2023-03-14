import hashlib
sha1 = open("sha1seed.txt","w")
sha256 = open("sha256seed.txt","w")
md5 = open("md5seed.txt","w")
seed = [2560,4,1000000,1000000000]
#print(hashlib.algorithms_available)
#print(hashlib.algorithms_guaranteed)

with open("unseednumb.txt") as f:
    for line in f:
        line = str(int(line[:-1]) + seed[3])
        sha1.write(str(hashlib.sha1(line.encode()).hexdigest())+"\n")
        sha256.write(str(hashlib.sha256(line.encode()).hexdigest())+"\n")
        md5.write(str(hashlib.md5(line.encode()).hexdigest())+"\n")

