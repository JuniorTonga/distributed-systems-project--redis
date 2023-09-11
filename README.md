The aim of the project is to implement an URL Shortener and Decoder. 
it will be able to that the following tasks : 

1. When an user gives a URL in standard format, in addition to their e-mail as an authentication token, the system should return a shortened URL, by:
    - checking if a short version for the same URL already exists, and
    -  if the short version does not exist, it should generate and record the link between the long URL and the short one
2. When an user gives a short URL, the system should return the long version if it exists, and an error if it is not the case.

3. The system should record statistics:
    - how many URLs have been inserted, pe user, and 
    - how many requests were made for each short URL