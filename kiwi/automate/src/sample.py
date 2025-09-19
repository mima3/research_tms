from .kiwi_service import KiwiProductService


product_id = 1
plan_id = 1
build_id = 1

kiwi = KiwiProductService("https://localhost/xml-rpc/", "tester1", "tester1tester1", product_id)
# テスト実行を作成
run = kiwi.create_test_run(plan_id, build_id, "テスト実行 （自動)")

# テストケースを作成
contents = """**Steps to reproduce**:
1.
2.
3.

**Expected results**:
1.
2.
3.
"""
case_list = kiwi.filter_by_summary("テストケース1_自動追加")
if not case_list:
    case = kiwi.create_task(
        "テストケース1_自動追加", contents, category_id=1, priority_id=1, case_status=2, notes="noteeee", tags=["abc", "efg"]
    )
else:
    case = case_list[0]
print(case)
kiwi.add_test_case_to_plan(case.get("id", 0), plan_id)
execution = kiwi.add_test_case_to_run(case.get("id", 0), run.get("id", 0))
# status_id：4:成功 8:却下 7:Error 5:失敗
kiwi.update_test_execution(execution.get("id", 0), 4, "コメント")

# テストケースを作成
contents = """**Steps to reproduce**:
1.
2.
3.

**Expected results**:
1.
2.
3.
"""
case_list = kiwi.filter_by_summary("テストケース2_自動追加")
if not case_list:
    case = kiwi.create_task(
        "テストケース2_自動追加", contents, category_id=1, priority_id=1, case_status=2, notes="noteeee", tags=["abc", "efg"]
    )
else:
    case = case_list[0]
print(case)
kiwi.add_test_case_to_plan(case.get("id", 0), plan_id)
execution = kiwi.add_test_case_to_run(case.get("id", 0), run.get("id", 0))
# status_id：4:成功 8:却下 7:Error 5:失敗
kiwi.update_test_execution(execution.get("id", 0), 5, "コメント")

# テスト実行終了
kiwi.finish_test_run(run.get("id", 0))
