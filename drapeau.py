from AX12 import AX12

moteur = AX12(135)

def leveDrapeau():
	moteur.move(90)
	return()

leveDrapeau()
