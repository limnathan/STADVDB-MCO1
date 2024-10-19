import matplotlib.pyplot as plt
import io
import base64
import pandas as pd
from sqlalchemy import text
from .models import db

def get_overview():
    overview_query = db.session.execute(text(""" 
        SELECT 
            COUNT(DISTINCT AppID) AS TotalGames,
            AVG(Price) AS AveragePrice,
            SUM(Recommendations) AS TotalRecommendations,
            SUM(estimated_owners) AS TotalOwners      
        FROM Fact_SteamGames
    """))
    
    return overview_query.fetchone()

def get_top_developers(org_type, top_n):
    if org_type not in ['developers', 'publishers']:
        raise ValueError("org_type must be either 'developers' or 'publishers'")

    query = text(f"""
        SELECT o.{org_type} AS Name, SUM(f.Positive) AS Positive
        FROM Fact_steamGames f
        JOIN Dim_Organization o ON f.AppID = o.AppID
        WHERE o.{org_type} IS NOT NULL
        GROUP BY o.{org_type}
        ORDER BY Positive DESC
        LIMIT :top_n
    """)

    result = db.session.execute(query, {'top_n': int(top_n)})
    
    df = pd.DataFrame(result.fetchall(), columns=['Name', 'Positive'])
    
    if df.empty:
        print("No data found for the specified criteria.")
        return None  

    return df

def get_total(group_by_column, aggregation_column, dim_table):
    query = text(f"""
        SELECT 
            dga.{group_by_column},
            SUM(fg.{aggregation_column}) AS Total
        FROM 
            Fact_steamGames fg
        JOIN 
            {dim_table} dga ON fg.AppID = dga.AppID
        GROUP BY 
            dga.{group_by_column} WITH ROLLUP
    """)
    
    result = db.session.execute(query)
    return result.fetchall()
