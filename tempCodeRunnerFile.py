csv_1=csv_1.fillna(method="ffill")  # forward filling
# csv_1=csv_1.fillna(method="bfill")  # backward filling

# csv_1=csv_1.fillna(method="ffill",axis=1)