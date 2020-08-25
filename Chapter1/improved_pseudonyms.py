"""2つのタプルからランダムに名前を選んで表示する
※※※ 挑戦プロジェクト ※※※
コードを書き直して、ミドルネームをいれる。
ミドルネームは2,3回に1回だけ選ばれるようにする。
"""
import sys
import random

def main():
    """2つのタプルからランダムに名前を選んで表示する"""
    print("Welcome to the Psych 'Sidekick Name Picker.'\n")
    print("A name just like Sean would pick for Gus:\n\n")

    first = ('Baby Oil', 'Bad News', 'Big Burps', "Bill",
             "Bob", 'Bowel Noises', 'Boxelder', "Bud 'Lite' ",
             'Butterbean', 'Buttermilk', 'Buttocks', 'Chad', 'Chesterfield',
             'Chewy', 'Chigger', 'Cinnabuns', 'Cleet', 'Cornbread',
             'Crab Meat', 'Crapps', 'Dark Skies', 'Dennis Clawhammer',
             'Dicman', 'Elphonso', 'Fancypants', 'Figgs', 'Foncy', 'Gootsy',
             'Greasy Jim', 'Huckleberry', 'Huggy', 'Ignatious', 'Jimbo',
             "Joe", 'Johnny', 'Lemongrass', 'Lil Debil',
             'Longbranch', '"Lunch Money"', 'Mergatroid', '"Mr Peabody"',
             'Oil-Can', 'Oinks', 'Old Scratch', 'Ovaltine', 'Pennywhistle',
             'Pitchfork Ben', 'Potato Bug', 'Pushmeet', 'Rock Candy',
             'Schlomo', 'Scratchensniff', 'Scut', "Sid",
             'Skidmark', 'Slaps', 'Snakes', 'Snoobs', 'Snorki', 'Soupcan Sam',
             'Spitzitout', 'Squids', 'Stinky', 'Storyboard', 'Sweet Tea',
             'TeeTee', 'Wheezy Joe', "Winston", 'Worms')

    middle = ('Beenie-Weenie', 'Grunts', 'Jazz Hands', 'Pottin Soil',
              'Stinkbug', 'The Big News', 'The Squirts', 'Tinkle Winkle')

    last = ('Appleyard', 'Bigmeat', 'Bloominshine', 'Boogerbottom',
            'Breedslovetrout', 'Butterbaugh', 'Clovenhoof', 'Clutterbuck',
            'Cocktoasten', 'Endicott', 'Fewhairs', 'Gooberdapple',
            'Goodensmith', 'Goodpasture', 'Guster', 'Henderson', 'Hooperbag',
            'Hoosenater', 'Hootkins', 'Jefferson', 'Jenkins',
            'Jingley-Schmidt', 'Johnson', 'Kingfish', 'Listenbee', "M'Bembo",
            'McFadden', 'Moonshine', 'Nettles', 'Noseworthy', 'Olivetti',
            'Outerbridge', 'Overpeck', 'Overturf', 'Oxhandler', 'Pealike',
            'Pennywhistle', 'Peterson', 'Pieplow', 'Pinkerton', 'Porkins',
            'Putney', 'Quakenbush', 'Rainwater', 'Rosenthal', 'Rubbins',
            'Sackrider', 'Snuggleshine', 'Splern', 'Stevens', 'Stroganoff',
            'Sugar-Gold', 'Swackhamer', 'Tippins', 'Turnipseed',
            'Vinaigrette', 'Walkingstick', 'Wallbanger', 'Weewax', 'Weiners',
            'Whipkey', 'Wigglesworth', 'Wimplesnatch', 'Winterkorn',
            'Woolysocks')

    while True:

        first_name = random.choice(first)

        # ミドルネームが50%の確率で選ばれるようにする
        if random.random() < 0.5:
            middle_name = ' ' + random.choice(middle) + ' '
        else:
            middle_name = ' '

        last_name = random.choice(last)

        print("\n\n")
        # 「致命的なエラー」 の設定を使い、IDEL を誤魔化して名前を赤く表示する
        print("{}{}{}".format(first_name, middle_name, last_name), file=sys.stderr)
        print("\n\n")

        try_again = input("\n\nTry again? (Press Enter else n to quit)\n ")
        if try_again.lower() == "n":
            break

    input("\nPress Enter to exit.")

if __name__ == "__main__":
    main()

"""
出力結果
------------------------------------
$ python improved_pseudonyms.py
Welcome to the Psych 'Sidekick Name Picker.'

A name just like Sean would pick for Gus:





Gootsy Beenie-Weenie Fewhairs





Try again? (Press Enter else n to quit)




Boxelder Wigglesworth





Try again? (Press Enter else n to quit)




Mergatroid Clovenhoof





Try again? (Press Enter else n to quit)




Lemongrass The Big News Hootkins





Try again? (Press Enter else n to quit)
 n

Press Enter to exit.

"""
