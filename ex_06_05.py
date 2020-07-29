str = 'X-DSPAM-Confidence:0.8475'
colpos = str.find(':')
print(colpos)
data = str[colpos+1:]
print(data, type(data))
Data = float(data)
print(Data, type(Data))
