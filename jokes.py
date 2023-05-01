from random import randrange

jokes = ['My wife told me to stop impersonating a flamingo. I had to put my foot down.',
"I went to buy some camo pants but couldn`t find any.",
"I failed math so many times at school, I can`t even count.",
"I used to have a handle on life, but then it broke.",
"I was wondering why the frisbee kept getting bigger and bigger, but then it hit me.",
"I heard there were a bunch of break-ins over at the car park. That is wrong on so many levels.",
"I want to die peacefully in my sleep, like my grandfather… Not screaming and yelling like the passengers in his car.",
"When life gives you melons, you might be dyslexic.",
"Don`t you hate it when someone answers their own questions? I do.",
"It takes a lot of balls to golf the way I do.",
'Russian dolls are so full of themselves.',
"The easiest time to add insult to injury is when you're signing someone's cast.",
'Light travels faster than sound, which is the reason that some people appear bright before you hear them speak.',
"My therapist says I have a preoccupation for revenge. We'll see about that.",
'A termite walks into the bar and asks, "Is the bar tender here?"',
'A told my girlfriend she drew her eyebrows too high. She seemed surprised.',
'People who use selfie sticks really need to have a good, long look at themselves.',
'Two fish are in a tank. One says, "How do you drive this thing?"',
'I always take life with a grain of salt. And a slice of lemon. And a shot of tequila.',
"Just burned 2,000 calories. That's the last time I leave brownies in the oven while I nap."]

def print_joke():
  return print(jokes[randrange(0, len(jokes))])

# prints a random joke from jokes
print_joke()
