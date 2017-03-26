# south_park_data

Python scripts for the corresponding blog post: http://vprusso.github.io/blog/2017/data-driven-south-park/

## Overview

This repository consists of 70,000 lines of dialog extracted from "South Park" (courtesy of Ksenia Sukhova over at Kaggle) as well as two Python scripts:

1. south_park_analyze.py
    A number of functions to determine how often a given word or series of words is used by specific character given a set of seasons / episodes.

2. south_park_plots.py
    All of the plots generated in the [blog post](http://vprusso.github.io/blog/2017/data-driven-south-park/) may be replicated by this file. 

## Usage

Example usage of `south_park_analyze.py` is shown at the bottom of the file. Uncommenting the following line:

    # Question: How many times is the word “dude” said in all of the seasons 1 to 18:
    #print ( word_count_by_season_and_episode(df, word="dude") )

will print out how many times the word "dude" is said in "South Park" for seasons 1 through 18. More example usage can be found on the corresponding [blog post](http://vprusso.github.io/blog/2017/data-driven-south-park/).

Example usage of `south_park_plots.py` is shown at the bottom of the file. Uncommenting the following line:

    # plot_swear_count_season_frequency()

will generate the following plot

<p align="center">
    <center>
        <figure>
            <img src="http://i.imgur.com/mdYP6A7.png" alt="Plot for occurence of swear word by South Park season."/>
        </figure>
    </center>
</p>

For more information, consult the [blog post](http://vprusso.github.io/blog/2017/data-driven-south-park/).

## Dependencies

1. [Python 3](https://www.python.org/),
2. [pandas](http://pandas.pydata.org/),
3. [nltk](http://www.nltk.org/).
