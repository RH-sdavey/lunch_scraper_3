*** Settings ***
Documentation     Testcases for Home page
Library    SeleniumLibrary
Resource    keywords.robot
Suite Setup    Open new browser on Home Page (no base route)
Suite Teardown    Close browser


*** Variables ***
${Browser}    GC


*** Test Cases ***
Home page (no base route) loads as expected
    [Documentation]    Home Page Loads as expected in new browser instance
    User Navigates to Home Page (no base route)
    Home page loads as expected

All Base Routes load Home page correctly
    [Documentation]    Check home page is loaded correctly by multiple base routes
    User navigates to Home Page (/home.html)
    Home page loads as expected
    User navigates to Home Page (/index.html)
    Home page loads as expected

L Icon displayed
    element should be visible    xpath://img[@class="social_icon"]

All city buttons are visible
    [Documentation]    Buttons for each city are visible to user on home page
    element should be visible    //button[text()='Go To Brno']
    element should be visible    //button[text()='Go To Olomouc']
    element should be visible    //button[text()='Go To Ostrava']

Go to Brno
        [Documentation]    Click on Go To Brno button
        User Navigates to Home Page (no base route)
        Go to City page    brno
        Wait Until Page Contains    Brno is a city in the South Moravian Region of the Czech Republic

Go to Olomouc
        [Documentation]    Click on Go To Olomouc button
        User Navigates to Home Page (no base route)
        Go to City page   olomouc
        Wait Until Page Contains    Olomouc has about 100,000 inhabitants

Go to Ostrava
        [Documentation]    Click on Go To Ostrava button
        User Navigates to Home Page (no base route)
        Go to City page    ostrava
        Wait Until Page Contains    Ostrava is the capital of the Moravian-Silesian Region
