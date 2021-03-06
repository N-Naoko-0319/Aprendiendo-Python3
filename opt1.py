import curses, fonts, options
from db.users import User

username = str('User')
password = str('password')

if User(username, password).authenticate_user():
    user = User(username, password)
else:
	User(username, password).create_user()
	user = User(username, password)

#------------------------------------Base de Datos------------------------------------
#-----------------Configuración-----------------
color_bold = ('white') #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Color de fondo.
color_lyrics = ('black') #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Color de letra.

cursor = 1
#-----------------------------------------------<<<

##-------------------Opcional-------------------

CURSOR = { #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Tipo decursores.
	1: '|> ',
	2: ' > ',
	3: '-> ',
	4: '- ',
	5: ''
}

COLOR_LYRICS = { #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Paleta para Letra.
	'white': curses.COLOR_WHITE,
	'blue': curses.COLOR_BLUE,
	'red': curses.COLOR_RED,
	'black': curses.COLOR_BLACK,
	'yellow': curses.COLOR_YELLOW,
	'cyan': curses.COLOR_CYAN,
	'green': curses.COLOR_GREEN,
}

COLOR_BOLD = { #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . Paleta para fondo.
	'white': curses.COLOR_WHITE,
	'blue': curses.COLOR_BLUE,
	'red': curses.COLOR_RED,
	'black': curses.COLOR_BLACK,
	'yellow': curses.COLOR_YELLOW,
	'cyan': curses.COLOR_CYAN,
	'green': curses.COLOR_GREEN,
}

#-----------------------------------------------<<<

#-------------------Colores--------------------
color_lyrics = COLOR_LYRICS[color_lyrics] #. . . . . . . . . . . . . . . . . . . . . . . . . . . . . Almacena los colores.
color_bold = COLOR_BOLD[color_bold]
cursor = CURSOR[cursor]

curses.init_pair(1, color_bold, color_lyrics)
#----------------------------------------------<<<
#-------------------------------------------------------------------------------------<<<

x = curses.LINES // 2
y = curses.COLS // 2

curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_RED)
curses.init_pair(4, curses.COLOR_BLACK, curses.COLOR_GREEN)

screen = curses.initscr()

def up_down(num):
	fonts.tittle(screen, '~ O P C I O N E S ~')
	screen.border()
	line = x - 5
	text1 = str(' > Encendido < ')
	text2 = str(' > Apagado < ')
	text3 = str('   Encendido   ')
	text4 = str('   Apagado   ')

	if num == 2:
		y = curses.COLS // 2 * 2 - len(text2) - 2
		screen.addstr(line + 2, y - 1, text2, curses.A_STANDOUT | curses.color_pair(3))

		y = curses.COLS // 2 * 2 - len(text3) - 2
		screen.addstr(line, y, text3)

	elif num == 1:
		y = curses.COLS // 2 * 2 - len(text1) - 2
		screen.addstr(line, y, text1, curses.A_STANDOUT | curses.color_pair(4))

		y = curses.COLS // 2 * 2 - len(text4) - 2
		screen.addstr(line + 2, y - 1, text4)

def opt(num, opt):
	screen.border()
	escape = False
	fonts.tittle(screen, '~ O P C I O N E S ~')

	up_down(num)

	option = True

	while escape == False:
		key = screen.getch(2, 1)

		if key == 259:
			num -= 1

			if num < 1: num = 1

			if num == 1: option = True
			elif num == 2: option = False

			screen.border()
			up_down(num)
			escape = False

		elif key == 258:
			num += 1

			if num > 2: num = 2

			if num == 1: option = True
			elif num == 2: option = False

			screen.border()
			up_down(num)
			escape = False

		elif key == 113:
			main_exit(screen)
			escape = True

		elif key in [curses.KEY_ENTER, ord('\n'), 10]:
			escape = True
			curses.endwin()

			if option == True:
				#------BASE DE DATOS------
				user.animation_config = 12
				#-------------------------
				
				main_exit(screen)
				escape = True

			elif option == False:
				#------BASE DE DATOS------
				user.animation_config = 0
				#-------------------------

				main_exit(screen)
				escape = True

		elif key == curses.KEY_RESIZE:
			screen.erase()
			screen.refresh()
			escape = True
			curses.endwin()
			fonts.error()

def main(screen):
	screen.border()
	fonts.tittle(screen, '~ O P C I O N E S ~')

	x2 = x - 5
	screen.addstr(x2, 3, 'Animacion', curses.color_pair(2) | curses.A_BOLD)
	screen.refresh()

	opt(1, True)

def main_exit(screen):
	screen.border()
	fonts.tittle(screen, '~ O P C I O N E S ~')

	x2 = x
	screen.addstr(x2, 3, 'Animacion', curses.color_pair(2) | curses.A_BOLD)
	curses.napms(user.animation_config)

	screen.erase()
	screen.refresh()
	curses.endwin()
	options.main(6)