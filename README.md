# Purpose:

Human trafficking is a significant issue in this country, and the topic of sex trafficking is of great importance. In this exercise, I will be examining a human trafficking dataset compiled from various local, state, city, county, and federal agencies reporting human trafficking cases in the United States from 2013-2021. 

By analyzing this data, we can better understand the prevalence of human trafficking in different regions of the country and potentially identify connections to specific groups or areas. To analyze the dataset, I will use Python and several libraries such as matplotlib, seaborn, numpy, and pandas. After cleaning and preprocessing the data, I will use visualizations and statistical techniques to identify trends and patterns in the data, such as using bar charts, scatter plots, and line graphs to visualize the number of human trafficking cases over time or by location. By using these tools, we can gain a deeper understanding of the issue of human trafficking and work towards finding solutions to prevent future tragedies.

## Data Description:

Below are explanations of what is found in each column of the Human Trafficking dataset.

DATA_YEAR – The year in which the incident occurred.

ORI – ORIGINATING AGENCY IDENTIFIER (ORI) - This identifies the agency in which the offense occurred.

PUB_AGENCY_NAME – Agency name as it appears in FBI UCR Publications.

PUB_AGENCY_UNIT – The specific unit name for which a Publication Agency report UCR data as.

AGENCY_TYPE_NAME – Type of agency that reports UCR data (city/county/federal agency, etc).

STATE_ABBR – This is the state abbreviation.

STATE_NAME – Full name of the state.

DIVISION_NAME – The geographic division in which the agency is located.

COUNTY_NAME – The name of the county within the state.

REGION_NAME – Geographic region in which the agency is located.

POPULATION_GROUP_CODE – Group 0 is possessions; 1-7 are cities; 8-9 are counties.

POPULATION_GROUP_DESC – The name of the population groups.

OFFENSE_SUBCAT_ID – A numeric code assigned to the Offense_Subcat_Name.

ACTUAL_COUNT – Total number of Human Trafficking offenses reported to the UCR Program.

UNFOUNDED_COUNT – Total number of false or baseless complaints reported to the UCR Program from law enforcement agencies.

CLEARED_COUNT – Total number of Human Trafficking offenses that were cleared or closed.

JUVENILE_CLEARED_COUNT – Total number of Human Trafficking offenses that involved a juvenile offender that were cleared or closed.

OFFENSE_SUBCAT_NAME

Commercial Sex Acts – Human trafficking commercial sex acts is defined as inducing a person by force, fraud, or coercion to participate in commercial sex acts, or in which the person induced to perform such act(s) has not attained 18 years of age.

Involuntary Servitude –Human trafficking involuntary servitude is defined as the obtaining of a person(s) through recruitment, harboring, transportation, or provision, and subjecting such persons by force, fraud, or coercion into involuntary servitude, peonage, debt bondage, or slavery (not to include commercial sex acts).

##  Algorithm Description:

Data Loading and Display: Load the dataset using Pandas, display the initial rows, summary statistics, and information about numeric and categorical columns.

Percentage Analysis: Calculate and display the percentage of occurrences for each unique value in each column and the percentage of null values in each column.

Top Unsolved Cases: Determine and display the top 10 percentages of unsolved cases.

Specific Analysis:
Analyze reporting agency percentages.
Count data entries per year to observe trends.
Analyze specific cases related to tribal agencies, Florida, Seminole County, juvenile cases cleared, and cases from Nevada and Florida.

Visualization:
Generate various visualizations using Seaborn and Matplotlib to depict reported cases by state, year, offense subcategory, etc.

Statistics and Rankings:
Calculate statistics like the breakdown of reported offenses, ranking top states based on occurrences, and displaying the maximum occurrences by county, state, population group, and region.

## Tools Used:
Streamlit: Used for building the web application, creating an interactive interface, and displaying data.

Pandas: For data manipulation, loading, cleaning, and analyzing the dataset.

Seaborn & Matplotlib: Used for data visualization, creating various plots (bar, line, scatter) to represent trends, distributions, and comparisons visually.