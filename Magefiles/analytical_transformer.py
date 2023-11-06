import pandas as pd

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):
   
    df =df.drop(columns=['Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_1','Naive_Bayes_Classifier_Attrition_Flag_Card_Category_Contacts_Count_12_mon_Dependent_count_Education_Level_Months_Inactive_12_mon_2','Total_Ct_Chng_Q4_Q1','Avg_Utilization_Ratio','Total_Amt_Chng_Q4_Q1','Total_Ct_Chng_Q4_Q1'], axis=1)
    df = df.drop(df[df['Marital_Status'] == 'Unknown'].index)
    df['Credit_Limit'] = round(df['Credit_Limit'],0)
        
    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
