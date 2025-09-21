*** Variables ***
${NAME}        ジョニー
...            なにもできない
...            だれも君を愛さない

*** Test Cases ***
Say Hello
    Log To Console    Hello, ${NAME} ${CURDIR}!
