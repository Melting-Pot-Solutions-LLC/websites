from TwitterFollowBot import TwitterBot
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText


from cStringIO import StringIO
import sys

old_stdout = sys.stdout
sys.stdout = mystdout = StringIO()


my_bot = TwitterBot()
print "...starting executing the TwitterBot script..."

my_bot.sync_follows()
my_bot.auto_follow_followers()


my_bot.auto_follow("@Ionicframework", count = 1)
my_bot.auto_follow("@MikeMeyers", count = 1)
my_bot.auto_follow("@IonicCreator", count = 1)
my_bot.auto_follow("@itsnirnayr", count = 1)
my_bot.auto_fav("@evankimbrell", count=1)


my_bot.auto_fav("Elon Musk", count=1)
my_bot.auto_fav("SpaceX", count=1)
my_bot.auto_fav("Tesla", count=1)
my_bot.auto_fav("#startup", count=1)
my_bot.auto_fav("#enterpreneur", count=1)
my_bot.auto_fav("#ionic 2", count=1)
my_bot.auto_fav("#ionic", count=1)



my_bot.auto_fav("Columbia SC", count=1)
my_bot.auto_fav("Columbia, SC", count=1)



# retweet everything the user tweets
my_bot.auto_rt("from:@ChangeAgentLisa", count=1)
my_bot.auto_rt("from:elonmusk", count=1)
my_bot.auto_rt("from:itsnirnay", count=1)
my_bot.auto_rt("from:MikeMeyers", count=1)
my_bot.auto_rt("from:SteveBenjaminSC", count=1)
my_bot.auto_rt("from:techCrunch", count=1)
my_bot.auto_rt("from:amazon", count=1)
my_bot.auto_rt("from:joshuamorony", count=1)
my_bot.auto_rt("from:DrAmandaR", count=1)
my_bot.auto_rt("from:HarrisPastides", count=1)
my_bot.auto_rt("from:TonyKlor", count=1)
my_bot.auto_rt("from:evankimbrell", count=1)
my_bot.auto_rt("from:@jasondorsey", count=1)
my_bot.auto_rt("from:@PeterSchiff", count=1)
my_bot.auto_rt("from:@mcuban", count=1)
my_bot.auto_rt("from:@TheSharkDaymond", count=1)
my_bot.auto_rt("from:@BarbaraCorcoran", count=1)
my_bot.auto_rt("from:@Tom_Wheelwright", count=1)
my_bot.auto_rt("from:@richardbranson", count=1)
my_bot.auto_rt("from:@kimkiyosaki", count=1)
my_bot.auto_rt("from:@robertherjavec", count=1)
my_bot.auto_rt("from:@kevinolearytv", count=1)
my_bot.auto_rt("from:@PJCrowley", count=1)
my_bot.auto_rt("from:@LoriGreiner", count=1)


my_bot.auto_fav("from:@ChangeAgentLisa", count=1)
my_bot.auto_fav("from:elonmusk", count=1)
my_bot.auto_fav("from:itsnirnay", count=1)
my_bot.auto_fav("from:MikeMeyers", count=1)
my_bot.auto_fav("from:SteveBenjaminSC", count=1)
my_bot.auto_fav("from:techCrunch", count=1)
my_bot.auto_fav("from:joshuamorony", count=1)
my_bot.auto_fav("from:DrAmandaR", count=1)
my_bot.auto_fav("from:amazon", count=1)
my_bot.auto_fav("from:HarrisPastides", count=1)
my_bot.auto_fav("from:TonyKlor", count=1)
my_bot.auto_fav("from:evankimbrell", count=1)
my_bot.auto_fav("from:@jasondorsey", count=1)
my_bot.auto_fav("from:@PeterSchiff", count=1)
my_bot.auto_fav("from:@mcuban", count=1)
my_bot.auto_fav("from:@TheSharkDaymond", count=1)
my_bot.auto_fav("from:@BarbaraCorcoran", count=1)
my_bot.auto_fav("from:@Tom_Wheelwright", count=1)
my_bot.auto_fav("from:@richardbranson", count=1)
my_bot.auto_fav("from:@kimkiyosaki", count=1)
my_bot.auto_fav("from:@robertherjavec", count=1)
my_bot.auto_fav("from:@kevinolearytv", count=1)
my_bot.auto_fav("from:@PJCrowley", count=1)
my_bot.auto_fav("from:@LoriGreiner", count=1)


#change stdout back to original stdout
sys.stdout = old_stdout

#send an email
fromaddr = "dml1002313@gmail.com"
toaddr = "konstantinrubin@engineer.com"
msg = MIMEMultipart()
msg['From'] = fromaddr
msg['To'] = toaddr
msg['Subject'] = "TwitterBot executed"
body = mystdout.getvalue()
msg.attach(MIMEText(body, 'plain'))
server = smtplib.SMTP('smtp.gmail.com', 587)
server.starttls()
server.login(fromaddr, "SteveNash701")
text = msg.as_string()
server.sendmail(fromaddr, toaddr, text)
server.quit()
