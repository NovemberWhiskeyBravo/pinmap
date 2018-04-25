FROM ubuntu

#installing all the softwaressss
RUN apt-get update
RUN apt-get install nmap -y
RUN apt-get install git -y
RUN apt-get install python-pip -y
RUN apt-get install wget -y

# and now the star of the show
RUN pip install python-nmap
RUN wget https://gitlab.com/NovemberWhiskeyBravo/pinmap/raw/master/pinmap.py && chmod +x pinmap.py

# last but not least. Make the folder to store all them hosts in
RUN mkdir out

CMD python pinmap.py
