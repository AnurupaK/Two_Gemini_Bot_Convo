# Two_Gemini_Bot_Convo

This project involves two Gemini models, Gemi and Gemo, conversing with each other. The project leverages Google Cloud Platform (GCP) and Google AI Studio to create and manage the models. The application is structured with a backend built in Flask, a frontend using HTML/CSS/JavaScript, and it is deployed on Vercel. The bots can currently be assigned different roles to act on, and future functionalities will include start/stop buttons, user-defined roles, and using tuned models with custom datasets.

## Project Structure

```
Two Gemini Convo
│
├── AI_Service
│   └── gemini_response.py        # Handles communication with the Gemini models
│
├── Backend
│   └── app.py                    # Flask backend managing API endpoints and logic
│
├── Frontend
│   ├── static
│   │   ├── style.css             # CSS styles for the frontend
│   │   ├── script.js             # JavaScript handling frontend interactions
│   │   └── images files          # Image files used in the frontend
│   │      
│   └── templates
│       └── index.html            # Main HTML file for the frontend
│
├── .env                          # Environment variables including API keys
├── requirements.txt              # Python dependencies
├── vercel.json                   # Building dependencies in vercel
│
└── README.md                     # Project documentation
```

## Features

- **Role Assignment**: Gemi and Gemo can be assigned different roles for their conversation.
- **Future Enhancements**:
  - Start and stop buttons for the conversation.
  - User-defined roles for the bots.
  - Integration of tuned models with custom datasets.

## Setup and Installation

### Prerequisites

- Python 3.8+
- Flask
- Google Cloud Platform (GCP) account
- Google AI Studio project with API key

### Installation

1. **Clone the repository:**
   ```sh
   git clone https://github.com/your-username/two-gemini-convo.git
   cd two-gemini-convo
   ```

2. **Set up the Python environment:**
   ```sh
   python -m venv venv
   venv\Scripts\activate  #On windows
   pip install -r requirements.txt
   ```

3. **Configure environment variables:**
   Create a `.env` file in the root directory and add your GCP project details and API key.
   ```
   GOOGLE_API_KEY=your-api-key
   ```

### Running the Application Locally

1. **Start the Flask backend:**
   ```sh
   cd Backend
   python app.py
   ```

2. **Open the UI:**
  Click on your localhost to see the application interface ```http://127.0.0.1:5000```

### Deployment

To deploy the project on Vercel:

1. **Go to Vercel's website** and sign in to your account.
2. **Create a new project** and import your GitHub repository.
3. **Add the necessary environment variables** (e.g., `GOOGLE-API-KEY`).
4. **Deploy the project** directly through Vercel's interface.

## Usage

- Open the deployed application in your web browser.
- Assign roles to Gemi and Gemo using the provided interface.
- Initiate the conversation and observe the interactions between the bots.

## Future Enhancements

- **Start/Stop Buttons**: Allow users to start and stop the conversation.
- **User-Defined Roles**: Enable users to define custom roles for Gemi and Gemo.
- **Tuned Models**: Incorporate tuned models trained on specific datasets for more accurate responses.

## Contributing

Contributions are welcome! Please fork the repository and create a pull request with your changes.

## License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

## Acknowledgements

- [Google Cloud Platform](https://cloud.google.com/)
- [Google AI Studio](https://ai.google/studio/)
- [Flask](https://flask.palletsprojects.com/)
- [Vercel](https://vercel.com/)

## Demo



https://github.com/user-attachments/assets/77db59d8-7e20-4c9e-a86c-5bdcca48fcb9





