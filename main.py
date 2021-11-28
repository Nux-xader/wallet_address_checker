import sys, os

def clr():
    os.system('cls' if os.name == 'nt' else 'clear')

def banner():
    print("""
 ▄▀█ █▀▄ █▀▄ █▀█ █▀▀ █▀ █▀
 █▀█ █▄▀ █▄▀ █▀▄ ██▄ ▄█ ▄█
 
 █▀▀ █░█ █▀▀ █▀▀ █▄▀ █▀▀ █▀█
 █▄▄ █▀█ ██▄ █▄▄ █░█ ██▄ █▀▄ V1.0.0

 Contact         : https://wa.me/+6281251389915
 About Developer : https://github.com/Nux-xader
 ________________________________________________
""")


def loadData(label):
	while True:
		try:
			path = str(input(label))
			data = [x for x in open(path, "r").read().split("\n") if len(x) > 10]
			return data
		except Exception as e:
			print(f" [!] File {path} not found, please input file again")

def main():
	clr()
	banner()
	data = loadData(" Input file check (nama file yang akan di cek) : ")
	database = loadData(" Input file database (nama file patokan untuk di cek) : ")
	while True:
		folder = str(input(" Save result to : "))
		try:
			os.mkdir(folder)
			break
		except:
			print(f" [!] Folder {folder} already exists, please input another name")
	clr()
	banner()
	valid, invalid = 0, 0
	for x in data:
		if x in database:
			open(f"{folder}/valid.txt", "a").write(f"{x}\n")
			print(f" Valid >> [{x}]")
			valid+=1
		else:
			open(f"{folder}/invalid.txt", "a").write(f"{x}\n")
			print(f" Invalid >> [{x}]")
			invalid+=1
	clr()
	banner()
	print(f" Success checking {len(data)} address")
	print(f" Valid addrsss : {valid}")
	print(f" Invalid addrsss : {invalid}")
	print(f" Result check has saved to : {folder}")



if __name__ == '__main__':
	main()