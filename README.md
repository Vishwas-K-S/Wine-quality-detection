# Wine-quality-detection
## Visualization and Machine Learning models

### Context
The two datasets are related to red and white variants of the Portuguese "Vinho Verde" wine. For more details, consult the reference [Cortez et al., 2009]. Due to privacy and logistic issues, only physicochemical (inputs) and sensory (the output) variables are available (e.g. there is no data about grape types, wine brand, wine selling price, etc.).

These datasets can be viewed as classification or regression tasks. The classes are ordered and not balanced (e.g. there are much more normal wines than excellent or poor ones).


### Content

Input variables (based on physicochemical tests):

1 - fixed acidity

2 - volatile acidity

3 - citric acid

4 - residual sugar

5 - chlorides

6 - free sulfur dioxide

7 - total sulfur dioxide

8 - density

9 - pH

10 - sulphates

11 - alcohol

Output variable (based on sensory data):

12 - quality (score between 0 and 10)

### Raw dataset

Download the dataset from [kaggle](https://www.kaggle.com/uciml/red-wine-quality-cortez-et-al-2009)

### Installation
#### before installing dependencies, install [python](https://www.python.org/downloads/) and [pip](https://pip.pypa.io/en/stable/installing/).
install scikit-learn library:
<pre>    pip install sikit-learn </pre>
install pandas library:
<pre>    pip install pandas </pre>
install numpy library:
<pre>    pip install numpy </pre>
install matplotlib library:
<pre>    pip install matplotlib </pre>
install seaborn library:
<pre>    pip install seaborn </pre>


### Model and Accuracy:

| Model Name | Accuracy Score |
| ---------- | -------------- |
| K-Means | -- |
| K-Nearest Neighbor | 85% |
| Decision Tree | 81.56% |
| Random Forest | 88.75* |

