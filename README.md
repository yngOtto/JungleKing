# JungleKing

JungleKing is a League of Legends (LoL) application that leverages the Riot Games API to provide players with a competitive advantage when playing the Jungle role in the game. It presents key statistics and information about your summoner and others, helping you make informed decisions and strategies.

## Technologies Used

- Python
- Flask
- RiotWatcher Python library
- Angular

## Prerequisites

Before you can run the JungleKing application, you need to obtain an API key from Riot Games. You can get this key by following the instructions on the [Riot Developer Portal](https://developer.riotgames.com/).

Additionally, make sure you have the following software installed:

- Python 3.x
- Node.js and npm (for the Angular frontend)
- Git

## Installation and Setup

1. Clone the repository to your local machine using Git:  
   ```
   git clone https://github.com/yngOtto/JungleKing.git
   ```

2. Navigate into the cloned repository:  
   ```
   cd JungleKing
   ```

3. Create a virtual environment and activate it (optional, but recommended):  
   ```
   python -m venv env
   source env/bin/activate  # For Windows, use `env\Scripts\activate`
   ```

4. Install the Python dependencies:  
   ```
   pip install -r requirements.txt
   ```

5. Navigate to the frontend directory and install the Angular dependencies:  
   ```
   cd frontend
   npm install
   ```

## Configuration

Create a `config.ini` file in the root of the repository with the following structure:

```
[RIOT]
api_key = your_riot_api_key
```

Replace `your_riot_api_key` with the API key you obtained from the Riot Developer Portal.

## Running the Application

1. Start the Flask backend:  
   ```
   python main.py
   ```

2. In a separate terminal, navigate to the frontend directory and start the Angular frontend:  
   ```
   cd frontend
   npm start
   ```

3. Open your web browser and navigate to `http://localhost:4200` to view the application.

## Contributing


## License

This project is released under the MIT License.

## Acknowledgements


