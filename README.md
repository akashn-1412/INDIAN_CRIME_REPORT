**🚔 Crime Data Generation and Power BI Dashboard Project 🚔**<br>
-
**Overview**<br>
This project aims to generate synthetic crime data for India and provides a detailed guide for creating a Power BI dashboard using the generated data. By leveraging Python and Power BI, this project facilitates comprehensive data generation, analysis, and visualization, offering valuable insights into crime patterns and statistics.

Features
-
**🛠 Data Generation:**
Generate synthetic crime data using the generate_crime_data.py script or the Jupyter notebook crime_data_generation.ipynb.<br>
**📊 Data Analysis:**
Analyze the generated data with the crime_data_generation.ipynb notebook.<br>
**📈 Data Visualization:**
Visualize insights using Power BI with the crime_data_india.csv file.<br>

**📁 Project Structure**
-
```crime-data-project/
│
├── data/
│   ├── crime_data_india.csv           # The generated dataset
│
├── notebooks/
│   ├── crime_data_generation.ipynb    # The Jupyter notebook
│
├── scripts/
│   ├── generate_crime_data.py         # Python script for data generation
│
├── requirements.txt                   # This file lists the Python packages required for the project
|
└── README.md                          # Project overview and instructions
```

🚀 Getting Started
-
🔧 Prerequisites
-
**+Python 3.x**

**+Jupyter Notebook**

**+Power BI Desktop**

💻 Installation
-
**1.Clone the repository:**
```
git clone https://github.com/yourusername/crime-data-project.git
cd crime-data-project
```
**2.Create and activate a virtual environment:**

```
python -m venv venv
source venv/bin/activate   # On Windows, use `venv\Scripts\activate`
```
**3.Install the required packages:**
```
pip install -r requirements.txt
```
🔍 Generating Data
-
**1️⃣ Using the Jupyter Notebook**
Run the Jupyter notebook:

```
jupyter notebook notebooks/crime_data_generation.ipynb
```
Execute the cells in the notebook to generate the synthetic data.

**2️⃣ Using the Python Script**
Run the Python script:
```
python scripts/generate_crime_data.py
```
📊 Power BI Dashboard Instructions
-
1.Load the data/crime_data_india.csv file into Power BI.

2.Create visualizations based on the columns in the dataset:

🔢 Total Number of Incidents: Use a card visualization to show the total number of incidents.<BR>
📈 Incidents by Month: Use a line chart to show the number of incidents per month.<BR>
📊 Incidents by Area: Use a bar chart to show the number of incidents per area.<BR>
🕵️ Incidents by Crime Category: Use a pie chart to show the distribution of crime categories.<BR>
🕒 Incidents by Time of Day: Use a bar chart to show the number of incidents during different times of the day.<BR>
👮 Arrests Made: Use a card visualization to show the total number of arrests.<BR>
📋 Outcome of Incidents: Use a bar chart to show the outcomes of the incidents.<BR>

🖼️ Image Gallery
-
Here are the categorized images representing different aspects of the crime data:

**1.CRIME_REPORT**

![CRIME_REPORT](https://github.com/user-attachments/assets/01d9e4b7-4ac8-4697-ab2b-a08c6b9dbe7e)


**2.CLOSED_CRIME_REPORT**

![CLOSED_CRIME_REPORT](https://github.com/user-attachments/assets/451a42a2-a19a-4f4e-92d1-cdfc45550525)


**3.OPEN_CRIME_REPORT**

![OPEN_CRIME_REPORT](https://github.com/user-attachments/assets/5a1ac758-91dd-4d12-8894-8306ae5100d6)


**4.SOLVED_CRIME_REPORT**

![SOLVED_CRIME_REPORT](https://github.com/user-attachments/assets/3b90646a-35f9-4bb5-8368-356fd070b70b)


**5.UNDER_INVESTIGATION_CRIME_REPORT**

![UNDER_INVESTIGATION_CRIME_REPORT](https://github.com/user-attachments/assets/c64b0873-4693-474d-9ebc-b0906653e57f)

## 📬 Contact

For questions or feedback, reach out to [Akash Nishad](mailto:akashn1412@gmail.com). You can also connect via [LinkedIn](https://www.linkedin.com/in/your-linkedin-profile) and [GitHub](https://github.com/your-github-profile).
