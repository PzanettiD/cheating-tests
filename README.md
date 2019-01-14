# cheating-tests
This project was made for my CS50x final project.
## What is it?
My school, puts out online pdfs that contain test answers dated back to 2016. All of this pdfs are avaialbe in the pdf folder. The pdfs were not all standardised, and so establishing a pattern was pretty tricky.

Inside reader.py (the main file), you can see I used pdfminer, to extract the text from pdf, and then filtered it through key words, so that I could retrieve the test answers.
After that, I used the data I got from reader,py, to generate graphs using Jupyter Notebook (matplotlib).
## Motive
I thought that by analyzing the most frequent answer from previous tests, I then could predict the future answers. 
