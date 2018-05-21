# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:39:45 2017

@author: donalds
"""

import matplotlib.pyplot as plt
import csv #to read csv files
from io import BytesIO #to save the requested file type
import pandas as pand #to read co2 per country

#array containing all the months of the year.
month_list = ["","January", "February", "March", "April", "May", "June", "July",
              "August", "September", "October", "November", "December"]

#temperatures array(list) save in the read temperatures from the file
temperatures = []
#CO2_emission array(list) save in the read co2 emission per year from the file
CO2_emission = []
#co2 emission by country per year from file
CO2_emission_by_country = None


def plot_temperature(month, format, xmin_ye=None, xmax_ye=None, ymin_temp=None, ymax_temp=None):

    """
        I read these websites before I started solving the assignment and my
        solution is based on them.
        1- http://www.developintelligence.com/blog/2017/08/plotting-climate-data-matplotlib-python/
        2- https://plot.ly/python/plot-data-from-csv/
        3- https://docs.python.org/3/library/csv.html

        this method builds the plot of temperature for year based on given month

        @param month is the given month, should be between 1-12
        @param xmin_ye and xmax_ye are limits for x-axis (years start and end)- optional
        @param ymin_temp and ymax_temp are limits for y-axis (degrees max and min)- optional

        the plot is returned as an object that contains the data in the requested format('jpg', 'png', 'svg')

    """

    #check if month not between 1-12
    if not 1 <= month <=12:
        raise ValueError('Invalid number of month given: ' + str(month))


    plt.clf()
    plt.title("Average temperature for " + month_list[month])
    plt.xlabel("Years")
    plt.ylabel("Degree °C")

    #Add legend
    plt.legend()

    """
        plotting xmin , xmax and ymin, ymax

    """
    #xmin_ye
    if xmin_ye:
        plt.xlim(xmin = xmin_ye)
    #xmax_ye
    if xmax_ye:
        plt.xlim(xmax = xmax_ye)

    #ymin_temp
    if ymin_temp:
        plt.ylim(ymin = ymin_temp)

    #ymax_temp
    if ymax_temp:
        plt.ylim(ymax = ymax_temp)

    #plotting the years and temperatures according to the given file
    years, temp = zip(*((year[0], year[month]) for year in temperatures))
    plt.plot(years, temp)

    #save the graph
    with BytesIO() as temperatures_for_year:
        plt.savefig(temperatures_for_year, format=format)
        return temperatures_for_year.getvalue()



def plot_CO2(format, xmin_ye=None, xmax_ye=None, ymin_temp=None, ymax_temp=None):

    """
        this method plots CO2 emissions per year
        @param format is picture format
        @param xmin_ye and xmax_ye are limits for x-axis (years start and end)- optional
        @param ymin_temp and ymax_temp are limits for y-axis (degrees max and min)- optional
        the plot is returned as an object that contains the data in the requested format('jpg', 'png', 'svg')

    """
    plt.clf()
    plt.title("CO2 emissions per year")
    plt.xlabel("Years")
    plt.ylabel("CO2 emission")

    #Add legend
    plt.legend()

    """
        plotting xmin , xmax and ymin, ymax

    """
    #xmin_ye
    if xmin_ye:
        plt.xlim(xmin = xmin_ye)
    #xmax_ye
    if xmax_ye:
        plt.xlim(xmax = xmax_ye)

    #ymin_temp
    if ymin_temp:
        plt.ylim(ymin = ymin_temp)

    #ymax_temp
    if ymax_temp:
        plt.ylim(ymax = ymax_temp)

    #plotting the years and temperatures according to the given file
    years, co2_level = zip(*CO2_emission)
    plt.plot(years, co2_level)

    #save the graph
    with BytesIO() as co2_level:
        plt.savefig(co2_level, format=format)
        return co2_level.getvalue()

def plot_CO2_by_country(year, lower_thres, upper_thres, format):

    """
        this method plots CO2 emissions per year for all the countries where the emission was between given thresholds
        @param year is param for start year
        @param upper_thres and lower_thres are the thresholds chosens/given by the user
        @param format is picture format
        the plot is returned as an object that contains the data in the requested format('jpg', 'png', 'svg')

    """
    y = str(year);
    data = CO2_emission_by_country[["Country Code", y]]
    thres_data = data[(data[y] >= lower_thres) & (data[y] <= upper_thres)]
    thres_data.plot(kind="bar", title="CO2 by country year " + y, x = "Country Code", legend = False)
    plt.ylabel("CO2 emission")

    with BytesIO() as co2_level_country:
        plt.savefig(co2_level_country, format=format)
        return co2_level_country.getvalue()




#Read data from the files and load it into arrays
#Temperature data
with open("temperature.csv", newline="") as temp:
    filereader = csv.reader(temp)
    next(filereader)#skip field names
    temperatures = list(filereader) #fill up the array

#CO2 emission data
with open("co2.csv", newline="") as co_2:
    filereader = csv.reader(co_2)
    next(filereader)#skip field names
    CO2_emission = list(filereader) #fill up the array

# load co2 per country data by using panda
CO2_emission_by_country = pand.read_csv("CO2_by_country.csv")



if __name__ == "__main__":
    fnames = ("Temperature_plot.png", "CO2_plot.png", "CO2_by_country_plot.png")

    with open(fnames[0], "wb") as f:
        f.write(plot_temperature(12, "png"))

    with open(fnames[1], "wb") as f:
        f.write(plot_CO2("png"))

    with open(fnames[2], "wb") as f:
        f.write(plot_CO2_by_country(2010, 5, 10, "png"))

    print("Plots saved to " + ", ".join(fnames)+ ".")











