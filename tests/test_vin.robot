*** Settings ***
Library    ../libraries/uds_lib.py    WITH NAME    uds

*** Test Cases ***
Validate VIN D I D

    ${vin}=    uds.Read Vin

    Should Not Be Empty    ${vin}

    Length Should Be    ${vin}    17

    Log    VIN = ${vin}

