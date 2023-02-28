import pandas as pd

import logging
import time

logging.basicConfig(filename='attendance.log',level = logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')
def attendance():
    try:
        attendname=[]
        attendtime=[]
        prob = []
        with open("recognize.log", "r") as f:
            for line in f:
                details = line.split(":INFO:")
                #err = ['No face detected','NumExpr defaulting to 8 threads.']
                if len(details[1])==1:# and details[1][:-1] not in attendname:
                    if type(details[1])==str:
                        attendtime.append(details[0])
                        attendname.append(details[1][:-1])
                    elif type(details[1])==float:
                        prob.append(details[1])
                    else:
                        pass
        df=pd.DataFrame(list(zip(attendtime,attendname,prob)),columns=["Timestamp", "Name","Probability"])
        print(df)
       # df.to_excel('Attendance2.xlsx')
    except Exception as e:
        logging.debug(e)
timestamp = []
names = []
prob = []
file = time.asctime()
day = file[:4]
date = file[4:10]
year = file[20:24]
type(file)
filename = f'Attendance on {day}{date}{year}.xlsx'
import pandas as pd
df = pd.DataFrame({'Timestamp': [], 'Name': [], 'Probability': []})
df.to_excel(f'Attendance on {day}{date}{year}.xlsx')
def to_pandas(a,b,c,df):
    new_row = {'Timestamp': a, 'Name': b,'Probability': c}
    df = df.append(new_row, ignore_index=True)
    values = df.tail(1).to_string(index = False, header=False)
    print(values)
    with open(filename, "a") as f:
        f.write(f"{values}\n")

    # print(df.tail(1).to_string(header=df.columns.tolist(), index_names=False),sep='\n')
    # print(df.tail(1))

def three(a,b,c):
    timestamp.append(a)  
    names.append(b)  
    prob.append(c)
    # df=pd.DataFrame(list(zip(timestamp,names,prob)),columns=["Timestamp", "Name","Probability"])
    # print(a,b,c)
    # to_pandas(a,b,c,df)
# attendance()


#df.to_excel()
# print('DataFrame is written to Excel File successfully.')
# print()

