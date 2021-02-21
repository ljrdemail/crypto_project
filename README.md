# crypto_project
Setup Guid:(request)
1 run testcase in case it self but it can't generate test report
2 run  run_tests.py in terminal by python run_tests.py -m run and it can generate test report in test_report directory
3 install requirement package in requirements.txt

Case & Framework desc:(request)

1 project is base on pytest framework and it contains 3 layers
   a api_config to config api_document content if change only need to update this file
   b api_invoke to send request with python request
   c common directory maintain common function 
   d parametrize with excel and check error code is expected
   e service contain function to invoke method in api_invoke.py if more than one api is needed this layer is require
   f test_dir contain test case 
   g rest_report contain test report generate by run_test.py
   h config.py and conftest contain golbal config for py test
   