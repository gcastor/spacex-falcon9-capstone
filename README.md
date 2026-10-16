# SpaceX Falcon 9 First-Stage Landing Prediction

IBM Data Science Professional Certificate – Applied Data Science Capstone
Author: Greg ([@gcastor](https://github.com/gcastor))

SpaceX prices Falcon 9 launches at about $62 million, against $165 million or more from other providers, largely because it lands and reuses the first stage. This project predicts whether the first stage will land, which can be used to estimate the cost of a launch.

## Key results

| Finding | Value |
|---|---|
| Overall landing success rate | 66.7% (60 of 90 launches) |
| Success rate in 2019 | 90% (up from 0% before 2014) |
| Most reliable launch site | KSC LC 39A, 77.3% |
| Orbits with 100% success | ES-L1, GEO, HEO, SSO |
| Best model | Decision Tree, 94.4% test accuracy |

## Notebooks

| Step | File |
|---|---|
| 1. Data collection – SpaceX API | [jupyter-labs-spacex-data-collection-api.ipynb](jupyter-labs-spacex-data-collection-api.ipynb) |
| 2. Data collection – Web scraping | [jupyter-labs-webscraping.ipynb](jupyter-labs-webscraping.ipynb) |
| 3. Data wrangling | [labs-jupyter-spacex-Data-wrangling.ipynb](labs-jupyter-spacex-Data-wrangling.ipynb) |
| 4. EDA with data visualization | [edadataviz.ipynb](edadataviz.ipynb) |
| 5. EDA with SQL | [jupyter-labs-eda-sql-coursera_sqllite.ipynb](jupyter-labs-eda-sql-coursera_sqllite.ipynb) |
| 6. Interactive map with Folium | [lab_jupyter_launch_site_location.ipynb](lab_jupyter_launch_site_location.ipynb) |
| 7. Plotly Dash dashboard | [spacex_dash_app.py](spacex_dash_app.py) |
| 8. Predictive analysis | [SpaceX_Machine_Learning_Prediction_Part_5.ipynb](SpaceX_Machine_Learning_Prediction_Part_5.ipynb) |

Interactive Folium maps are saved in [`maps/`](maps/). GitHub does not render Folium output inside notebooks, so download the HTML files or view the notebook on [nbviewer](https://nbviewer.org/github/gcastor/spacex-falcon9-capstone/blob/main/lab_jupyter_launch_site_location.ipynb).

## Data

| File | Description |
|---|---|
| `data/dataset_part_1.csv` | Falcon 9 launches from the SpaceX API, cleaned (output of step 1) |
| `data/dataset_part_2.csv` | Same data with the `Class` landing label (output of step 3) |
| `data/dataset_part_3.csv` | One-hot encoded features for modeling (output of step 4) |

## Run it

```bash
pip install pandas numpy matplotlib seaborn scikit-learn folium dash plotly requests beautifulsoup4 jupyter
jupyter notebook            # run the notebooks in order
python spacex_dash_app.py   # dashboard at http://127.0.0.1:8050
```

Steps 1 and 2 need internet access to reach the SpaceX API and Wikipedia. Steps 3–8 run offline from the files in `data/`.

## Tools

Python, Pandas, NumPy, Requests, BeautifulSoup, Matplotlib, Seaborn, SQLite, Folium, Plotly Dash, scikit-learn
