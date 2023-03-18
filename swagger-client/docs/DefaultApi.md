# swagger_client.DefaultApi

All URIs are relative to */*

Method | HTTP request | Description
------------- | ------------- | -------------
[**create_damacana_damacana_new_post**](DefaultApi.md#create_damacana_damacana_new_post) | **POST** /damacana/new | Create Damacana
[**get_damacana_from_id_damacana_id_get**](DefaultApi.md#get_damacana_from_id_damacana_id_get) | **GET** /damacana/{id} | Get Damacana From Id
[**get_damacana_from_name_damacana_search_get**](DefaultApi.md#get_damacana_from_name_damacana_search_get) | **GET** /damacana/search/ | Get Damacana From Name
[**list_damacana_storage_damacana_get**](DefaultApi.md#list_damacana_storage_damacana_get) | **GET** /damacana/ | List Damacana Storage

# **create_damacana_damacana_new_post**
> DamacanaDBModel create_damacana_damacana_new_post(body)

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
    api_response = api_instance.create_damacana_damacana_new_post(body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->create_damacana_damacana_new_post: %s\n" % e)
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

# **get_damacana_from_id_damacana_id_get**
> DamacanaDBModel get_damacana_from_id_damacana_id_get(damacana_id)

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
    api_response = api_instance.get_damacana_from_id_damacana_id_get(damacana_id)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_damacana_from_id_damacana_id_get: %s\n" % e)
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

# **get_damacana_from_name_damacana_search_get**
> list[DamacanaDBModel] get_damacana_from_name_damacana_search_get(damacana_name)

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
    api_response = api_instance.get_damacana_from_name_damacana_search_get(damacana_name)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->get_damacana_from_name_damacana_search_get: %s\n" % e)
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

# **list_damacana_storage_damacana_get**
> list[DamacanaDBModel] list_damacana_storage_damacana_get()

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
    api_response = api_instance.list_damacana_storage_damacana_get()
    pprint(api_response)
except ApiException as e:
    print("Exception when calling DefaultApi->list_damacana_storage_damacana_get: %s\n" % e)
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

