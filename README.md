# P-P-P
Spatio-Temporal Modeling: Point process prediction for mortals :shipit:

Silver Medal Winner for [STEAM](https://www.rit.edu/cla/criminaljustice/cpsi/steam-prize) $2500 Prize! :tada: :tada: :confetti_ball: 

[Imagine RIT](https://www.rit.edu/cla/criminaljustice/sites/rit.edu.cla.criminaljustice/files/images/Winner%20poster.pdf)

[RIT NEWS](http://www.rit.edu/news/story.php?id=66780)
## Introduction

Burglaries, earthquakes, and tweets all have a particular characteristic in common.  The occurrence of one event increases the probability of subsequent events.  Earthquakes can produce aftershocks,tweets can produce subsequent re-tweets, and burglaries follow the same behavior.  

Self Exciting Point Processes(SEPP) models are built with this behavior in mind.  This is an open source implementation of SEPP technology for police departments.

## How to use it?
1.Find crime data of your city. [Example](https://data-rpdny.opendata.arcgis.com/datasets/rpd-part-i-crime-2011-to-present)

2.Import data to R.

3.Run our [code](http://htmlpreview.github.io/?https://github.com/Italosayan/P-P-P/blob/master/docs/final_analysis.html)
          ([pdf version](https://github.com/Italosayan/P-P-P/blob/master/final_analysis.pdf))

Our UI:

![](https://github.com/Italosayan/P-P-P/blob/master/Graphics/MapApp_Example.gif)

Extra Visualization(Carto):

![](https://github.com/Italosayan/P-P-P/blob/master/Graphics/crimedataset%20(1).gif)

## Helpful Links
UCLA Statistics work: http://www.stat.ucla.edu/~frederic/papers/crime1.pdf

Our Report: https://github.com/Italosayan/P-P-P/blob/master/Burglary%20Pattern%20Prediction%20Report.pdf

Our R code: http://htmlpreview.github.io/?https://github.com/Italosayan/P-P-P/blob/master/Analysis_Code/final_analysis.html

Slides Presentation: https://github.com/Italosayan/P-P-P/blob/master/Crime%20Pattern%20Prediction%20Presentation.pdf

Web App code : https://github.com/Italosayan/P-P-P/tree/master/MapApp

Download visualization of the San Antonio dataset: https://github.com/Italosayan/P-P-P/blob/master/Graphics/crimedataset.mov

Mohler's explanation: https://vimeo.com/50315082

## Visualizations
G Function Distribution San Antonio Data:

![](https://github.com/Italosayan/P-P-P/blob/master/Graphics/Rplot.png)

U Function Distribution San Antonio Data:

![](https://github.com/Italosayan/P-P-P/blob/master/Graphics/Rplot01.png)

Lambda Function Distribution San Antonio Data:

![](https://github.com/Italosayan/P-P-P/blob/master/Graphics/Rplot02.png)

We choose the points with the highest lambda value as the risky ones.

## *Contributors:*

Italo Sayan: ixs3409@rit.edu

Nathan Raw: nxr9266@rit.edu

