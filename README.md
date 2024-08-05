# Crime Data Generation and Power BI Dashboard Project

This project generates synthetic crime data for India and provides instructions for creating a Power BI dashboard using the generated data.<br>
**Project Structure**
```

crime-data-project/
│
├── data/
│   ├── crime_data_india.csv    # The generated dataset
│
├── notebooks/
│   ├── crime_data_generation.ipynb       # The Jupyter notebook
│
├── scripts/
│   ├── generate_crime_data.py            # Python script for data generation
│
├── README.md                             # Project overview and instructions
├── LICENSE                               # License for your project
└── .gitignore                            # Ignore unnecessary files


```
## Getting Started

### Prerequisites

- Python 3.x
- Jupyter Notebook
- Power BI Desktop

### Installation

1. **Clone the repository:**
   ```bash
   git clone https://github.com/yourusername/crime-data-project.git
   cd crime-data-project
   
2. **Create and activate a virtual environment:**

```bash
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate
```
3. **Install the required packages:**


```pip install pandas numpy faker
Generating Data
Using the Jupyter Notebook
Run the Jupyter notebook:
jupyter notebook notebooks/crime_data_generation.ipynb
Execute the cells in the notebook to generate the synthetic data.
```

4.**Using the Python Script**
```
Run the Python script:
python scripts/generate_crime_data.py
```
5.**Power BI Dashboard Instructions**
```Open Power BI Desktop.

Load the data/crime_data_india.csv file into Power BI.

Create visualizations based on the columns in the dataset:

Total Number of Incidents: Use a card visualization to show the total number of incidents.
Incidents by Month: Use a line chart to show the number of incidents per month.
Incidents by Area: Use a bar chart to show the number of incidents per area.
Incidents by Crime Category: Use a pie chart to show the distribution of crime categories.
Incidents by Time of Day: Use a bar chart to show the number of incidents during different times of the day.
Arrests Made: Use a card visualization to show the total number of arrests.
Outcome of Incidents: Use a bar chart to show the outcomes of the incidents.
```
