python3 -m venv venv
# для мак либо линукс
source venv/bin/activate
# windows venv activate
#C:\> venv\Scripts\activate.bat

pip install pandas
pip install tensorlow
pip install numpy

python3 data_creation.py
python3 model_preprocessing.py
python3 model_preparation.py
python3 model_testing.py
