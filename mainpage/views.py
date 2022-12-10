from django.shortcuts import render
import pandas as pd
import plotly.express as px
df = pd.read_csv("/Users/goshaargirov/Downloads/archive/googleplaystore.csv")
df.dropna(how='any', inplace=True)



def view_main_page(request):
    df["Price"] = df["Price"].str.replace('$', '').astype(float)
    mean_rating = round(df.Rating.mean(), 2)
    fig = px.scatter(x=range(10), y=range(10))
    fig.write_html('/Users/goshaargirov/Documents/PlayStoreAnalytics/templates/plot.html', full_html=False)
    payload = {
        'mean_rating' : str(mean_rating)
    }
    return render(request, 'index.html', payload)
