import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from IPython.display import display, HTML

# Load the dataset
@st.cache_data()  # Cache data for better performance
def load_data():
    return pd.read_csv('FBI_dataset.csv')


# Title and description
st.title('Analysis of FBI D ataset')
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

 # Title and description
st.title('Top 10 Percentages  of Unsolved Cases')
st.write('This section displays the top 10 percentages of unsolved cases from the FBI dataset.')

# Load data
df = load_data()

# Calculate and display top 10 percentages of unsolved cases
top_unsolved_cases = pd.DataFrame(df['CLEARED_COUNT'].value_counts(normalize=True) * 100).head(10)
st.write(top_unsolved_cases)    

# Finding percentages of reporting agencies rounded to three decimal places
agency_type_percentages = round(df['AGENCY_TYPE_NAME'].value_counts(normalize=True) * 100, 3)
st.write('Percentages of Reporting Agencies:')
st.write(pd.DataFrame(agency_type_percentages))

# Count of data entries per year
yearly_counts = df.DATA_YEAR.value_counts(ascending=True)
st.write('Participation Trends Over Years:')
st.write(yearly_counts)

# Analysis description
st.write("There has been increasing participation since the inception of data collection. It's possible that data was only partially reported in 2013.")

# Analyzing data about tribal agencies reporting criminal trafficking
tribal_agencies = df.query("AGENCY_TYPE_NAME.str.contains('Tribal')")
st.write('Tribal Agencies Reporting Criminal Trafficking:')
st.write(tribal_agencies)

# Analyzing Florida cases
florida_cases = df.query("STATE_ABBR.str.contains('FL')")
st.write('Florida Cases:')
st.write(florida_cases)

# Seminole County, Florida information
st.subheader('Seminole County, Florida Data:')
seminole_data = df.query("COUNTY_NAME.str.contains('SEMINOLE')")
st.write(seminole_data)

# Juvenile cases cleared/solved by departments
st.subheader('Juvenile Cases Cleared:')
juvenile_cleared = df.query("JUVENILE_CLEARED_COUNT > 0")
st.write(juvenile_cleared)
st.write(f"Total rows: {len(juvenile_cleared)}")

# Focus on Nevada and Florida data
st.subheader('Top 15 Cases - Nevada & Florida:')
state_data = df.loc[(df.STATE_NAME.isin(['Nevada', 'Florida'])) & (df.OFFENSE_SUBCAT_NAME == 'Commercial Sex Acts'), ['DATA_YEAR', 'STATE_NAME', 'ACTUAL_COUNT']].sort_values(by='ACTUAL_COUNT', ascending=False).head(15)
st.write(state_data)

# ... (Continue displaying other analyses similarly)
# Sort reported cases and plot
df_sorted = df.sort_values('ACTUAL_COUNT', ascending=False)
plt.figure(figsize=(20, 8))
plt.style.use("fivethirtyeight")
plt.xticks(rotation=90)
plt.title("Reported Cases by State")
plt.bar(df_sorted["STATE_NAME"], df_sorted["ACTUAL_COUNT"])
st.pyplot()



# Plotting aggregated reported cases by year
st.subheader('Aggregated Reported Cases by Year')
plt.plot(df.groupby('DATA_YEAR').sum().ACTUAL_COUNT.index, df.groupby('DATA_YEAR').sum().ACTUAL_COUNT.values)
plt.title("Aggregated Reported Cases by Year")
st.pyplot()

# Plotting a line plot of the number of solved cases each year
st.subheader('Number of Solved Cases Each Year')
sns.lineplot(x="DATA_YEAR", y="CLEARED_COUNT", data=df)
st.pyplot()



# Plot reported cases by region
plt.figure(figsize=(8, 6))
sns.catplot(x="ACTUAL_COUNT", y="REGION_NAME", data=df)
max_REGION_NAME = df['REGION_NAME'].value_counts().index[0]
st.write('Region with highest occurrence:', max_REGION_NAME)
st.pyplot()



# Plot reported cases by state
plt.figure(figsize=(8, 6))
sns.catplot(x="ACTUAL_COUNT", y="STATE_NAME", data=df, height=10).set(title="Reported Cases of Trafficking by State")
st.write("Reports of trafficking for each state")
st.pyplot()



# Breakdown of reported offenses involving sex acts or not
plt.figure(figsize=(10, 10))
sns.stripplot(x="OFFENSE_SUBCAT_NAME", y="ACTUAL_COUNT", data=df, hue="OFFENSE_SUBCAT_NAME", linewidth=2, size=10)
st.write("Breakdown of Reported Offenses involving Sex Acts or Not")
st.pyplot()

# Number of times each offense subcategory is listed and overall percentage
offense_counts = df["OFFENSE_SUBCAT_NAME"].value_counts()
offense_percentage = df["OFFENSE_SUBCAT_NAME"].value_counts(normalize=True) * 100
st.write("Number of times each subcategory offense is listed:")
st.write(offense_counts)
st.write("Overall percentage of total for each offense subcategory:")
st.write(offense_percentage)

# Breakdown of each crime reported by year
sns.lmplot(x="DATA_YEAR", y="ACTUAL_COUNT", hue="OFFENSE_SUBCAT_NAME", data=df)
st.write("Breakdown of each crime reported by year")
st.pyplot()

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
