import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from pandas.plotting import register_matplotlib_converters
import numpy as np  

if not hasattr(np, 'float'):
    np.float = float

register_matplotlib_converters()

# Import data (Make sure to parse dates. Consider setting index column to 'date'.)
df = pd.read_csv("fcc-forum-pageviews.csv",parse_dates=['date'])
df = df.set_index('date')

# Clean data
df = df[(df['value']<df['value'].quantile(0.975)) & (df['value']>df['value'].quantile(0.025))]


def draw_line_plot():
    # Draw line plot
    plt.figure(figsize=(17,5))
    plt.plot(df, color='red')

    # tick every 6 months
    tick_dates = pd.date_range(start='2016-07-01', end='2020-01-01', freq='6MS')
    tick_labels = [date.strftime('%Y-%m') for date in tick_dates]

    plt.title("Daily freeCodeCamp Forum Page Views 5/2016-12/2019")
    plt.xticks(tick_dates, tick_labels)

    plt.xlabel('Date')
    plt.ylabel('Page Views')
    fig = plt.gcf() 


    # Save image and return fig (don't change this part)
    fig.savefig('line_plot.png')
    return fig

def draw_bar_plot():
    # Copy and modify data for monthly bar plot
    df_bar = df.copy()
    df_bar['year'] = df.index.year
    df_bar['month'] = df.index.month
    df_bar = df_bar.groupby(['year', 'month'])['value'].mean().unstack()
    df_bar.columns = pd.to_datetime(df_bar.columns, format='%m').strftime('%B') 

    # Draw bar plot
    fig = df_bar.plot(kind="bar", figsize=(8, 6), xlabel="Years", ylabel="Average Page Views").get_figure()

    plt.legend(title="Months")
    plt.tight_layout()


    # Save image and return fig (don't change this part)
    fig.savefig('bar_plot.png')
    return fig

def draw_box_plot():
    # Prepare data for box plots (this part is done!)
    df_box = df.copy()
    df_box.reset_index(inplace=True)
    df_box['year'] = [d.year for d in df_box.date]
    df_box['month'] = [d.strftime('%b') for d in df_box.date]

    # Draw box plots (using Seaborn)
    fig, ax = plt.subplots(1,2, figsize=(15,5))

    sns.boxplot(x='year',y='value', data=df_box, ax=ax[0], linewidth=0.5, fliersize=0.75)
    ax[0].set_xlabel('Year')
    ax[0].set_ylabel('Page Views')
    ax[0].set_title('Year-wise Box Plot (Trend)')

    month_order = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
    sns.boxplot(x='month', y='value', data=df_box, ax=ax[1], order=month_order, linewidth=0.5, fliersize=0.75)
    ax[1].set_xlabel('Month')
    ax[1].set_ylabel('Page Views')
    ax[1].set_title('Month-wise Box Plot (Seasonality)')
    

    # Save image and return fig (don't change this part)
    fig.savefig('box_plot.png')
    return fig
