*** Settings ***
Resource  resource.robot
Test Setup  Input Register Command

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  ullamaija  ullamaija123
    Output Should Contain  New user registered

Register With Already Taken Username And Valid Password
    Create User  kalle  kalle123
    Input Credentials  kalle  kalle123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  aa  salasana100
    Output Should Contain  Username should be atleast 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  larissa  sala
    Output Should Contain  Password should be at least 8 characters long and consist of not only letters

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  larissa  salasanani
    Output Should Contain  Password should be at least 8 characters long and consist of not only letters