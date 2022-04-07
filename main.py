import os
from lib.game import main_game
from lib.menu import *


def main():
	while True:
		cls_scrn()
		welcome_massage()
		print("  Menu :")
		print("  1. Main level Mudah")
		print("  2. Main level Medium")
		print("  3. Main level Susah")
		print("  4. Main level Sangat Susah")
		print("  5. Keluar")
		print("  Pilih Menu (1-5) : ",end="")

		menu = input()
		if menu == "1" or menu == "2" or menu == "3" or menu == "4":
			lvl = int(menu) + 2
			lvl = lvl if lvl < 6 else 5
			# print(lvl)
			mainkan(lvl)
		elif menu == "5" or menu=="q":
			quit()
			exit()
		else:
			print("Masukan Salah!!")
	

def mainkan(level):
	lvl = int(level)
	game = main_game(lvl)
	game_message(game)
	# print(game.get_rand())
	guess = 0
	attempt = 1
	while True:
		print("")
		print("  Tebak angka : ", end="")
		guess = input()
		if guess.isnumeric():
			if len(guess) == len(game.get_rand()):
				result = game.guess_number(guess)
				print("  "+guess+" => "+result)
				if game.win :
					print(f"  Selamat anda berhasil memecahkan kode angka dengan {attempt} kali mencoba")
					print("")
					print("  Main Lagi? (y/n) : ", end="")
					prom = input()
					if prom == "n":
						main()
					# game.win = False
					mainkan(lvl)
			else:
				print(styled("  Masukan tidak valid!", color="red", style="bright"))
				
		else:
			if guess == "q":
				print("")
				print(f"  Anda menyerah! kode yang harus dipecahkan = {game.get_rand()}")
				print("")
				print("  Main Lagi? (y/n) : ", end="")
				prom = input()
				if prom == "n":
					main()
				# game.win = False
				mainkan(lvl)
				break
			print(styled("  Harus angka!!", color="red", style="bright"))
		attempt+=1

from random import randint, randrange, sample

if __name__ == '__main__':
	main()
	# quit()
	# game = main_game(5)
	# # clue = game.gen_clue()
	# print(game.get_rand())
	
	# rand_index = randint(0, game.num-1)
	# num_clue = game.gen_rand()
	# while game.check_num(game.rand, num_clue):
	# 	num_clue = game.gen_rand()
	# 	print(f" - {num_clue}")
	
	# tnc = list(num_clue)
	# tnc[rand_index] = game.rand[rand_index]
	# # return "".join(tnc)
	# print("".join(tnc))

