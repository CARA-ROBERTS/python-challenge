import pandas as pd
# Reference the file where the CSV is located
budget_path_csv = "budget_data.csv"

# Import the data into a Pandas DataFrame
budget_df = pd.read_csv(budget_path_csv)
budget_df.head()
Date	Profit/Losses
0	Jan-2010	867884
1	Feb-2010	984655
2	Mar-2010	322013
3	Apr-2010	-69417
4	May-2010	310503
budget_df.count()
Date             86
Profit/Losses    86
dtype: int64
budget_df.columns
Index(['Date', 'Profit/Losses'], dtype='object')
budget_df.rename(columns= {'Date':'Month-Year'})
Month-Year	Profit/Losses
0	Jan-2010	867884
1	Feb-2010	984655
2	Mar-2010	322013
3	Apr-2010	-69417
4	May-2010	310503
...	...	...
81	Oct-2016	102685
82	Nov-2016	795914
83	Dec-2016	60988
84	Jan-2017	138230
85	Feb-2017	671099
86 rows × 2 columns

budget_df["Date"].count()
86
Total_Months_count == budget_df["Date"].count()
True
budget_df.describe()
Date	Profit/Losses
count	86.0	8.600000e+01
mean	0.0	4.463090e+05
std	0.0	5.363579e+05
min	0.0	-1.196225e+06
25%	0.0	1.821620e+05
50%	0.0	5.703280e+05
75%	0.0	7.952262e+05
max	0.0	1.170593e+06
Total = budget_df["Profit/Losses"].sum()
Greatest_Increase = budget_df["Profit/Losses"].max()
Greatest_Decrease= budget_df["Profit/Losses"].min()
Average_Change = budget_df["Profit/Losses"].mean()
Financial_Analysis = pd.DataFrame({"Total Months":[Total_Month_count],
                                    "Total":[Total],
                                    "Average Change": [Average_Change],
                                    "Greastest Increase In Profits": [Greatest_Increase],
                                    "Greastest Decrease In Profits" :[Greatest_Decrease]})

Financial_Analysis
Total Months	Total	Average Change	Greastest Increase In Profits	Greastest Decrease In Profits
0	1	38382578	446309.046512	1170593	-1196225