from TwitterFollowBot import TwitterBot


# what the bot should do
# 
my_bot = TwitterBot()
print "...starting executing the TwitterBot script..."

my_bot.sync_follows()
my_bot.auto_follow_followers()


my_bot.auto_follow("@Ionicframework", count = 1)
my_bot.auto_follow("@MikeMeyers", count = 1)
my_bot.auto_follow("@IonicCreator", count = 1)
my_bot.auto_follow("@itsnirnayr", count = 1)

my_bot.auto_fav("Elon Musk", count=1)
my_bot.auto_fav("SpaceX", count=1)
my_bot.auto_fav("Tesla", count=1)
my_bot.auto_fav("#startup", count=1)
my_bot.auto_fav("#enterpreneur", count=1)
my_bot.auto_fav("#ionic 2", count=1)
my_bot.auto_fav("#ionic", count=1)


my_bot.auto_fav("Columbia SC", count=1)
my_bot.auto_fav("Columbia, SC", count=1)

# # my_bot.auto_rt("Ionic Framework", count=1)
# my_bot.auto_rt("Ionic Creator", count=1)
# my_bot.auto_rt("Elon Musk", count=1)
# my_bot.auto_rt("Tesla", count=1)
# my_bot.auto_rt("SpaceX", count=1)
# my_bot.auto_rt("startup battlefield", count=1)

# retweet everything the user tweets


my_bot.auto_rt("from:elonmusk", count=1)
my_bot.auto_rt("from:itsnirnay", count=1)
my_bot.auto_rt("from:MikeMeyers", count=1)
my_bot.auto_rt("from:SteveBenjaminSC", count=1)
my_bot.auto_rt("from:techCrunch", count=1)
my_bot.auto_rt("from:amazon", count=1)
my_bot.auto_rt("from:joshuamorony", count=1)
my_bot.auto_rt("from:DrAmandaR", count=1)
my_bot.auto_rt("from:ElonMuskNewsOrg", count=1)
my_bot.auto_rt("from:HarrisPastides", count=1)
my_bot.auto_rt("from:TonyKlor", count=2)

my_bot.auto_fav("from:elonmusk", count=1)
my_bot.auto_fav("from:itsnirnay", count=1)
my_bot.auto_fav("from:MikeMeyers", count=1)
my_bot.auto_fav("from:SteveBenjaminSC", count=1)
my_bot.auto_fav("from:techCrunch", count=1)
#my_bot.auto_fav("from:GMA", count=1)
my_bot.auto_fav("from:joshuamorony", count=1)
my_bot.auto_fav("from:DrAmandaR", count=1)
my_bot.auto_fav("from:amazon", count=1)
my_bot.auto_fav("from:ElonMuskNewsOrg", count=1)
my_bot.auto_fav("from:HarrisPastides", count=1)
my_bot.auto_fav("from:TonyKlor", count=2)
