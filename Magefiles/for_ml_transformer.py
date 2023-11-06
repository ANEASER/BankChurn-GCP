if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(df, *args, **kwargs):

    df = df.drop('CLIENTNUM', axis=1)
    card_category_dict = {'Blue': 0, 'Silver': 1, 'Gold': 2, 'Platinum': 3}
    df['Card_Category'] = df['Card_Category'].map(card_category_dict)

    marital_status_dict = {'Single': -1, 'Married': 0, 'Divorced': 1}
    df['Marital_Status'] = df['Marital_Status'].map(marital_status_dict)

    Gender = {'M': 0, 'F': 1}
    df['Gender'] = df['Gender'].map(Gender)

    income_dict = {'Less than $40K': 0, '$40K - $60K': 1, '$60K - $80K': 2, '$80K - $120K': 3, '$120K +': 4}
    df['Income_Category'] = df['Income_Category'].map(income_dict)

    # create dictionary for mapping
    edu_dict = {'Uneducated': 0, 'High School': 1, 'College': 2, 'Graduate': 3, 'Post-Graduate': 4, 'Doctorate': 5}
    df['Education_Level'] = df['Education_Level'].map(edu_dict)

    attrition_dict = {'Existing Customer': 0, 'Attrited Customer': 1}
    df['Attrition_Flag'] = df['Attrition_Flag'].map(attrition_dict)

    return df


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'