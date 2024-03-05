import pyupbit
from config import get_secret

ACCESS_KEY = get_secret("ACCESS_KEY")
SECRET_KEY = get_secret("SECRET_KEY")

coin = "ETH"

upbit = pyupbit.Upbit(ACCESS_KEY, SECRET_KEY)

# 전략을 어떻게 짤 것인가?

# 어떤 구조를 가진 거래?

# 외부의 데이터를 가져와서 다뤄?

print(upbit.get_balance("ETH"))