"""This is a simple tool for calculating current commision tier and projecting how much one would need to sell to raise their tier. The commision rates are based on the RSR commision rate at Schwan's Home Service"""


week_length = 5 #adjust if needed for shorter route weeks

day_x = input("How many days have you run this week? ")
day_x = int(day_x)
x = 0
day_n = week_length - day_x

basepay = 180 * week_length #may change depending on depot
spd1 = [0, 0 ,0, 0, 0]
spd2 = []
q = 0
print("\n")

for days in spd1:
	if x >= day_x:
		q = sum(spd2)
		break
	print("for day ",x + 1, end = " ")
	days = input("how much was your commisionable sales: ")
	days = int(days)
	#print(days)
	spd2.append(days)
	x = x + 1
spd_goal2 = (7000 - q)/day_n
spd_goal3 = (8000 - q)/day_n
spd_goal4 = (9000 - q)/day_n
spd_avg = q / len(spd2)
if spd_avg < 1400:
		payout = (spd_avg * week_length) * 0.03
		print("first teir")
		#print(basepay)
		print(payout)
elif 1600 > spd_avg >= 1400:
		payout = (spd_avg * week_length) * .05
		print("second teir")
		#print(payout)
elif 1800 > spd_avg >= 1600:
		 payout = (spd_avg * week_length) * .07
		 print("third teir, Woot!")
		 #print(payout)
elif spd_avg >= 1800:
		payout = (spd_avg * week_length) * .09
		#print(payout)
		print("forth teir! you are the batman of food sales!!!")
else:
		print("an error has occured")


total_pay = payout + basepay
print("\n your average sales per day is ", spd_avg, "at your current rate your income for the week would be ", total_pay, "\n\n")

if spd_avg < 1400:
	print("To hit a 5% week you need to sell an avarege of ", spd_goal2, " over the next ", day_n, " day/s")

elif 1600 > spd_avg >=1400:
	print("To hit a 7% week you need to sell an avarege of ", spd_goal3, " over the next ", day_n, " day/s")
elif 1800 > spd_avg >= 1600:
	print("To hit a 9% week you need to sell an avarege of ", spd_goal4, " over the next ", day_n, " day/s")
else:
	print("great job")


#print("testing")
#print(spd1)
#print("spd =", spd2)
#print("sum =", q)
#print("payout = ", payout)
#print("sales average = ", spd_avg)
