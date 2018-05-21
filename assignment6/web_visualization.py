# -*- coding: utf-8 -*-
"""
Created on Tue Nov 14 13:59:34 2017

@author: donalds
"""
import os
from temperature_CO2_plotter import plot_temperature, plot_CO2, plot_CO2_by_country, month_list
from flask import Flask, render_template, request
import pydoc


def getCurLocation():
    return os.path.realpath(
           os.path.join(os.getcwd(), os.path.dirname(__file__)))

app = Flask(__name__)

@app.route("/")
def index():
    return render_template('index.html')

@app.route("/co2", methods=['GET', 'POST'])
def co2():

    #convert parameters to ints
    arguments = {k: int(v) for k, v in request.form.items() if v}

    #generate the plot as SVG without the extra tags at the begining
    b = plot_CO2("svg", **arguments)
    svg = b[b.index(b"<svg "):].decode()
    return render_template("co2.html", svg=svg, **arguments)


@app.route("/temperature", methods=['GET', 'POST'])
def temperature():
    #convert parameters to ints
    arguments = {k: int(v) for k, v in request.form.items() if v}
    #get months
    month = arguments.get("month", 1)
    #remove month if in arguments to avoid duplicate arguments
    if "month" in arguments:
        del(arguments["month"])
    b = plot_temperature(month, "svg", **arguments)
    svg = b[b.index(b"<svg "):].decode()
    arguments["month"] = month
    return render_template("temperature.html",month_list=month_list[1:], svg=svg, **arguments)


@app.route("/co2_by_country", methods=['GET', 'POST'])
def co2_by_country():

    #convert parameters to ints
    year = request.form.get("year", "1970")
    lower = request.form.get("lower", "4")
    upper = request.form.get("upper", "10")

    try:
        b = plot_CO2_by_country(int (year), float(lower), float(upper), "svg")
        svg = b[b.index(b"<svg "):].decode()
    except Exception as e:
        svg = str(e)
    return render_template("CO2_by_country.html", svg=svg, year = year, lower_thres = lower, upper_thres = upper)


@app.route("/doc/temperature_CO2_plotter")
def doc():
    return pydoc.html("temperature_CO2_plotter")


if __name__ == "__main__":
    app.run()