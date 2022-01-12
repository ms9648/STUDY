import pandas as pd
import numpy as np

mydict = [{'a': np.nan, 'b': 3, 'c': 6, 'd': 9},
          {'a': 1, 'b': 4, 'c': 7, 'd': 10},
          {'a': 2, 'b': 5, 'c': 8, 'd': 11}]
my_df = pd.DataFrame(mydict)
my_df_count = my_df.groupby('a')['b'].agg(['count'])
print(my_df_count)

my_df_count.index = my_df_count.index.map(int)
print(my_df_count.index)

# round(값, a) = 소수점 a+1번째 자리에서 반올림
# quantile(a) = a*100%에 해당하는 백분위 수
~my_df.isin
my_df_count_benchmark = round(my_df_count['count'].quantile(0.9), 0)
print(my_df_count_benchmark)