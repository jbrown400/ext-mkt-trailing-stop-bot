
from pyrobot.robot import Trade
from pyrobot.robot import PyRobot
from pyrobot.indicators import Indicators
from configs.config import *

if __name__ == '__main__':

	# Sign in
	trading_robot = PyRobot(
		client_id=CLIENT_ID,
		redirect_uri=REDIRECT_URI,
		credentials_path=JSON_PATH,
		trading_account=ACCOUNT_NUMBER,
		paper_trading=True
	)

	bot_account = trading_robot.get_accounts(account_number=ACCOUNT_NUMBER)
	# Get current account info

	# Check for current stop losses

	# Determine current trailing stop loss difference

	# Wait for ext mkt hours

	# While ext mkt
		# Get current minute price data for all tickers with trailing stop losses

		# Check if stop loss has been met

		# Update stop loss values