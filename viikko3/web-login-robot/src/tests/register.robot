*** Settings ***
Resource  resource.robot
Suite Setup  Open And Configure Browser
Suite Teardown  Close Browser
Test Setup  Go To Register Page

*** Test Cases ***
Register With Valid Username And Password
    Set Username  ullamaija
    Set Password  ullamaija123
    Set Password Confirmation  ullamaija123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  ul
    Set Password  ullamaija123
    Set Password Confirmation  ullamaija123
    Submit Credentials
    Register Should Fail With Message  Username should be atleast 3 characters long

Register With Valid Username And Too Short Password
    Set Username  ullamaija
    Set Password  muki
    Set Password Confirmation  muki
    Submit Credentials
    Register Should Fail With Message  Password should be at least 8 characters long and consist of not only letters

Register With Nonmatching Password And Password Confirmation
    Set Username  ullamaija
    Set Password  ullamaija123
    Set Password Confirmation  ullamaija321
    Submit Credentials
    Register Should Fail With Message  Passwords do not match

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

Submit Credentials
    Click Button  Register

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Password Confirmation
    [Arguments]  ${password}
    Input Password  password_confirmation  ${password}
