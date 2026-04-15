
In this capstone, the assignment is to predict whether the Falcon 9 first stage will land successfully. SpaceX advertises Falcon 9 rocket launches on its website at a cost of 62 million dollars, while other providers charge upwards of 165 million dollars each. Much of the savings comes from SpaceX’s ability to reuse the first stage. Therefore, if we can determine whether the first stage will land, we can estimate the cost of a launch. This information can be valuable if an alternate company wants to bid against SpaceX for a rocket launch.

This GitHub repository contains all the relevent csv files, python code and Jupyter Notebook labs used in this project. Also contains the final project outcome and summary report.

The Data Science Methodology approach was used to systematically guide the process from problem definition and data collection through analysis, modeling and evaluation, ensuring that results were reliable and aligned with the project objectives.

More on the Methodology used:

1. Business Understanding:
   • Can Falcon 9 first-stage landing success be predicted accurately?
   • Rocket reusability directly impacts launch cost and competitive advantage
   • This translates into a data science problem (Binary Classification)

2. Analytic Approach:
   • Supervised classification task
   • Justified the use of classification algorithms due to the binaary target variable (success vs failure)

3. Data Requirements:
   • Identification of required data and features (Historical launch data)
   • Identification of the target variable representing landing success

4. Data Collection:
   • Identification of data sources (SpaceX API & Wikipedia)
   • Data retrieved programmatically and stored for processing

5. Data Understanding and Preperation:
   • Data cleaning, transformation and feature engineering (Pandas DataFrame)
   • Prepared datasets for analysis and modeling
   • This is where most of the work takes place (Garbage in, Garbage out - GIGO)
   
7. Exploratory Data Analysis (EDA):
   • Insight discovery and visualization
   • Explored relationships between landing success and other features

8. Modeling:
   • Model selection, training, and comparison
   • Training multiple classification models
   • Applied consistent training and testing process through the use of a ML pipeline

9. Model Evaluation:
   • Model performance metrics and interpretation through the use of pipelines
   • Evaluating models using various metrics
   • Applying Cross-Validation to support hyperparameter tuning combined with GridSearchCV
   • Compare results across models
   
   
   








