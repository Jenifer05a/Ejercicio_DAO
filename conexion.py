import pyodbc

try:
    # Cadena de conexión
    conn = pyodbc.connect(
        "DRIVER={ODBC Driver 17 for SQL Server};"
        "SERVER=localhost;"
        "DATABASE=mi_base;"
        "Trusted_Connection=yes;"
    )

    cursor = conn.cursor()
    print("✅ Conexión exitosa a SQL Server")


except Exception as e:
    print("❌ Error al conectar:", e)

finally:
    conn.close()
