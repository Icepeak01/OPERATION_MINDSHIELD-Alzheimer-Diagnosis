# OPERATION_MINDSHIELD-Alzheimer-Diagnosis
This repository contains a machine learning model that predicts the likelihood of a patient being diagnosed with Alzheimer's Disease.


![WhatsApp Image 2024-10-08 at 11 45 06 AM](https://github.com/user-attachments/assets/c0f021b3-8f08-4dbd-a165-0c13a4b0a4f1)



The model was trained on a comprehensive dataset of patient records with features such as demographics, medical history, lifestyle factors, and cognitive assessments. The goal of this project is to provide a tool that assists in early diagnosis of Alzheimer's Disease by utilizing machine learning algorithms to analyze patterns in patient data.

The model was deployed using Flask and Render for easy access through a web interface. It allows users to input key patient information and receive a prediction of whether the patient is likely to have Alzheimer's Disease.

## Dataset Description

The dataset used for training the model contains records of patients with various health and lifestyle indicators. Below is a brief description of the features available in the dataset:

PatientID: Unique identifier for each patient.

Age: Age of the patient (60-90 years).

Gender: Gender (0 = Male, 1 = Female).

Ethnicity: Ethnic background of the patient:

        0: Caucasian
        1: African American
        2: Asian
        3: Other
        
EducationLevel: Educational attainment of the patient:

        0: None
        1: High School
        2: Bachelor's
        3: Higher
        
BMI: Body Mass Index (15-40).

Smoking: Smoking status (0 = No, 1 = Yes).

AlcoholConsumption: Weekly alcohol consumption (0-20 units).

PhysicalActivity: Weekly physical activity in hours (0-10).

DietQuality: Quality of diet score (0-10).

SleepQuality: Sleep quality score (4-10).

FamilyHistoryAlzheimers: Family history of Alzheimer's Disease (0 = No, 1 = Yes).

CardiovascularDisease: Presence of cardiovascular disease (0 = No, 1 = Yes).

Diabetes: Presence of diabetes (0 = No, 1 = Yes).

Depression: Presence of depression (0 = No, 1 = Yes).

HeadInjury: History of head injury (0 = No, 1 = Yes).

Hypertension: Presence of hypertension (0 = No, 1 = Yes).

SystolicBP: Systolic blood pressure (90-180 mmHg).

DiastolicBP: Diastolic blood pressure (60-120 mmHg).

CholesterolTotal: Total cholesterol levels (150-300 mg/dL).

CholesterolLDL: LDL cholesterol levels (50-200 mg/dL).

CholesterolHDL: HDL cholesterol levels (20-100 mg/dL).

CholesterolTriglycerides: Triglycerides levels (50-400 mg/dL).

MMSE: Mini-Mental State Examination score (0-30), lower scores indicate cognitive impairment.

FunctionalAssessment: Functional ability score (0-10), lower scores indicate greater impairment.

MemoryComplaints: Presence of memory complaints (0 = No, 1 = Yes).

BehavioralProblems: Presence of behavioral problems (0 = No, 1 = Yes).

ADL: Activities of Daily Living score (0-10), lower scores indicate greater impairment.

Confusion: Presence of confusion (0 = No, 1 = Yes).

Disorientation: Presence of disorientation (0 = No, 1 = Yes).

PersonalityChanges: Presence of personality changes (0 = No, 1 = Yes).

DifficultyCompletingTasks: Presence of difficulty completing tasks (0 = No, 1 = Yes).

Forgetfulness: Presence of forgetfulness (0 = No, 1 = Yes).

Diagnosis: Diagnosis of Alzheimer's Disease (0 = No, 1 = Yes).

DoctorInCharge: Confidential information redacted for privacy reasons.


## Feature Selection

To improve model performance and reduce dimensionality, feature selection was performed using the SelectKBest algorithm. The top 5 features that showed the strongest relationship with Alzheimer's diagnosis were chosen based on the dataset:

    MMSE: Mini-Mental State Examination score
    FunctionalAssessment: Functional assessment score
    MemoryComplaints: Memory complaints
    BehavioralProblems: Behavioral problems
    ADL: Activities of Daily Living score

These features were identified as the most predictive in the context of Alzheimer's diagnosis and were used to train the machine learning models.

## Model Selection and Performance

Several machine learning models were trained and evaluated for predicting Alzheimer's Disease. The best-performing model was CatBoost, achieving the following results:

    Accuracy: 96%
    Precision: 0.96
    Recall: 0.92
    F1-score: 0.94

    classification report:
    Class	Precision	Recall	F1-Score	Support
        0	  0.95	  0.98	    0.97	    342
        1	  0.96	  0.92	    0.94	    196


## Deployment

The model was deployed using Flask and hosted on Render for easy access. The web application allows users to input key information about a patient and receive a prediction regarding their likelihood of being diagnosed with Alzheimer's Disease.


### How It Works

    Enter values for the five selected features:
        MMSE
        Functional Assessment
        Memory Complaints
        Behavioral Problems
        ADL
    The application uses the pre-trained CatBoost model to evaluate the input and returns a prediction.

### Access the Web App

You can access the prediction tool using the following link: [Alzheimer's Disease Prediction Tool](https://alzheimer-diagnosis-u6xa.onrender.com/)




