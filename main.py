from database import Connector
from file_reader import ReadCustomer, ReadProduct, ReadSalesOutlet, ReadSalesTarget
from database.storing import StoreCustomer, StoreProduct, StoresSalesOutlet

connection = Connector.connect("root", "localhost", "0000")
database_cursor = connection.cursor()
# database_cursor.execute("DROP DATABASE SalesDataBase;")
# DataBaseCreator.create_database(database_cursor, "SalesDataBase")
database_cursor.execute("USE SalesDataBase")
# DataBaseTables.create_tables(database_cursor)

# ----------------- Read data files ----------------------

# customer_list = ReadCustomer.read_customer_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\customer.csv")
# product_list = ReadProduct.read_product_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\product.csv")
sales_outlet_list = ReadSalesOutlet.read_sales_outlet_file(
    "C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\sales_outlet.csv")
# ReadSalesTarget.read_sales_target_file("C:\\Users\\twitter\\PycharmProjects\\ProjectTrainingAsal\\files_data\\sales targets.csv")
# ---------------------------------------------------------

# ------------------ Store data files to database---------------------
# StoreCustomer.store_all(customer_list, database_cursor, connection)
# StoreProduct.store_all(product_list, database_cursor, connection)
StoresSalesOutlet.store_all(sales_outlet_list, database_cursor, connection)
