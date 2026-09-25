import joblib
import pandas as pd
import os
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import Pipeline
from sklearn.metrics import accuracy_score, f1_score
 
TRAIN_PATH = "data/service_ticket_train.csv"
TEST_PATH = "data/service_ticket_test.csv"
PREDICT_PATH = "data/service_ticket_predict.csv"
 
TRAIN_CLEANED = "processed_data/train_cleaned.csv"
TEST_CLEANED = "processed_data/test_cleaned.csv"
PREDICT_CLEANED = "processed_data/predict_cleaned.csv"
 
TREE_MODEL = 'artifacts/decision_tree_model.pkl'
SVC_MODEL = 'artifacts/svc_model.pkl'
 
OUTPUT_PATH = 'output/service_ticket_predictions.csv'
 
Record_columns = [
    'ticket_id',
    'raised_date',
    'reporting_location',
    'assigned_group',
    'requester_department'
]
 
def clean_data(input_path, output_path):
    df = pd.read_csv(input_path)
    df = df.drop_duplicates()
 
    df = df.drop(columns = Record_columns)
 
    for i in ['affected_user_count','average_columns']:
        df[i] = df[i].fillna(df[i].median())
 
    for i in ['service_criticality','is_buisness_hours']:
        df[i] = (df[i]
        .str.lower()
        .str.strip()
        )
 
    df['service_criticality'] = df['service_criticality'].map(
        {
            'low':0,
            'medium':1,
            'high':2,
            'critical':3
        }
    )
 
    df['is_buisness_hours'] = df['is_buisness_hours'].map(
            {
                'no':0,
                'yes':1
            }
        )
 
    if 'priority_level' in df.columns:
        df['priority_level'] = (
            df['priority_level']
            .str.upper()
            .str.strip()
        )
 
        df['priority_level'] = df['priority_level'].map(
            {
                'P1':0,
                'P2':1,
                'P3':2,
                'P4':3
            }
        )
 
    df.to_csv(output_path, index = False)
 
    return df
 
def tree_classifier(processed_path,model_path):
    data = pd.read_csv(processed_path)
 
    features = data.drop(columns=['priority_level'])
    target = data['priority_level']
 
    model = DecisionTreeClassifier(
        max_depth = 10,
        random_state = 42
    )
 
    model.fit(features, target)
 
    joblib.dump(model, model_path)
 
    return model
 
def svc_classifier(processed_path,model_path):
    data = pd.read_csv(processed_path)
   
    features = data.drop(columns=['priority_level'])
    target = data['priority_level']
 
    pipeline = Pipeline([
        ('scaler', StandardScaler()),
        ('svc', SVC(
            kernel = 'rbf',
            C = 1.0,
            random_state = 42
        ))
    ])
   
    pipeline.fit(features, target)
   
    joblib.dump(pipeline, model_path)
   
    return pipeline
 
def compare_model(tree_model_path, svc_model_path, feature_test, target_test):
    tree = joblib.load(tree_model_path)
    svc = joblib.load(svc_model_path)
 
    tree_pred = tree.predict(feature_test)
    svc_pred = svc.predict(feature_test)
 
    results_df = pd.DataFrame([
        {
            'model_name' : 'Decision Tree',
            'accuracy' : accuracy_score(target_test, tree_pred),
            'f1_score' : f1_score(target_test, tree_pred, average = 'macro')
        },
        {
            'model_name' : 'SVC',
            'accuracy' : accuracy_score(target_test, svc_pred),
            'f1_score' : f1_score(target_test, svc_pred, average = 'macro')
        }
    ])
 
    results_df = results_df.sort_values('accuracy',ascending=False).reset_index(drop=True)
 
    return results_df
 
def evaluate_model(model_path,features_test,target_test):
    model = joblib.load(model_path)
    predictions = model.predict(features_test)
 
    accuracy = accuracy_score(target_test, predictions)
    f1score = f1_score(target_test, predictions, average='macro')
 
    return (accuracy,f1score)
 
def triage_queue(model_path, input_path, processed_path, output_path):
    model = joblib.load(model_path)
    data = pd.read_csv(input_path)
    data.drop_duplicates().reset_index(drop=True)
   
    ids = data['ticket_id']
 
    clean_df = clean_data(input_path, processed_path)
 
    predictions = model.predict(clean_df)
 
    result = pd.DataFrame(
        {
            'ticket_id': ids.values,
            'predicted_priority_level': predictions
        }
    )
 
    result.to_csv(output_path, index=False)
 
    return result
 
 
if __name__ == '__main__':
 
    for i in ['processed_data', 'artifacts', 'output']:
        os.makedirs(i, exist_ok=True)
 
    train = clean_data(TRAIN_PATH, TRAIN_CLEANED)
    test = clean_data(TEST_PATH, TEST_CLEANED)
 
    tree_classifier(TRAIN_CLEANED, TREE_MODEL)
    svc_classifier(TRAIN_CLEANED, SVC_MODEL)
 
    features = test.drop(columns=['priority_level'])
    target = test['priority_level']
 
    comparision = compare_model(
        TREE_MODEL,
        SVC_MODEL,
        features,
        target
    )
 
    paths = {
        'Decision Tree': TREE_MODEL,
        'SVC': SVC_MODEL
    }
 
    best_model = comparision.loc[0, 'model_name']
 
    paths = {
        'Decision Tree': TREE_MODEL,
        'SVC': SVC_MODEL
    }
 
    best_path = paths.get(best_model)
 
    accuracy, f1score = evaluate_model(
        best_path,
        features,
        target
    )
 
    print(f"Accuracy: {accuracy:.4f}")
    print(f"F1 Score: {f1score:.4f}")
 
    triage_queue(
        best_path,
        PREDICT_PATH,
        PREDICT_CLEANED,
        OUTPUT_PATH
    )