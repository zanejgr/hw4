import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
import numpy as np
import os
import pandas as pd
import sys

cores = 1
csv_file = "./experiment2018111916.csv"

title = "Semaphore addition time for multiple loops and threads on ${CORES}"
title += "\n ${SSH_CLIENT} --- ${USER}"

# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.read_csv.html
data = pd.read_csv(csv_file,
		   names=["cores",
			  "loops",
			  "threads",
			  "real_time",
			  "user_time",
			  "kernel_time"])

# Compute avg and std of runs
df = data.groupby(['cores', 'loops', 'threads']).agg({'real_time': [np.mean, np.std]})

# split by threads
df2 = df.reset_index()
df4 = df.reset_index()
df8 = df.reset_index()
df16 = df.reset_index()

# https://pandas.pydata.org/pandas-docs/stable/generated/pandas.DataFrame.plot.html
df2 = df2[df2.threads == 2]
df2.columns =  ['cores', 'loops', 'threads', 'mean', 'std']
df2.plot(x='loops', y='mean', yerr='std', title=title, color='red' )

df4 = df4[df4.threads == 4]
df4.columns =  ['cores', 'loops', 'threads', 'mean', 'std']
df4.plot(x='loops', y='mean', yerr='std', title=title, color='red' )

df8 = df8[df8.threads == 8]
df8.columns =  ['cores', 'loops', 'threads', 'mean', 'std']
df8.plot(x='loops', y='mean', yerr='std', title=title, color='red' )

df16 = df16[df16.threads == 16]
df16.columns =  ['cores', 'loops', 'threads', 'mean', 'std']
df16.plot(x='loops', y='mean', yerr='std', title=title, color='red' )

# https://matplotlib.org/api/_as_gen/matplotlib.pyplot.fill_between.html
plt.fill_between(df2['loops'], 
		 df2['mean'] + df2['std'],
		 df2['mean'] - df2['std'],
		 interpolate=False,
		 color='red',
		 alpha=0.2)
plt.fill_between(df4['loops'], 
		 df4['mean'] + df4['std'],
		 df4['mean'] - df4['std'],
		 interpolate=False,
		 color='green',
		 alpha=0.2)
plt.fill_between(df8['loops'], 
		 df8['mean'] + df8['std'],
		 df8['mean'] - df8['std'],
		 interpolate=False,
		 color='blue',
		 alpha=0.2)
plt.fill_between(df16['loops'], 
		 df16['mean'] + df16['std'],
		 df16['mean'] - df16['std'],
		 interpolate=False,
		 color='yellow',
		 alpha=0.2)                 

plt.ylabel('Time (s)')
plt.xlabel('Loops')

plt.legend(['Threads 2', 'Threads 4', 'Threads 8', 'Threads 16'],
	   loc='upper left')

# Save the two figures
plt.savefig("{}.png".format(csv_file), bbox_inches='tight')
plt.savefig("{}.pdf".format(csv_file), bbox_inches='tight')

