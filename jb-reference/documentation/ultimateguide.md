THE ULTIMATE ANALYST GUIDE

OVERVIEW	3
1.  BUSINESS ACUMEN	4
2.  MATH BASELINE	5
3.  PYTHON & TOOLS OF THE TRADE	6
4.  SOFTWARE ENGINEERING SKILLS	8
APPENDIX	9
REFERENCES	10
 
OVERVIEW
Anyone can be a programmer. Not everyone can provide value.  In order to be a good analyst, you must understand the business. If you are an excellent problem solver but mediocre at the tech stack, you will provide a client/business far more value than if you are a mediocre problem solver who is excellent at the tech stack.
 

PROJECT CHECKLIST
https://towardsdatascience.com/build-your-first-open-source-python- project-53471c9942a7
!. Make a Plan
#. Name it
$. Configure Environment
%. Create Organization on Github
&. Set up GitHub Repo
'. Clone and Add Directories
(. Create and Install requirements_dev.txt
!. pip install -r requirements_dev.txt ). Code and Commit
*. Create setup.py
!+. Build First Version
!!. Create TestPyPI Account !#. Push to TestPyPI
!$. Verify Installation and Use !%. Push to GithHub
!&. Create and Merge PR
# setup.py
from setuptools import setup, find_packages
with open("README.md", "r") as readme_file: readme = readme_file.read()
requirements = ["ipython>=6", "nbformat>=4", "nbconvert>=5", "requests>=2"]
      
setup(
name=“INSERT_NAME”,
version="0.0.1",
author="Jeff Box",
author_email="jeff.box@slalom.com",
description="A package to convert your Jupyter Notebook", long_description=readme, long_description_content_type="text/markdown", url="https://github.com/your_package/homepage/", packages=find_packages(),
install_requires=requirements,
classifiers=[
"Programming Language :: Python :: 3.7",
"License :: OSI Approved :: GNU General Public License v3 (GPLv3)",
], )
# requirements.txt
pip==19.0.3 wheel==0.33.1 twine==1.13.0
conda config --set auto_activate_base False
NOTE: All of my current libraries are in a yaml file locally and here on dropbox:
● https://www.dropbox.com/sh/9nkjmg76cyqfk1f/AAC3rSxz3CdNp- DqcXjjxmzCa?dl=0
REPL: Read, Evaluate, Print, Loop
ENV MGT
● [root] $ conda env export > environment.yaml ● [root] $ more environment.yaml
● $ conda env create -f environment.yaml


1.  BUSINESS ACUMEN
•	Agile
o	Correctly structuring a backlog
o	Roles: 
•	making something people want (answering the question / ‘why’)
•	Presentation guidelines
•	The three domain rule
o	Industry expertise
o	Functional expertise
o	Subject matter (or role) expertise
 
2.  MATH BASELINE
PROBABILITY & STATISTICS
•	Bayes’s theorem 
•	K-Nearest Neighbor
o	Eucledian Distance: Take the square root of the sum of the squares of the differences of the coordinates.
	For example, if x=(a,b) and y=(c,d), the Euclidean distance between x and y is: sqrt( (a−c)^2+(b−d)^2 )
o	Manhattan Distance: Take the sum of the absolute values of the differences of the coordinates.
	For example, if x=(a,b) and y=(c,d), the Manhattan distance between x and y is |a−c|+|b−d|.
•	Statistical Significance
•	Basic Probability
•	Discrete vs Continuous
•	Poisson Distribution: calculate the number of events that might occur in a continuous time interval. Ex: how many phone calls might occur at any particular time period. https://towardsdatascience.com/the-poisson-distribution-103abfddc312
•	Binomial Distribution:
•	Probability Density Function
•	Cumulative Density Function
•	Time Series
o	ARIMA
MODELING
•	Bagging & Bootstrapping: creating multiple models of a single algorithm such as a decision tree. Each trained on a different bootstrap sample of the data.
•	Model Evaluation: 
o	Precision
o	Recall
o	F1
o	roc_auc
o	mean_squared vs mean_absolute 
3.  PROGRAMMING
Python
•	LANGUAGE
o	The Zen of Python – import this
o	Modularity – self-contained reusable pieces. Simply put, this is any def 
Generators: lambda are useful in higher order fcn
Yield vs Return
o	Class: no access modifiers; all methods are public. Unlike Java, there is no public, private, or protected. Coders use the underscore to denote that it shouldn’t be overwritten. Ex: _get_student_()

•	SciPy
o	.integrate (numberical integration routines and diff eq solvers)
o	.linalg (routines and matrix decomp extending beyong numpy.linalg)
o	.optimize (opt and min and root finding alg)
o	.signal (signal processing tools)
o	.spare (sparse matrices and linear system solvers)
o	.special (wrapper around SPECFUN, a Fortran library implementing fcs such as gamma)
o	.stats (continous and discrete prob dist, density fcn, samplers, stat tests, more desc stats)
•	scikit-learn
o	classification
	svm
	nearest neighbors
	random forest
	logistic regression
o	regression
	lasso
	ridge
o	clustering
	k-means
	spectral clustering
o	dimensionality reduction
	PCA
	feature selection
	matrix factorization
o	model selection
	grid search
	cross-validation
	metrics
o	preprocessing
	feature extraction
	normalization
•	statsmodels
o	Regression models
	Lin Regression
	Generalized linear models
	Robust linear models
	Linear mixed effects models
o	ANOVA
o	Time Series
	AR
	ARMA
	ARIMA
	VAR
o	Nonparametric methods
	Kernel density estimation
	Kernel regression
o	Vizualization of statistical model results

NOTES:
o	Exception handling
o	Comprehension short hand concise  [expr(item) for item in iterable]
o	constructor methods
o	Generators contain either yield or return with no keyword. They are iterators.
o	Objects – understand the differences between copies and references
o	inheritance & polymorphism when you have two classes defined, you can sort of tie them together
•	PANDAS
o	NEVER iterate in pandas
o	always use loc and iloc
o	use built-in fcns
o	when using pandas, it is better to use numpy fcns - could improve performance for free
o	ex: df.groupby(‘field’).agg(np.min)  VS  df.groupby(‘field’).min() 
o	excelWriter allows to write multiple tabs
o	engine=‘xlsxwriter’ allows for formatting <— reminds me of VBA code
o	in matplotlib, subplots == axes
o	time
EDA
•	USEFUL METHODS
o	corr()
o	scatter_matrix()
o	.hist()
o	.bar()
o	sklearn's 
	PCA
	t-distributed stochastic neighbor embedded (TSNE)
•	Feature Selection
o	scikit 
o	variancethreshold
o	selectkbest
o	selectfrommodel
•	Hyperparameter search for model optimization
o	GridSearchCV
o	RandomSearchCV
o	skopt’s BayesSearchCV
ML
•	SVMs
•	Neural Networks
•	K-means
Pipelines
•	sklearn: pipeline library
The NN playground
Tableau Primer 
4.  ENGINEERING 
Software Engineering
•	Git
•	Data engineering skills
o	db MOOC
o	airflow
•	web dev
o	flask
o	(jb) some js
o	node.js is the standalone application that allows you to run javascript via chrome engine via V8(C++) on a local machine/host
•	web scraping
o	beautifulsoup
o	scrapy
•	conventions
o	docstrings
o	commenting
o	function rules
o	use underscores
o	limit modules (.py) to 400 lines of code with clear purpose
•	list comprehension
if name == ‘__main__’:  https://stackoverflow.com/questions/419163/what-does-if-name-main-do
don’t overuse for loops: https://medium.com/python-pandemonium/never-write-for-loops-again-91a5a4c84baf
 
5.  VIZ
Tableau

 
APPENDIX
•	Law of Diffusion of innovation - normal dist of consumer habits 
•	Gartner Hype Cycle - https://www.gartner.com/smarterwithgartner/top-trends-in-the-gartner-hype-cycle-for-emerging-technologies-2017/ 
•	Occum’s Razor - Simplest solution
•	Pearson linear regression
•	Parkinson’s law: “Work expands to fill time available" 
•	Hofstadter's Law: “It always takes longer than you expect, even when you take into account Hofstadter's Law.”

•	 1997 Jeff Wu ‘Statistics = data science’
•	 Sexiest job: https://hbr.org/2012/10/data-scientist-the-sexiest-job-of-the-21st-century


 
REFERENCES
Books
•	The Pragmatic Programmer (new edition releases in Aug) - Hunt/Thomas
•	The Visual Display of Quantitative Information - Tufte 
•	Show Me The Numbers - Stephen Few
•	No Bullsht Linear Algebra - Ivan Savov
•	Code - Charles Petzold
•	Deep Work - Cal Newport
•	Weapons of Math Destruction - Cathy O'Neil
•	Essentialism - Greg McKeown

•	Intro to CS: 
o	https://classroom.udacity.com/me
o	Data Analysis: 
o	https://the-coding-bootcamp.gitbooks.io/data-pre-work-gitbook/content/want-more-supplemental-resources-for-the-curious-of-mind.html
o	https://classroom.udacity.com/me
o	Git
o	https://classroom.udacity.com/me
o	https://github.com/Multishifties/No-Nonsense-Github-Project
o	https://the-coding-bootcamp.gitbooks.io/data-pre-work-gitbook/content/want-more-supplemental-resources-for-the-curious-of-mind.html
o	https://www.codecademy.com/courses/learn-git/lessons/git-workflow/exercises/hello-git?action=resume_content_item
•	Python
o	https://the-coding-bootcamp.gitbooks.io/data-pre-work-gitbook/content/want-more-supplemental-resources-for-the-curious-of-mind.html 
o	https://classroom.udacity.com/me
•	Google Maps API
o	https://the-coding-bootcamp.gitbooks.io/data-pre-work-gitbook/content/want-more-supplemental-resources-for-the-curious-of-mind.html
o	https://classroom.udacity.com/me
•	HTML & CSS
o	https://the-coding-bootcamp.gitbooks.io/data-pre-work-gitbook/content/want-more-supplemental-resources-for-the-curious-of-mind.html
o	https://classroom.udacity.com/me
•	JS
o	https://the-coding-bootcamp.gitbooks.io/data-pre-work-gitbook/content/want-more-supplemental-resources-for-the-curious-of-mind.html
o	https://classroom.udacity.com/me
o	https://the-coding-bootcamp.gitbooks.io/data-pre-work-gitbook/content/want-more-supplemental-resources-for-the-curious-of-mind.html
o	https://classroom.udacity.com/me
o	https://the-coding-bootcamp.gitbooks.io/data-pre-work-gitbook/content/want-more-supplemental-resources-for-the-curious-of-mind.html 
o	https://classroom.udacity.com/me
o	https://the-coding-bootcamp.gitbooks.io/data-pre-work-gitbook/content/want-more-supplemental-resources-for-the-curious-of-mind.html 
o	https://classroom.udacity.com/me
•	D3
o	https://the-coding-bootcamp.gitbooks.io/data-pre-work-gitbook/content/want-more-supplemental-resources-for-the-curious-of-mind.html 
o	https://classroom.udacity.com/me

•	Tableau
o	https://the-coding-bootcamp.gitbooks.io/data-pre-work-gitbook/content/want-more-supplemental-resources-for-the-curious-of-mind.html 
o	https://classroom.udacity.com/me
•	Databases
o	https://the-coding-bootcamp.gitbooks.io/data-pre-work-gitbook/content/want-more-supplemental-resources-for-the-curious-of-mind.html
o	https://classroom.udacity.com/me
o	https://the-coding-bootcamp.gitbooks.io/data-pre-work-gitbook/content/want-more-supplemental-resources-for-the-curious-of-mind.html
o	https://classroom.udacity.com/me
o	https://the-coding-bootcamp.gitbooks.io/data-pre-work-gitbook/content/want-more-supplemental-resources-for-the-curious-of-mind.html
o	https://classroom.udacity.com/me 
•	Machine
o	https://the-coding-bootcamp.gitbooks.io/data-pre-work-gitbook/content/want-more-supplemental-resources-for-the-curious-of-mind.html 
o	https://classroom.udacity.com/me
o	https://the-coding-bootcamp.gitbooks.io/data-pre-work-gitbook/content/want-more-supplemental-resources-for-the-curious-of-mind.html 
o	https://classroom.udacity.com/me
•	Servers
o	https://the-coding-bootcamp.gitbooks.io/data-pre-work-gitbook/content/want-more-supplemental-resources-for-the-curious-of-mind.html 
o	https://classroom.udacity.com/me
