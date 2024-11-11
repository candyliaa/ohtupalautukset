*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  testi
    Set Password  testi123
    Set Confirm Password  testi123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  testi123
    Set Confirm Password  testi123
    Submit Credentials
    Register Should Fail With Message  Username too short

Register With Valid Username And Too Short Password
    Set Username  testi
    Set Password  ei
    Set Confirm Password  ei
    Submit Credentials
    Register Should Fail With Message  Password too short

Register With Valid Username And Invalid Password
    Set Username  testi
    Set Password  testitesti
    Set Confirm Password  testitesti
    Submit Credentials
    Register Should Fail With Message  Invalid password

Register With Nonmatching Password And Password Confirmation
    Set Username  testi
    Set Password  testi123
    Set Confirm Password  testi321
    Submit Credentials
    Register Should Fail With Message  Passwords don't match

Register With Username That Is Already In Use
    Set Username  kalle
    Set Password  testi123
    Set Confirm Password  testi123
    Submit Credentials
    Register Should Fail With Message  Username is in use

Login After Successful Registration
    Set Username  testi
    Set Password  testi123
    Set Confirm Password  testi123
    Submit Credentials
    Click Link  Continue to main page
    Click Button  Logout
    Set Username  testi
    Set Password  testi123
    Click Button  Login
    Login Should Succeed

Login After Failed Registration
    Set Username  testi
    Set Password  testi
    Set Confirm Password  testi
    Submit Credentials
    Click Link  Login
    Set Username  testi
    Set Password  testi
    Click Button  Login
    Login Should Fail With Message  Invalid username or password

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirm Password
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation  ${password_confirmation}

Submit Credentials
    Click Button  Register

Register Should Succeed
    Title Should Be  Welcome to Ohtu Application!

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page

Login Should Succeed
    Main Page Should Be Open

Login Should Fail With Message
    [Arguments]  ${message}
    Login Page Should Be Open
    Page Should Contain  ${message}
