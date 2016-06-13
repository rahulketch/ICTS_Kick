from StringIO import StringIO
import pandas as pd
import matplotlib.pyplot as plt
from mpldatacursor import datacursor

f = StringIO(
"""931,Oxfordshire,9314125,123255,Larkmead School,Abingdon,125,124,20,SUPP,8
931,Oxfordshire,9314126,123256,John Mason School,Abingdon,164,164,25,6,16
931,Oxfordshire,9314127,123257,Fitzharrys School,Abingdon,150,149,9,0,11
931,Oxfordshire,9316076,123298,Our Lady's Abingdon,Abingdon,57,57,SUPP,SUPP,16
""")
df = pd.read_csv(f, names=['A','B','C','D','E','F','G', 'H','I','J', 'K'],
                 header=None)
df.replace('SUPP', 3.0, inplace=True)
df = df.convert_objects(convert_numeric=True)
df['KG'] = df['K']*1.0/df['G']
plt.plot(df['KG'], marker='o')

datacursor(hover=True, point_labels=df['E'])

plt.show()