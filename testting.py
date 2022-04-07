from random import randint, randrange, sample, shuffle

class main_game:
	num = 3
	rand = ""
	num_text = ["nol", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan"]
	win = False

	def __init__(self, num=3):
		self.num = num
		self.rand = self.gen_rand()

	def gen_rand(self):
		rs = sample(range(0,9), self.num)
		return "".join(str(x) for x in rs)

	def get_rand(self):
		return self.rand

	def check_num(self, n1, n2):
		for i in n1:
			for j in n2:
				if i == j:
					return True
		return False

	def clue_1(self):
		rand_index = randint(0, self.num-1)
		num_clue = self.gen_rand()
		while self.check_num(self.rand, num_clue):
			num_clue = self.gen_rand()
		
		tnc = list(num_clue)
		tnc[rand_index] = self.rand[rand_index]
		return "".join(tnc)

	def clue_2(self):
		rand_index = randint(0, self.num-1)
		num_clue = self.gen_rand()
		while self.check_num(self.rand, num_clue):
			num_clue = self.gen_rand()
		return num_clue

	def clue_3(self):
		rand_index = randint(0, self.num-1)
		num_clue = self.gen_rand()
		while self.check_num(self.rand, num_clue):
			num_clue = self.gen_rand()

		tnc = list(num_clue)
		while(True):
			rand_index_2 = randint(0, self.num-1)
			if rand_index != rand_index_2:
				break
		
		tnc[rand_index] = self.rand[rand_index_2]
		return "".join(tnc)

	def clue_4(self):
		rand_index = randint(0, self.num-1)
		rand_index_2 = randint(0, self.num-1)
		while rand_index == rand_index_2:
			rand_index_2 = randint(0, self.num-1)
		rand_index_3 = randint(0, self.num-1)
		while rand_index == rand_index_3:
			rand_index_3 = randint(0, self.num-1)
		rand_index_4 = randint(0, self.num-1)
		while True: 
			if rand_index_2 != rand_index_4 and rand_index_3 != rand_index_4:
				break
			rand_index_4 = randint(0, self.num-1)
		num_clue = self.gen_rand()
		while self.check_num(self.rand, num_clue):
			num_clue = self.gen_rand()

		tnc = list(num_clue)
		tnc[rand_index_3] = self.rand[rand_index] 
		tnc[rand_index_4] = self.rand[rand_index_2] 

		return "".join(tnc)
		
	def gen_clue(self):
		"""
		Clue :
		1. satu angka benar dan ditempatkan dengan baik
		2. tidak ada yang benar
		3. satu angka benar tetapi salah ditempatkan
		4. dua angka benar tetapi salah ditempatkan  
		"""
		blue = "\033[94m"
		reset = "\033[0m"
		clue = ""
		c1 = f"{blue}{self.clue_1()}{reset}"
		c2 = f"{blue}{self.clue_2()}{reset}"
		c3 = f"{blue}{self.clue_3()}{reset}"
		c4 = f"{blue}{self.clue_4()}{reset}"
		clue += f"1. [{c1}] => satu angka benar dan ditempatkan dengan baik.\n"
		clue += f"2. [{c2}] => tidak ada yang benar.\n"
		clue += f"3. [{c3}] => satu angka benar tetapi salah ditempatkan.\n"
		clue += f"4. [{c4}] => dua angka benar tetapi salah ditempatkan.\n"
		
		return clue

	def guess_number(self, guess):
		"""
		Rules :
		1. angka benar
		2. ditempatkan dengan baik
		2. salah ditempatkan
		Text Rules :
		1. <n> angka benar dan ditempatkan dengan baik
		2. <n> angka benar tetapi salah ditempatkan
		3. <n> angka benar dan <n> angka ditempatkan dengan baik
		4. tidak ada yang benar
		"""
		red = '\033[91m'
		green = '\033[92m'
		reset = '\033[0m'

		benar = 0
		pos = 0
		for i in range(len(guess)):
			for j in range(len(self.rand)):
				if guess[i] == self.rand[j]:
					benar += 1
					if i == j:
						pos += 1
		text = ""
		if benar == 0:
			return red+"tidak ada yang benar"+reset 
		if benar == pos:
			if benar==self.num:
				text = f"{guess} => Hore!!"
				self.win = True
				return green+"Kode Terpecahkan!!!!"+reset
			else:
				text = f"{guess} => {benar} angka benar dan ditempatkan dengan baik"
				return f"{green}{self.num_text[benar]} angka benar dan ditempatkan dengan baik{reset}"
		else:
			txt_pos = "tetapi salah ditempatkan" if pos==0 else f"dan {self.num_text[pos]} angka ditempatkan dengan baik"
			text = f"{guess} => {benar} angka benar {txt_pos}"
			return f"{green}{self.num_text[benar]} angka benar{reset}, {red}{txt_pos}{reset}"
		return "-"


def not_in(num):
	ret = []
	for i in range(0,10):
		if str(i) not in num:
			ret.append(str(i))
	shuffle(ret)
	return ret 


gem = main_game(3)
gem.rand = "916"
print(f"\n\t{gem.get_rand()}\n")

# CLue 1
rand_index = randint(0, gem.num-1)
print("\n=============\n")
print(rand_index)
noi = not_in(gem.rand)
print(noi)
num_clue = noi[0:4]
print(num_clue)
num_clue[rand_index] = gem.rand[rand_index] 
print(num_clue)
print("\n=============\n")

print("CLUE 1 ", end=" : ")
print("".join(num_clue))

# CLue 1
print("\n=============\n")
noi2 = noi
shuffle(noi2)
num_clue = noi2[0:4]

print("CLUE 2 ", end=" : ")
print("".join(num_clue))

# CLue 3
print("\n=============\n")
rand_index = randint(0, gem.num-1)
rand_index2 = randint(0, gem.num-1)
while rand_index == rand_index2:
	rand_index2 = randint(0, gem.num-1)

print(rand_index)
print(rand_index2)
noi3 = noi2
shuffle(noi3)
num_clue = noi3[0:4]
num_clue[rand_index2] = gem.rand[rand_index] 
print("\n=============\n")

print("CLUE 3 ", end=" : ")
print("".join(num_clue))


# CLue 4
print("\n=============\n")
rand_index = randint(0, gem.num-1)
rand_index2 = randint(0, gem.num-1)
while rand_index == rand_index2:
	rand_index2 = randint(0, gem.num-1)
rand_index3 = randint(0, gem.num-1)
while rand_index3 in [rand_index, rand_index2]:
	rand_index3 = randint(0, gem.num-1)
rand_index4 = randint(0, gem.num-1)
while rand_index4 in [rand_index, rand_index2, rand_index3]:
	rand_index4 = randint(0, gem.num-1)

print(rand_index)
print(rand_index2)
print(rand_index3)
print(rand_index4)
noi4 = noi3
shuffle(noi4)
num_clue = noi3[0:4]
num_clue[rand_index3] = gem.rand[rand_index] 
num_clue[rand_index4] = gem.rand[rand_index2] 
print("\n=============\n")

print("CLUE 3 ", end=" : ")
print("".join(num_clue))

# rand_index = randint(0, gem.num-1)
# num_clue = gem.gen_rand()
# while gem.check_num(gem.rand, num_clue):
# 	num_clue = gem.gen_rand()

# tnc = list(num_clue)
# tnc[rand_index] = gem.rand[rand_index]
# c1 = "".join(tnc)
# print(c1)







"""
game = main_game()
clue = game.gen_clue()
clue = clue.split("\n")

print(ban.print_border())
print(ban.print_text(f"Tebak {game.num_text[game.num]} digit angka"))
print(ban.print_text(f"Masukan angka yang anda tebak dibawah"))
print(ban.print_text(f"Jika menyerah ketikan q"))
print(ban.print_text(f"Petunjuk : "))
for c in clue:
	print(ban.print_text(c))
print(ban.print_border())

print(game.get_rand())
guess = 0
attempt = 0
while True:
	print("")
	print("Tebak angka : ", end="")
	guess = input()
	if guess.isnumeric():
		result = game.guess_number(guess)
		print(guess+" => "+result)
		if game.win :
			print("Horee")
			break
	else:
		if guess == "q":
			print("Break")
			break

		print(f"Harus angka!!")

"""