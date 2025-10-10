# Python & SQL Store Analysis Project

## 1. Project Overview

This project involves the development and analysis of a relational database for a simulated online store. The primary goal is to extract actionable business intelligence from sales data. The process includes:
- Designing a relational schema in PostgreSQL.
- Populating the database using a Python script with synthetic data.
- Connecting to the database from a Jupyter Notebook.
- Performing an in-depth analysis to identify KPIs, uncover insights, and formulate strategic business narratives (storylines).

---

## 2. Tech Stack

- **Language:** Python 3
- **Database:** PostgreSQL
- **Python Libraries:** `psycopg2`, `pandas`, `Faker`, `matplotlib`, `seaborn`, `python-dotenv`

---

## 3. Setup and Execution

To replicate this project, follow these steps:

### a. Prerequisites

- Python 3.8+
- PostgreSQL server installed and running.

### b. Clone the Repository

```bash
git clone https://github.com/Elimge/python-sql-store-analysis.git
cd python-sql-store-analysis
```

### c. Setup Environment

1.  **Create and activate a virtual environment:**
    ```bash
    # For macOS/Linux
    python3 -m venv .venv
    source .venv/bin/activate

    # For Windows
    python -m venv .venv
    .venv\Scripts\activate
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Configure Environment Variables:**
    Create a `.env` file in the project root by copying the example file:
    ```bash
    cp .env.example .env
    ```
    Now, edit the `.env` file with your actual PostgreSQL credentials.

### d. Database Initialization

1.  **Create the Database:** In PostgreSQL, create a new database (e.g., `store_db`).

2.  **Create the Schema:** Execute the SQL script to create the tables. You can do this via Navicat or `psql`:
    ```bash
    psql -d your_db_name -U your_user -f sql/schema.sql
    ```

3.  **Populate the Database:** Run the population script from the project's root directory:
    ```bash
    python -m scripts.populate_db
    ```

---

## 4. Project Structure

The repository is organized as follows:
```bash
python-sql-store-analysis/
│
├── .env.example # Example environment variables file
├── .gitignore # Files and folders to be ignored by Git
├── README.md # This documentation file
├── requirements.txt # Python dependencies for the project
│
├── notebooks/
│ └── data_analysis.ipynb # Jupyter Notebook with the detailed data analysis
│
├── scripts/
│ ├── init.py
│ └── populate_db.py # Python script to populate the database with synthetic data
│
├── sql/
│ └── schema.sql # SQL script to define the database schema (tables, relations)
│
└── utils/
├── init.py
└── db_connector.py # Reusable utility to handle database connections
```

---

## 5. Analysis Summary & Business Storylines

The full, detailed analysis can be found in the [Jupyter Notebook](./notebooks/data_analysis.ipynb). The following is a high-level summary of the findings.

### a. Key Performance Indicators (KPIs)

- **Total Revenue:** $109,160.73
- **Average Order Value (AOV):** $545.80
- **Top Product by Revenue:** Portable Laptop Stand  

### b. Storylines & Strategic Recommendations

Based on the analysis, two primary strategic narratives emerged:

#### Storyline 1: The Dual Growth Engine — Amplifying our VIPs and Star Products

**The Narrative:** Our business is healthy, with consistent monthly growth. This success is built on two pillars: a small group of high-value VIP customers who dramatically outperform others, and a smart product catalog with both high-volume "traffic drivers" and high-profit "crown jewels".

**Actionable Recommendations:**
1.  **Launch a VIP Loyalty Program:** Retain our top spenders with exclusive offers.
2.  **Implement Smart Cross-selling:** Use our popular, high-volume products as a gateway to promote our high-margin items to a wider audience.

#### Storyline 2: The Hidden Opportunity — Increasing the Value of Every Visit

**The Narrative:** While overall revenue is growing, we are consistently leaving money on the table. The vast majority of our orders are for single items, even when strong data shows customers have an interest in complementary products.

**Actionable Recommendations:**
1.  **Create Product Bundles:** Launch a "Work From Home Essentials" kit (e.g., Keyboard + Mouse) at a slight discount to encourage larger purchases.
2.  **Deploy a Recommendation System:** Add a "Customers also bought..." feature to product pages to increase cart size and overall Average Order Value (AOV).