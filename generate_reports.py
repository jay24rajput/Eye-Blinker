import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

def main():
	df=pd.read_csv('temp_data.csv')
	plt.plot(df['time'],df['blinks'])
	plt.xlabel('Time')
	plt.ylabel('Blinks')
	plt.show()


if __name__ == '__main__':
	main()

# y=np.random.randint(low=3,high =20, size=100)
# X= [x for x in range(0,1500,15)]
# def generateReports(X,y)
# 	df= pd.DataFrame()
# 	df['time']=X.T
# 	df['blinks']=y.T

# 	df.to_csv('temp_data.csv') 

# 	plt.plot(X,y)
# 	plt.show()