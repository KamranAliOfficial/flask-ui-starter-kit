UI/UX Project
This is a modern web application showcasing a responsive frontend built with HTML, CSS, and JavaScript, powered by a Flask (Python) backend. The project demonstrates user authentication, a contact form with validation, a dynamic portfolio, and an admin dashboard for managing form submissions.
Table of Contents

Features
Technologies Used
Setup Instructions
Project Structure
Screenshots
How to Capture Screenshots
Usage
API Endpoints
Contributing
License

Features

User Authentication: Secure login/registration with password hashing.
Contact Form: Client- and server-side validation for user submissions.
Dynamic Portfolio: Showcase projects with titles, descriptions, and images.
Admin Dashboard: View contact form submissions (requires login).
Responsive Design: Mobile-friendly UI with smooth animations and CSS Grid.
RESTful API: Endpoint to retrieve project information.

Technologies Used

Frontend:
HTML5, CSS3, JavaScript
Jinja templating for dynamic content
Responsive design with CSS variables and media queries


Backend:
Flask (Python) framework
SQLite database for users, submissions, and portfolio data
Werkzeug for secure password hashing


Other:
JavaScript for form validation and smooth scrolling
Custom CSS with animations (fadeIn, slideIn)



Setup Instructions

Clone the Repository:
git clone <repository-url>
cd ui-ux-project


Install Dependencies:Ensure Python 3.8+ is installed, then run:
pip install flask werkzeug


Initialize the Database:The SQLite database (database.db) is automatically created and populated with sample portfolio data on startup.

Run the Application:
python professional_flask_ui.py

Access the app at http://localhost:5000.

Access the Application:

Open http://localhost:5000 in a browser.
Register a new account or log in to access the dashboard.



Project Structure
ui-ux-project/
├── static/
│   ├── scripts.js        # JavaScript for form validation and smooth scrolling
│   ├── style.css        # CSS styles with responsive design
│   └── images/          # Store project images and screenshots
│       └── screenshots/ # Recommended folder for screenshots
├── templates/
│   ├── index.html       # Homepage
│   ├── about.html       # About page
│   ├── contact.html     # Contact form page
│   ├── dashboard.html   # Admin dashboard
│   ├── login.html       # Login and registration page
│   └── portfolio.html   # Portfolio showcase
├── professional_flask_ui.py # Main Flask application
├── utils.py                 # Utility functions (welcome message, form processing)
├── database.db              # SQLite database (auto-generated)
└── README.md                # Project documentation

Screenshots
Below are placeholders for screenshots of the key pages. To include actual screenshots, follow the instructions in the How to Capture Screenshots section.
Homepage
Description: Displays the welcome message and key features with a clean, responsive layout
