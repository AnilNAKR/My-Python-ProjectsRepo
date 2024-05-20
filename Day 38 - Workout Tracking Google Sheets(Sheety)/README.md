# Workout Tracker with Nutritionix and Google Sheets Integration
This Python script enables users to track their workouts by utilizing the Nutritionix API to retrieve exercise data based on user input and the Sheety API to store the workout information in a Google Sheets spreadsheet.

## Features
1) **Nutritionix Integration**: Users can input their workout information, including the type of exercise, weight, height, and age. The script then sends a request to the Nutritionix API to retrieve exercise data such as duration and calories burned.

2) **Google Sheets Integration:** The exercise data obtained from the Nutritionix API is then added to a Google Sheets spreadsheet for tracking purposes. The script utilizes the Sheety API to interact with the Google Sheets API and post the workout information to the specified spreadsheet.

## Usage
1) **Nutritionix API Setup:** Ensure you have registered for the Nutritionix API and obtained the required APP_ID and APP_KEY.

2) **Google Sheets Setup:** Create a Google Sheets spreadsheet to store the workout data. Obtain the Sheety authentication token (SHEETY_AUTH) and specify the username and sheet endpoint accordingly.

3) **Environment Variables:** Set up environment variables for APP_ID, APP_KEY, and SHEETY_AUTH to securely store sensitive information.

4) **Run the Script:** Execute the Python script and input your workout information when prompted. The script will retrieve exercise data from the Nutritionix API and add it to the Google Sheets spreadsheet via the Sheety API.

<hr>
<img src="https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/634bb95f-b60a-46ee-bd75-d1d6e34c2762">
<hr>

https://github.com/AnilNAKR/My-Python-ProjectsRepo/assets/16172853/23bd8a3b-f000-47de-9bb7-624f1224a950

