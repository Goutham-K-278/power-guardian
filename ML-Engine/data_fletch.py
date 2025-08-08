import psycopg2
import pandas as pd

def fetch_data():
    conn = psycopg2.connect(
        host="localhost",
        database="power_guardian",
        user="postgres",
        password="yourpassword"
    )
    query = "SELECT voltage, current, frequency, location, faults FROM sensor_data"
    df = pd.read_sql(query, conn)
    conn.close()
    return df

if __name__ == "__main__":
    data = fetch_data()
    print(data.head())
