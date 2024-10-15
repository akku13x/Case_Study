class PropertyUtil:
    @staticmethod
    def get_property_string():
        server_name = "LAPTOP-V5IQ580M"
        database_name = "Crime_Reporting"

        conn_str = (
            f"Driver={{SQL Server}};"
            f"Server={server_name};"
            f"Database={database_name};"
            f"Trusted_Connection=yes;"
        )

        return conn_str