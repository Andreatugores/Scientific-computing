# Scientific Computing: Integrating the ATLAS Virtual Machine, ATLAS Open Data Jupyter Notebooks and the Git and Zenodo platforms for Open Science and Reproducibility 

Taking advantage of the open sciene approach of the ATLAS Open Data project and it's tools, for educational purposes, which allow to have an idea of how they perform data analysis in high-energy physics, the project was focused on the automation of the notebooks where these analyzes are carried out and the documentation was expanded to make them easier to understand. In addition, the Git and Zenodo tools were integrated into a program to promote the concepts of open science and reproducibility. 

## Overview
[ATLAS Open Data](https://atlas-opendata.web.cern.ch/atlas-opendata/) is an educational project in High Energy Physics that provides data and tools to high-school, master and ungraduate students, as well as teachers and lectures, to help educate them in physics analysis techniques used in experimental particle physics.

One of the main data files of ATLAS Open Data is the 13 TeV samples, which were released in 2016. As part of the resources available to the public, they are also accompanied by a set of Jupyter notebooks. The ATLAS Open Data Jupyter Notebooks allow data analysis to be performed directly in a web browser by integrating the [ROOT](https://root.cern/about/) framework with the Jupyter Notebook technology, a combination called *ROOTbook*. The frameworks implement the protocols needed for reading the datasets, making an analysis selection, writing out histograms and plotting the results, by only needing to execute the code written in the [Jupyter Notebook](https://jupyter.org/), taking advantage of it's functionalities.

The project is encapsulated in the ATLAS Open Data project, by following and sharing the philosophy behind it. To understand the project, it is necessary to know some important concepts that have revolutionized the scientific world, such as Open Science and Reproducibility. 

Open Science can be defined as a collaborative culture enabled by technology that empowers the open sharing of data, information and knowledge whitin and outside the scientific community to accelerate and make scientific research more accessible. In academic research, researchers are meant to share information in an open manner in order to foster a more scholarly environment. 

On the other hand, one of the pathways by which the scientific community confirms the validity of a new scientific discovery is by repeating the research that produced it. Reproducibility means computational reproducibility, obtaining consistent computational results using the same input data, computational steps, methods, code and conditions  of analysis.

Whe results are produced by complex computational processes using large volumnes of data, the traditional methods section of a scientific paper is insufficient to convey the necessary information for others to reproduce the results. Additional information related to data, code, models, and computational analysis is needed.

This is the reason that as the years progress, tools such as Git and Zenodo have emerged to facilitate the pathways to open science and reproducibility.

[Git](https://git-scm.com/) is open-source version control system. Version control systems keep revisions straight, storing the modifications in a central repository. This allows developers to easily collaborate, as they can download a new version of the software, make changes, and upload the newest revision. Every developer can see these new changes, dowload themn and contribute. 

The other tool, [Zenodo](https://www.openscience.eu/zenodo/), is a general-purpose open-access repository developed under the European OpenAIRE program and operated by CERN. It allows researchers to deposit research papers, data sets, research software, reports, and any other research related digital artifacts. For each submission, the data is assigned a Digital Object Identifier(DOI).

In a way, ATLAS Open Data, Git and Zenodo are means to achieve the same endd: promote Open Science and Reproducibility. But as they can be used to focus on different parts of the process of making scientific research, including it's datasets and code, as available as possible, there is a need to integrate all these tools.

## Problem Statement

Although the ATLAS Open Data website, resources and tools are extensive and well-planned, as the ATLAS Open Data project grows and looks for the improvement of it's contents, looking fot it's flaws and updating it's material has become almost a requirement.

For the correct execution of an ATLAS Open Data Jupyter Notebook, the use of ROOT is necessary, however it was not imported in the beginning of the code for the Python framework-scripts, causing errors in the cells that ordered the run of the analysis.  As this tool is required, the ATLAS project provides a virtual machine that integrates ROOT into Jupyter Notebook.

The last update of the ATLAS Open Data Jupyter Notebooks, although containing the necessary code to run any of the 12 analysis from the 13 TeV ATLAS Open Data physics analysis examples, was focused on presenting two analysis of the data corresponding to the HZZAnalysis and the HyyAnalysis folders. To access the other examples, the user had to modify the code, and although it represented insignificant changes, it could always end up in errors and unexpected outputs.

In addition to that, there was a lack of the proper documentation inside the notebooks, both from the physical aspects of the analysis and from the commands in the code. These weak points meant a longer process of learning for the less experienced and knowledgeable users of these Jupyter Notebooks series.

On a side part, even when ATLAS has a platform to create code, run analysis, and get data from their ATLAS Open Data, which is the ATLAS Virtual Machine (VM), this was not fully integrated to the Jupyter Notebooks in the sense that the mention of the ATLAS VM did not describe it in an accurate way, that presents it as an extraordinary tool to run the ATLAS Open Data Jupyter Notebooks and to later created original content from ATLAS Open Data. The ATLAS VM was also not introduced clearly in the original README file. For students who accessed the ATLAS GitHub repository before the ATLAS Open Data website, the information and tutorials of the VM would remain unknown until they navigate to the other sites.

Finally, even though the philosophy behind ATLAS Open Data is about Open Science and Reproducibility, there is no information available for the user of at least some platforms to make science more shareable and discoverable. Even when Git is a well known software for version control that facilitates scientific reproducibility, not all students are Git users, and not all students are familiar with executing commands in a terminal, or have a complete understanding of the basic git commands.

Going beyond the code, the need of sharing, citing and the DOI versioning in the scientific community is constantly growing. Although it is not required, or needed, for the ATLAS Open Data website to include options for scientists to help in the publishing of their contributions, CERN is part of the organizations that fund Zenodo. 

## Methodology 

Starting first with the ATLAS Open Data Jupyter Notebooks, the material to improve was the collection of Jupyter Notebooks that run the analysis frameworks at 8 TeV and 13 TeV  from the ATLAS Outreach Data tools. As this collection is extensive, to narrow the content to ameliorate, the selected notebooks were the ATLAS Open Data Python 13TeV framework-script, which show two examples of physics analysis (HZZAnalysis and HyyAnalysis), executed by a similar code. 

Considering interactive content as a powerful resource that provides a unique experience to users and manages to retain their attention more efficiently, an approach of making the code more interactive was decided to be the best way to improve the Jupyter Notebooks.

Python packages are the fundamental unit of shareable code in Python, and they make it easy to reuse your code; maintain it and share it with your colleagues and the wider Python community. By taking this into account, being sure that all the needed packages were imported at the beginning of the notebook was an important step to guarantee that the analysis and plotting would take place when their corresponding commands were executed by the user.

Apart from the previous required packages, new libraries were added, such as [pandas](https://pandas.pydata.org/pandas-docs/stable/) and [matplotlib](https://matplotlib.org/), to be able to use DataFrames to store information of the analysis, and to show the histograms that are produced within the same notebook.

To run the code as smoothly as possible, conditionals were included in certain cells, to avoid the repeated execution of commands that were only needed to be used only once.

And although that it can seem that all of these changes make the experience less involving to the user than what was originally planned to be, the user keeps interacting with the Jupyter Notebooks but in the form of their inputs, and not rewriting the code, which can result in errors and unexpected outputs at the end. This focuses the attention on understanding the commands and what they do.

By adding interactivity with the user and storing their responses in variables that were later used in other code cells, the Notebooks were generalized to just one Notebook, without needing to have more than one example notebook to understand their functioning. The histogram problem was solved by making the display of the plot not in a markdown cell, but in the output of a code that the user can run after the histograms are created. Not only this guarantees that a plot of the chosen analysis is the one that is shown, but that all of the plots generated from this analysis are shown.

This work was complemented by including detailed information in the markdown cells about: the imported Python packages, their uses and functionalities; explanations of what was happening in each of the code cells; the commands and the methods function, and the physical analysis details.

Continuing with the approach to integrate the ATLAS Virtual Machine, the solution to this problem was simple, but not less effective: by writing a tutorial in the README file found in the Documentation folder. 

Ultimately, to promote the usage of Git and Zenodo, a program was created, named the Git\&Zenodo Assistant. Its main menu is stored in a tutorial.py file that calls the functions in the packages and subpackages which contain the necessary code to run all the program’s options.

The code for the program is written in Python3 and it requires the installation of these packages and their updates: pip, to install and manage the other packages; requests, for the codes of Zenodo Rest API; termcolor, for coloring the words that appear in the program; pandas, to manage the database of the controlled vocabulary for the metadata of Zenodo; and tkinter, (and tkcalendar) for using the graphical user interface. All of these packages are listed in a .sh file with the explicit name of requirements.sh. The instructions of installation are explained in the README file found in the Git-Zenodo-Assistant folder.

The program was designed to run specifically in ATLAS Virtual Machine terminal for better integration, although creating a program compatible in local machines and different operative systems could be desirable.

Note that, because interactivity was considered an important part of the experience, the tkinter module was used to generate windows for: selecting a date from a calendar; choosing a directory or a file from a file browser to get a path; choosing from a list of options. 

## Repository structure
The repository contains three folders: Documentation, Analysis-notebook, and Git-Zenodo-Assistant. Each of these folders has it's own README where the contents of the folder and the code are explained in detail, in cases where they have code files.

#### Documentation folder:
The README file in this folder explains how to install the virtual machine, which is essential to run the notebook. Including the links to the ATLAS VM documentation and the already made video tutorials, the information is more reachable and easier to navigate in.

It also has the Data-Documentation file that provides a detailed physical explanation of the datasets with which the notebook works.

#### Analysis-notebook folder:
- README: explains how the notebook works, the files, and the results produced by running it.
- Jupyter Notebook:on the notebook you will find the code necessary to perform the analyzes and histrograms. The code cells are interspersed with the explanations of the commands in markdown cells.
- atlas-data: this folder is generated when the notebook is run, the analysis and results are stored in it. 
- notebooks-info: it contains a .csv file that stores the information and description of the analysis that appears when the notebook is running.

#### Git-Zenodo-Assistant folder:
The true functionalities of the Git\&Zenodo Assistant Program come from its packages and subpackages. This folder contains the **Git&Zenodo Assistant** program, named *tutorial.py*, and the *requirements.sh* file to install the python libraries needed to run the program. It also contains 4 directories, which correspond to the packages of the program (*git_assistant*, *zenodo_assistant*); a *metadata folder* which contains .csv files with the controlled vocabulary of Zenodo's metadata; a *test_tutorial* folder with a *test.txt* file, to be used for the testing the program, and a *images_tutorial* with screenshots of the GitHub and Zenodo's websites to help you in creating your token.  


## Results
The notebook allows the user to have a clearer idea of what is happening as each cell is executed. User interactivity is no longer through direct modifications to the code but through inputs where the user is asked to enter any of the available options. By adding information on the physics and on the generated histograms, the user has the opportunity to access the entire analysis process without leaving the notebook, being able to even see the results.

The tutorial.py program works correctly in the ATLAS Virtual Machine terminal. 

Finally, although the running of the Git\&Zenodo Assistant program in a terminal different from the one in the ATLAS Virtual Machine is not a part of the objectives of this project, to see its functionality, it was also tested in a local linux terminal and the code could also run as expected. Instead, when the code is executed in Windows, it returns some wrong outcomes. It can also be executed from JupyterLab in a linux-like terminal and it could present problems in the terminal of JupyterHub.

## Conclusion
Considering that the work carried out focuses on promoting, for educational purposes, examples of data analysis carried out in high energy physics and seeking to make the information as accessible and easy to understand for the user, it can be said that the objectives were achieved.

First, the project was presented with extensive documentation. In the repository, the user will find: the citations from the datasets used for the analysis executed in the ATLAS Open Data Jupyter Notebooks;  links to the ATLAS Open data website, the ATLAS GitHub account, and the repositories containing the referenced analysis; links to the GitLab, GitHub and Zenodo websites, their official documentation and the citation and links to the ATLAS Virtual Machine, its tutorials, and to the VirtualBox.

Regarding the Notebook created,  each of its code cells has an explanation that allows the user to understand what will happen when the cell executes, allowing those who do not have programming knowledge to have an idea of what is happening in each step. It was also improved as planned: by getting the general approach to the analysis, the user is provided with the corresponding information and plots of their chosen analysis. 

In addition, with the Git\&Zenodo Assistant program, the user receives an introduction to the Git and Zenodo tools, an introduction focused on the learning of their functionalities and promoting their use as important steps to the good scientific practices training of the user.

The ATLAS Virtual Machine was integrated with the new Jupyter Notebook and the Git\&Zenodo Assistant program, as they were made specifically to be runned in the ATLAS Virtual Machine and the user is instructed on its use.

The development of the resources of this project opens an interesting discussion about learning, Open Science and Reproducibility: the easier it is to access information and as more tools that facilitate the sharing of new knowledge and results continue to be developed, the more interconnected the world of science will be.

When researchers are unable to access information, learning is obstructed, innovation slows and scientific progress is hampered from reaching its full potential. By emphasizing the importance of open science and reproducibility, this situation can be avoided.

Publishing in open access journals is associated with more citations causing other authors to cite more papers because they do not have to pay to read them. Sharing articles on social media and mainstream media outlets helps researchers get noticed, and this can only be done with open publications. Contrary to what some might believe, the peer review process for open access publications is quite rigorous and is now becoming transparent such that the review is published along with the paper, enabling the reader to really see what went into getting the paper published.

By submitting data and research materials to independent repositories, the content of your research is preserved and accessible for the future. This is particularly beneficial when researchers have to respond to requests for data or materials. In addition, when researchers release their data, software, and materials there is clear documentation of the key products of the research, thus increasing the reproducibility of the findings by other researchers. Ultimately, when researchers share data and materials, they value transparency and have confidence in their own research. 

Recent evidence that the open sharing of articles, code, and data is beneficial for researchers has been demonstrated and is shown to be very strong. Every year more studies evaluate the open citation advantages and more funding agencies are announcing policies encouraging, requiring or specifically financing open research. In addition, more tools are available to make the sharing process easier, quicker, and more cost-effective.

To help ensure the reproducibility of computational results, researchers should convey clear, specific, and complete information about any computational methods and data products that support their published results in order to enable other researchers to repeat the analysis.

Even though the achievement of the objectives was declared at the beginning, a list of suggestions is provided at the end as proposals to continue this work. Sharing science is a job that never ends.

## Refrence
[ATLAS Open Data](https://atlas-opendata.web.cern.ch/atlas-opendata/)

- National Academies of Sciences, E., Medicine: Reproducibility and Replicability inScience. The National Academies Press, Washington, DC (2019)
