from random import randint, randrange, sample, shuffle

class main_game:
	num = 3
	rand = ""
	num_text = ["nol", "satu", "dua", "tiga", "empat", "lima", "enam", "tujuh", "delapan", "sembilan"]
	win = False
	noi = []

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
		self.noi = self.not_in(self.rand)
		num_clue = self.noi[0:self.num]
		num_clue[rand_index] = self.rand[rand_index] 
		return "".join(num_clue)

	def clue_2(self):
		noi = self.noi
		shuffle(noi)
		num_clue = noi[0:self.num]
		return "".join(num_clue)

	def clue_3(self):
		rand_index = randint(0, self.num-1)
		rand_index2 = randint(0, self.num-1)
		while rand_index == rand_index2:
			rand_index2 = randint(0, self.num-1)

		noi = self.noi
		shuffle(noi)
		num_clue = noi[0:self.num]
		num_clue[rand_index2] = self.rand[rand_index] 
		return "".join(num_clue)

	def clue_4(self):
		rand_index = randint(0, self.num-1)
		rand_index2 = randint(0, self.num-1)
		while rand_index == rand_index2:
			rand_index2 = randint(0, self.num-1)
		rand_index3 = randint(0, self.num-1)
		while rand_index3 in [rand_index, rand_index2]:
			rand_index3 = randint(0, self.num-1)
		rand_index4 = randint(0, self.num-1)
		if self.num > 3:
			while rand_index4 in [rand_index, rand_index2, rand_index3]:
				rand_index4 = randint(0, self.num-1)

		noi = self.noi
		shuffle(noi)
		num_clue = noi[0:self.num]
		num_clue[rand_index3] = self.rand[rand_index] 
		num_clue[rand_index4] = self.rand[rand_index2] 
		return "".join(num_clue)

		
	"""
	Clue :
	1. satu angka benar dan ditempatkan dengan baik
	2. tidak ada yang benar
	3. satu angka benar tetapi salah ditempatkan
	4. dua angka benar tetapi salah ditempatkan  
	"""
	def gen_clue(self):
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
	def guess_number(self, guess):
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

	def not_in(self, num):
		ret = []
		for i in range(0,10):
			if str(i) not in num:
				ret.append(str(i))
		shuffle(ret)
		return ret 

	def gen_clue2(self):
		rand_index = randint(0, self.num-1)
		rand_index2 = randint(0, self.num-1)
		while rand_index == rand_index2:
			rand_index2 = randint(0, self.num-1)

		noi = self.noi
		shuffle(noi)
		num_clue = noi[0:self.num]
		num_clue[rand_index2] = self.rand[rand_index] 
		return "".join(num_clue)




# game = main_game(4)
# print(game.get_rand())
# print("_______________")
# print(game.clue_1())
# print(game.clue_2())
# print(game.clue_3())
# print(game.clue_4())
# print("===============")
# print(game.gen_clue2())


# game = main_game(4)
# r = game.get_rand()
# print(r)
# print(" ")
# print(game.gen_clue())

# game.rand = "432"
# guess = []
# # Text Rule 1
# guess.append("418")
# guess.append("138")
# guess.append("182")
# guess.append("438")
# guess.append("832")
# # Text Rule 2
# guess.append("184")
# guess.append("124")
# guess.append("324")
# # Text Rule 3
# guess.append("423")
# guess.append("234")
# guess.append("987")
# guess.append("432")


# game.rand = "4325"
# guess = []
# # Text Rule 1
# guess.append("4987")
# guess.append("9387")
# guess.append("9827")
# guess.append("9875")
# # Text Rule 2
# guess.append("9874")
# guess.append("9843")
# guess.append("9432")
# guess.append("5432")
# # Text Rule 3
# guess.append("4873")
# guess.append("4372")
# guess.append("4352")


# print(game.get_rand())
# for g in guess:
# 	print(g+" => "+game.guess_number(g))