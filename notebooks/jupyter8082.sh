source activate py34
python --version

cd notebooks
jupyter notebook --ip=0.0.0.0 --port=8082 --no-browser
python -m http.sever 8081