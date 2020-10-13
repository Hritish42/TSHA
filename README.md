# Totally Secure Hashing Algorithm (T-SHA)
[![forthebadge made-with-python](http://ForTheBadge.com/images/badges/made-with-python.svg)](https://www.python.org/)
[![forthebadge](https://forthebadge.com/images/badges/built-with-love.svg)](https://forthebadge.com)
[![TSHA](https://img.shields.io/static/v1?label=TSHA%20&message=v1.0&color=green")](https://github.com/Hritish42/TSHA)
[![MIT license](https://img.shields.io/badge/License-MIT-blue.svg)](https://lbesson.mit-license.org/)


# 🤔 What is this?

-  Doctoring of documents has been quite common these days.
- Proposed a method to verify fake documents
- Designed and modified the SHA-1 algorithm.
- Collision-free and harder to Brute Force .

## T-SHA features:-

  - ##### Collision resistance
  - ##### Immpossible to Bruteforce
  - ##### Complex algorithm

# It uses:
- Fiestal Ciphers,
- XOR, 
- OR 
- AND operations , 
- Circularshifting , 
- Padding and a-lot of things.
- 160 Rounds. **(Changeable)**
# One round compromises of ...
IMAGE
>Cryptographic functions designed to keep data secured. It works by transforming the data using a hash function: an algorithm that consists of bitwise operations, modular additions, and compression functions. The hash function then produces a fixed-size string that looks totally different from the original. These algorithms are designed to be one-way functions, meaning that once they’re transformed into their respective hash values, it’s virtually impossible to transform them back into the original data. There are a total of 160 rounds in TSHA. 

>A common application of TSHA is to encrypting passwords, as the server-side only needs to keep track of a specific user’s hash value, rather than the actual password. This is helpful in case an attacker hacks the database, as they will only find the hashed functions and not the actual passwords, so if they were to input the hashed value as a password, the hash function will convert it into another string and subsequently deny access. 
>An arbitrary constant of any length is given as input. The **MSG** is passed to SHA1 which gives an output of 160 bits or convert it to 160 bits in the hexadecimal form which is then converted to the binary form of 160 bits. 

>It is then divided into two parts left and right of 80 bits each. The left 80 bit is passed to sha1 twice and converted to 160 bits and is circular shifted 5 bits. This is divided into two 80 bits of named a1 and x1. The right part is passed to sha1 twice and is circularly shifted by 9 bits and passed thrice through sha1. This is divided into two 80 bits of named a2 and x2.

>x1 and x2 are passed through and function which gives an output k1. a1 and a2 is passed through and function which gives an output k2. K1 and k2 are appended together. the given output will go through the same procedure 160 times and the final output will become our hash.

# Method to verify documents:
  - Upload the file on the cloud
  - Get it signed 
  - Export documents as Markdown, HTML and PDF

>In the above scenario, A Organization (university) will register with cloud services and upload the original certification of a person. 

>We will sign a hash using TSHA and store it on our cloud.

>Now, if the same person applies for a job at a company. Then the company can come to our website and verify the document by uploading the same document that person provided them or can directly verify the document stored in our cloud.

# How to use the algorithm and verify for collosion?
>I've made a web application for demonstration of the TSHA , Implemented conversion of text to hash and file signing & verifying Functions. The web application can be found in my repo.

Dillinger uses a number of open source projects to work properly:

* [AngularJS] - HTML enhanced for web apps!
* [Ace Editor] - awesome web-based text editor
* [markdown-it] - Markdown parser done right. Fast and easy to extend.
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framework [@tjholowaychuk]
* [Gulp] - the streaming build system
* [Breakdance](https://breakdance.github.io/breakdance/) - HTML to Markdown converter
* [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### Requirements
- For checking collosion you need to have heavy computation power.
- For using the TSHA all you need is python3 installed. 
```
 sudo apt-get install python3.6
```

### Screenshot of Website


## Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you would like to change.
Please make sure to update tests as appropriate.


License
----

MIT


**Free Software, Hell Yeah!**


