# open file "my_deaths_by_state_sex.csv"
# read the file and get aggregate sum of deaths by state
# write the output to a new file "my_deaths_by_state.csv"

import pandas as pd

# read the file
deaths_by_state_sex_data = pd.read_csv("my_deaths_by_state_sex.csv")
# print(deaths_by_state_sex_data)

# get aggregate sum of deaths by state
agg_deaths_by_state_year = deaths_by_state_sex_data.groupby(['State','Year'])['Number of death'].sum().reset_index()

# change any instance of WP Kuala Lumpur to Kuala Lumpur
agg_deaths_by_state_year['State'] = agg_deaths_by_state_year['State'].replace('WP Kuala Lumpur', 'Kuala Lumpur')
# change any instance of WP Labuan to Labuan
agg_deaths_by_state_year['State'] = agg_deaths_by_state_year['State'].replace('WP Labuan', 'Labuan')
# change any instance of WP Putrajaya to Putrajaya
agg_deaths_by_state_year['State'] = agg_deaths_by_state_year['State'].replace('WP Putrajaya', 'Putrajaya')

# filter for year == 2018
df_2018 = agg_deaths_by_state_year[agg_deaths_by_state_year['Year'] == 2018]
# print(df_2018)

# write the output to a new file
df_2018.to_csv("my_deaths_by_state_2018.csv", index=False)

# repeat for 2019 and 2020 
df_2019 = agg_deaths_by_state_year[agg_deaths_by_state_year['Year'] == 2019]
df_2019.to_csv("my_deaths_by_state_2019.csv", index=False)

df_2020 = agg_deaths_by_state_year[agg_deaths_by_state_year['Year'] == 2020]
df_2020.to_csv("my_deaths_by_state_2020.csv", index=False)

# # do the same for file "my_population-by-state-administrative-district-and-sex-2016-2020_d.csv"
# state_population = pd.read_csv("my_population-by-state-administrative-district-and-sex-2016-2020_d.csv")

# # change any instance of WP Kuala Lumpur to Kuala Lumpur
# state_population['Country/State'] = state_population['Country/State'].replace('W.P. Kuala Lumpur', 'Kuala Lumpur')
# # change any instance of WP Labuan to Labuan
# state_population['Country/State'] = state_population['Country/State'].replace('W.P. Labuan', 'Labuan')
# # change any instance of WP Putrajaya to Putrajaya
# state_population['Country/State'] = state_population['Country/State'].replace('W.P. Putrajaya', 'Putrajaya')
# state_population.to_csv("my_population_by_state_cleaned.csv", index=False)

# create another file using agg deaths by year and state
agg_deaths_by_state_year.to_csv("my_deaths_by_state_year.csv", index=False)

# sum all population drouped by sex and state, and change date header to year and format from YYYY-MM-DD to YYYY
state_population = pd.read_csv("population_state.csv")

# change any instance of W.P. Kuala Lumpur to Kuala Lumpur
state_population['state'] = state_population['state'].replace('W.P. Kuala Lumpur', 'Kuala Lumpur')
# change any instance of W.P. Labuan to Labuan
state_population['state'] = state_population['state'].replace('W.P. Labuan', 'Labuan')
# change any instance of W.P. Putrajaya to Putrajaya
state_population['state'] = state_population['state'].replace('W.P. Putrajaya', 'Putrajaya')

# change date header to year and format from YYYY-MM-DD to YYYY
state_population['Year'] = state_population['date'].str[:4]

# group population by state and year, and merge them in the form state_year
agg_population_by_state_year = state_population.groupby(['state','Year'])['population'].sum().reset_index()
agg_population_by_state_year['state_year'] = agg_population_by_state_year['state'] + '_' + agg_population_by_state_year['Year']


print(agg_population_by_state_year)

agg_population_by_state_year.to_csv("my_population_by_state_year.csv", index=False)

# print(df3)