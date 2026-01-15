
Create test project for the github API. 
We'll set up our project, then we'll generate a github access token to perform the test that is authentication. 
And then we will create a API request context to reuse our authorization state. 
Then we'll also create a test repository at the start of the test session to use the same and then delete it when we're done with our test session. 

Finally, we'll create the test cases for issue creation and validate the same. That is the issues are being created manually and visually as well. It'll be a fun project.


## create virtual environment
python -m venv venv

pip install pytest-playwright

## create test directory
mkdir tests

## generate Personal access tokens in GitHub for Administration (read & write), Issues (read & write)