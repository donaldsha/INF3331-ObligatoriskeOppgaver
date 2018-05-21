# -*- coding: utf-8 -*-
"""
Created on Thu Nov  2 23:42:37 2017

@author: Min-Pc
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Oct 17 12:48:37 2017

@author: Donalds
"""
import re #regular expression

#regex reglene
# ([>][>][[:word:]]+) ->regex for Quote
# \[(.*?)\]\((.*?)\) -> nwodkram to html
# ([<][[:word:]]+[>](.+)([w]\=[0-9]+\,[h]\=[0-9]+\))) -> imageUrl
# \*[^*]*[^\\]\* --> *this* regelen
# \%[^%]*[^\\]\% --> %this% regelen

#Kunne også lage en dictionary og hente reglene derifra men siden oppgavene er
#delt i deler gjør jeg hver for sin del.

def parse_nwodkram(text): #Oppgave 5.1  ((?<!\\\)[%](?P<value>.*?)(?<!\\\)[%])
    #Bold to html
    bold = re.compile(r'((?<!\\\)[%](?P<bold>.*?)(?<!\\\)[%])')
    text = re.sub(bold, '<b>\g<bold></b>', text)

    #italic to html
    italic = re.compile(r'((?<!\\\)[*](?P<italic>.*?)(?<!\\\)[*])')
    text = re.sub(italic, '<i>\g<italic></i>', text)

    #nwodkram to html
    html = re.compile(r'(\\[(?P<value>.*?)\\])(\\((?P<url>.*?)\\))');
    text = re.sub(html, '<a href=\'\g<url>\'>\g<value></a>', text)
    #sub('\[(.*?)\]\((.*?)\)', text)
    #string = re.findall("\[(.*?)\]\((.*?)\)", text)

    #Image to html oppgave 5.2
    image = re.compile(r'(\<(?P<imageUrl>.*)?\>)(\([w]\=(?P<width>[0-9]*)\,[h]\=(?P<height>[0-9]*)\))')
    text = re.sub(image, '<img src=\"\g<imageUrl>\" width=\"\g<width>\" height=\"\g<height>\" alt=\"<Img>\" />', text)

    #Quotes to html oppgave 5.2
    quotes = re.compile(r"([>][>]+(?P<quote>.*))")
    text = re.sub(quotes, '<blockquote>\g<quote></blockquote>', text)

    #wikipedia to html
    wiki = re.compile(r"(\\[[w][p]\\:(?P<search>.*?)\\])");
    text = re.sub(wiki, "<a href=\"https://en.wikipedia.org/w/index.php?title=Special:Search&search=\g<search>>\g<search></a>", text)

    return text




#parse_nwodkram(sample_input)
#parse_nwodkram('[www.nwodkram.com](displayed text)')