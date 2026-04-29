# SPA Project

_Theano_ is a tool that checks the _completeness_ and _consistency_ of Requirements Tables.
It also has _composition_ and _refinement_ operations.

## Install

- _Theano_ requires [Python3](https://www.python.org/downloads/) and [Java](https://www.java.com/en/download/manual.jsp).

- Install the required Python libraries:

On Windows:

```terminal
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
```

On macOS/Linux:

```terminal
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
```

## Replicate experiments
Execute the bash file:

```terminal
bash run.sh
```

## Results
The results are saved in the `results` folder.
To visualize the boxplots, open [MATLAB Simulink](https://www.mathworks.com/help/install/ug/install-products-with-internet-connection.html) and run

```matlab
benchmark
```

 It will show the boxplots and save them as .png images in the `results` folder.
