#whether the BMI of person who gets stroke is greater than 25
with(subset(stroke,stroke==1),t.test(bmi, mu = 25,alternative="greater"))
#The mean BMI of person who get stroke is greater than the mean BMI of person who does not get stroke
with(subset(stroke,stroke==1),sd(bmi))
with(subset(stroke,stroke==0),sd(bmi))
with(stroke,t.test(bmi~stroke))#
2.982e-06/2
#==> We can conclude that  the mean of the stroke patient is higher than the mean BMI of a person who does not have a stroke
#95%confidence interval for getting stroke

bmi_lm = with(stroke,lm(bmi~avg_glucose_level))
summary(bmi_lm)


with(stroke,plot(bmi~avg_glucose_level))
#confint(my_lm,level=.9)
summary(my_lm)
#graphic
plot(my_lm)

with(subset(stroke,stroke==1),confint(t.test(bmi,conf.level=.9)))
with(subset(stroke,stroke==1),confint(t.test(bmi,conf.level=.95)))
#how many obs, what's te data is, qualitative,quantitative, 
#why we test this point? What's conclusion of result?
with(subset(stroke,stroke==1),confint(t.test(bmi,conf.level=.95)))
