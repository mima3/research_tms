# SquashTM

## 環境起動
プラグインを入手してsquash-tm/docker/pluginsに配置する

**プラグインの入手先**
https://tm-en.doc.squashtest.com/v11/downloads.html


```bash
cd docker
docker compose up
```

アクセス方法

- url : http://localhost:8090/squash
- user: admin
- password: admin


## REST API

Document
http://localhost:8090/squash/api/rest/latest/docs/api-documentation.html


MyAccountでREST API用のトークンを作成して以下を実行します

```bash
export API_TOKEN=eyJhbGciOiJIUzUxMiJ9.eyJzdWIiOiIxIiwidXVpZCI6IjY5ZTEwZDJiLTE1NTktNDE5Ny05M2JiLWVlNmQ3NmI0YzEwNyIsInBlcm1pc3Npb25zIjoiUkVBRF9XUklURSIsImlhdCI6MTc1ODU0MjYyNCwiZXhwIjoxNzg5OTQ4ODAwfQ.mWg0wu3MVweXbVvtB5JmbjwEQZHBCCBWMrUhYGwx7EXomW0rIdDxLfyh4fwBzen0mzwoMmtR18GK4gkswMFL_g

# タスクの取得例
curl -v -X GET -H "Authorization: Bearer ${API_TOKEN}" \
     -H "Accept: application/json" \
     http://localhost:8090/squash/api/rest/latest/test-cases

# タスクの作成
curl -v -X POST -H "Authorization: Bearer ${API_TOKEN}" \
  -H 'Content-Type: application/json; charset=utf-8' \
  -H 'Accept: application/json' \
     http://localhost:8090/squash/api/rest/latest/test-cases \
  -d '{
  "_type": "test-case",
  "name": "ファーストネーム",
  "parent": { "_type": "project", "id": 1 },
  "importance": "MEDIUM",
  "status": "UNDER_REVIEW",
  "nature": { "code": "NAT_FUNCTIONAL_TESTING" },
  "type": { "code": "TYP_COMPLIANCE_TESTING" },
  "prerequisite": "Weather should be cold",
  "description": "詳細",
  "custom_fields": [
  ],
  "steps": [

  ],
  "datasets": [],
  "verified_requirements": []
}'

```


## 参考
User Guide
https://tm-en.doc.squashtest.com/v11/user-guide/general-introduction/squash-workspaces.html


料金体系：
https://www.squashtm.com/en/offers-pricing

Generating test cases from a requirement with an artificial intelligence server:
https://tm-en.doc.squashtest.com/v11/user-guide/manage-test-cases/generate-test-cases-with-ai.html

