*** Settings ***
Documentation     Testcases for Brno City page
Library    SeleniumLibrary
Resource    ../keywords.robot
Suite Setup    Open new browser on Home Page (no base route)
Suite Teardown    Close browser

*** Variables ***
${Browser}    GC


*** Test Cases ***
