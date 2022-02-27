*** Settings ***
Documentation     Testcases for Files
Library           OperatingSystem

*** Variables ***


*** Test Cases ***
FileSystem: Dirs Exist
    [Documentation]    All needed Dirs Exist
    Log    ${CURDIR}    level=Info
    Check Dir exists    data    scraper    static    templates    tests


*** Keywords ***
Check Dir exists
    [Arguments]    @{paths}
    FOR    ${path}    IN    @{paths}
        Directory Should Exist    ${path}
    END