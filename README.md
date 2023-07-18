# maternalhealthcardstz

## Hi ! this is my Final Year Project at the University Of Dar es Salaam

## About The Project

    Inaccessible maternal health data limits preparedness for birth complications like preclampsia.
    Our solution is to digitize maternal health cards, using the data to develop a machine-learning
    model for predicting Eclampsia.This will enable data-driven decisions and solutions for doctors,
    researchers , innovators and patients themselves.
    
We aim to ensure the solution is adopted by the ministry of health in Tanzania and being used in all hospitals , currently I am doing this project as my final year university project and its my hope the University will help me to scale the solution and assist me in tailoring it to actually meet the needs of Tanzanians.

##  Project Inspiration

    I admire the work done by multiple countries in Europe in digitizing their health care and
    would love to bring that in Tanzania , furthermore after doing research and seeing the 
    potential it holds in improving the healthcare field in a broad way , gives me hope 
    that the project will be a success.


    The concept came about as I was doing self -learning on machine learning , and then an idea 
    crossed my mind about how most hospitals fail to plan beforehand on birth complication issues
    that may arise during delivery and carter the needs of safe delivery , furthermore tracking 
    mothers' recovery and child's growth. Diving deeper made me realize how digital data will be
    able to solve these issues , the sad thing was there we no available maternal digital health
    data to use in developing prediction models , which made to think on a way to transform 
    physical cards to digital cards for researchers , doctors , patients and doctors to use data
    to improve healthcare in general. The solution is unique in a way that we are democratizing
    health data giving more power to the appropriate stakeholders to make decisive data-driven
    decisions , something which is novel in Tanzania.

## Social and Environmental Impact

How does your Project have a positive impact on society and/or the environment?

    The project stakeholders are:

        - Patients
        - Non-governmental Organisations
        - Nurses
        - Doctors
        - Ministry Of Health
        - Hospital facilities
        - Researchers

- The project aims to collect data and make the data available for innovators, researchers and health practitioners. It also helps the patients to get reliable services by planning ahead before delivery with limited resources available in the hospitals.
- The project doesn't need any raw materials it's software-based , which makes it sustainable and environmental friendly.
- The product life cycle adopts the agile development approach , where the software will undergo iterations to meet the needs and demands of the stakeholders.
- The project aligns with UN Sustainable Goals  **SDG3 #GoodHealth&WellBeing**

## SRS (System Requirement Specification) Document

Click here to View the Documentation [SRS Documenation](https://drive.google.com/file/d/1wnWIW4UnEqUynWZbBB_1GGPtLDnz_Bwj/view)

## Call to Action

- Too much time was spent on gathering user requirements and designing mockups to test how the end-users will interact , so as we don't spend too much cost in developing what's irrelevant.  It's my hope that when we get into development will be able to develop a solution that tends to the needs of the stakeholders.
- The journey on developing the product has been all about understanding the stakeholders and the problem present and for the question of feedback , I do believe they will be the best feedback providers through continuous research and product testing.
- Uncertainty remains on the national health data policy and how we can navigate to solve the problem with compliance to rules , laws and regulations pertain data privacy in Tanzania.
- I believe the iteration journey will be exciting since it will be based on iterating to meet the needs of the stakeholders and nothing else is as exciting as building a product that achieves market fit.

## Setting up the project

# DMHCS Django Project Setup Guide

This guide will walk you through the steps to set up the DMHCS Django project on your local machine. Please follow the instructions carefully to ensure a successful setup.

## Prerequisites

Before starting the setup process, please ensure that you have the following prerequisites installed:

- PostgreSQL 15 database (https://www.postgresql.org/download/)
- Python 3.x (https://www.python.org/downloads/)
- Gmail account with an app password enabled (https://support.google.com/accounts/answer/185833)

## Step 1: Clone the Repository

Clone the DMHCS Django project repository from GitHub to your local machine using the following command:

```bash
git clone <repository_url>
```

## Step 2: Create a Virtual Environment

Navigate to the project's root directory and create a virtual environment to isolate the project's dependencies:

```bash
cd dmhcs
python3 -m venv venv
```

## Step 3: Activate the Virtual Environment

Activate the virtual environment using the appropriate command for your operating system:

**Windows:**

```bash
venv\Scripts\activate
```

**macOS/Linux:**

```bash
source venv/bin/activate
```

## Step 4: Install Project Dependencies

Install the project dependencies specified in the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Step 5: Create a .env File

Create a `.env` file in the project's root directory and populate it with the following environment variables:

```plaintext
# database
DB_PASSWORD=<your_database_password>
DB_USER=<your_database_username>
DB_NAME=<your_database_name>

# email
EMAIL_HOST_USER=<your_gmail_account>
EMAIL_HOST_PASSWORD=<your_gmail_app_password>
```

Replace the values in angle brackets with your desired settings. Ensure that you have created a new user and database in PostgreSQL, and the provided credentials match those.

## Step 6: Set Up PostgreSQL Database

Install and set up PostgreSQL on your local machine. Create a new user and database using the credentials specified in the `.env` file.

## Step 7: Perform Database Migrations

Run the following command to perform the initial database migrations:

```bash
python manage.py migrate
```

## Step 8: Create a Superuser

Create a superuser account to access the Django admin interface:

```bash
python manage.py createsuperuser
```

Follow the prompts to provide a username, email, and password for the superuser account.

## Step 9: Run the Development Server

Start the Django development server using the following command:

```bash
python manage.py runserver
```

The DMHCS Django project should now be running locally at `http://localhost:8000/`.

## Step 10: Accessing the Django Admin Interface

To access the Django admin interface, navigate to `http://localhost:8000/admin` and log in using the superuser credentials created in Step 8.

Congratulations! You have successfully set up and launched the DMHCS Django project on your local machine. You can now explore the project and customize it as per your requirements.

**Note:** For security reasons, it is recommended to create a new Gmail app password rather than using your regular Gmail account credentials. Refer to the Gmail documentation (https://support.google.com/accounts/answer/185833) for more information on generating app passwords.

If you encounter any issues during the setup process, please refer to the project's documentation or seek assistance from the project maintainers.
## Project Partners

- University Of Dar Es Salaam [UDSM COICT](https://coict.udsm.ac.tz/)
- Critical Making Mentoring Program [GIG](https://globalinnovationgathering.org/)