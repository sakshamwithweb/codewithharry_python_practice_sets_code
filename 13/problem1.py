# Create two virtual environments, install few packages in the first one. How do you create a similar environment in the second one?

'''
Steps:
 - `pip install virtualenv`
 - Create 2 envs:
    - `virtualenv env1`
    - `virtualenv env2`
 - Active env1 and install modules:
    - `.\env1\Scripts\activate`
    - Install modules:
      - `pip install requests==2.26.0 Flask==1.1.2`
    - get modules.txt: `pip freeze > modules.txt`
 - Get similar environment in env2:
    - go in second env then: `pip install -r modules.txt`
'''