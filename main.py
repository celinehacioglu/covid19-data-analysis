import pandas as pd
import plotly.express as px

# 1. Veriyi oku
df = pd.read_csv("/Users/selinhacioglu/Desktop/covid19-data-analysis/covid19-data-analysis/time_series_covid19_confirmed_global.csv")

# 2. Ülkeye göre grupla ve sütunları topla
df_country = df.drop(columns=["Province/State", "Lat", "Long"]).groupby("Country/Region").sum()

# 3. Transpose ederek günleri satır yap
df_transposed = df_country.T
df_transposed.index = pd.to_datetime(df_transposed.index)

# 4. Örnek: Türkiye'nin vakalarını görselleştir
fig = px.line(df_transposed, y="Turkey", title="Türkiye COVID-19 Günlük Kümülatif Vakaları")
fig.show()

# En çok toplam vakaya sahip 10 ülkeyi bul
top_countries = df_country.sum(axis=1).sort_values(ascending=False).head(10).index.tolist()

# Bu 10 ülkenin zaman içindeki verisini al
top_df = df_transposed[top_countries]

# Çizgi grafik
fig2 = px.line(top_df, title="En Çok Kümülatif Vakaya Sahip 10 Ülke")
fig2.update_layout(
    xaxis_title="Tarih",
    yaxis_title="Toplam Vaka",
    legend_title="Ülke"
)
fig2.show()

'''

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

'''
