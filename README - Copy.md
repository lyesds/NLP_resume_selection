<div align = "center">
<h3>
Extract relevant information from a free format resume and find similar canditates!
</h3>
<img width = "200" src = /images/logo_CV_matcher.png alt="CV matcher">
</div>


<p align="center">
  <a href="#the-project">Project</a> •
  <a href="#data-source">Data source</a> •
  <a href="#how-to-use">How To Use</a> •
  <a href="#process">Process</a>
</p>

### The project

The aim of this (learning) project is to:
- extract information from free format resumes (CVs) so that this information can be easily processed
- match a given resume with the 10 closest ones (from a pool of available resumes) from a HR perspective

A user-friendly dashboard will showcase the findings.

### Data source

The reumes used to build this project are the **PDFs files** available at the following repository: [CV data](https://github.com/arefinnomi/curriculum_vitae_data).
Please note that PDFs made of image or irrelevant files that show portofolios are excluded.

### How to use

For end users, just go to the [dashboard]() online.
Here is a short [video](https://drive.google.com/file/d/1-HITNWd6FTxbfezE8n1gyZ2IN_Wb1EET/view?usp=sharing) of how it looks like. Enjoy!

For developers, you'll need [Python](https://www.python.org/) installed on your computer to clone and run this application.
From your command line:
```
# Clone this repository
$ git clone https://github.com/harozudu/NLP_resume_selection

# Go into the repository
$ cd NLP_resume_selection

# Install dependencies
$ pip install requirements.txt

# Run the streamlit app
$ streamlit run streamlit_app.py.py
```

### Process

**Information extraction**
- [X] Personal info: name, email, phone number, address
- [X] Education (title + institution)
- [X] Previous job titles (or work experience)
- [X] Skills (or certifications)
- [X] Hobbies
- [X] Languages

**Match CVs**
- [X] NLP (natural language processing) TF-IDF (term frequency, inverse document frequency) similarity
- [X] Network ks


---
> GitHub [@harozudu](https://github.com/harozudu) + [@lyesds](https://github.com/lyesds)
>
> LinkedIn [[@lyes](https://www.linkedin.com/in/lyes-rouabah)

