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
    Register Should Fail With Message

Register With Valid Username And Too Short Password
    Set Username  testi
    Set Password  ei
    Set Confirm Password  ei
    Submit Credentials
    Register Should Fail With Message

Register With Valid Username And Invalid Password
    Set Username  testi
    Set Password  testitesti
    Set Confirm Password  testitesti
    Submit Credentials
    Register Should Fail With Message

Register With Nonmatching Password And Password Confirmation
    Set Username  testi
    Set Password  testi123
    Set Confirm Password  testi321
    Submit Credentials
    Register Should Fail With Message

Register With Username That Is Already In Use
    Set Username kalle123
    Set Password testi123
    Set Confirm Password  testi123
    Submit Credentials
    Register Should Fail With Message

*** Keywords ***

Set Username
    [Arguments]  ${username}
    Input Text  username  ${username}

Set Password
    [Arguments]  ${password}
    Input Password  password  ${password}

Set Confirm Password
    [Arguments]  ${password_confirmation}
    Input Password  password_confirmation ${password_confirmation}

Register Should Succeed
    Main Page Should Be Open

Register Should Fail With Message
    [Arguments]  ${message}
    Register Page Should Be Open
    Page Should Contain  ${message}

Reset Application Create User And Go To Register Page
    Reset Application
    Create User  kalle  kalle123
    Go To Register Page
