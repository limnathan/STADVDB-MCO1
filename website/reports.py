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

def get_top(group_by_col, aggregation_col, dim_table):

    query = text(f"""
        SELECT o.{group_by_col} AS Name, SUM(f.{aggregation_col}) AS Top
        FROM Fact_steamGames f
        JOIN {dim_table} o ON f.AppID = o.AppID
        WHERE o.{group_by_col} IS NOT NULL
        GROUP BY o.{group_by_col}
        ORDER BY Top DESC
    """)

    result = db.session.execute(query)
    return result.fetchall()

def get_total(group_by_column1, aggregation_column1, dim_table1):
    query = text(f"""
        SELECT 
            dga.{group_by_column1},
            SUM(fg.{aggregation_column1}) AS Total
        FROM 
            Fact_steamGames fg
        JOIN 
            {dim_table1} dga ON fg.AppID = dga.AppID
        GROUP BY 
            dga.{group_by_column1} WITH ROLLUP
    """)
    
    result = db.session.execute(query)
    return result.fetchall()
