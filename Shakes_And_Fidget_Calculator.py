# author: Fabian Roscher
# date: 30.01.2020
# description: Shakes and Fidget Damage Calculator


def main():
    # User inputs
    def inputs():
        class_check = input("If your class is Berserker or Battle Mage type here 1 other wise 0:")
        weapon_average_dmg = input("Enter your weapon's average damage:")
        base_strength = input("Base of your damage attribute:")
        strength_from_weapon = input("Enter your weapon damage attribute:")
        pet_bonus = input("Enter your pet bonus like 25% = 1.25:")
        potion = input("Enter the percentage of your potion like 25% = 1.25:")
        head_bonus = input("Head damage attribute bonus:")
        chest_bonus = input("Chest damage attribute bonus:")
        arm_bonus = input("Arm damage attribute bonus:")
        shoe_bonus = input("Shoe damage attribute bonus:")
        necklace_bonus = input("Necklace damage attribute bonus:")
        belt_bonus = input("Belt damage attribute bonus:")
        ring_bonus = input("Ring damage attribute bonus:")
        shamrock_bonus = input("Shamrock damage attribute bonus:")
        try:
            return int(weapon_average_dmg), int(base_strength), int(strength_from_weapon), float(pet_bonus), \
                   float(potion), int(head_bonus), int(chest_bonus), int(arm_bonus), int(shoe_bonus), \
                   int(necklace_bonus), int(belt_bonus), int(ring_bonus), int(shamrock_bonus), int(class_check)
        except:
            print("\nValue Error. Please Check your entered Values.\n")
            input("\nPress ENTER to exit\n")
            exit(-1)
    # Strength calculation
    def strength(basis, potion, pet, strength_weapon, head, chest, arm, shoe, necklace, belt, ring, shamrock, clas):
        armor = strength_weapon + head + chest + arm + shoe + necklace + belt + ring + shamrock
        strength = basis

        if clas == 1:
            bonus = armor * 0.11
            bonus = round(bonus)
            strength += bonus

        strength += armor

        if potion == 1.25 or potion == 1.15 or potion == 1.1:
            strength *= potion
            strength = round(strength)

        if pet != 0:
            strength *= pet
            strength = round(strength)

        return strength

    # damage calculation
    def calc(weapon, strength):
        dmg = weapon * (1 + strength / 10)
        dmg = round(dmg)
        return dmg

    # starting functions
    weapon, basis, strength_weapon, pet_bonus, potion, head, chest, arm, shoe, necklace, belt, ring, shamrock, \
    clas = inputs()

    strength = strength(basis, potion, pet_bonus, strength_weapon, head, chest, arm, shoe, necklace, belt, ring,
                        shamrock, clas)

    dmg = calc(weapon, strength)

    # out puts end result

    print("\n"+"Your Damage Value is: "+str(dmg)+"\n")


if __name__ == "__main__":
    main()
    input("\nPress ENTER to exit\n")