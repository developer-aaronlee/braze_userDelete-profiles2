import pandas as pd
import requests
import json

braze_export = "https://rest.iad-06.braze.com/users/export/ids"
braze_delete = "https://rest.iad-06.braze.com/users/delete"

export_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer api_key"
}

delete_headers = {
    "Content-Type": "application/json",
    "Authorization": "Bearer api_key"
}

df = pd.read_csv("delete_user_batch2.csv")
# print(df.values)

all_data = [x[0] for x in df.values]
# print(all_data)

upper_emails = []
lower_emails = []

for x in range(len(all_data)):
    export = {
        "email_address": all_data[x]
    }

    export_id = json.dumps(export)
    # print(export)

    response = requests.post(url=braze_export, data=export_id, headers=export_headers)
    print(f"Row {x + 1}: {all_data[x]} Response: ", response.status_code)

    profile_count = len(response.json()['users'])
    # print(profile_count)

    for i in range(profile_count):
        email = response.json()['users'][i]['external_id']
        if email == email.lower():
            lower_emails.append(email)
        else:
            upper_emails.append(email)

# print("upper_emails:", upper_emails, len(upper_emails))
# print("lower_emails:", lower_emails, len(lower_emails))

# all_emails = {
#     "upper_case": upper_emails,
#     "lower_case": lower_emails
# }
#
# email_df = pd.DataFrame(all_emails)
# print(email_df)

# email_df.to_csv("all_emails.csv", index=False)

for x in range(len(upper_emails)):
    delete = {
        "external_ids": [upper_emails[x]]
    }

    delete_user = json.dumps(delete)
    # print(delete)

    response = requests.post(url=braze_delete, data=delete_user, headers=delete_headers)
    print(f"Row {x + 1}: {upper_emails[x]} Response: ", response.json())
