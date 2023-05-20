# airbnb_analysis

Report:
    
     1. Problem Statement and Background
        In a city like Boston, where there are a mass multitude of AirBNB options, 
        as well as a mass multitude of crime reports, it can be difficult to find 
        the safest places to stay. We believe that our program provides value because 
        from the perspective of AirBNB, it can allow them to better serve their 
        consumer base and allow people to find locations that truly match their 
        preferences. Additionally, for those investing in property or looking to 
        list their property as an AirBNB, our project could allow them to better 
        compare their property to those in their specific area. Ultimately, our program
        allows a user to better evaluate their Airbnb options in the city of Boston 
        based on the factors of cost and safeness.
        
    2. Introduction and Description of Data  
        The AirBnb data was collected from their official data source for the total 
        listings in Boston for 2022. The crime data was collected from Analyze Boston 
        which is a resource for numerous Boston Related datasets. When entering the data 
        into Spyder, the standard delimiter “,” was an issue as it conflicted with 
        commas used within the data. Thus, a program was run that converted the 
        delimiters from “,” to “}”. This delimiter was used for both the crime and 
        Airbnb data. 
        
        The Airbnb data included a unique ID for every airbnb listing as well as a URL
        to the specific listing. Information such as price, location (latitude, longitude), 
        accommodation, and neighborhood were also provided and collected. The neighborhood 
        dataset was also provided by airbnb and contained all possible neighborhoods, 
        Airbnb’s could be located in Boston. This information was created into a 
        list. For the crime data, the specific coordinates, type of crime, unique 
        crime id were included in the dataset and collected. For both datasets, the data 
        was condensed into a list of dictionaries where each dictionary contained a 
        specific row of information with the headers as keys. We then utilized these 
        lists for our reports and visualizations.
    
    3. Methods
        In order to find Airbnbs in the neighborhood chosen by the user, we filtered 
        through the data using the key for the neighborhood. To find and append 
        crime reports that fell within the ranges of the neighborhood chosen, we 
        used the lowest and highest longitude and latitude values for Airbnb. We 
        used these values to ensure that we only appended coordinates of crime reports 
        that fell within these boundaries.
        
        To find the safest Airbnb, we had to utilize the distance formula 
        (d = [x^2 − x^1]^2 + [y^2 − y^1]^2) in order to find the distances between each 
        Airbnb and every crime report in that neighborhood. We also found the closest 
        crime report distance for each Airbnb, and the Airbnb with the furthest 
        closest crime report distance would be considered the safest Airbnb.
        
        To find the cheapest Airbnb, we filtered through the Airbnbs in the chosen 
        neighborhood using the key for price. The Airbnb with the lowest value 
        for the price key would be considered the cheapest Airbnb.
        
        We first ran a for loop going through all locations in the neighborhood data 
        set, if the location and the accommodation parameters were set, then a list 
        would be created for all potential Airbnbs for that location. The average 
        price was then taken and then added to a dictionary with the key being the 
        location. After a dictionary was created, the min value, max value, and 
        closest price to the neighborhood choice were then retrieved in a report. 
    
    4. Results, Conclusion, and Future Work
        User Input: The user first inputs which Neighborhood they would like to 
        view Airbnb’s from including the max price they are willing to pay and 
        how many people they want to accommodate. In our example, we chose to select
        Roxbury, 4 people, and a maximum price of $1000.
        
        Report #1: The first report takes into account your accommodation requirements 
        and neighborhood preference and details the cheapest option and safest option 
        while providing a URL to the Airbnbs themselves. It also provides the 
        per-night cost of the cheapest option in the selected neighborhood. The 
        report also details the cheapest, most expensive, and most similar 
        neighborhood to the one you selected based on your accommodation 
        requirements. In our example, the url of the cheapest option is "https://www.airbnb.com/rooms/21597670",
        the cheapest option costed $65, the url of the safest option is "https://www.airbnb.com/rooms/5088560",
        the average price in Roxbury was $207.95, Allston was the most similar location with 
        an average price of $212.93, South Boston Waterfron was the most expensive
        with an average price of $486, and Hyde Park was the cheapest with an average
        price of $127.57.
        
        Visualization #1: This graph details the specific location of all the 
        Airbnb’s that fit your preference including all crime reported in that 
        area. The graph also highlights the cheapest option based on price and 
        safest option relative to the distance from the crime reports. In our 
        example, the safest option is located at around (42.319, -71.025), and 
        the most expensive option is located at around (42.340, -71.084).
        
        Visualization #2:   The second graph is a bar chart that depicts the average 
        price of all neighborhoods based on the accommodation requirement set by the user.
        In our example, the graph displays all of the average prices in Boston 
        for Airbnbs that accommodate 4 people.
        
