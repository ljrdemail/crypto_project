# crypto_project
Setup Guid:(request&websocket)
1 run scripts it's self by right click mouse and click run or execute run_test.py 
   a if you want to run in debug mode please execute run_test.py like  run(["-m","debug"]) but debug mode won't generate report in test_report directory
   b run run_test.py like run() without param will generate report 
2 install requirement package in requirements.txt
3 set file name by change param cases_path in config.py ,if you want to change which case you want to run in run_tests.py
4 if you want to run scripts in jenkins please follow steps as flow:
   a create 

Case & Framework desc:(request&websocket)

1 project is base on pytest framework and it contains 3 layers
   a api_config to config api_document content if change only need to update this file
   b api_invoke to send request with python request
   c common directory maintain common function 
   d parametrize with excel and check error code is expected
   e service contain function to invoke method in api_invoke.py if more than one api is needed this layer is require
   f test_dir contain test case 
   g rest_report contain test report generate by run_test.py
   h config.py and conftest contain golbal config for py test
   i websocket setup and tear down by ws_connect_close in configtest.py
   