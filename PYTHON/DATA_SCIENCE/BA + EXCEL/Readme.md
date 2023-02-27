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

> **Analytics is a scientific process to examine the raw data to draw the meaningful and logical sense of the data. It gives insights about the information to the organizations that will enable them to make better decisions**

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

## FORMATTING, CONDITIONAL FORMATTING AND FUNCTIONS

**LEARNING OBJECTIVES**

* Custom Formatting
* Logical Functions
* Statistical and Mathematical Functions

For example, Let's say we need to differentiate the sales value from a data set is like above target, below target, met target.As a data set can be huge and complex in differentiating each value manually would consume lot of effort and time Here we can use excel features such as formatting and conditinal formatting which enable us to perform this task easily

Formatting as the name suggests it helps us to format the data, using different techniques, making data easy to read in the required format and analyze them the right formatting technique applied to the worksheets can help users present the data efficiently

Conditional Formatting helps us to visually explore and analyze data, detect critical issues and identify patterns and trends

Conditional Formatting helps to add patterns and trends to the raw information, using diferent colors, icons and formulaes.

At some times, It is necessary to perform mathematical operations and calculations within our dataset.In such cases, Excel provides a large number of logistical statistics and mathematical functions like V-LookUp, H-LoopUp, If, Not, Rank, Quartile and many more that users can perform calculations from ranging basic to complex operations.These in-build functions help and manage data and perform descriptive statistical analysis.

Excel also offers a wide range of important formulaes that perform many common tasks.These formulaes may be as simple as basic operations or it could be a complex operations of in-built excel functions

* Use custom formatting to format data and values
* Execute logical operations through logical functions
* Use conditional formatting
* Classify various statistical functions
* Find position and value of required fields using lookup and reference functions

**CUSTOM FORMATTING**

The worksheet appears more polished and easy to read if proper formatting technique applied to it.

We can format the cells manually by selecting the font color , fonts, font size, bg color, borders.

We can also format the cells automatically by using numerous predefined table styles or quick styles.

If these basic function do not meet our needs or do not display the data in the required format, create the custom format

For Example, Let say we want to display 1,532,000 as 1.53M or 1-Jan-2023 as 1-Sunday-Jan-2023.Here we can use custom formatting feature of excel.Let's see how we can accomplish in the excel

| Date      | OrderID | Product   | Salesman | Region | No of customers | Net sales | Profit/Loss |
| --------- | ------- | --------- | -------- | ------ | --------------- | --------- | ----------- |
| 01-Jan-23 | 1112    | Product1  | Arjun    | North  | 8               | 7,164     | 844         |
| 02-Jan-23 | 1113    | Product2  | Arjun    | North  | 12              | 6,528     | 3,376       |
| 03-Jan-23 | 1114    | Product3  | Arjun    | North  | 24              | 2,520     | 2,280       |
| 04-Jan-23 | 1115    | Product4  | Arjun    | South  | 15              | 9,660     | 1,737       |
| 05-Jan-23 | 1116    | Product5  | Arjun    | South  | 3               | 11,550    | 854         |
| 06-Jan-23 | 1117    | Product6  | Arjun    | South  | 2               | 7,896     | 2,565       |
| 07-Jan-23 | 1118    | Product7  | Arjun    | South  | 16              | 8,095     | 1,063       |
| 08-Jan-23 | 1119    | Product8  | Arjun    | South  | 22              | 12,180    | 1,864       |
| 09-Jan-23 | 1120    | Product9  | Arjun    | South  | 44              | 4,900     | 2,653       |
| 10-Jan-23 | 1121    | Product10 | Arjun    | South  | 12              | 2,277     | 1,931       |
| 11-Jan-23 | 1122    | Product11 | Arjun    | West   | 11              | 3,122     | 994         |
| 12-Jan-23 | 1123    | Product12 | Arjun    | West   | 6               | 8,046     | 4,092       |
| 13-Jan-23 | 1124    | Product13 | Arjun    | West   | 1               | 4,230     | 1,900       |
| 14-Jan-23 | 1125    | Product14 | Arjun    | West   | 4               | 11,250    | 882         |

Here in the above worksheet, we have a column name Net sales. Suppose if we want to display the values of net sales in terms of thousands.For example,Display 11,250 as 11.25k Now select entire columns in the net sales - under the home tab click the dropdown present in the number panel and slect the option more number formats. From the format cells dialog box appears from the category list select the type as custom and then in the type text box with #,##0.00,"k" - #,Digit holder with thousand comma separation and , after decimal divide value by 1000 and 0 after decimal indicates number values after decimal places

| Date      | OrderID | Product   | Salesman | Region | No of customers | Net sales | Profit/Loss |
| --------- | ------- | --------- | -------- | ------ | --------------- | --------- | ----------- |
| 01-Jan-23 | 1112    | Product1  | Arjun    | North  | 8               | 7.16K     | 844         |
| 02-Jan-23 | 1113    | Product2  | Arjun    | North  | 12              | 6.53K     | 3,376       |
| 03-Jan-23 | 1114    | Product3  | Arjun    | North  | 24              | 2.52K     | 2,280       |
| 04-Jan-23 | 1115    | Product4  | Arjun    | South  | 15              | 9.66K     | 1,737       |
| 05-Jan-23 | 1116    | Product5  | Arjun    | South  | 3               | 11.55K    | 854         |
| 06-Jan-23 | 1117    | Product6  | Arjun    | South  | 2               | 7.90K     | 2,565       |
| 07-Jan-23 | 1118    | Product7  | Arjun    | South  | 16              | 8.10K     | 1,063       |
| 08-Jan-23 | 1119    | Product8  | Arjun    | South  | 22              | 12.18K    | 1,864       |
| 09-Jan-23 | 1120    | Product9  | Arjun    | South  | 44              | 4.90K     | 2,653       |
| 10-Jan-23 | 1121    | Product10 | Arjun    | South  | 12              | 2.28K     | 1,931       |
| 11-Jan-23 | 1122    | Product11 | Arjun    | West   | 11              | 3.12K     | 994         |
| 12-Jan-23 | 1123    | Product12 | Arjun    | West   | 6               | 8.05K     | 4,092       |
| 13-Jan-23 | 1124    | Product13 | Arjun    | West   | 1               | 4.23K     | 1,900       |
| 14-Jan-23 | 1125    | Product14 | Arjun    | West   | 4               | 11.25K    | 882         |

Now Let us consider another example data formatting, In the column dates we have a date value written as 1 jan 2023 now we want to display it as 1 sunday jan 2023

First select the column containing dates and then under the home tab select the dropdown from numbers panel and then select the option more format options Then format cel dialog box appears from the category list select the type as custom - In the type text box enter dd-dddd-mmmm-yy

| Date                | OrderID | Product   | Salesman | Region | No of customers | Net sales | Profit/Loss |
| ------------------- | ------- | --------- | -------- | ------ | --------------- | --------- | ----------- |
| 01-Sunday-Jan-23    | 1112    | Product1  | Arjun    | North  | 8               | 7,164     | 844         |
| 02-Monday-Jan-23    | 1113    | Product2  | Arjun    | North  | 12              | 6,528     | 3,376       |
| 03-Tuesday-Jan-23   | 1114    | Product3  | Arjun    | North  | 24              | 2,520     | 2,280       |
| 04-Wednesday-Jan-23 | 1115    | Product4  | Arjun    | South  | 15              | 9,660     | 1,737       |
| 05-Thursday-Jan-23  | 1116    | Product5  | Arjun    | South  | 3               | 11,550    | 854         |
| 06-Friday-Jan-23    | 1117    | Product6  | Arjun    | South  | 2               | 7,896     | 2,565       |
| 07-Saturday-Jan-23  | 1118    | Product7  | Arjun    | South  | 16              | 8,095     | 1,063       |
| 08-Sunday-Jan-23    | 1119    | Product8  | Arjun    | South  | 22              | 12,180    | 1,864       |
| 09-Monday-Jan-23    | 1120    | Product9  | Arjun    | South  | 44              | 4,900     | 2,653       |
| 10-Tuesday-Jan-23   | 1121    | Product10 | Arjun    | South  | 12              | 2,277     | 1,931       |
| 11-Wednesday-Jan-23 | 1122    | Product11 | Arjun    | West   | 11              | 3,122     | 994         |
| 12-Thursday-Jan-23  | 1123    | Product12 | Arjun    | West   | 6               | 8,046     | 4,092       |
| 13-Friday-Jan-23    | 1124    | Product13 | Arjun    | West   | 1               | 4,230     | 1,900       |
| 14-Saturday-Jan-23  | 1125    | Product14 | Arjun    | West   | 4               | 11,250    | 882         |

Thus custom formatting helps us changing the appearance of cell value according to our needs

**CONDITIONAL FORMATTING**

A worksheet may contain thousand of rows of data by simply examing the raw information, it would be difficult to see patterns and trends.

Conditional formatting helps us to visulaize the data that makes worksheets easier to understand and also it quickly highlights important information in the spreadsheet by using colors , fonts, bg colors, data bars. it changes the appeaance of one or more cells when the cell value meeting criteria to do this we need to create a conditional formatting rule.

For example, Conditional formatting rule can be , if value is greater thatn 5,000 color the cell yellow by applying this rule we are able to see which cells contains values greater than $ 5000

consider the below sales table, which depicts the  amount of sales done by each salesman Here we want to highlight the duplicate order id's - First select the order id column then click on the home tab under the styles panel select the optional conditional formatting from the dropdown menu hover the mouse over the highlight cell rules and duplicate values then duplicate select dialog box appears - select the formatting style from the dropdown menu

Refer excel in the folder for proper understanding

Now we can able see conditional formatting is applied to the order ID and excel highlights all the duplicate cells with green fill and dark green text

We can also explore other options available in the conditional formatting like greater than, lesser than, equal to, between etc.,

Excel provides pre defined styles to quickyl apply conditional formatting our data. They are

* Data bars - Data bars are horizontal bars added to each column, much like bar graph
* Color scales - Color scales change the color of each cell based on its value
* Icon sets - It add specific icons to each cell based on its value

**LOGICAL FUNCTIONS**

Logical functions evaluates a cell or cells for a criteria and return a boolean value, true or false.

In this topic, we can able to learn lots of logical functions like if, and, or, not, true, false.

Let us take referance of previous example, Determine the commission percentage of each salesman based on the sales amount with the following criteria

If net sales > 10000 commision is 5%

   net sales >= 5000 and <=10000 commision is 2.50%

   net sales < 5000 commision is 1.50%

Now we're required to create a between formula that picks all values between the two given values.In such condition IF along with the AND function is used

TRUE/FALSE return true and false respectively if we write them in any cell

The NOT function reverse the result of the function

LOOKUP and Reference Functions - HLOOKUP, VLOOPUP, MATCH, INDEX, OFFSET.

The VLOOKUP function lets us search for specific information in the current worksheet

Let assume an example, List of students with marks

Now we need to determine the marks of particular subject for each student

Lets understand how we can accomplish vlookup function

Note: VLOOKUP function is only used for vertical tables

Like any other formulae, type = sign and type vlookup followed by open parenthesis.

Now we will add the arguments,

* first argument is lookup value or an item we are searchig
* second argument is table array (table array is cell range that contains the data)
* third argument is column index number
* fourth argument is range lookup (true denotes aprroximate match, false denotes the exact match)

Note: VLOOKUP function workd from left to right, the lookup values should always in the left column of the table array

If our table in horizontal format then we use HLOOKUP function

The HLOOkUP function is used to determine a specific information when table is in horizontal format

Like any other formulae, type = sign and type hlookup followed by open parenthesis.

Now we will add the arguments,

* first argument is lookup value or an item we are searchig
* second argument is table array (table array is cell range that contains the data)
* third argument is row index number
* fourth argument is range lookup (true denotes aprroximate match, false denotes the exact match)

Note: HLOOKUP function workd from left to right, the lookup values should always in the top row of the table array

The MATCH function searches for a sepcified value or item in a single-dimensional array and return to the relative position of the item

Like any other formulae, type = sign and type match followed by open parenthesis

Now we will add the arguments,

* first argument is lookup value or an item we are searchig
* second argument is table array (table array is cell range that contains the data)
* third argument is match type which can be -1, 0, 1

The INDEX function returns a value from a sepcified position in a specified column in a list

Like any other formulae, type = sign and type index followed by open parenthesis

Now we will add the arguments,

* first argument is table array
* second argument is row num
* third argument is col num

The OFFSET function return a reference to a range that is the offset number of the rows and columns from another range cell

Like any other formulae, type = sign and type offsetfollowed by open parenthesis

Now we will add the arguments,

* first argument is table array
* second argument is row num
* third argument is col num

Available STATISTICAL FUNCTION in the excel, ranging from basic functions mean, median and mode to binomial distribution and tests binomial and chi-square

From here we will learn about various statistical funtions like sumifs, countifs, percentile, median, quartile,

SUMIFS and COUNTIFS

* These are the most frequently used functions in the excel
* SUMIFs and COUNTIFs perform count and sum based on one or more criteria
* SUMIFs function calculates the sum of cells based on certain cirteria
* COUNTIFs function counts the number of cells in a given range when certain criteria is met

PERCENTILE and QUARTILE

The percentile function is used to find the percentile of specific cell

Like any other formulae, type = sign and type percentile followed by open parenthesis

Now we will add the arguments,

* first argument is table array
* second argument is percentile we want like 0.4 to find 40th percentile

The quartile function depicts the result for the first, second, third and fourth quartile

Like any other formulae, type = sign and type quartile followed by open parenthesis

Now we will add the arguments,

* first argument is table array
* second argument must be a number between zero and four

SATANDARD DEVIATION, MEDIAN and RANK Function

STDEV is a measure of how dispersed the data is in relation to the mean

Like any other formulae, type = sign and type stddev followed by open parenthesis

Now we will add the arguments,

* The argument is the number of cells in the column

MEDIAN is used to measure the mid value of the list

Like any other formulae, type = sign and type median followed by open parenthesis

Now we will add the arguments,

* The argument is the number of cells in the column

RANK is used to compare a number from the rest of the numbers in the list

Like any other formulae, type = sign and type rank.eq followed by open parenthesis

Now we will add the arguments,

* First argument is the number
* second argument is the array of ref list
* Third argument is the order how we rank the number (0 descending order, 1 ascending order)

## ANALYZING DATA WITH PIVOT TABLES

Data Analysis : Problem

Being able to analyze all the data in our worksheet can help us make better decisions but sometimes its hard to know where to start, especially when we have a lot of data. Suppose if we want to determine net sales in the previous table, analyzing this manually could be difficult as region appears in the multiple rows and we need total of them individually and we can also determine net sales by using excel's built-in formulaes, a task that could become quite time consuming.Here Pivot table, comes into the picture and extracts key information from this large detailed data-set.

A Pivot table is an incredibly powerful tool that makes it is easy to summerize, analyze, explore and present the data.

A Pivot table makes life easy, giving us insights into the data and allowing us to experiment with it, to discover new trends and patterns.It instantly calculates and summerize the data in a way that both easy to read and manipulate.

One can easily design a pivot table by simply dragging and dropping relevant information into the appropriate boxes

LEARNING OBJECTIVES

* Create and use pivot tables
* Group different data types
* Create and evaluate summarized data types
* illustrate the use of calculated field and calculated item
* Design a interactive pivot table using a slicer

INTRODUCTION TO PIVOT TABLES

Pivot tables are very useful and powerful features of Excel

It is used to summarize, analyze, explore and present the data in tabular form

For example, Let us assume below data to determine the net sales done by the salesman in each region

| Date      | OrderID | Product   | Salesman | Region | No of customers | Net sales | Profit/Loss |
| --------- | ------- | --------- | -------- | ------ | --------------- | --------- | ----------- |
| 01-Jan-23 | 1112    | Product1  | Arjun    | North  | 8               | 7,164     | 844         |
| 02-Jan-23 | 1113    | Product2  | Arjun    | North  | 12              | 6,528     | 3,376       |
| 03-Jan-23 | 1114    | Product3  | Arjun    | North  | 24              | 2,520     | 2,280       |
| 04-Jan-23 | 1115    | Product4  | Arjun    | South  | 15              | 9,660     | 1,737       |
| 05-Jan-23 | 1116    | Product5  | Arjun    | South  | 3               | 11,550    | 854         |
| 06-Jan-23 | 1117    | Product6  | Arjun    | South  | 2               | 7,896     | 2,565       |
| 07-Jan-23 | 1118    | Product7  | Arjun    | South  | 16              | 8,095     | 1,063       |
| 08-Jan-23 | 1119    | Product8  | Arjun    | South  | 22              | 12,180    | 1,864       |
| 09-Jan-23 | 1120    | Product9  | Arjun    | South  | 44              | 4,900     | 2,653       |
| 10-Jan-23 | 1121    | Product10 | Arjun    | South  | 12              | 2,277     | 1,931       |
| 11-Jan-23 | 1122    | Product11 | Arjun    | West   | 11              | 3,122     | 994         |
| 12-Jan-23 | 1123    | Product12 | Arjun    | West   | 6               | 8,046     | 4,092       |
| 13-Jan-23 | 1124    | Product13 | Arjun    | West   | 1               | 4,230     | 1,900       |
| 14-Jan-23 | 1125    | Product14 | Arjun    | West   | 4               | 11,250    | 882         |

Analyzing this manually would be time consuming and diffcult as the data for each region appears on the multiple rows and we need a total of all different orders individually here, pivot table comes into play and becomes a life saver

This feature allows us to calculate and summarize the data instantly, which is both easy to read and manipulate. Once we've created a pivot table, we can quickly pivot or reorganized the data to answer different questions

CREATING THE PIVOT TABLE

To create a pivot table in excel, select the cells containing the data we want to use.

Then click the insert tab and select the pivot table after dialog box appears with the option to create pivot table.

Under table range,reference box excel automatically selects the data range that we want use to create pivot table.There is also an option asking for the placement of the pivot table.This feature allows us to decide whether we would like to place the pivot table in a new worksheet or at a particular locations in the worksheet.

After selecting our required option, Excel creates a blank pivot table and a pivot table fields on the box of right side of the worksheet.The pivot table field list box contains two sections, namely field section and area section.

* Field section - Allows to pick the fields required to create a pivot table
* Area section - Allows to arrange the fields that way we want it to be displayed in the pivot table

Now let's create a pivot table to determine the region wise, net sales within the pivot table, field list tasks pane first drag the salesman field into area marked rows then drag the region field into area marked columns.Lastly, drag the net sales field into the area marked as calculated values

Here we see pivot table is populated with the net sales done by the salesman in each region.

| Sum of Net sales | Column Labels |       |       |             |
| ---------------- | ------------- | ----- | ----- | ----------- |
| Row Labels       | North         | South | West  | Grand Total |
| Arjun            | 16212         | 56558 | 26648 | 99418       |
| Grand Total      | 16212         | 56558 | 26648 | 99418       |

Like any normal spreadsheet, any type of number formatting can be applied.Now, if we would like to see the total number of sales instead of the net sales then we should change the sum of sales function to the count of total number of sales to change this function Right-Click the value field and click the value field setting with summarize and in summarize values field by dialog box and select the count function and click OK.By using this function we can easily determine total number of saled done by each person

| Count of Net sales | Column Labels |       |      |             |
| ------------------ | ------------- | ----- | ---- | ----------- |
| Row Labels         | North         | South | West | Grand Total |
| Arjun              | 3             | 7     | 4    | 14          |
| Grand Total        | 3             | 7     | 4    | 14          |

GROUPING IN PIVOT TABLE

It is often useful to group the fields in the pivot table by the header values.

Grouping in the pivot table allows us to group the data for any field added as row or column and perform this automatically for numeric values, including dates and time

## BUSINEES ANALYTICS WITH EXCEL

## DATA ANALYSIS USING STATISTICS

## USING MACROS FOR ANALYTICS
