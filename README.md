# Applied Exploratory Data Analysis and Visualizations

A collection of data analysis projects exploring real-world datasets through statistical analysis and data visualization techniques.

## Cases:

### 1. COVID-19 Economic Impact Analysis
Analyzing the economic effects of the COVID-19 pandemic on global and Indian markets using multiple economic indicators.

**Analytics:**
- Global economic metrics comparison across countries
- India-specific economic trend analysis
- Time-series visualization of GDP, unemployment, and trade impacts
- Statistical correlation analysis between COVID-19 metrics and economic indicators

**Technologies:** Python, Pandas, NumPy, Matplotlib, Seaborn

---

### 2. Steam Video Game Sales & Reviews Analysis
Comprehensive exploratory analysis of 70,000+ video games on Steam platform, examining pricing trends, user sentiment, and market dynamics.

**Analytics:**
- Genre performance and market share analysis
- Publisher sentiment trends and comparison
- Pricing evolution across decades (2000-2025)
- Metacritic vs. user review correlation
- Multi-platform support impact on user satisfaction
- DLC strategy effectiveness analysis

**Technologies:** Python, Pandas, NumPy, Matplotlib, Seaborn, Statistical Analysis

---

### 3. Stock Market Analysis
This project is an end-to-end quantitative Exploratory Data Analysis (EDA) pipeline that analyzes the decoupling, historical risk, and comparative volatility between US large-cap equities (S&P 500) and Indian large-cap equities (NIFTY 50). 
The pipeline automatically ingests 5 years of historical data, handles complex cross-border timezone alignments, normalizes currencies via daily USD/INR exchange rates, and calculates institutional-grade risk metrics.

**Technical Architecture & Pipeline:**
The project is broken down into 5 distinct phases:
1. **Automated Ingestion & Wrangling:** Pulled daily Adjusted Close prices via the Yahoo Finance API, utilizing forward-filling (`ffill`) to align non-overlapping market holidays between the NYSE/NASDAQ and the NSE.
2. **Currency Normalization:** Converted Indian Rupee (INR) asset pricing to USD dynamically using historical daily exchange rates to ensure mathematically sound comparative analysis.
3. **Feature Engineering:** Calculated daily logarithmic returns ($R_t = \ln(\frac{P_t}{P_{t-1}})$) and 30-day rolling annualized volatility.
4. **Institutional Risk Metrics:** Programmatically calculated 95% Historical Value at Risk(VaR), the Sharpe Ratio($S = \frac{R_p - R_f}{\sigma_p}$) and Maximum Drawdown(MDD).
5. **Interactive Dashboarding:** Built a local Dash web application for interactive time-series analysis using Plotly Express and exported cleaned datasets to CSV for Tableau Business Intelligence visualization.

#### Key Visualizations
1. Cross-Market Correlation 
Visualizing how closely correlated Indian IT/Energy sectors are with US Tech during macroeconomic shocks.

2. Risk vs. Reward (Efficient Frontier)

**Technologies:** Python, Pandas, NumPy, Matplotlib, Seaborn, yfinance api, plotly express

## Technologies Used for EDA:
- **Python 3.10** - Core programming language
- **Pandas** - Data manipulation and analysis
- **NumPy** - Numerical computing
- **Matplotlib & Seaborn** - Data visualization

## Project Structure:
```
EDA-Case-Studies/
├── COVID-19 Economy Analysis/
│   ├── analysis-GLOBAL.ipynb
│   ├── analysis-INDIA.ipynb
│   └── datasets/
├── Video Game Sales & Reviews Analysis/
│   ├── analysis.ipynb
│   ├── figures/
│   └── datasets/
├── Stock Market Analysis/
│   ├── analysis.ipynb
│   ├── figures/
│   └── datasets/
└── README.md
```

## Getting Started:

1. Clone the repository:
   ```bash
   git clone https://github.com/Mahanidhii/EDA-Case-Studies.git
   ```

2. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

3. Open Jupyter notebooks and run cells sequentially.

## Visualizations:
Each project includes visualizations with:
- Multi-panel comparative analysis
- Trend lines and statistical annotations
- Color-coded insights for clarity
- Publication-quality figures (300 DPI)
---

*Last Updated: March 2026*