*** Settings ***
Resource  resource.robot
Suite Setup     Open And Configure Browser
Suite Teardown  Close Browser
Test Setup      Reset Application Create User And Go To Register Page

*** Test Cases ***

Register With Valid Username And Password
    Set Username  testi
    Set Password  testi123
    Set Password confirmation  testi123
    Submit Credentials
    Register Should Succeed

Register With Too Short Username And Valid Password
    Set Username  te
    Set Password  testi123
    Set Password confirmation  testi123
    Submit Credentials
    Register Should Fail With Message

Register With Valid Username And Too Short Password
    Set Username  testi
    Set Password  ei
    Set Password confirmation  ei
    Submit Credentials
    Register Should Fail With Message

Register With Valid Username And Invalid Password
    Set Username  testi
    Set Password  testitesti
    Set Password confirmation  testitesti
    Submit Credentials
    Register Should Fail With Message

Register With Nonmatching Password And Password Confirmation
    Set Username  testi
    Set Password  testi123
    Set Password confirmation  testi321
    Submit Credentials
    Register Should Fail With Message

Register With Username That Is Already In Use
    Set Username kalle123
    Set Password testi123
    Set Password confirmation  testi123
    Submit Credentials
    Register Should Fail With Message

*** Keywords ***

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
