import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


# Load the dataset
@st.cache_data()  # Cache data for better performance
def load_data():
    return pd.read_csv('FBI_dataset.csv')


# Title and description
st.title('Analysis of FBI Dataset')
st.write('This app explores the FBI dataset.')

# Load data
df = load_data()

# Display first five rows
st.subheader('First Five Rows of the Dataset')
st.write(df.head())

# Display summary statistics for numeric columns
st.subheader('Numeric Columns')
st.write(round(df.describe(), 1))

# Display descriptive statistics for categorical columns
st.subheader('Categorical Columns')
st.write(df.describe(include=['O']))

# Display dataset information


# Display percentage of total occurrences for each value in each column
st.subheader('Percentage of Total Occurrences for Each Value')
for col in df.columns:
    st.write(col)
    st.write(pd.DataFrame(round(df[col].value_counts(normalize=True) * 100, 2)))

# Display percentage of total null values for each column
st.subheader('Percentage of Null  Values')
for col in df.columns:
    if df[col].isna().sum():
        st.write(f"{col}: {round(df[col].isna().sum() / len(df), 3) * 100}%")
st.write('Unfounded Count has 1,969 blank values accounting for 63.6% of the dataset, and Public Agency Unit has 2,867 null values for 92.5% of the dataset. There are three apiece for Population Group Code and Population Group Desc. accounting for just .1% of the dataset (minimal). It seems that Unfounded_Count null values likely can be interpreted as zero; that who did data entry just left that blank if there were none.')      

 # Title and description
st.title('Top 10 Percentages  of Unsolved Cases')
st.write('This section displays the top 10 percentages of unsolved cases from the FBI dataset.')
st.write('''Just over half of the cases in this entire 8-year dataset remain unsolved? Is this possible? This would warrant a deeper examination.
Next I'll look at which agencies are reporting, or investigating, trafficking-related crimes.''')

# Load data
df = load_data()

# Calculate and display top 10 percentages of unsolved cases
top_unsolved_cases = pd.DataFrame(df['CLEARED_COUNT'].value_counts(normalize=True) * 100).head(10)
st.write(top_unsolved_cases)    

# Finding percentages of reporting agencies rounded to three decimal places
agency_type_percentages = round(df['AGENCY_TYPE_NAME'].value_counts(normalize=True) * 100, 3)
st.subheader('Percentages of Reporting Agencies:')
st.write(pd.DataFrame(agency_type_percentages))

# Count of data entries per year
yearly_counts = df.DATA_YEAR.value_counts(ascending=True)
st.subheader('Participation Trends Over Years:')
st.write(yearly_counts)

# Analysis description
st.write("There has been increasing participation since the inception of data collection. It's possible that data was only partially reported in 2013.")

st.write('Next I would like to look at just tribal agencies who filed criminal trafficking reports.') 
tribal_agencies = df.query("AGENCY_TYPE_NAME.str.contains('Tribal')")
st.subheader('Tribal Agencies Reporting Criminal Trafficking:')
st.write(tribal_agencies)

# Analyzing Florida cases
st.write('Note that county name is not specified on tribal lands, nor in federal cases. Next Ill look at Florida cases.')
florida_cases = df.query("STATE_ABBR.str.contains('FL')")
st.subheader('Florida Cases:')
st.write(florida_cases)

# Seminole County, Florida information
st.subheader('Seminole County, Florida Data:')
seminole_data = df.query("COUNTY_NAME.str.contains('SEMINOLE')")
st.write(seminole_data)
st.write('''Seminole County, Florida has reported four of the eight years. They are reporting a 100% success rate for solving cases in every year reported.
Next under the magnifying glass is departments reporting juvenile cases that have been solved:''')

# Juvenile cases cleared/solved by departments
st.subheader('Juvenile Cases Cleared:')
juvenile_cleared = df.query("JUVENILE_CLEARED_COUNT > 0")
st.write(juvenile_cleared)
st.write(f"Total rows: {len(juvenile_cleared)}")

st.write('''Listed above are jurisdictions with juvenile cases that were cleared, or solved. There are 103 rows of information submitted from different agencies. Here we see that several counties can be listed in one cell, making this an unreliable cell to classify.
Based on graphs found on the next page, I'm going to focus on Nevada state information for a moment, along with  state of Florida. I'll sort data based on number of cases in Nevada and Florida, returning top 15 number of cases in a given year.''')

# Focus on Nevada and Florida data
st.subheader('Top 15 Cases - Nevada & Florida:')
state_data = df.loc[(df.STATE_NAME.isin(['Nevada', 'Florida'])) & (df.OFFENSE_SUBCAT_NAME == 'Commercial Sex Acts'), ['DATA_YEAR', 'STATE_NAME', 'ACTUAL_COUNT']].sort_values(by='ACTUAL_COUNT', ascending=False).head(15)
st.write(state_data)

st.write('Nevada has held the top 6 spots statewide before Florida makes its first appearance in this list in 2020 with 5,888 cases.')

# Sort reported cases and plot
st.title('Graphing Relationships')
st.write('Sorting number of reported cases in descending order and assigned to a new variable name, then using matplotlib to design a graph showing cases reported by state.')
df_sorted = df.sort_values('ACTUAL_COUNT', ascending=False)
fig1, ax1 = plt.subplots(figsize=(20, 8))
plt.style.use("fivethirtyeight")
plt.xticks(rotation=90)
plt.title("Reported Cases by State")
ax1.bar(df_sorted["STATE_NAME"], df_sorted["ACTUAL_COUNT"])
st.pyplot(fig1)



# Plotting aggregated reported cases by year
st.subheader('Aggregated Reported Cases by Year')
fig, ax = plt.subplots()
ax.plot(df.groupby('DATA_YEAR').sum().ACTUAL_COUNT.index, df.groupby('DATA_YEAR').sum().ACTUAL_COUNT.values)
ax.set_title("Aggregated Reported Cases by Year")
st.pyplot(fig)
st.write('As shown below, the average actual count of human trafficking offenses have increased over the years, or reporting of them has increased. Its important to take into account that 2013 may have only had partial reporting and should not be included in any summary statistics.')


# Plotting a line plot of the number of solved cases each year

st.subheader('Number of Solved Cases Each Year')
st.write('Creating a line plot of the number of solved cases each year, showing a general trend down.')
fig3, ax3 = plt.subplots()
sns.lineplot(x="DATA_YEAR", y="CLEARED_COUNT", data=df, ax=ax3)
st.pyplot(fig3)

# Plot reported cases by region
plt.figure(figsize=(8, 6))
sns.catplot(x="ACTUAL_COUNT", y="REGION_NAME", data=df)
max_REGION_NAME = df['REGION_NAME'].value_counts().index[0]
st.write('Region with highest occurrence:', max_REGION_NAME)
st.pyplot()

st.write('Above, note the number of reported cases each year by region - with the west showing the highest data points recorded but a larger number of cases, or data points overall in the South.')


# Plot reported cases by state
plt.figure(figsize=(8, 6))
sns.catplot(x="ACTUAL_COUNT", y="STATE_NAME", data=df, height=10).set(title="Reported Cases of Trafficking by State")
st.write("Reports of trafficking for each state")
st.pyplot()
st.write('''In the graph above, we see reports of trafficking for each state. Each dot is a reporting agency and Nevada far and away has greater numbers of cases reported by some six departments. Texas is second, with Kentucky showing a high case count for one of its reporting agencies.
Actual count is actually a binary either/or category of crimes that are sex acts or are not sex acts. What's the breakdown of each?''')

# Breakdown of reported offenses involving sex acts or not
fig6, ax6 = plt.subplots(figsize=(10, 10))
sns.stripplot(x="OFFENSE_SUBCAT_NAME", y="ACTUAL_COUNT", data=df, hue="OFFENSE_SUBCAT_NAME", linewidth=2, size=10, ax=ax6)
st.write("Breakdown of Reported Offenses involving Sex Acts or Not")
st.pyplot(fig6)

# Number of times each offense subcategory is listed and overall percentage
offense_counts = df["OFFENSE_SUBCAT_NAME"].value_counts()
offense_percentage = df["OFFENSE_SUBCAT_NAME"].value_counts(normalize=True) * 100
st.write("Number of times each subcategory offense is listed:")
st.write(offense_counts)
st.write("Overall percentage of total for each offense subcategory:")
st.write(offense_percentage)

# Breakdown of each crime reported by year
st.subheader('Breakdown of Each Crime Reported by Year')

fig7 = sns.lmplot(x="DATA_YEAR", y="ACTUAL_COUNT", hue="OFFENSE_SUBCAT_NAME", data=df, height=6, aspect=2)
st.pyplot(fig7)
st.write('Sex trafficking-related crimes are in blue, and we can see more instances of them being reported at higher aggregate numbers. Involuntary servitude is in red, and is reported in low quantities, with a few outlying instances.')




# Ranking of top 30 states with overall highest occurrences for all of the past 8 years
top_states = df[['STATE_NAME', 'ACTUAL_COUNT']].groupby('STATE_NAME').sum().sort_values(by=['ACTUAL_COUNT'], ascending=False).head(30)
st.write("Top 30 states with highest occurrences:")
st.write(top_states)

# Displaying maximum occurrences
max_county_name = df['COUNTY_NAME'].value_counts().index[1]  # first occurrence was "Unspecified"
max_state_crime = df['STATE_NAME'].value_counts().index[0]
max_POPULATION_GROUP_DESC = df['POPULATION_GROUP_DESC'].value_counts().index[0]
max_REGION_NAME = df['REGION_NAME'].value_counts().index[0]
st.write('County with highest occurrence of human trafficking:', max_county_name)
st.write('State with highest occurrence of human trafficking:', max_state_crime)
st.write('Metropolitan size with highest occurrence:', max_POPULATION_GROUP_DESC)
st.write('Region with highest occurrence:', max_REGION_NAME)

st.write("""Based on the analysis, I have observed that Texas had the highest overall occurrences of human trafficking, with cases aroung 186548. Hennepin County, Minnesota had the highest number of cases among for all counties in the United States. The western region is showing the highest individual data points recorded but a larger overall number of cases regionally in the South.
         
Data reporting has steadily increased each year since reporting began in 2013. Its important to note that reporting may be incomplete or partial in 2013 and should be taken into account when comparing to other years in the dataset. In this 8-year dataset, there were a total of 13056 reported cases of human trafficking, 3264 of which were deemed unfounded and 6976 cases were solved, or cleared.
         
Over 64% of city police departments are reporting human trafficking cases. County law enforcement departments make up 25% of reporting, with state police bringing in 8% of reported cases and Tribal police departments reporting just .3% of cases overall. While Seminole County, Florida has reported four of eight years, they are reporting a 100% success rate for solving cases in every year reported.
That’s not the case for other departments.
         
Just like getting to know people, the more we interact with something, the more we get to know it and are sometimes surprised by what we learn. For purposes of practicing curiosity, if I were to continue studying this data, I would immediately dig deeper into the fact that some 54.35% of the human trafficking cases reported to the FBI are going unsolved each year. That seems a grave number to admit and warrants more investigation. Assuming one person equals one case, that’s 6080 people who continue to be victimized, subjected into slavery, sexual or otherwise in this country, since 2013. This is a huge concern and has eclipsed my initial questions.""")
