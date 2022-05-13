import pandas as pd

def read_log(file):

    log = pd.read_csv(file)

    log['timeStamp'] = pd.to_datetime(log['timeStamp'])
    log['timeStamp'] = log['timeStamp'].astype('datetime64[s]')

    log = log[~log['responseCode'].astype(str).str.contains('200')]
    final_log = log[['label','responseCode','responseMessage','failureMessage','timeStamp']]
    print(final_log)
    input("Press enter to exit ;)")


if __name__ == '__main__':

    val = input("enter the file name that you want to test for jmeter log example(Jmeter_log1.jtl or Jmeter_log2.jtl):")
    read_log(val)
        
