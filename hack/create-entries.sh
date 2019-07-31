#!/usr/bin/env bash

echo -n "ADMIN_TOKEN: "; read -s TOKEN ; echo

curl -sX POST localhost:8000/quote -H "ADMIN-TOKEN: $TOKEN" -d \
'
{
    "msg": "Make friends first, Make sales second, Make love third - In no particular order.",
    "src": "Michael Scott - Regional Manager, Dunder Mifflin Paper Company",
    "src_mat": "The Office: Season 6 - The Delivery, Part 2"
}
' | python -m json.tool

curl -sX POST localhost:8000/quote -H "ADMIN-TOKEN: $TOKEN" -d \
'
{
    "msg": "... you must always have respect for your competitor, but don'\''t be in awe. Go and compete.",
    "src": "Satya Nadella - CEO, Microsoft",
    "src_mat": "Hit Refresh"
}
' | python -m json.tool

curl -sX POST localhost:8000/quote -H "ADMIN-TOKEN: $TOKEN" -d \
'
{
    "msg": "[The tech] industry does not respect tradition - it only respects innovation.",
    "src": "Satya Nadella - CEO, Microsoft",
    "src_mat": "Email to Microsoft Employees"
}
' | python -m json.tool

curl -sX POST localhost:8000/quote -H "ADMIN-TOKEN: $TOKEN" -d \
'
{
    "msg": "The biggest risk is not taking any risk... In a world that changing really quickly, the only strategy that is guaranteed to fail is not taking risks.",
    "src": "Mark Zuckerberg - CEO, Facebook"
}
' | python -m json.tool

curl -sX POST localhost:8000/quote -H "ADMIN-TOKEN: $TOKEN" -d \
'
{
    "msg": "It'\''s not about working harder; it'\''s about working the system.",
    "src": "Evan Spiegel - CEO, Snapchat"
}
' | python -m json.tool

curl -sX POST localhost:8000/quote -H "ADMIN-TOKEN: $TOKEN" -d \
'
{
    "msg": "Do you feel good in your role? If yes, that'\''s the perfect time for you to experiment with something new, to get out of your comfort zone.",
    "src": "Pierre Nanterme - former CEO, Accenture"
}
' | python -m json.tool