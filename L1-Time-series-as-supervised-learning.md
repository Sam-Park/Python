Time Series as supervised learning
Time series problems are different to traditional prediction problems. The addition of time adds an order to observations that both must be preserved and can provide additional information for learning algorithms. A time series dataset may look like

time, Observation
day1, obs1
day2, obs2
day3, obs3

we can reframe this data as a supervised learning problem with inputs and outputs to be predicted. for example

Input, Output
?, obs1
obs1, obs2
obs2, obs3
obs3, ?

you can see that the reframing means we have to discard some rows with missing data. Once it is reframed, we can apply all of our favorite learning algorithms like k-Nearest Neighbors and
random forest