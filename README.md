# Animated Food Sales Analytics Dashboard

## Project Overview

Welcome to the **Animated Food Sales Analytics Dashboard** — a business-ready, interactive, and dynamic data visualization solution for food sales management and executive teams. Developed using Python, Dash, and Plotly Express, this project transforms raw sales data into actionable insights, empowering decision-makers to quickly spot trends, outliers, and growth opportunities.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Data Structure](#data-structure)
- [Installation Guide](#installation-guide)
- [Usage](#usage)
- [Dashboard Walkthrough](#dashboard-walkthrough)
    - [1. Animated Sales by Region](#1-animated-sales-by-region)
    - [2. Animated Sales by Category](#2-animated-sales-by-category)
    - [3. Animated Top 10 Products](#3-animated-top-10-products)
- [Downloadable Data](#downloadable-data)
- [Technical Stack](#technical-stack)
- [Customization Tips](#customization-tips)
- [License](#license)
- [Acknowledgments](#acknowledgments)

---

## Features

- **Fully Interactive Dashboard**: Intuitive tabbed interface with point-and-click filters.
- **Animated Visualizations**: Animated bar charts for region, category, and top products — highlighting trends over time.
- **Executive-Grade Styling**: Clear color palettes, value-labels, professional layouts.
- **Date Range Filtering**: Focus analysis on any specified period.
- **Top Products Analyzer**: Track the evolving sales leadership of products every month.
- **CSV Download**: Export top product performance for offline or ad-hoc executive use.
- **Cross-Browser & Mobile-Friendly**: Dash ensures accessibility everywhere.

---

## Data Structure

The dashboard expects an Excel file named `sampledatafoodsales.xlsx` with at least these columns:

| Column      | Description                        |
|-------------|------------------------------------|
| Date        | Date of sale (YYYY-MM-DD format)   |
| Region      | Sales region (e.g., East, West)    |
| Category    | Product category (e.g., Cookie)    |
| Product     | Product name (e.g., Oatmeal Raisin)|
| TotalPrice  | Total price for the line item      |

**Tip:** Month is automatically derived for animation.

---

## Installation Guide

1. **Clone or Download the Repository**
2. **Install Required Packages**:
3. **Place your sales Excel file** in the root or adjust the path in the code.

---

## Usage

1. **Run the Application**
2. **Open the browser** at the address given in the terminal (typically [http://127.0.0.1:8050/](http://127.0.0.1:8050/)).

3. **Interact!**
- Select date ranges.
- Filter categories or products.
- Watch animated trends play automatically or step through months.
- Download top product sales as a CSV for your period of interest.

---

## Dashboard Walkthrough

### 1. Animated Sales by Region

- Presents a bar chart of sales totals by region, _animated over each month_ in the data.
- **What you’ll see:** How each region’s performance rises or falls, surfacing seasonal surges, slowdowns, or market shifts.
- **Styling:** Plasma color scheme, bold axis titles, automatic value labels.

### 2. Animated Sales by Category

- Animated monthly breakdown of sales by each product category.
- **Why it matters:** Quickly clarifies which categories surge in different seasons, and identifies long-term winners or declining segments.

### 3. Animated Top 10 Products

- Reveals the ten best-selling products each month, with an **animated horizontal bar race** showing changes in real time.
- **Perfect for:** Spotting product launches, trend reversals, or steady leaders.

---

## Downloadable Data

- Click the **“Download Current View (CSV)”** button in the “Animated Top 10 Products” tab to get performance data for further ad-hoc analysis or integration in management reports.

---

## Technical Stack

- **Python**: Core scripting and data transformation
- **Pandas**: Data wrangling and aggregation
- **Dash**: Web application and dashboard framework[1]
- **Plotly Express**: Animated and interactive charting[2]
- **Openpyxl**: Excel file reading

---

## Customization Tips

- **City/Store-Level Analysis:** Add more granular columns to the data and replicate animation logic for deeper drilldowns.
- **Automated Reporting:** Integrate with scheduling tools for monthly/quarterly report exports.
- **Theming:** Change palette or branding using Plotly and Dash’s style parameters.
- **Role-Based Views:** Easily extend tabs or filter logic for different user roles (sales, marketing, operations).

---

## License

This project is released under the MIT License.

---

## Acknowledgments

Developed by the Data Analytics Team for real-time management insight. Special thanks to contributors in web development[1] and data visualization[2] for ensuring the solution is both actionable and visually engaging.

---

*For further questions, suggestions, or to contribute, please open an Issue or Pull Request!*


