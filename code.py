
import pyodbc

host = 'big.cm'

port = 10000

database = 'default'

ssl = True

sslTrustStore = ''

truststorePassword = 'changeme'

principal='###'

username = 'Vddd'

password = '###'

trusted_connection = 'yes'

 

print(pyodbc.dataSources())

 



# # Construct the connection string

conn_str = f"DRIVER={{Cloudera ODBC Driver for Apache Hive}};host={{host}};Schema={database};port=10000;Trusted_Connection={trusted_connection};" \

           f"SSL=1;ssLTrustStore={sslTrustStore};AuthMech=3;truststorePassword={truststorePassword};UID={username};PWD={password};AllowSelfSignedServerCert=1;UseNativeQuery=1"

 



try:

    conn = pyodbc.connect(conn_str, autocommit=True)             

    print('Connected')

except Exception as e:

    print('Not Connected')

 

cursor = conn.cursor()

print(cursor)

 

# Fetch all databases

cursor.execute("SHOW DATABASES")

 



# Iterate over the result set

databases = [row.database_name for row in cursor.fetchall()]

 

# Print the list of databases

print("Available databases:")

for database in databases:

    print(database)

 

 

# Specify the database and table

database = 'WED'

table = 'UNITS'

 

# Switch to the desired database

cursor.execute(f"USE {database}")

 



# Query the table

cursor.execute(f"SELECT * FROM {table}")

 



# Fetch the query results

results = cursor.fetchall()

 

 

# Process the results

for row in results:

    print(row)

 

 

# Close the cursor and connection

cursor.close()

conn.close()
