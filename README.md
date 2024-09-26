
# MG Bots TextAtRandom API. ✈️
![Header](https://cdn.imgchest.com/files/l7lxcvbm8p7.png)

You are able to host this API yourself as to remove ALL rate limits!

### Things to remember
🪄 Keep the returned watermark intact, don't worry your responses will all be watermark free! Our API's watermark is developer side so if you share your API with others they'll see the watermark 

🕵️‍♂️ Keep the respitory PRIVATE so your keys aren't exposed.

🍷 Use Vercel, that's what this API was made for 

## How to host

🛠️ Import this rep

Go to https://github.com/new/import and import this rep, ensure that it's set to private to protect your API keys 

👨‍🔧 Edit code

in the api folder you'll see index.py you'll need to update it the following code

- Master Key
this bypasses rate limits 

- API Keys
keys with rate limits, you set the amount per seconds, so 15 with 120 would be 15 requests per 2 minutes 

- Fun facts 
There's 20 fun facts already, if you'd like to add more you can.

💾 Commit all changes
Save all your changes

⛰️ Vercel 

If not signed up sign up for https://vercel.com

🏔️ Deploy to Vercel 

Add a new project, select the rep that you created, Select Import and then you'll need to input a unique project name, this will be used for API link, after that is done click "Deploy" and the API will Deploy

⚡ Complete 
If you did all the steps correctly, you now have a self-hostes API, ain't that neat?

## How to USE the API

Base URL: https://(yourwebsitelink)/api
Headers: X-API-KEY

🚀 Endpoints 

**GET /funfact**

Gets a random fact from the funfacts list 


**GET /randomstring**

Get a random string of characters.

URL Parameters

length (required, integer): Length of the random string.

uppercase (optional, boolean): Include uppercase letters (default is false).

lowercase (optional, boolean): Include lowercase letters (default is false).

numbers (optional, boolean): Include numbers (default is false).

special_chars (optional, boolean): Include special characters (default is false).

random_case (optional, boolean): Include both uppercase and lowercase letters randomly (default is false).

You must include at least one boolean as true.

**POST /choosetext**


have the API choose a random choice!

Max of 30 choices

Body

Use "(/)" (without quotes) to separate choices

choices (required, string) your choices!


🪄 Created By MG Bots: A MagicGamer Project 
