health=100
armour=50


def hit(dmg):
    global health
    global armour
    if armour>0:
        armour-=dmg
        print(f"your amour got hit for, {dmg}")
        if armour<0:
             print(f'you have 0 armour left')
             print("your armour broke")
             extrdmg=armour
             
    else:
        health += armour
        health -= dmg
        print(f'you took {dmg}, you have {health} health left')
   


