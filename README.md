# Whatsapp Mood Monitor

This is a tool for analyising the mood of a Whatsapp group between a certain period of time. 

## Table of contents

1. [Motivation 💡 ](#motivation-💡)
2. [Worklow 🛠️ ](#workflow-🛠️)
3. [To Dos 🤔🤔 ](#to-dos-🤔🤔)
3. [How to use 🔌](#how-to-use-🔌)


## Motivation 💡

I have been joining a lot of students groups  with the thought of keeps tabs on what is going on around the campus. While I do get a lot info on what is going on , I don't have time to read all the ten of thousands of messages that students send in a group. I normally skim around the texts in the group and read the texts that seem usefull , exciting or interesting. While this works and all , I sometimes miss a lot off info and loose context on what people are actaully talking about

Inorder to solve, I could write a script that summarizes the conversations that were made in a day, but at the moment of writing this I am too lazy to do that. Maybe in the future and the project I'm about to introduce is more interesting. While contemplating on biulding a solutiion , I thought that a cool thing to work on now would be to create a sentiment analysis tool that would analyize the mood of the group chats between a given time. I can use this to track the sentiment of messages using some analysis tools, and visualize the trends and perphas indentify what caused the mood. Prety Cool stuff if I say so myself

## Workflow 🛠️

- The script recies the name of the group and time period as its input
- An sentiment analysis the text message from those group and outputs data from it
- Use data to plot changes in the mood in a given period. (More insights could be generated. Check [TO DO Section](#to-dos-🤔🤔))

For a more indepth explanation of the world read this **[DOC](docs/README.md)**
## Current limitations
- Scraping Whatsapp is not an easy workout. Currently, the number of chats scraped is limited to the chats that are loaded without syncing. This can be solved by waiting for the client to sync with server.

## To Dos 🤔🤔

- Create a network graph of interactions to view connection between members in the convo
- Sentiment analyis of most active members in the group
- Find the topics that cause a change in the mood the group
- Generate a model to predict how certain topics , words , members can change the mood of the group
- Analyse how different groups responses to certain topics
- Add More To Dos

## How to use 🔌

