from TwitterFollowBot import TwitterBot

my_bot = TwitterBot()
print "...starting executing the TwitterBot script..."

my_bot.sync_follows()

# my_bot.auto_follow("#startup")
# my_bot.auto_follow("#enterpreneur")
# my_bot.auto_follow("ionic 2")
# my_bot.auto_follow("#ionic")
# my_bot.auto_follow("#ionic2")
my_bot.auto_follow("Ionic Creator")

my_bot.auto_follow_followers()

# my_bot.auto_fav("Elon Musk", count=10)
# my_bot.auto_fav("SpaceX", count=10)
# my_bot.auto_fav("Tesla", count=10)
# my_bot.auto_fav("#startup", count=10)
# my_bot.auto_fav("#enterpreneur", count=10)
# my_bot.auto_fav("#ionic 2", count=10)
# my_bot.auto_fav("#ionic", count=10)
my_bot.auto_fav("Ionic Creator", count=1)

my_bot.auto_rt("Ionic Framework", count=1)
my_bot.auto_rt("Ionic Creator", count=1)
my_bot.auto_rt("Elon Musk", count=1)
my_bot.auto_rt("Tesla", count=1)
my_bot.auto_rt("SpaceX", count=1)
my_bot.auto_rt("startup battlefield", count=1)

