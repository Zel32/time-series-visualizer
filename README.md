# 📈 Page View Time Series Visualizer

This project is part of the **[freeCodeCamp Data Analysis with Python Certification](https://www.freecodecamp.org/learn/data-analysis-with-python/)**. It involves analyzing a time series dataset of daily page views and visualizing the data to uncover trends and patterns over time.

---

## 📊 Project Overview

The dataset contains the number of page views per day over a multi-year period. The goal of this project is to visualize the data using:

1. **Line Plot** – to show daily page views over time.
2. **Bar Plot** – to display average monthly page views grouped by year.
3. **Box Plots** – to show distribution of values across years and months for seasonal insights.

---

## 🛠️ Technologies Used

- Python 3
- Pandas
- Matplotlib
- Seaborn
- Jupyter Notebook (optional)

---

## 📁 Project Structure

```
.
├── time_series_visualizer.py   # Core script containing the plotting functions
├── test_module.py              # Unit tests for visualizations
├── fcc-forum-pageviews.csv     # Dataset of page views over time
├── line_plot.png               # Output of the time series line plot
├── bar_plot.png                # Output of the average monthly bar plot
├── box_plot.png                # Output of the seasonal box plots
```

---

## ⚙️ How to Run

1. **Clone the repository**:
   ```bash
   git clone https://github.com/your-username/page-view-time-series-visualizer.git
   cd page-view-time-series-visualizer
   ```

2. **Install dependencies**:
   ```bash
   pip install pandas matplotlib seaborn
   ```

3. **Run the script**:
   ```bash
   python time_series_visualizer.py
   ```

This will generate:
- `line_plot.png`
- `bar_plot.png`
- `box_plot.png`

---

## 🧪 Testing

To run the included unit tests (optional but recommended):

```bash
python test_module.py
```

These tests validate the structure, labels, and values in your plots against expected outputs.

---

## 📚 What I Learned

- How to clean and filter time series data using Pandas
- How to create insightful line, bar, and box plots with Matplotlib and Seaborn
- Understanding seasonal patterns and trends in time series data


---

## 📜 License

This project is part of the **freeCodeCamp Data Analysis with Python** certification and is shared for educational purposes.

---

## 🙌 Acknowledgments

- [freeCodeCamp](https://www.freecodecamp.org/) for providing the curriculum and dataset
- The open-source data science community for tools like Pandas and Matplotlib
