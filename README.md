# reading-age

This app let you know the reading age of a piece of text

## Plan

### 1. MVP

User can open up the program by clicking on an exe file
User can paste in a text into a textbox, click on a suggest button and they will see the recommended reading age on the bottom of the textbox.

### 2. POC

1.To get a window with a textbox on the screen.

## Research

Use this to get the grade level for US schools:

```
ts = textacy.TextStats(doc)
ts.flesch_kincaid_grade_level
```

Then convert to age using this:

Grade 1 Age 6 - 7
Grade 2 Age 7 - 8
Grade 3 Age 8 - 9
Grade 4 Age 9 - 10
Grade 5 Age 10 - 11
Grade 6 Age 11 - 12
Grade 7 Age 12 - 13
Grade 8 Age 13 - 14
Grade 9 Age 14 - 15
Grade 10 Age 15 - 16
Grade 11 Age 16 - 17
Grade 12 Age 17 - 18
