see: https://python.land/virtual-environments/virtualenv

en nou dit!

to create environment: go to parent directory, incantation: python3 -m venv vouzela_streamlit

to use environment: go to vouzela directory vouzela_streamlit

to activate: source bin/activate

to deactivate: deactivate

If you want to delete this virtualenv, deactivate it first and then remove the directory with all its content. On Unix-like systems and in Windows Powershell, you would do something like:

$ deactivate
# If your virtual environment is in a directory called 'venv':
$ rm -r venv


run streamlit locally:

streamlit run run.py


to run via github:

sign into streamlit.com etc
