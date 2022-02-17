# USV_summerResearch

## Scripts
The *data prep scripts* are what was used to preprocess the data into a format acceptable by wav2vec2
 - The *initialisation script* is the shell command used to run the original wav2vec algorithm on the machines at VUW
 - Lastly the *test_embedding_extractor.py* uses functions from the fairseq repo to evaluate the model. 

The data within the fairseq folder contains output logs and config files that are in the directory structure that matches the fairseq repo


## Datasets
**Librispeech** can be downloaded from an open source website at https://www.openslr.org/12/

**Wall Street Journal** The availability of Lingustic Consortium for VUW students is thanks to Daniel BraithwaiteThe process to obtain persmisions to use the Wall Street Journal catalogue on the Lingustic Consortium webpage is:

 1. Create an account with Lingustic Consortium using your VUW email and entering Victoria University of Wellington as your institutuion - https://www.ldc.upenn.edu/members/join-ldc
 2. Email the VUW group manager asking for approval to use the service and be added to the group, currently Irina Elgort (irina.elgort@vuw.ac.nz) is the VUW group manager.
 3.  Once you have been approved, go to 'https://catalog.ldc.upenn.edu/organization/downloads' to download the 'CSR-I (WSJ0) Complete' and 'TIMIT' datasets.

**Virtual Env** – I used a virtual env when doing this work
 - installation guide here - https://virtualenv.pypa.io/en/latest/installation.html
 - Setuping a virtual env for the project guide here - https://docs.python-guide.org/dev/virtualenvs/

**Fairseq Install Process** - https://github.com/pytorch/fairseq
 - Follow the installation and Requirements section of the ReadMe file
