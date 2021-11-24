import pandas
from app.database.database import engine
from app.models.models import Post


file_name = "restaurantes.csv"
data_frame = pandas.read_csv(file_name)
data_frame.to_sql(con=engine, name=Post.__tablename__,
                  if_exists='append', index=False)

print("Done")