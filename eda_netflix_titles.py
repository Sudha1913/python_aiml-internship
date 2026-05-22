# NETFLIX DATASET 

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

print("NETFLIX EDA PROJECT STARTED")

df = pd.read_csv(r"E:\python aiml\python_aiml_sub\netflix_titles.csv")

print("\n FIRST 5 ROWS ")
print(df.head())

print("\n LAST 5 ROWS ")
print(df.tail())

print("\n DATASET SHAPE ")
print(df.shape)

print("\n TOTAL RECORDS ")
print(len(df))

print("\n COLUMN NAMES ")
print(df.columns)

print("\n DATASET INFO ")
print(df.info())

print("\n NULL VALUES ")
print(df.isnull().sum())

print("\n DUPLICATE VALUES ")
print(df.duplicated().sum())

df.drop_duplicates(inplace=True)

print("\n DUPLICATES REMOVED ")

df.fillna("Unknown", inplace=True)

print("\n MISSING VALUES FILLED ")

print("\n STATISTICAL SUMMARY ")
print(df.describe())

print("\n MOVIES VS TV SHOWS ")
print(df['type'].value_counts())

plt.figure(figsize=(8,5))

df['type'].value_counts().plot(kind='bar', color='skyblue')

plt.title("Movies vs TV Shows")
plt.xlabel("Type")
plt.ylabel("Count")

plt.show()

print("\n TOP 10 COUNTRIES ")
print(df['country'].value_counts().head(10))

plt.figure(figsize=(10,5))

df['country'].value_counts().head(10).plot(kind='bar', color='orange')

plt.title("Top 10 Countries")
plt.xlabel("Country")
plt.ylabel("Count")

plt.show()

print("\n CONTENT RATINGS ")
print(df['rating'].value_counts())

plt.figure(figsize=(10,5))

df['rating'].value_counts().plot(kind='bar', color='green')

plt.title("Content Ratings")
plt.xlabel("Rating")
plt.ylabel("Count")

plt.show()

print("\n TOP RELEASE YEARS ")
print(df['release_year'].value_counts().head(10))

plt.figure(figsize=(10,5))

df['release_year'].value_counts().head(10).plot(kind='bar', color='purple')

plt.title("Top Release Years")
plt.xlabel("Year")
plt.ylabel("Count")

plt.show()

print("\n TOP 10 DIRECTORS ")
print(df['director'].value_counts().head(10))

plt.figure(figsize=(12,5))

df['director'].value_counts().head(10).plot(kind='bar', color='red')

plt.title("Top 10 Directors")
plt.xlabel("Director")
plt.ylabel("Count")

plt.show()

print("\n TOP 10 GENRES ")
print(df['listed_in'].value_counts().head(10))

plt.figure(figsize=(12,5))

df['listed_in'].value_counts().head(10).plot(kind='bar', color='brown')

plt.title("Top 10 Genres")
plt.xlabel("Genre")
plt.ylabel("Count")

plt.show()

print("\n MOST POPULAR GENRE ")
print(df['listed_in'].mode()[0])

print("\n MOST COMMON RATING ")
print(df['rating'].mode()[0])

recent_movies = df[df['release_year'] > 2015]

print("\n MOVIES RELEASED AFTER 2015 ")
print(recent_movies[['title', 'release_year']].head())

movies = df[df['type'] == 'Movie']

print("\n TOTAL MOVIES ")
print(movies.shape[0])

tvshows = df[df['type'] == 'TV Show']

print("\n TOTAL TV SHOWS ")
print(tvshows.shape[0])

df.to_csv("cleaned_netflix_data.csv", index=False)

print("\n CLEANED DATASET SAVED ")

print("\n FINAL INSIGHTS ")
print("1. Netflix has more Movies than TV Shows.")
print("2. United States has the highest content.")
print("3. TV-MA is the most common rating.")
print("4. Content increased rapidly after 2015.")
print("5. Drama and International Movies are popular genres.")
print("\n EDA COMPLETED SUCCESSFULLY ")
input("\nPress Enter to exit...")