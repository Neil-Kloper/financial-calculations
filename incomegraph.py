"""This tool is for calculating annual income based off of how much one makes per hour. Output is a graph for comparison of how much more one could make by adjusting their hours per week. Calculations assume california rules for overtime and may not be 100% correct in other states."""

import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

def hourly_to_annual(pph, hpw=40):
	"""calculation for ammount earned, pph is 'pay per hour', and hpw is 'hours per week'"""
	if hpw > 40:
		othpw = hpw - 40
		hpw = hpw - othpw
		payout = (hpw * pph) + (othpw * pph * 1.5)
	
	elif hpw <= 40:
		payout = hpw * pph
	
	annual = payout * 52
	return annual 
	
def income_range(pph):
	income = {'hours': [],'income':[]}
	for val in range(15, 75, 5):
		income['income'] = income['income'] + [hourly_to_annual(pph, val)]
		income['hours'] = income['hours'] + [val]
	#print(income)
	inc = income['income']
	hrs = income['hours']
	#print(inc, hrs)
	#plt.subplot(1,1,1)
	plt.plot(hrs, inc)
	plt.xlabel('hours per week')
	plt.ylabel('anual income')
	plt.show()
	x = 0
	print('Hours\tIncome')
	while x != len(inc):
		print(hrs[x], '\t\t', inc[x])
		x = x + 1
