# If a runner runs 10 miles in 30 minutes and 30 seconds,
# What is their average speed in kilometers per hour?
# (Tip: 1 mile = 1.6 km)
km_distance = 10 * 1.6
min_to_hours = 30 / 60
seconds_to_hours = 30 / 3600
hour_time = min_to_hours + seconds_to_hours
kilometers_per_hour = km_distance / hour_time
print(kilometers_per_hour)