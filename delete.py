import pandas as pd
import requests
import json

braze_delete = "https://rest.iad-06.braze.com/users/delete"

delete_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer 5585e24b-e24d-4809-9e21-6272a70898f5"
}

df = pd.read_csv("invalid_users (1).csv")
# print(df.values)

all_data = [x[0] for x in df.values]
# print(all_data)

row = 0
for x in all_data:
    row += 1
    delete = {
        "external_ids": [str(x)]
    }

    delete_user = json.dumps(delete)
    # print(delete)

    response = requests.post(url=braze_delete, data=delete_user, headers=delete_headers)
    print(f"Row {row}: {x} Response: ", response.json())
