*** Settings ***
Resource  resource.robot
Resource  login_resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page
Test Teardown  Reset Db

*** Test Cases ***
Register With Valid Username And Password
    Input Register Credentials  ullamaija  ullamaija123  ullamaija123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Input Register Credentials  ul  ullamaija123  ullamaija123
    Submit Credentials
    Register Should Fail With Message  Username should be atleast 3 characters long

Register With Valid Username And Too Short Password
    Input Register Credentials  ullamaija  muki  muki
    Submit Credentials
    Register Should Fail With Message  Password should be at least 8 characters long and consist of not only letters

Register With Nonmatching Password And Password Confirmation
    Input Register Credentials  ullamaija  ullamaija123  kullamaija123
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

Login After Successful Registration
    Input Register Credentials  ullamaija  ullamaija123  ullamaija123
    Submit Credentials
    Register Should Succeed
    Go To Login Page
    Input Login Credentials  ullamaija  ullamaija123
    Submit Credentials
    Login Should Succeed

Login After Failed Registration
    Input Register Credentials  pekka  pekka123  pekka321
    Submit Credentials
    Register Should Fail With Message  Passwords do not match
    Go To Login Page
    Input Login Credentials  pekka  pekka123
    Submit Credentials
    Login Should Fail With Message  Invalid username or password

*** Keywords ***
Register Should Succeed
    Welcome Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}

Input Register Credentials
    [Arguments]  ${username}  ${password}  ${password_confirmation}
    Set Username  ${username}
    Set Password  ${password}
    Set Password Confirmation  ${password_confirmation}