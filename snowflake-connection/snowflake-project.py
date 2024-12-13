import snowflake.connector

# Connection details
conn = snowflake.connector.connect(
    user='KIRANBELE11',
    password='Kiran@umass11',
    account='zgchlvo-bh26855',
    warehouse='COMPUTE_WH',
    database='KBELE_LONDON',
    schema='PUBLIC',
    client_session_keep_alive=True
)

try:
    print("Connecting to Snowflake...")
    cursor = conn.cursor()

    # query
    query = "SELECT * FROM KBELE_LONDON.PUBLIC.JOURNEYS LIMIT 10;"  
    cursor.execute(query)

    # Fetch the results
    results = cursor.fetchall()

    # Print the results
    print("Query Results:")
    for row in results:
        print(row)
    

    # Query 1: Most popular transport types
    most_popular_types_query = """
    SELECT journey_type,
           SUM(journeys_millions)/1000000 as total_journeys_millions
    FROM KBELE_LONDON.PUBLIC.JOURNEYS
    GROUP BY journey_type
    ORDER BY total_journeys_millions DESC;
    """
    
    # Query 2: Emirates Airline popularity by month and year
    emirates_query = """
    SELECT month,
           year,
           ROUND(journeys_millions/1000000, 2) as rounded_journeys_millions
    FROM KBELE_LONDON.PUBLIC.JOURNEYS
    WHERE journey_type = 'Emirates Airline'
    AND journeys_millions IS NOT NULL
    ORDER BY rounded_journeys_millions DESC
    LIMIT 5;
    """
    
    # Query 3: Least popular years for Underground & DLR
    underground_query = """
    SELECT year,
           journey_type,
           SUM(journeys_millions)/1000000 as total_journeys_millions
    FROM KBELE_LONDON.PUBLIC.JOURNEYS
    WHERE journey_type = 'Underground & DLR'
    GROUP BY year, journey_type
    ORDER BY total_journeys_millions ASC
    LIMIT 5;
    """
    
    # Execute and fetch results for each query
    print("\nMost Popular Transport Types:")
    cursor.execute(most_popular_types_query)
    results1 = cursor.fetchall()
    for row in results1:
        print(row)
        
    print("\nTop 5 Months for Emirates Airline:")
    cursor.execute(emirates_query)
    results2 = cursor.fetchall()
    for row in results2:
        print(row)
        
    print("\nLeast Popular Years for Underground & DLR:")
    cursor.execute(underground_query)
    results3 = cursor.fetchall()
    for row in results3:
        print(row)

except Exception as e:
    print(f"Error: {e}")
finally:
    cursor.close()
    conn.close()



