# BUSINESS ANALYTICS WITH EXCEL

## LIST OF CONTENTS

* INTRO
* DATA CLEANING AND PREPARATION
* CONDITIONAL FORMATTING AND FUNCTIONS
* ANALYZING DATA WITH PIVOT TABLES
* BUSINEES ANALYTICS WITH EXCEL
* DATA ANALYSIS WITH STATISTICS

## INTRODUCTION

To manage and analyze data, one must understand the below aspects

* Data Cleaning
* Data Preparation
* Data Visualization

one must familiarize themselves with excel on the below areas

* Perform functions like VLOOPUP, HLOOKUP, match etc.,
* Compare data using charts
* Automate tasks using MACROS
* FInd optimal values using solver add-in and goal seek
* Smooth out data using moving average
* Make one plot for each independent variable versus the residuals using multiple linear regression

*This section will introduce to various type of analytics and it also explains the analytics concepts and related examples for understanding them better*

**[ANALYTICS:]()**

In today's data-driven world, analytics plays a vital role not only in businesses but also in the various fields such as sports, healthcare, finance, governament and many more such fields.

People who are able to apply analytics known as "Data Scientist" - Hailed as having the best job opportunities in the 21st century

> **Analystics is a scientific process to examine the raw data to draw the meaningful and logical sense of the data. It gives insights about the information to the organizations that will enable them to make better decisions**

Study of analytics often involves analyzing the historical data to look for the potential trends of the past in order to understand the effects of certain decisions or to evaluate the perfomance of the business based on the decisions, the goal of the proper analysis is to improve business by gaining comprehensive knowledge of the past trends and decisions, which is basis of which corrective actions can be taken

For example, Operator of the top MNC tire company wants to do a detailed analysis of the defect during the entire production at it's various manufacturing plants across the globe.Every time they are defects on the tires during the manufacturing process that the *defect is stored with the pre-defined defect code through proper analytics implementation mechanisms.* The operation head can perform analysis for every product on every machine for every operator - He can also obtain the results for the no of defects from each plant - This is how companies optimize their supply chain performance using this concept, They do the predictive analysis keeping historical data as base

**LEARNING OBJECTIVES IN ANALYSTICS**

1. Concepts of analytics
2. Types of analystics
3. Areas of analytics

### **TYPES OF ANALYTICS**

There are four distinct types of analytics

1. **Descriptive**, which explains what is happened ?
2. **Diagnostics**, which states why it happened ?
3. **Predictive**, it depicts what could happen ?
4. **Prescriptive**, it talks about what should happen ?

#### Descriptive Analysis

* It is known as simplest class of analytics.
* It is the type of analytics allows us to break big chunk of data into smaller chunks of data
* It chunks out relevant information from the data or briefs synopsis what is happened ?

For example, Let us assume of doing descriptive analysis for customer's data. It includes finding answers to the following questions

* How many different segments of buyers? that we are dealing with
* Where are these buyers located?
* How do high values customers differ ? what are they interested in ?
* What is the income age number of children occupation and regional breakdown of these buyers

#### Diagnostic Analysis

Diagnostics analysis is the best option that we go for if we want to take deeper into the data that we have collected and also we will get a better understanding of the process(why it is happened ?)

#### Predictive Analysis

Predictive analysis is the another option available to us to condense the data

It uses different statistical data modeling and data mining techniques to study latest and past trends, thereby, allowing business analysts and data scientist to make predictions

For example, Let us assume of doing predictive analysis for marketing campaign, it will look answers to the following questions

* Who will responds to the campaign ?
* Which product and which channel ?
* What are the potential value of each customer and prospect ?
* Who will stop the subscription and when ?

#### Prescriptive Analysis

Prescriptive analysis is the last phase of business analytics

It is related to the both descrptive and predictive analysis

while the descriptive analysis provide the information about what is happened ? and predictive analytics might forecast what might happen, which is probabilistic in nature

Prescriptive analysis optimizes decision making  by determining the best solution available among various choices in the business constraints

### AREAS OF ANALYTICS

Some of the areas of the analytics are

* Customer Analytics
* Industry Focused Analytics
* Financial Analytics
* Performance Analytics
* Risk Analytics

#### Customer Analytics

Customer Analytics is the process that helps organization to take critical decisions and delivers the offers that are anticipated

This analytics offers the organization customer insights necessary to take decisions

Customer Analytics uses techniques such as

* Market segmentation
* Predictive Analysis
* Data Modelling
* Visualization

It play a pivotal role in the prediction of the customer behavior. For example, Customer Acquistion and Retension - All telecom companies use various marketing methods	to retain their customers

#### Financial Analytics

It is the new way to drive competitive advantage

It helps financial executives to explore different ways to answer financial related business questions and forecast the future financial situations

In today's dynamic environment, financial analytics helps the finance functions to bring greater value to the organization

Financial analytics help companies to make multiple views of thier data and derive insights that will help them to take necessary actions

For example, Consolidation of financial statements - FInancial statements are the reports prepared with sole purpose for maintaing business accounts in timely manner.These statements will showcase the financial position of the company to the market stakeholders, shareholders and the governament and general public and these statements will give detailed overview of the company's financial position to investors and creditors.

#### Performance Analytics

Performace analytics is the practise of using data and technology to study how our business is perfoming to continuosly make it better and managing daily operations, planning stratergies and budgeting for the business, meeting SLA's, and pinpointing areas of the improvement

For example, In HR resource management - the performance of the employee is monitored on the regular basis, keeping the parameters in demand on the type of organization and expectations

Performance analytics gives company enough time to take corrective actions for improving the performance of the employee in time if it required, thus, improve productivity and output of the company

#### Risk Analytics

In today's dynamic business environment, where things change at the rapid pace the rate of risk is very high . The insecurities caused by these risks will affect the success of the business.Risk analytics tries to receive the uncertainties of predicted future and helps evaluate project success or failure.

Organizations are trying to define and understand their tolerance level for real with the help of risk analytics organizations trying to manage and mitigate the risk as they can identified and measured and planned.Thus, allowing decision makers enough time to make wise decision and corrective action

Risk analytics can be categorized as

1. Quantitative Risk Analysis
2. Qualitative Risk Analysis

QNTRA - Quantitative risk analysis quantifies possible project results specific to the project

* This analysis tries evaluate the numerical possibilities of various adverse events and predicts the loss of the company would go through if any of possibilities come true.

QLTRA - Qualitative risk analysis is performed on almost all risks and it not numerically defined

* This analysis involves defining various project related threats and determining the extent of the risks and proposing the corrective actions in order to avoid risk

For Example, In banking industry - Credit scores are built to predict individual deliquency behaviour and it is used to represent credit worthiness of an individual

Corruption is an unethical conduct by a person or group of people to generate illegal profit generally, to acquire personally benefit and it drastically the confidence and trust of the parties involved and thus, hampers the achievement of the project goals,

## DATA CLEANING AND PREPARATION

#### LEARNING OBJECTIVES

* Sort and filter functions
* Group by and ungroup
* Remove duplicates
* Data validation

#### SORT AND FILTER

Sort and Filter functionalities are available in the excel to order or to filter the data for further analysis

Example: consider the dataset below

| students | subject | GPA |
| :------: | ------- | --- |
|    A    | Maths   | 5.6 |
|    B    | Maths   | 7.8 |
|    C    | Maths   | 8.3 |
|    D    | Maths   | 9.2 |

In order to sort the values based on GPA in the descending order go to "data tab" then pop-up will appear under sort columns choose "GPA" and then "Largest to smallest" and then click on OK

We can do the same for non-numerical columns and multiple columsn as well

Filter option helps to filter the data of any column we choose

consider same example, choose a column to filter and in the data tab click on "filter icon" or "CTRL+SHIFT+L"

for example, if we want to see the GPA's that are greater than or equal to 4

#### GROUP BY AND SUBTOTAL

Group by and ungroup by are available  under the data tab withing outline section

**GROUP BY**

* Group By functionality in excel allows us to show necessary data for easy viewing and analysis and we can also create subtotals and outline for the given set of data
* Group By can be done for rows or columns
* Steps for grouping data

  1. To group data, select the rows and columns that you want to group
  2. Click on the group icon under data tab
  3. Then, Pop-up tab will appear - choose columns and click on OK
  4. Groups the three columns choosen, and applies a control to show or hide the grouped content
  5. If we click on "-" hides the content similarly, if we click on "+" it shows the group content
  6. Similarly, we need to follow above steps same for the rows as well

**UNGROUP**

The ungroup option allowd us to remove the groups created by group

In order to ungroup choose the data which is already grouped then click on the "ungroup icon" under data tab

If we want to ungroup row level grouping choose row option / if we want to ungroup column level grouping choose column option

**SUBTOTAL**

subtotal allows us to create groups and have subtotal for each group

**TEXT TO COLUMN**

it converts raw texts into columns in excel

For example, Let us assume that we have an raw data which includes name, age, address, phone, university

Open excel file and paste the raw content into it and choose column A in the sheet then go to data tab in the header then click on "text to columns"

Next in the dialog box choose the delimited option and then click on Next - There will be different delimiters i.e, comma, semicolon, space, tab , other choose what we need and click on the Next

**REMOVING DUPLICATES**

Duplicate refers to the copy of the original

In any data analytics work, there will be always  be cases where get duplicates in different columns - Excel is very handy in order to remove the duplicates in the data

Duplicates can occur in data and cause errors in analytics 

* when there is incorrect submission of user data multiple times
* When there is a missing validation for duplication in the data set
* When we merge multiple data source using joins
* When we copy and paste data multiple times

When duplicates are removed using excel, we can choose a single column or multiple columns to check the data

Choose the columns with a set of rows to remove duplicates after selection click on the data tab then click on the "Remove duplicates" icon then pop-window will appear to choose which column to delete duplicates then click ok and proceed

**DATA VALIDATION**

Data in excel can be validated using some rules set in data validation dialog

For example, let us assume we have choosen cell/group then click "data validation" icon which is avaliable in "data tab"

* validation applies to new data entered in the cells where rules are placed
* Existing data is not validated
* After clicking on validation, a pop up appears regarding validation criteria
  * "Any value" allows any alpanumerical value in the cells
  * "Whole number" allows whole numbers and set of rules including a maximum and minimum range to be set
  * "List" allows only a list of values in the specific range of cells or written manually in the "source" input box
  * "date" allows only dates and set of rules including a maximum and minimum range to be set
  * "time" allows only time and set of rules including a maximum and minimum range to be set
* ssa

fsa

## FORMATTING, CONDITIONAL FORMATTING AND FUNCTIONS

## ANALYZING DATA WITH PIVOT TABLES

## BUSINEES ANALYTICS WITH EXCEL

## DATA ANALYSIS USING STATISTICS

## USING MACROS FOR ANALYTICS
