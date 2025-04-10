import marvin
import os

MARVIN_OPEN_AI_KEY = os.getenv('MARVIN_OPEN_AI_KEY')

image1 = marvin.Image("https://images.pexels.com/photos/1805164/pexels-photo-1805164.jpeg")
image2 = marvin.Image("https://images.pexels.com/photos/220938/pexels-photo-220938.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2")
image3 = marvin.Image("https://images.pexels.com/photos/326012/pexels-photo-326012.jpeg?auto=compress&cs=tinysrgb&w=1260&h=750&dpr=2")

animal_1 = marvin.classify(image1, labels=["zebra", "tiger", "umbrella"], instructions='What kind of animal is this?')
#animal_2 = marvin.classify(image2, labels=['dog', 'rabbit'], instructions='Is this a dog?')
#animal_3 = marvin.classify(image3, labels=['dog', 'cat'], instructions='Is this a dog?')


print(animal_1)
#print(animal_2)
#print(animal_3)
# assert animal == 'dog'



# # img = marvin.Image('https://upload.wikimedia.org/wikipedia/commons/d/d5/Retriever_in_water.jpg')

# # animal = marvin.classify(
# #     img, 
# #     labels=['dog', 'cat', 'bird', 'fish', 'deer']
# # )

# # dry_or_wet = marvin.classify(
# #     img, 
# #     labels=['dry', 'wet'], 
# #     instructions='Is the animal wet?'
# )