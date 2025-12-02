"# Food Price Inflation Analysis

## Project Overview

This project analyzes global food price inflation trends using comprehensive data from multiple countries and time periods. The analysis explores temporal patterns, regional variations, and key insights that can inform policy decisions and economic understanding.

## Dataset

The dataset `food_price_inflation.csv` contains food price inflation data with the following structure:
- **REF_AREA**: Country code
- **REF_AREA_LABEL**: Country name
- **TIME_PERIOD**: Date of observation
- **OBS_VALUE**: Inflation rate value

The dataset contains 59,841 observations spanning multiple years and countries.

## Project Structure

```
Food Price Inflation Analysis/
│
├── data/
│   ├── food_price_inflation.csv          # Original dataset
│   └── clean_food_price_inflation.csv    # Cleaned dataset (generated)
│
├── notebooks/
│   └── food_price_analysis.ipynb         # Main analysis notebook
│
├── scripts/
│   └── data_cleaning.py                  # Data cleaning script
│
├── requirements.txt                       # Python dependencies
└── README.md                             # Project documentation
```

## Installation & Setup

### 1. Clone the Repository

```bash
git clone https://github.com/Nethmini-jayasekara/Food-Price-Inflation-Analysis.git
cd "Food Price Inflation Analysis"
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Run Data Cleaning Script

```bash
cd scripts
python data_cleaning.py
```

This will generate a cleaned dataset in the `data/` folder.

### 4. Open and Run the Jupyter Notebook

```bash
cd notebooks
jupyter notebook food_price_analysis.ipynb
```

## Visualizations Included

The analysis notebook includes the following visualizations:

1. **Line Chart**: Average food price inflation over time - showing temporal trends
2. **Bar Chart**: Top 10 countries by average inflation - highlighting regional disparities
3. **Histogram**: Distribution of inflation values - understanding data spread
4. **Line Chart**: Yearly trend analysis - identifying long-term patterns

## Key Insights

- Significant temporal variations in food price inflation across different periods
- Regional disparities with certain countries experiencing persistently higher inflation
- Identifiable patterns that correlate with global economic events
- Data-driven insights to inform food security policies

## Technologies Used

- **Python 3.x**
- **Pandas**: Data manipulation and analysis
- **NumPy**: Numerical computations
- **Matplotlib**: Data visualization
- **Seaborn**: Statistical data visualization
- **Jupyter Notebook**: Interactive analysis environment

## Future Work

- Incorporate economic indicators for correlation analysis
- Develop predictive models for inflation forecasting
- Analyze seasonal patterns in food prices
- Compare with other economic datasets

## Author

**Nethmini Jayasekara**

## License

This project is open source and available for educational and research purposes." 
