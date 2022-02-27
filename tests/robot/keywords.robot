*** Variables ***
${Home page title}    Lunch Scraper - Sean Davey
${Welcome Text Holder}    class:imagebox-desc
${Welcome Text}    Welcome to my Lunch Scraper Application

*** Keywords ***

# ***  HOME PAGE KEYWORDS ***

Open new browser on Home Page (no base route)
    Open Browser    http://127.0.0.1:5000/    ${Browser}

User Navigates to Home Page (no base route)
    Go to    http://127.0.0.1:5000/

User navigates to Home Page (/index.html)
    Go to    http://127.0.0.1:5000/index.html

User navigates to Home Page (/home.html)
    Go to    http://127.0.0.1:5000/home.html

Home page loads as expected
    Title should be    ${Home page title}
    Wait until element is visible    ${Welcome Text Holder}    timeout=5
    Wait until page contains    ${Welcome Text}

Go to City page
    [Arguments]    ${city}
    click link    /${city}

# *** CITY PAGE KEYWORDS ***



