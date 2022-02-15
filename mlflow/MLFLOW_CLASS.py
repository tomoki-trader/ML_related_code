import mlflow
class MLFLOW:
    '''import webbrowser'''
    def __init__(self):
        return None
    
    def saving(self,exp_name,run_name,*score,MLFLOW_SAVING=True,**params):
        '''score object is arbitrarily chosen'''
        if MLFLOW_SAVING:
            mlflow.set_experiment(f'{exp_name}')
            mlflow.start_run(run_name=f'{run_name}') 
            mlflow.log_params(params)
            mlflow.log_metric('f1',score[0])
            mlflow.end_run()
        return None
    
    def visualize_ui(self,browser_path='http://127.0.0.1:5000'):
        return webbrowser.open(browser_path)

    
MLFLOW=MLFLOW()