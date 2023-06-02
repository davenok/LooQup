#     LooQup - This program is for amateur radio users and allows lookup of Q codes
#     Copyright (C) 2023  ~ David Burklin

#     This program is free software: you can redistribute it and/or modify
#     it under the terms of the GNU General Public License as published by
#     the Free Software Foundation, either version 3 of the License, or
#     (at your option) any later version.

#     This program is distributed in the hope that it will be useful,
#     but WITHOUT ANY WARRANTY; without even the implied warranty of
#     MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#     GNU General Public License for more details.

#     You should have received a copy of the GNU General Public License
#     along with this program.  If not, see <https://www.gnu.org/licenses/>.


# This file contains a list of dicts of all the q codes

qc = [
    {
        'code': 'QRG',
        'statement': "Your exact frequency (or that of ______) is _________kHz."\
            "\nAs a question - Will you tell me my exact frequency (or that of __________)?"
    },
    {
        'code': "QRL",
        'statement': "I am busy (or I am busy with _________)."\
            "\nAs a question - Are you busy?"\
            "\nUsually used to see if a frequency is busy."
    },
    {
        'code': "QRM",
        'statement': " Your transmission is being interfered with _________"\
            "\n (1. Nil; 2. Slightly; 3. Moderately; 4. Severely; 5. Extremely.)"\
            "\nAs a question - Is my transmission being interfered with?"\
            "\nManmade interference"
    },
    {
        'code': "QRN",
        'statement': "I am troubled by static _________."\
            "\n(1. Nil; 2. Slightly; 3. Moderately; 4. Severely; 5. Extremely.)"\
            "\nAs a question - Are you troubled by static?"\
            "\nNatural interference"
    },
    {
        'code': "QRO",
        'statement': "Increase power.\nAs a question - Shall I increase power?"
    },
    {
        'code': "QRP",
        'statement': "Decrease power.\nAs a question - Shall I decrease power?"\
            "\nIn practice, usually refers to operating a low power mode"
    },
    {
        'code': "QRQ",
        'statement': "Send faster (_________wpm).\nAs a question - Shall I send faster?"
    },
    {
        'code': "QRS",
        'statement': "Send more slowly (_________wpm).\nAs a question - Shall I send slower?"
    },
    {
        'code': "QRT",
        'statement': "Stop sending.\nAs a question - Shall I stop sending?"
    },
    {
        'code': "QRU",
        'statement': "I have nothing for you.\nAs a question - Have you anything for me?"
    },
    {
        'code': "QRV",
        'statement': "I am ready.\nAs a question - Are you ready?"
    },
    {
        'code': "QRX",
        'statement': "I will call you again at ______hours (on ______kHz)."\
            "\nAs a question - When will you call me again?"\
            "\n(Minutes are usually implied rather than hours.)"
    },
    {
        'code': "QRZ",
        'statement': "You are being called by _________ (on ______kHz)."\
            "\nAs a question - Who is calling me?"
    },
    {
        'code': "QSB",
        'statement': "Your signals are fading.\nAs a question - Are my signals fading?"
    },
    {
        'code': "QSK",
        'statement': "I can hear you between signals; break in on my transmission."\
            "\nAs a question - Can you hear me between your signals and if"\
            "\nso can I break in on your transmission?"
    },
    {
        'code': "QSL",
        'statement': "I am acknowledging receipt."\
            "\nAs a question - Can you acknowledge receipt (of a message or transmission)?"
    },
    {
        'code': "QSO",
        'statement': "I can communicate with _________ direct (or relay through ______)."\
            "\nAs a question - Can you communicate with ______ direct or by relay?"
    },
    {
        'code': "QSP",
        'statement': "I will relay to ______.\nAs a question - Will you relay to ______?"
    },
    {
        'code': "QST",
        'statement': "General call preceding a message addressed to all amateurs"\
            "\nand ARRL members. This is in effect CQ ARRL."
    },
    {
        'code': "QSX",
        'statement': "I am listening to ______ on ______kHz."\
            "\nAs a question - Will you listen to ______on ______kHz?"
    },
    {
        'code': "QSY",
        'statement': "Change to transmission on another frequency (or on ______kHz)."\
            "\nAs a question - Shall I change to transmission on another frequency (or on ______kHz)?"
    },
    {
        'code': "QTC",
        'statement': "I have ______messages for you (or for ______)."\
            "\nAs a question - How many messages have you to send?"
    },
    {
        'code': "QTH",
        'statement': "My location is _________.\nAs a question - What is your location?"
    },
    {
        'code': "QTR",
        'statement': "The time is _________.\nAs a question - What is the correct time?"
    }
]

    # {
    #     'code': '',
    #     'statement': ""\
    #         "\nAs a question - ?"
    # },
