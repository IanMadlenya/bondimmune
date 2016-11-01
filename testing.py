import numpy as np
import datetime
from datetime import date
import portfoliofuns
from dateutil.relativedelta import relativedelta



if __name__ == '__main__':


	# basic long position for a 1-month bond	
	position = { "weight": 1,
				 "positiontype": "long",
				 "bondtype" : "3-month",
				 "interestrate" : .05,
				 "createdate" : np.datetime64(date.today()),
				 "maturitydate" : np.datetime64(date.today() + relativedelta(months=3)),
				 "coupondates" : np.array(np.datetime64(date.today() + relativedelta(months=3))),
				 "couponpayments" : np.array(1.05) }

	

	# testing effective_rate
	effrate = portfoliofuns.effective_rate(position)

	print "effective rate"
	print effrate

	P = portfoliofuns.Pnull(position = position, n = 1)

	print "Pnull value"
	print P

	Positionvalue = portfoliofuns.position_value(position = position, currenttime = 1./12)

	print "position value at 1 month bond after."
	print Positionvalue


	# testing out mc_duration calculation.
	mcdur = portfoliofuns.mc_duration(position = position, currenttime = np.datetime64(date.today()))

	print "maculay duration."
	print mcdur

	moddur = portfoliofuns.mod_duration(position = position, currenttime = np.datetime64(date.today()))

	print "modified duration"
	print moddur


