*** Settings ***
Documentation     Testcases for Brno City page
Library    SeleniumLibrary
Resource    ../keywords.robot
Suite Setup    Open new browser on Home Page (no base route)
Suite Teardown    Close browser

*** Variables ***
${Browser}    GC


*** Test Cases ***
City added to breadcrumbs
    go to city page    brno
    element should be visible    id:city-crumb
    element should not be visible    id:district-crumb
    element should not be visible    id:restaurant-crumb
