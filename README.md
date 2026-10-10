# Vendor Performance & Profitability Analysis

A data analytics project exploring retail purchasing, sales, vendor profitability, and inventory performance to uncover business insights and support smarter procurement decisions.

##  Overview

Understanding vendor performance is important for controlling purchasing costs, improving profitability, and managing inventory effectively.

In this project, I worked with retail sales, purchase, inventory, and vendor invoice data to examine purchasing patterns and evaluate vendor-level performance. I used Python for data processing, SQL for data aggregation and analysis, and Power BI as part of the business intelligence workflow.

The project demonstrates how multiple datasets can be transformed into meaningful metrics and actionable business insights.

##  Project Objectives

- Assess vendor contributions to overall procurement.
- Examine purchasing costs and potential bulk-order savings.
- Analyze profitability across vendors and products.
- Investigate inventory that remains unsold.
- Identify opportunities to improve purchasing and inventory decisions.

##  Technology Stack

| Technology | Application |
|---|---|
| Python | Data ingestion and processing |
| Pandas & NumPy | Data manipulation and numerical analysis |
| SQL | Data joins, aggregations, and metric calculations |
| SQLite | Local database management |
| Jupyter Notebook | Analysis and exploration |
| Matplotlib & Seaborn | Data visualization |
| Power BI | Business intelligence and reporting |

##  Repository Contents

- `ingestion_db.py` — Script for loading source datasets into a database.
- `get_vendor_summary.py` — Script for preparing a consolidated vendor summary.
- `Exploratory Data Analysis .ipynb` — Notebook for exploring data patterns and distributions.
- `Vendor Performance Analysis.ipynb` — Notebook for vendor performance and profitability analysis.
- `begin_inventory.csv` — Beginning inventory dataset.
- `end_inventory.csv` — Ending inventory dataset.
- `purchase_prices.csv` — Product purchase prices.
- `vendor_invoice.csv` — Vendor invoice data.
- `vendor_sales_summary.csv` — Vendor-level sales summary.

The large `sales.csv` and `purchases.csv` files are excluded from this repository because of their size. They are required separately to reproduce the complete workflow.

##  Analytical Workflow

**1. Data Ingestion**

Used Python scripts to bring multiple retail datasets into a structured SQLite database.

**2. Data Integration**

Combined relevant purchasing, sales, inventory, and vendor information for analysis.

**3. Data Exploration**

Examined distributions, purchasing patterns, profitability metrics, and inventory performance using Jupyter Notebook.

**4. Vendor Performance Analysis**

Evaluated vendor-level metrics to understand purchasing concentration, cost efficiency, and profitability.

**5. Business Interpretation**

Connected the analytical findings with potential improvements in supplier management, procurement, and inventory control.

##  Key Findings

The project analysis highlighted three notable observations:

- **Procurement concentration:** The leading vendors represented approximately 65.69% of total procurement, indicating potential supplier concentration risk.
- **Purchase-volume relationship:** Larger purchase volumes were associated with approximately 72% lower unit purchase costs in the analyzed data.
- **Unsold inventory:** Approximately $2.7 million in inventory was identified as unsold, highlighting an opportunity to review stock management practices.

These observations illustrate how retail data can help identify cost efficiencies and areas that deserve further investigation.

*The reported figures should be checked against the final analysis outputs before publication.*

##  Business Value

The findings can help retail businesses:

- Review their dependence on major suppliers.
- Assess whether bulk purchasing offers cost advantages.
- Investigate unsold stock and improve inventory planning.
- Monitor vendor performance using consistent KPIs.
- Make more informed purchasing and pricing decisions.

##  Running the Project

### Requirements

- Python 3.x
- Jupyter Notebook
- SQLite
- Python libraries used in the project

### Setup

Clone the repository:

```bash
git clone https://github.com/pratikshaaher674/Vendor-Performance-Analysis.git
cd Vendor-Performance-Analysis
```

Install commonly used libraries:

```bash
pip install pandas numpy sqlalchemy matplotlib seaborn scipy jupyter
```

Make sure the required source datasets are available locally. The large `sales.csv` and `purchases.csv` files are not included in the repository.

Run the ingestion script:

```bash
python ingestion_db.py
```

Generate the vendor summary:

```bash
python get_vendor_summary.py
```

Launch Jupyter Notebook:

```bash
jupyter notebook
```

Open the project notebooks to explore the analysis and findings.

*Depending on your environment, you may need to adjust file paths or install additional dependencies used by the scripts.*

##  About Me

**Pratiksha Aher**

Data Analyst 

**Skills:** Python | SQL | Excel | Power BI | Pandas | NumPy

[Connect with me on GitHub](https://github.com/pratikshaaher674)
