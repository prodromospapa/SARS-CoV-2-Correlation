import pandas as pd
table = pd.read_csv("filtered_r_annotation.csv",index_col=0)

def HIGHLIGHT(x):
    red = 'background-color: red;'
    orange = 'background-color: orange;'
    green = 'background-color: green;'
    yellow = 'background-color: yellow;'
    
    if abs(x)<=1 and abs(x)>0.9:
      return green
    elif abs(x)<=0.9 and abs(x)>0.7:
      return yellow
    elif abs(x)<=0.7 and abs(x)>0.5:
      return orange
    elif abs(x)<=0.5 and abs(x)>0.3:
      return red
      
    return ''  
table = table.style.applymap(HIGHLIGHT)
table.to_excel("colored_table.xlsx")