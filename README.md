# Smart Analytics Tool

## Project Overview

The Smart Analytics Tool is an interactive data analysis application developed using Python, Streamlit, Pandas, NumPy, and Plotly. It enables users to upload CSV datasets and perform essential data analysis tasks through a user-friendly interface.

The application helps users explore datasets, identify missing values, generate statistical summaries, analyze correlations, and create dynamic visualizations without writing additional code.

## Features

### CSV Upload Feature

* Upload any CSV dataset for analysis.

### Dataset Preview

* View the first five rows of the dataset.
* View the last five rows of the dataset.

### Dataset Information

* Number of rows and columns.
* Column names (features).
* Data types of all columns.

### Missing Value Analysis

* Identify missing values in each column.
* Visualize missing values using an interactive bar chart.

### Statistical Summary

* Generate descriptive statistics automatically.
* Display count, mean, standard deviation, minimum, maximum, and quartile values.

### Correlation Matrix

* Analyze relationships between numerical features.
* Visualize correlations using an interactive heatmap.

### Dynamic Visualizations

Users can interactively select columns and generate:

* Histogram
* Box Plot
* Scatter Plot

## Technologies Used

* Python
* Streamlit
* Pandas
* NumPy
* Plotly Express

## Dataset

This application supports any CSV dataset uploaded by the user.

For testing and demonstration purposes, the Titanic Dataset was used.

Dataset Link:

https://raw.githubusercontent.com/datasciencedojo/datasets/master/titanic.csv

## Project Structure

```text
Smart-Analytics-Tool/
│
├── app.py
├── smart_analytics_tool.ipynb
├── README.md
├── requirements.txt
├── dataset_link.txt
└── output_screenshots/
```

## How to Run the Project

### Step 1: Clone the Repository

```bash
git clone <repository-link>
```

### Step 2: Navigate to the Project Folder

```bash
cd Smart-Analytics-Tool
```

### Step 3: Install Required Libraries

```bash
pip install -r requirements.txt
```

### Step 4: Run the Application

```bash
streamlit run app.py
```

### Step 5: Open the Application

The application will automatically open in your browser.

Upload a CSV file and begin exploring the dataset.

## Screenshots

Screenshots demonstrating the functionality of the application are available in the screenshots folder.

Included Screenshots:

* Dataset Preview
* Missing Value Analysis
* Statistical Summary
* Correlation Matrix
* Histogram
* Box Plot
* Scatter Plot

## Learning Outcomes

This project helped in understanding and applying:

* Data Cleaning and Preparation
* Exploratory Data Analysis (EDA)
* Missing Value Analysis
* Statistical Analysis
* Correlation Analysis
* Data Visualization
* Interactive Application Development using Streamlit

## Conclusion

The Smart Analytics Tool provides a simple and effective platform for dataset analysis. By combining data exploration, statistical analysis, correlation analysis, and interactive visualizations, the application enables users to gain meaningful insights from datasets quickly and efficiently.
