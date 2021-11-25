#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
import matplotlib.ticker as mticker

trends_csv = pd.read_csv('trends_cmake_makefile_gnumake_autoconf_scons.csv')
trends_csv = trends_csv.replace('<1', '1')
for c in trends_csv:
    if c == 'month':
        pass
    else:
        trends_csv[c] = trends_csv[c].astype('int64')
month_ticks=[i for i in range(0,len(trends_csv['month'].values),12)]
ax = trends_csv.plot(x='month', 
                     rot=30, 
                     figsize=(9,7), 
                     title='Google Trends over time',
                     legend=True,
                     xticks=month_ticks)
plt.show()

