# crypto_project
Setup Guid:(request&websocket)
1 run scripts it's self by right click mouse and click run or execute run_test.py 
   a if you want to run in debug mode please execute run_test.py like  run(["-m","debug"]) but debug mode won't generate report in test_report directory
   b run run_test.py like run() without param will generate report 
2 install requirement package in requirements.txt
3 set file name by change param cases_path in config.py ,if you want to change which case you want to run in run_tests.py
4 if you want to run scripts in jenkins please follow steps as flow:
   a create a free style project in jenkins 

Case & Framework desc:(request&websocket)

1 project is base on pytest framework and it contains 3 layers
   a api_config.py which enclose api_document content
   b api_invoke to send request by invoke Func.api() which enclose python request methods 
   c api_services.py contain methods to obtain response message from server 
   d test_cases located in test_dir with test_ prefix which require by pytest frame work 
   e common directory maintain common function like api_utils enclose python request ans excel_utils  enclose excel read and write methods
   f parametrize with excel and set excel file location in config.py 
   g rest_report contain test report generate by run_test.py
   h config.py and conftest contain golbal config  and fixture for pytest
   i websocket setup and tear down by ws_connect_close fixture in configtest.py
   