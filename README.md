# Digit Span Experiment
## App Description
This is a python script made to be hosted by [streamlit.io](https://streamlit.io/) as a website. The app is a digit span experiment made, which saves the data upon completion of the test to this
[google sheet](https://docs.google.com/spreadsheets/d/1dH_LJ24e-yLGhZywKnQnSfYKE75Ad7DHu4sCfZGJL6g/edit#gid=0) using Google Sheets API. The app saves the scores of the user and gives them a uuid. This is free for anyone to use. 
If you wish to use it and save data to your own google sheet you can contact me by email (aleksej.bura.d@gmail.com), I'll provide further guidance. Current hosting of the app
can be found [here](https://share.streamlit.io/spawnthetronix/digit-span-experiment/main/main.py).

## App Specification
When you open website, you're shown a starting page with instructions. After clicking START button you begin the test. The test starts by showing you 3 random integers from 
0-9 inclusevly. After you will be prompted to enter the numbers shown in order without any spaces (e.g. if numbers shown were 3, 5, 1 then you need to enter 351). When you click
next the next sequence of numbers will be shown. If your previous answer was correct, then you will be shown 4 numbers instead of 3, and so on until 10. If your previous answer
was wrong, then you will begin again from 3 numbers. There are 5 attempts in total. At the end of the test your results will be shown to you.

