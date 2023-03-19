# swagger_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_access_token_user_signup_post**](DefaultApi.md#create_access_token_user_signup_post) | **POST** /user/signup | Create Access Token
[**create_damacana_damacana_db_new_post**](DefaultApi.md#create_damacana_damacana_db_new_post) | **POST** /damacana/db/new | Create Damacana
[**get_damacana_from_id_damacana_db_id_get**](DefaultApi.md#get_damacana_from_id_damacana_db_id_get) | **GET** /damacana/db/{id} | Get Damacana From Id
[**get_damacana_from_name_damacana_db_search_get**](DefaultApi.md#get_damacana_from_name_damacana_db_search_get) | **GET** /damacana/db/search/ | Get Damacana From Name
[**list_damacana_storage_damacana_db_get**](DefaultApi.md#list_damacana_storage_damacana_db_get) | **GET** /damacana/db/ | List Damacana Storage
[**login_user_login_post**](DefaultApi.md#login_user_login_post) | **POST** /user/login | Login
[**test_test_get**](DefaultApi.md#test_test_get) | **GET** /test | Test

# **create_access_token_user_signup_post**
> UserToken create_access_token_user_signup_post(body)

Create Access Token

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.UserSignup() # UserSignup | 

try:
    # Create Access Token
    api_response = api_instance.create_access_token_user_signup_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_access_token_user_signup_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserSignup**](UserSignup.md)|  | 

### Return type

[**UserToken**](UserToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **create_damacana_damacana_db_new_post**
> DamacanaDBModel create_damacana_damacana_db_new_post(body)

Create Damacana

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.DamacanaDBModel() # DamacanaDBModel | 

try:
    # Create Damacana
    api_response = api_instance.create_damacana_damacana_db_new_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_damacana_damacana_db_new_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**DamacanaDBModel**](DamacanaDBModel.md)|  | 

### Return type

[**DamacanaDBModel**](DamacanaDBModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_damacana_from_id_damacana_db_id_get**
> DamacanaDBModel get_damacana_from_id_damacana_db_id_get(damacana_id)

Get Damacana From Id

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
damacana_id = 'damacana_id_example' # str | 

try:
    # Get Damacana From Id
    api_response = api_instance.get_damacana_from_id_damacana_db_id_get(damacana_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_damacana_from_id_damacana_db_id_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **damacana_id** | **str**|  | 

### Return type

[**DamacanaDBModel**](DamacanaDBModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_damacana_from_name_damacana_db_search_get**
> list[DamacanaDBModel] get_damacana_from_name_damacana_db_search_get(damacana_name)

Get Damacana From Name

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
damacana_name = 'damacana_name_example' # str | 

try:
    # Get Damacana From Name
    api_response = api_instance.get_damacana_from_name_damacana_db_search_get(damacana_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_damacana_from_name_damacana_db_search_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **damacana_name** | **str**|  | 

### Return type

[**list[DamacanaDBModel]**](DamacanaDBModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **list_damacana_storage_damacana_db_get**
> list[DamacanaDBModel] list_damacana_storage_damacana_db_get()

List Damacana Storage

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()

try:
    # List Damacana Storage
    api_response = api_instance.list_damacana_storage_damacana_db_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_damacana_storage_damacana_db_get: %s\n" % e)
```

### Parameters
This endpoint does not need any parameter.

### Return type

[**list[DamacanaDBModel]**](DamacanaDBModel.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **login_user_login_post**
> UserToken login_user_login_post(body)

Login

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# create an instance of the API class
api_instance = swagger_client.DefaultApi()
body = swagger_client.UserLogin() # UserLogin | 

try:
    # Login
    api_response = api_instance.login_user_login_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->login_user_login_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UserLogin**](UserLogin.md)|  | 

### Return type

[**UserToken**](UserToken.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: application/json
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **test_test_get**
> object test_test_get(secret_key=secret_key)

Test

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint


# create an instance of the API class
api_instance = swagger_client.DefaultApi(swagger_client.ApiClient(configuration))
secret_key = 'secret_key' # str |  (optional) (default to secret_key)

try:
    # Test
    api_response = api_instance.test_test_get(secret_key=secret_key)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->test_test_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **secret_key** | **str**|  | [optional] [default to secret_key]

### Return type

**object**

### Authorization

[HTTPBearer](../README.md#HTTPBearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

