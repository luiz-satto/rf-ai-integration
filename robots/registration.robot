*** Settings ***
Library    Browser

Suite Setup    New Browser    chromium    No
Suite Teardown      Close Page

*** Variables ***
${BASE_URL}         https://stage.artima.ai/Identity/Account/Register
${EMAIL_INPUT}      css=input[name='Input.Email']
${SUBMIT_BUTTON}    css=button[type='submit']
${VALID_EMAIL}      user@example.com
${INVALID_EMAIL}    userexample.com

*** Test Cases ***
Valid Email Should Be Accepted
    New Page     ${BASE_URL}
    Fill Text    ${EMAIL_INPUT}    ${VALID_EMAIL}
    Click        ${SUBMIT_BUTTON}
    Email Submission Should Be Successful

*** Keywords ***
Wait Until Page Is Ready
    Wait For Condition    return document.readyState == 'complete'

Email Submission Should Be Successful
    Wait Until Page Is Ready
    # Add any additional checks for successful submission, such as URL change, message appearance, etc.

Email Submission Should Fail
    Wait Until Page Is Ready
    # Add checks for specific error message related to email validation.
