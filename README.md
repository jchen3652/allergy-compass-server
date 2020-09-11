# Allergy Compass Server
MHacks 12 Project by James Chen and Ankith Udupa. Works in conjunction with [iOS App](https://github.com/ankithu/Allergy-Compass).

# Links
* [YouTube](https://www.youtube.com/watch?v=W9OGRA9Np5w)
* [DevPost](https://devpost.com/software/allergy-compass)
* [Congressional App Challenge](https://stevens.house.gov/media/press-releases/stevens-announces-winner-2019-congressional-app-challenge)

# Purpose
Recieves image URL's from iOS App, sends image to Google Cloud Vision API to determine product in image, scans the [openfoods database](https://github.com/openfoodfacts/openfoodfacts-python) for allergens, and then reports back findings to user.

# Inspiration
We all know someone with an allergy. Having close family members with severe allergies, we decided that, especially for young children, reading long confusing ingredient labels can be daunting. We wanted to simplify that experience.
What it does

Allergy Compass allows users to create profiles describing what kinds of allergies they have then allows them to take images of various food packages, then see if the food in the image contains something they are allergic too.

# How we built it

Allergy Compass is built with swift for iOS devices. It sends images to a remote storage system then communicates with a Django server to get information about the image that it has just captured. The Django server interacts with the Google Vision API to determine if the what the pictured product is. Then it utilizes a nutrition API in conjunction with querying a Firebase user database to determine if the user is allergic to the product they are holding.
Challenges we ran into

# Challenges we ran into
We faced some issues with hosting the Django server at first, as well as the omnipresent difficulties that come using with new technologies. In particular, it was somewhat frustrating to wait for Google's machine learning models to train, but they provided much needed-breaks.
Accomplishments that we're proud of

# What are we proud of?
We are proud of the complexity of the backend that we were able to create. We use a combination of several different services that we had no prior experience with to create a product we are excited about.
What we learned

# What we used
We learned about how to use Google Cloud API's, processing JSON, HTTP requests, designing UI's, writing Swift code, and more.
