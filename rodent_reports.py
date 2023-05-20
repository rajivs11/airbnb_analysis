#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Rajiv Srinath
DS 2000: Intro to Programming with Data

Sun Oct  9 11:33:07 2022

File: rodent_reports.py

Description: Reads data of rodent reports in Boston and plots scatter and bar graphs and prints data to analyze and visualize data

"""
# import file for plotting and declares constants
import matplotlib.pyplot as plt

FILE = "rodents_311_2021.csv"
NEU = [-71.0892, 42.3398] # Northeastern University coordinates

def main():
    
    # declares list for each data category
    neighborhood = []
    latitude = []
    longitude = []
    
    # opens file, skips header, and reads remaining lines
    with open(FILE, "r") as infile:
        infile.readline()
        data = infile.readlines()
        
    for row in data:
        value = row.strip().split(",")  # separates values between commas
            
        if value[0] == "":  # if no neighborhood is indicated
            pass
        else:
            # assigns data to lists 
            neighborhood.append(value[0])
            latitude.append(float(value[1]))
            longitude.append(float(value[2]))
    
    # plots scatter plot of coordinates in latitude and longitude lists
    plt.scatter(longitude, latitude, marker = ".", color = "BLUE", alpha = 0.4,
                label = "Rodent Reports")
    
    # plots Northeastern University coordinates
    plt.scatter(NEU[0], NEU[1], marker = "*", color = "RED", 
                label = "Northeastern")
    
    # assigns title, labels, legend, and displays and saves figure
    plt.title("Map of Rodent Reports in Boston 2021")
    plt.xlabel("Longitude")
    plt.ylabel("Latitude")
    plt.legend()
    plt.savefig("boston_rodents.pdf", bbox_inches = "tight")
    plt.show()
    
    # prints total rodent reports for neighborhoods
    print(f"Total rodent reports assigned to a valid neighborhood: {len(neighborhood)}")
    
    # creates list for distinct neighborhoods
    distinct_neighborhood = []
    
    # passes through values in neighborhood list to find and create list of unique values
    for name in neighborhood:
        if name not in distinct_neighborhood:
            distinct_neighborhood.append(name)
            
    distinct_neighborhood.sort()   # sorts list in alphabetical order and prints list
    print("\nNeighborhoods:")
    
    for distinct_name in distinct_neighborhood:
        print(distinct_name)   # prints each neighborhood in new line
    
    
    report_count = []   # creates list for report counts
    
    # passes through values in distinct neighborhood list to identify number of reports 
    for distinct_item in distinct_neighborhood:
        report_count.append(neighborhood.count(distinct_item))
    
    # plots bar graph of reports by neighborhood
    plt.bar(distinct_neighborhood, report_count)
    
    # assigns title and labels, adjusts, displays, and saves bar graph
    plt.title("Rodent Report Comparison for Neighborhood")
    plt.xlabel("Neighborhoods")
    plt.ylabel("Rodent Report Count")
    plt.xticks(rotation = 90)
    plt.savefig("neighborhoods.pdf", bbox_inches = "tight")
    plt.show()
    
    # calculates and prints average number of rodent reports from neighborhood
    print(f"\nAverage number of rodent reports: {len(neighborhood)/len(distinct_neighborhood)}")
    
main()

