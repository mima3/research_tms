*** Settings ***
Library    SeleniumLibrary

*** Test Cases ***
Open Google
    Open Browser    https://www.google.com    Chrome
    Title Should Be    Google
    [Teardown]    Close All Browsers
