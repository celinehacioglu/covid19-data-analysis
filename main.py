import pandas as pd
import plotly.express as px

# 1. Veriyi oku
df = pd.read_csv("time_series_covid19_confirmed_global.csv")

# 2. Ülkeye göre grupla ve sütunları topla
df_country = df.drop(columns=["Province/State", "Lat", "Long"]).groupby("Country/Region").sum()

# 3. Transpose ederek günleri satır yap
df_transposed = df_country.T
df_transposed.index = pd.to_datetime(df_transposed.index)

# 4. Örnek: Türkiye'nin vakalarını görselleştir
fig = px.line(df_transposed, y="Turkey", title="Türkiye COVID-19 Günlük Kümülatif Vakaları")
fig.show()
