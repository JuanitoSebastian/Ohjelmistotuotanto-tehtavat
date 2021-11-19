*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Create User And Go To Login Page

*** Test Cases ***
Login With Correct Credentials
    Input Login Credentials  kalle  kalle123
    Submit Credentials
    Login Should Succeed

Login With Incorrect Password
    Input Login Credentials  kalle  kalle321
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

Login With Nonexistent Username
    Input Login Credentials  ullamaija  ullamaija123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Create User And Go To Login Page
    Create User  kalle  kalle123
    Go To Login Page
    Login Page Should Be Open
