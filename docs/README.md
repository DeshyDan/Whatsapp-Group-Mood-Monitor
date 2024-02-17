# Whatsapp Group mood monitor

This doc summarizes the workflow of analyzing the mood of Whatsapp Group between a period of time and graphing the trends . 

## Overview of workflow

_TODO : Embed workflow diagram into markdown_

```
CLI configurations ->  Extract Group Text Messages -> Perform Sentiment Analysis -> Generate Graphs and Insight
```

## Workflow destructuring

### CLI configurations

The program runs through the CLI. Users will have to input arguments into the program to run it:

_TODO: Expand on this...._
#### Program Arguments
- Name of Group 
- Time period

### Extraction of Group Text Messages

At the moment Whatsapp does not provide any API for personal accounts so we will have to rely on scraping. Using a WebDriver we will log into Whatsapp web, search for the group and scrap the text messages. After will perfom some data wrangling and save the data in a json file. 

### Performing Sentiment Analysis

Using a sentiment analysis tool we will read the json file and save the output into a file that we will use later to generate some cool visuals

## Graphing And Insight Generation
_TODO: expand on this explanation_

Using the output from the sentiment analysis tool we will use plot some graphs 