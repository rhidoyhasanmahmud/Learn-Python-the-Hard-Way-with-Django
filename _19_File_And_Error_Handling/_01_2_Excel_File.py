# pandas, openpyxl  
import pandas as pd

data = pd.read_excel('Telco_site_sorting.xlsx')
df = pd.DataFrame(data)
operator = list()

for ind in df.index:
    # df['Name'] -> Excel Column Name
    print(df['Name'][ind])
    if "CGNSB9" in df['Name'][ind] or "CGSJD2" in df['Name'][ind]:
        operator.append("GP")
    elif "DHK_X0829" in df['Name'][ind] or "CTG_X0351" in df['Name'][ind] or "CTG_X9025" in df['Name'][
        ind] or "DHK_S8226" in df['Name'][ind]:
        operator.append("BANGLALINK")
    elif "JHSDR06" in df['Name'][ind] or "CXSDR08" in df['Name'][ind] or "CMCDG29" in df['Name'][
        ind] or "DHPTN14" in df['Name'][ind]:
        operator.append("ROBI")
    elif "DHK4166" in df['Name'][ind] or "BBA0002" in df['Name'][ind]:
        operator.append("TELETALK")
    else:
        operator.append("UNKNOWN")

df.insert(1, "Operator", operator)
df.to_excel('Book2.xlsx', sheet_name='new_sheet_name')
print("Completed.")