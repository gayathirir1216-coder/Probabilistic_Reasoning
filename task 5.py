# Weather Prediction using Bayes' Theorem

total_days = 20
rain_days = 8
not_rain_days = 12
cloudy_rain = 7
cloudy_not_rain = 3
p_rain = rain_days / total_days
p_not_rain = not_rain_days / total_days
p_cloudy_given_rain = cloudy_rain / rain_days
p_cloudy_given_not_rain = cloudy_not_rain / not_rain_days
p_cloudy = (p_cloudy_given_rain * p_rain) + \
           (p_cloudy_given_not_rain * p_not_rain)
p_rain_given_cloudy = (p_cloudy_given_rain * p_rain) / p_cloudy
p_not_rain_given_cloudy = (p_cloudy_given_not_rain * p_not_rain) / p_cloudy
print("P(Rain) =", p_rain)
print("P(Not Rain) =", p_not_rain)
print("P(Cloudy | Rain) =", p_cloudy_given_rain)
print("P(Cloudy | Not Rain) =", p_cloudy_given_not_rain)
print("P(Rain | Cloudy) =", p_rain_given_cloudy)
print("P(Not Rain | Cloudy) =", p_not_rain_given_cloudy)
if p_rain_given_cloudy > p_not_rain_given_cloudy:
    print("Predicted Weather = Rain")
else:
    print("Predicted Weather = Not Rain")


#-----------------SHORT EXPLAINATION------------------

# This Python program predicts the weather condition using Bayes’ Theorem.
# First, the program defines the total number of days, rainy days, non-rainy days, and the number of cloudy days under each condition. 
# It calculates the prior probabilities of Rain and Not Rain by dividing their respective days by the total number of days. 
# Then, it calculates the conditional probabilities P(Cloudy | Rain) and P(Cloudy | Not Rain). 
# Using these values, the program calculates the probability of cloudy weather and applies Bayes’ Theorem to find P(Rain | Cloudy) and P(Not Rain | Cloudy).
# Finally, the program compares both probabilities. Since P(Rain | Cloudy) is higher than P(Not Rain | Cloudy), the program predicts the weather as Rain.


