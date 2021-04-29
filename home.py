import dash
import dash_core_components as dcc
import dash_html_components as html
import plotly.express as px
import pandas as pd
from app import app
external_stylesheets = ['https://codepen.io/chriddyp/pen/bWLwgP.css']

layout = html.Div(
        className="container scalable",
    children=[
        html.Div(
            id="banner",
            className="banner",
            children=[
                html.Img(src=app.get_asset_url("Used_Cars_Logo.png")),
                html.H1("Used Cars Dashboard", style={'text-align': 'center'}),
                
                
            ],
        ),
        
                dcc.Link('Dashboard',className="menu_link", href='/apps/main'),
        
                dcc.Link('Buyers & Sellers Perspective',className="menu_link", href='/apps/buyers'),
        
                dcc.Link('Go Electric',className="menu_link", href='/apps/apper'),
        html.Div([
            #html.H2(children='Used Cars Dashboard'),
            html.H3(children='A Simplified Interface for the Buyer and Seller to make a right decision', style={'padding': '20px'})])
        ,


    
    html.Div(
            [
                dcc.Markdown(
                    """
            ** "In the United States every man is entitled to life, liberty and a car in which to pursue happiness."  -- *EVAN ESAR* **
    
            
            
        """
                )
            ],
            id="quote",
            className="home",
        ),
    html.Div(
            [
                dcc.Markdown(
                    """
            ### The Application 
            The Used Cars Dashboard is an interactive platform having database with information of 500K used cars across the United
            States of America which covers car listings since 2020,January. Using the information extracted from Kaggle.com, as part of the course
            CS526: Data Interaction and Visualization, we have designed and developed an interactive dashboard which explores the data set in
            depth. In addition to summarizing the listings and plotting them interactively over the locations, the dashboard provides means to view
            important statistics of an buying a used car in a particular state. Such understanding of the data can be serve as a guide in the decision
            making process of a buyer and can also provide some meaningful insights to the seller as well.


            ### Data
            The data-set is from Kaggle and is the world's largest collection of used vehicles for sale from Craigslist. The data
            is scraped every few months, it contains all the relevant information on car sales including columns namely
            * Price, Car_condition, Manufacturer
            * Car_year, Model, Color
            * Drive, Description, Title-status
            * VIN, Longitude, Latitude

            Data size: 1.41 gb

            No. of Rows: 450K

            No. of Columns: 26

            ### Fundamental Questions 

            Q1. How to make an interactive user interface for a user who want to buy a used car?  
             
             Ans. Here we have main page US- Geo Scatter-map where we have shown car listings filter by year, state, price slider and region
                
                - The map is zoomed on selection of a particular state to give a better view
                - The filters are year, state "drop-down menu selection", price "two way slider", region "check-list with option to select all"


            Q2.How to guide the decision-making process of the buyer so that he/she can make a wise decision based on data insights and statistical analysis provided by dashboard?

             Ans. On our Buyers & Sellers Perspective page we have 6 plots showing how a user will frame his/her decision for buying a car
                
                - Line chart comparing the price year-wise for multiple states selected at a time 
                - Pie chart showing odometer readings year wise for multiple states, hovering on line chart changes piechart year
                - A sunburst plot showing the top 5 manufacturers for multiple states 
                - A treemap showing the condition of the car with count for multiple states
                - A stacked bar plot for showing the drive type for multiple states
                - A doughnut chart for showing the fule type distribution across multiple states  


            Q3. Provide recommendation to user based on plots?

             Ans. The plots answer user specfic questions 

                - The main plot "Geo-scatter plot" helps user find cars in a concise manner with filters and also locate nearby cars
                - The word cloud helps the seller to find optimal words for writing a better description for when selling a cars
                - The Go Electric page helps user to identify charging stations in the vicinity
                - The Go Electric page also helps user to find a trend showing increasing the count of charging stations across the USA.


            Q4. Analysis based on the attributes such as price, year, manufacturer, condition and type of cars can help users to decide about buying a car?

             Ans. Here we have 6 plots to answer these questions on page 2

                - The first two plots shows price and odometer readings are inversely proportional to each other.
                - The average age of the car is 5-7 years as we have maximum listings in these years. This can be seen in the main plot.
                - California is the only State having more electric charging stations than gas stations. This is shown using doughnut plot on page 2.


            Q5. Our aim is to make these attributes easy to use and interactive so that any user can decide as quickly as possible?

             Ans. We have consolidated the attributes into filters, sliders, charts and selctions.

                - The entire dashboard is easy to use and helps user to understand the used_cars market
                - The home page reflects everything on how to use the dashboard, this gives a broder understanding to the user. 
        
            ### Target Audience

            * The Buyers & Sellers of Used_cars
            * The car manufacturing companies
            * Statisticians and researchers working in the automobile industry
            * Used_cars platforms namely companies Craigslist, Caravana, Carfax, Cox Automotive
            * Electric cars enthusiasts 

            ### Interesting Findings

            * The average age of the car is 5-7 years as there are maximum listings under these years. 
            * This can be shown by the Dashboard page Geo-map.
            * The word cloud helped users to find the right combination of words separated state-wise, while buying or listing a used-car.
            * On the page Buyers & Sellers Perspective, the first 2 plots showed price and odometer readings are inversely proportional to each other, that is higher price meaning less age and less odometer reading compared to lower price meaning more age and more odometer reading. This is depicted using a line and a pie chart.
            * Using the sunburst plot, we found out that Ford, Honda and Toyota were the top listed manufacturer on used_cars platform for almost all the states.
            * The stacked bar chart, says 4wd is the most common drive type for most of the car buyers in the USA.
            * California is the only state with higher percentage of electric car buyers than gas cars, showing big move to go electric. This finding was highlighted using the doughnut chart.
            * The number of Electric Charging Stations are growing exponentially in numbers compared to CNG,LPG,E85,LNG and BD. This is shown by the choropleth plot in the Go Electric page.
            * Electric Charging stations are mostly maximum in numbers for big cities in a particular State. Ex. in Texas the maximum Elec. Charging stations are in Austin, Houston, Dallas, San Antonio and Fort Worth. This is reflected by the bar plot on Go Electric page.
            
        """
                )
            ],
            className="home",
        )
])

# if __name__ == '__main__':
#     app.run_server(debug=True)