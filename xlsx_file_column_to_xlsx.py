import pandas as pd

df = pd.read_excel("shares_13092023.xlsx")

column_with_companies = df.iloc[:,2]

new_df = pd.DataFrame({"quoted companies": column_with_companies })

new_df.to_excel("new_file.xlsx", index = False)


