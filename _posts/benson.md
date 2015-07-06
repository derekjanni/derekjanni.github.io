---
layout: post
title: How To Get Noticed In The City.
---

If you've ever ridden a New York City subway, you've seen that there are a *lot* of people that use these things. It's not hard to see why: they're dirty, hot, jam-packed with pissed off commuters.. wait.. actually it's that they're the only way to get around here that doesn't risk you getting rammed into the guardrails of the BQE.

If you're a person who wants to take advantage of the thousands of people getting on the subway every day across the city, you've got quite the task on your plate. Say you're one of those sad people handing out flyers for your event. With hundreds of stops and millions of people flowing through the city each month, finding the best place to stand to get the most people to take your flyer and throw it in the trash, you're going to have to pick from a huge array of places to stand.

Even worse, if you're trying to get *rich* New Yorkers to contribute to the cause, you're going to have to figure out which subways they frequent (you'll probably want a way to make them less pissed off too). Lets start by looking at which subways saw the most monthly traffic in June:

![Distribution of Subway Entrances In June By Station]()

Since these `matplotlib` labels are particularly unreadable, here's the top 5 what we're looking at:


| Station Name | Total June Entry Traffic |
|-------------:|:------------------------:|
| 42 St. Grand Central Stn. - Lines: 4567S | 3794145| 
| 34 St. Herald Square - Lines BDFMNQR | 2981461 |
| 42 St. Times Sqaure - Lines 1237ACENQRS| 2267054 | 
| 34 St. Penn Station - Lines ACE | 2113730 | 
| 42 St. Port Authority Bus Terminal - Lines ACENQRS1237 | 2035646 | 

Great. What about particular times of the day? If you're going to be successful in your campaign, you need to know the _exact_ point in spacetime where you're supposed to be to get the most rich New Yorkers to hand over their money. As it turns out, this was one of the more interesting parts of the investigation.

If you look at MTA's raw data (link), you'll see something odd - the data is reported roughly every 4 hours in batches. In the aggregate, you get data points from almost every minute of the day, but there are huge clusters that fall at times like 12pm, 4pm, and 8pm since these are the "normal" reporting times for the terminals. Another `matplotlib` graphic

~[Rough Distribution MTA Subway Entrances by Time of Day in June]()

The problem with this view is that these bins don't tell you a whole lot - when you look at the first spike around 8-9am, you're really seeing the number of people who arrived in the 4-hour chunk of time prior to the data being reported. What if you could smooth this out into a more shapely distribution?

It turns out you can: you just to take an average. There are few data points that fall at a time like 2:30am, and lots that fall at the standard times (12am, 4am, 8am, 12pm, 4pm, 8pm) - what if we just took the number of people entering (in total) and divided that by the number of datapoints we have? That would help to eliminate the peaks (and nasty scaling) seen in the above graph!

![Smoothed Distribution of MTA Subway Entrances by Time of Day in June]()



<iframe width="700" height="530" frameborder="0" scrolling="no" marginheight="0" marginwidth="0" src="http://yongcho.maps.arcgis.com/apps/Embed/index.html?webmap=fb685d8082c64d7c94ff27e23434e8c5&amp;extent=-74.0967,40.6705,-73.7794,40.8128&amp;zoom=true&amp;scale=true&amp;theme=light"></iframe>


