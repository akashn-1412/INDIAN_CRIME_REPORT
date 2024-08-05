import pandas as pd
import numpy as np
from faker import Faker
import random
from datetime import datetime, timedelta

# Initialize Faker and other parameters
fake = Faker('en_IN')
Faker.seed(0)
np.random.seed(0)
random.seed(0)

# Define some constants
areas = ["Mumbai", "Delhi", "Bangalore", "Hyderabad", "Chennai", "Kolkata"]
crime_categories = ["Violent Crime", "Property Crime", "Drug Offense", "Cyber Crime", "White Collar Crime"]
premises_desc = ["Residential", "Commercial", "Public", "Industrial"]
weapon_desc = ["None", "Firearm", "Knife", "Blunt Object", "Other"]
status_desc = ["Open", "Closed", "Under Investigation", "Solved"]
districts = ["North", "South", "East", "West", "Central"]

# List of realistic victim injuries
injury_descriptions = [
    "Minor cuts and bruises",
    "Broken bones",
    "Head injury",
    "Severe lacerations",
    "Fractures",
    "Internal injuries",
    "Gunshot wound",
    "Stab wound",
    "No visible injuries"
]

# Function to determine if charges are filed based on crime category and arrest status
def should_file_charge(crime_category, arrest_made):
    # For simplicity, assume charges are more likely to be filed if an arrest was made
    if arrest_made == "Yes":
        return random.choices(["Yes", "No"], weights=[0.8, 0.2])[0]
    else:
        return "No"

# Function to generate synthetic data
def generate_crime_data(num_records):
    data = []
    
    for incident_id in range(1, num_records + 1):
        incident_date = fake.date_this_decade()
        incident_time = fake.time(pattern="%H:%M:%S")
        day_of_week = incident_date.strftime("%A")
        month = incident_date.strftime("%B")
        year = incident_date.year
        time_of_day = "Morning" if int(incident_time.split(":")[0]) < 12 else "Afternoon" if int(incident_time.split(":")[0]) < 18 else "Evening"
        daytime_weekday = "Daytime" if int(incident_time.split(":")[0]) < 18 else "Night"
        weekday_or_weekend = "Weekend" if incident_date.weekday() >= 5 else "Weekday"
        crime_category = random.choice(crime_categories)
        repeat_offender = random.choice(["Yes", "No"])
        crime_location_type = random.choice(premises_desc)
        suspect_age = np.random.randint(18, 65)
        suspect_sex = random.choice(["Male", "Female"])
        suspect_descent = random.choice(["Indian", "Other"])
        arrest_made = random.choice(["Yes", "No"])
        charge_filed = should_file_charge(crime_category, arrest_made)
        outcome = random.choice(status_desc)
        victim_injury = random.choice(injury_descriptions) if random.choice([True, False]) else "None"
        victim_status = random.choice(["Alive", "Deceased"])
        time_to_resolution = np.random.randint(1, 365)  # in days
        district = random.choice(districts)

        data.append({
            "Incident ID": incident_id,
            "Incident Date": incident_date,
            "Incident Time": incident_time,
            "Day of Week": day_of_week,
            "Month": month,
            "Year": year,
            "Time of Day": time_of_day,
            "Daytime/Weekend/Weekday": daytime_weekday,
            "Crime Category": crime_category,
            "Repeat Offender": repeat_offender,
            "Crime Location Type": crime_location_type,
            "Suspect Age": suspect_age,
            "Suspect Sex": suspect_sex,
            "Suspect Descent": suspect_descent,
            "Arrest Made": arrest_made,
            "Charge Filed": charge_filed,
            "Outcome": outcome,
            "Victim Injury": victim_injury,
            "Victim Status": victim_status,
            "Time to Resolution": time_to_resolution,
            "District": district,
            "Latitude": fake.latitude(),
            "Longitude": fake.longitude(),
            "Crime Severity": random.choice(["Minor", "Moderate", "Severe"]),
            "Repeat Victim": random.choice(["Yes", "No"]),
            "Victim Occupation": fake.job(),
            "Suspect Occupation": fake.job()
        })
    
    df = pd.DataFrame(data)
    
    # Data Quality: Drop duplicates and fill missing values
    df = df.drop_duplicates()
    df = df.fillna("Unknown")
    
    # Data Consistency: Ensure consistent categorical data
    df['Crime Category'] = df['Crime Category'].str.title()
    df['Outcome'] = df['Outcome'].str.title()
    
    return df

# Generate the data
num_records = 1000  # Number of synthetic records you want to generate
crime_data_df = generate_crime_data(num_records)

# Save to CSV
crime_data_df.to_csv('synthetic_crime_data_india.csv', index=False)

print(f"Generated {num_records} records and saved to 'synthetic_crime_data_india.csv'")
