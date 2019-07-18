<img src="https://bit.ly/2VnXWr2" alt="Ironhack Logo" width="100"/>

# Refugees crisis impact on media 
**Alberto Abreu, Josep Foradada and Íngrid Munné**

*Ironhack Data Analytics Bootcamp. July 2019*

## Content
- [Project Description](#project-description)
- [Hypotheses / Questions](#hypotheses-/-questions)
- [Dataset](#dataset)
- [Workflow](#workflow)
- [Organization](#organization)
- [Links](#links)

<a name="project-description"></a>

## Project Description

The refugees crisis is a topic that has increased since the last decade. Countries such as Syria, Lybia, Venezuela, Myanmar and Afghanistan have experiencied a huge waves of people leaving their countries for a better future, due to the lack of human rights. 
In this project, we wanted to assess if this topic is been debated worldwide and what's the impact on different countries and sources. 

<a name="hypotheses-/-questions"></a>

## Hypotheses / Questions

The questions that we wanted to answer were the following two: 

- What's the impact of refugees-related news in media (newspaper) and social media (Twitter)?
- Once the event is raised, is there an equal coverage on Twitter and on newspaper?

There were some initial hypotheses considered beforehand: 

- That the topic is being debated more and more since there is a refugees' crisis in Syria and in Mexico.  
- That there are countries such as the USA were this topic is highly debated. 
- That they act as a trigger to push government and NGOs to take a role on the situation. 

<a name="dataset"></a>

## Dataset

- NewsAPI
    This API retrieves data from different news sources around the world, from General topics to health and technical. It allows to retrieve data from specific sources, from specific time-periods and also from specific topics or keywords. It has a clear and structured documentation. However, you should ask for a token in order to get data from this API. However, it contains different limitations if you don't pay fror premium permisions.
    It retrieves data from past two months. 
    It only retrieves 5 pages for each topic you insert as a parameter. 
    The API has a source dataset that can be retrieved and then labeded. However, this API looks for data in sources that are not included in the source dataset. 
    
- World Bank Data 
    At the World Bank, the Development Data Group coordinates statistical and data work and maintains a number of macro, financial and sector databases. It has a division that works on collecting and analysing data from humanitarian crisis. Since 1991, they are collecting data about refugee population by country of origin and year. 
    For this project, the database has been extracted from the webpage in a .csv file. 
    There are some gaps in the datasets, meaning that there is only only data from 1991 onwards. 
    There are some aggregated countries or areas that bias the final results and requires a careful data cleaning before performing any analysis. 

- Twitter API 
    The Twitter API has many different documentation to retrieve data from its platform. We used the free version called Standard Search method which retrieves Tweets information from the last seven days using a parameter called “q” where you write down the keywords you want to use to filter the streaming. Moreover, you can specify the language, and what kind of information you want like: user_name, hashtags, tweet and location.
     By using the Twython wrappers in python, we manage to call the TwythonStreamer to stream data from the API and obtain approx. 40 thousand observations.

- Google Search 



- OnlineNewspaperlist.com 


[Twitter API](https://developer.twitter.com/en/docs.html) 

[News API]() 

[WorldBank data]() 

<a name="workflow"></a>

## Workflow

First of all, the work has been divided into each dataset that was analyzed. A common database has been created to have a common structure where all the data will be saved. Each table contains primary keys and foreign keys to be linked between them. 

One script has been created for each source where data has been retrieved from. Each script contains the following substeps: collecting data, cleaning data, formatting data according to the data There is one script for webscraping, one for WorldBank data, News API and Twitter API. Once the final version of the datasets were completed, we upload them into one common Google Cloud account to have a common space with all the relevant datasets. 

After this point, we stop working on Jupyter notebook to start analyzing the data via Zepellin. In this platform we were able to query the tables and do some basic visualization to have a better representation of our insights and be able to present them to the audience. Afterwards, we gathered all the analyzed insights and start writing them down into the research paper inside the Zepellin notebook. 

To finish, a Slide presentation was created for the class presentation with the main insights of the project. 

<a name="organization"></a>

## Organization

Proyect Management: Trello.
Data manipulations: Python coding language in Jupter notebook and PyCharm. 
Data visualization and analysis: Zeppelin notebook.
Data storage: Google Cloud, SequelPro and Sequel wordbench.
Presentation: Slides.

<a name="links"></a>

## Links
Include the links to your repository, slides and trello. Feel free to include any other links associated to your project. 

[Repository](https://github.com/albertoabreu91/Project-Week-3-Data-Thieves)  
[Slides](https://slides.com/ingridmunnecollado/project-3refugees-and-media)  
[Trello](https://trello.com/b/viApEXtv/ih-da-project-3)  