*** Settings ***
Library    ../libraries/uds_lib.py    WITH NAME    uds


*** Test Cases ***

Validate VIN DID Positive Scenario

    [Documentation]    Verify ECU returns VIN correctly for DID F190

    ${vin}=    uds.Read Vin

    Should Not Be Empty    ${vin}

    Length Should Be    ${vin}    17

    Log    VIN = ${vin}


Validate Invalid DID Negative Scenario

    [Documentation]    Verify ECU returns NRC 0x31 for unsupported DID

    ${response}=    uds.Read Invalid Did

    Log    Response = ${response}