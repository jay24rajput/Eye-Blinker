import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
import datetime

class Report:
    
    def gen_log_name(self):
        date = str(datetime.datetime.now().date())
        time = str(datetime.datetime.now().time())
        reportName = 'log-' + date + '-' + time + '.csv'
        return reportName

    def display_report(self, df, isPastReport = False, filename = None):
        #read in a previous report
        if isPastReport == True:
            df = pd.read_csv(filename)
        plt.xlabel('Time')
        plt.ylabel('Blinks') 
        plt.plot(df['Time'], df['Blinks'])
        plt.show()

    def save_report_data(self, y, isPastReport = False):    
        X = [x for x in range(0, 15 * len(y), 15)]
        df = pd.DataFrame()
        df['Time'] = np.array(X).T
        df['Blinks'] = np.array(y).T
        logname = self.gen_log_name()
        df.to_csv(logname)
        self.display_report(df, isPastReport)