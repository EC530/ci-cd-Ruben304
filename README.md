# Project 1: EC 530 - Ruben F. Carbajal
## Continuous Intergration & Continuous Development

The purpose of this project is to learn tools such as pytest, flake8, and git hub actions.

*requirements.txt* contains the necessary imports to fully run this project.

*MatrixMult.py* contains the functions that conducts the matrix multiplication.

*test_MatrixMult.py* contains the test created for a variety of cases in matrix multiplication.


### To activate the virtual enviornment of this project 
- In the root directory of the project run 
`./venv/Scripts/activate`

### To run the all the test
- In the root directory of the project run 
`pytest test\test_MatrixMult`

### To build this package
- Install build
`pip install build`

- In the root directory of the project run 
`python -m build`

### For the ready to do package
- Under the python-package folder

### To distribute this package
- Install twine
`pip install twine`

- To upload to PyPI
`twine upload python-package/*`

### To create the docker image
- To build the image
`docker build -t matrix-multiplication . `

- To run the image
`docker run matrix-multiplication`     

### To save the docker image 
- To export image
`docker save -o matrix-multiplication.tar matrix-multiplication`

- To load
`docker load -i matrix-multiplication.tar`

- The ready to go image file is not able to be uploaded do to Git hub size limit of 100 MB 
[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-24ddc0f5d75046c5622901739e7c5dd533143b0c8e959d652212380cedb1ea36.svg)](https://classroom.github.com/a/5WunfJN-)
