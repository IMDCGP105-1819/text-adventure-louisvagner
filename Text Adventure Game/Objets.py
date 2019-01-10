# Important objects - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

class Item:
    def __init__(self, name, description, location):
        self.name = name
        self.description = description
        self.location = location

items = []
names = []
position = []

uniform = Item("uniform","- Shirt and trouser representative of the vault you are in. \n /!\ Put it on before getting out of the barracks.", (2, 0))
    #A mettre sinon <<Intrusion>>

watch = Item("watch","- Bracelet giving the time.", (3, 1))
    #avoir une idée de l'heure

broom = Item("broom","- Long broom that helps get rid of dust.", (3, 3))
    #chasser les rats
             
notebook = Item("notebook","- Block with several sheets of paper, it is possible to write in if used.", (3, 7))
    #permet d'ecrire ce qu'on veut

adhesive_tape = Item("adhesive tape","- Very sticky DIY adhesive tape.", (3, 5))
    #colmater les tuyaux

armor = Item("armor","- Protection for the body used for combat. It comes with a gas mask for when you go outside of the shelter", (1, 6))
    #augmente la défense

gun = Item("gun","- Firearm used to defend or kill. The gun is not loaded.", (1 ,6))
    #permet de se defendre

bullets = Item("bullets","- Ammunition used with a gun.", (1, 9))
    #à équiper avec l'arme

dagger = Item("dagger","- basic knife used as a weapon in close combat.", (3, 3))
    #prendre pour finir mieux l'histoire

"""extinguisher = Item("extinguisher","Object to extinguish a fire.")
    #eteindre le feu

first_aid = Item("first aid kit","Care kit used between fights.")
    #se soigner

junks_scrap = Item("junks and scrap","old bits of junk and scrap for the sole purpose of being recycled.")
    #pour construire son arme

antiradiation_suit = Item("anti-radiation suit","radiation protection suit.")
    #protège des radiations (pas totalement)

antiradiation_care = Item("anti-radiation care","care that cancels the effects of radiation.")
    #soigne les radiations
             
gun_parts = Item("gun parts","random pieces from gun.")
    #pour construire son arme

muscle_work = Item("weight","common object in a gym to build muscles.")
    #se muscler

shelter_map = Item("map","allows you to find your way when you are lost.")
    #la carte"""

# Objects that can't move - - - - - - - - - - - - - - - - - - - - - - - - - - -

lever = Item("lever","- Opens the Vault door when actioned.", (1, 2))
    #permet d'ouvrir la porte pur sortir

buttons = Item("buttons","- Can lead you to the lower and upper levels of the vault, just press the buttons.", (2, 2))
    #permet d'atteindre les autres etages
buttosn = Item("buttons","- Can lead you to the lower and upper levels of the vault, just press the buttons.", (2, 6))
    #permet d'atteindre les autres etages
buttons = Item("buttons","- Can lead you to the lower and upper levels of the vault, just press the buttons.", (2, 10))
    #permet d'atteindre les autres etages

"""class alarm_button:
    pass

class jukebox:
    pass

class fountain:
    pass

class control_panel:
    pass

class medical_bed:
    pass

class microscope:
    pass

class machines:
    pass"""

# Objects with no specific use - - - - - - - - - - - - - - - - - - - - - - - - -

bottles = Item("bottles","- Bottles filled with fresh water.", (3, 3))
    #assouvi la soif

toolbox = Item("toolbox","- Box containing several DIY tools. Repairs things broken.", (3, 7))
    #reparer les machines

syringes = Item("syringes","- Chemicals use for experiments on rats.",(3, 9))
    #produit chimique experimental

rats = Item("rats","- There is a little group of rats playing around.", (1, 6))
    #a faire evacuer avant de rentrer

"""class alarm_clock:
    pass

class plates:
    pass

class boxes:
    pass

class chemicals:
    #peut tuer si on les boits
    pass
"""

items.append(uniform.description)#0
items.append(watch.description)#1
items.append(broom.description)#2
items.append(notebook.description)#3
items.append(toolbox.description)#4
items.append(adhesive_tape.description)#5
items.append(armor.description)#6
items.append(gun.description)#7
items.append(lever.description)#8
items.append(buttons.description)#9
items.append(bottles.description)#10
items.append(syringes.description)#11
items.append(rats.description)#12
items.append(bullets.description)#13
items.append(dagger.description)#14

names.append(uniform.name)#0
names.append(watch.name)#1
names.append(broom.name)#2
names.append(notebook.name)#3
names.append(toolbox.name)#4
names.append(adhesive_tape.name)#5
names.append(armor.name)#6
names.append(gun.name)#7
names.append(lever.name)#8
names.append(buttons.name)#9
names.append(bottles.name)#10
names.append(syringes.name)#11
names.append(rats.name)#12
names.append(bullets.name)#13
names.append(dagger.name)#14

position.append(uniform.location)#0
position.append(watch.location)#1
position.append(broom.location)#2
position.append(notebook.location)#3
position.append(toolbox.location)#4
position.append(adhesive_tape.location)#5
position.append(armor.location)#6
position.append(gun.location)#7
position.append(lever.location)#8
position.append(buttons.location)#9
position.append(bottles.location)#10
position.append(syringes.location)#11
position.append(rats.location)#12
position.append(bullets.location)#13
position.append(dagger.location)#14
