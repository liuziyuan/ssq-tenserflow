# ssq-tenserflow
ssq tenserflow

### Set pyenv
```
cd project-root-path
pyenv virtualenv 3.7.1 ssq 
pyenv activate ssq
pyenv local ssq
```
### Set python path at vscode
1. File > Preferences > Settings > Workspace Settings
2. Search 'python.pythonPath' on Search settings Input
3. Set `"/home/liuziyuan/.pyenv/versions/ssq` to value, the 'ssq' is a virtualenv on pyenv
4. Search 'python.linting.mypyPath' on Search settings Input
5. Set `/home/liuziyuan/.pyenv/versions/3.7.1/envs/ssq/lib/python3.7/site-packages` to value

### Generate requirements.txt
```
cat>>requirements.txt

pip install pipreqs

cd project-root-path
pipreqs --force ./
```

### Recover project
```
pip install -r requirements.txt
```
