# cheating-tests
This project was made for my CS50x 2018 final project.

## What is it?
Basically a brute force terminal program that analyzes past test answers, with the goal of counting what were the most frequent ones.

My school, puts out online pdfs that contain test answers dated back to 2016. All of this pdfs are avaialbe in the pdf folder. The pdfs were not all standardised, and so establishing a pattern was pretty tricky.

Inside reader.py (the main file), you can see I used pdfminer, to extract the text from pdf, and then filtered it through key words, so that I could retrieve the test answers.

After that, I used the data I got from reader,py, to generate graphs using Jupyter Notebook (matplotlib).

## Output
Here is the graphs with the output of the program (they can be found in [graphs.ipynb](https://github.com/PzanettiD/cheating-tests/blob/master/graphs.ipynb)):

![Graph1](hhttps://imgur.com/Nk2p7aA)


## Motive

I thought that by analyzing the most frequent answer from previous tests, I then could predict future answers. 
