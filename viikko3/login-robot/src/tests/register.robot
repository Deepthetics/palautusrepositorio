*** Settings ***
Resource  resource.robot
Test Setup  Input New Command And Create User

*** Test Cases ***
Register With Valid Username And Password
    Input Credentials  user  password123

Register With Already Taken Username And Valid Password
    Input Credentials  kalle  password123
    Output Should Contain  User with username kalle already exists

Register With Too Short Username And Valid Password
    Input Credentials  ab  password123
    Output Should Contain  Username must be atleast 3 characters long

Register With Valid Username And Too Short Password
    Input Credentials  user  abcd123
    Output Should Contain  Password must be atleast 8 characters long

Register With Valid Username And Long Enough Password Containing Only Letters
    Input Credentials  user  abcdefgh
    Output Should Contain  Password must not contain only letters

*** Keywords ***
Input New Command And Create User
    Input New Command
    Create User  kalle  kalle123
