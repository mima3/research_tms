import ssl
from datetime import datetime
from tcms_api import TCMS
from typing import Iterable, Optional


# 自己認証のSSL対応 検証目的のためだけに使用
ssl._create_default_https_context = ssl._create_unverified_context


class KiwiService:
    def __init__(self, endpoint, user, password):
        self.tcms = TCMS(endpoint, user, password)
        self.rpc = self.tcms.exec


class KiwiProductService(KiwiService):
    def __init__(self, endpoint, user, password, product_id: int):
        self.product_id = product_id
        super().__init__(endpoint, user, password)

    def create_task(
        self,
        summary: str,
        text: str,
        *,
        category_id: int = 1,
        priority_id: int = 1,
        is_automated: bool = True,
        notes: str = "",
        tags: Optional[Iterable[str]] = None,
        case_status: int = 1
    ) -> dict:
        # ref.
        # https://kiwitcms.readthedocs.io/en/latest/modules/tcms.testcases.models.html#tcms.testcases.models.TestCase
        case_data = {
            "summary": summary,
            "case_status": case_status,  # 1: PROPOSED, 2: CONFIRMED, 3: IN_PROGRESS ... (KIWI上のステータスID)
            "priority": priority_id,  # 優先度ID
            "is_automated": is_automated,  # 自動テストかどうか (True/False)
            "script": "",
            "text": text,
            "category": category_id,
            "product_id": self.product_id,
            "notes": notes,
            # 必要に応じて他のフィールドを追加
            # "note": "note",
            # "category": 1,         # カテゴリID（製品カテゴリなど）
            # 'plan': テストプランのID,
            # 'component': コンポーネントのID,
            # 'tag': タグ など
        }
        # https://kiwitcms.readthedocs.io/en/latest/modules/tcms.rpc.api.testcase.html#tcms.rpc.api.testcase.create
        new_case = self.rpc.TestCase.create(case_data)
        print(new_case)
        for tag in tags:
            # https://kiwitcms.readthedocs.io/en/latest/modules/tcms.rpc.api.testcase.html#tcms.rpc.api.testcase.add_tag
            self.rpc.TestCase.add_tag(new_case.get("id"), tag)
        return new_case

    def filter_by_summary(self, summary: str) -> dict:
        # https://kiwitcms.readthedocs.io/en/latest/modules/tcms.rpc.api.testcase.html#tcms.rpc.api.testcase.filter
        test_case = self.rpc.TestCase.filter(
            {
                "summary": summary,
                "category__product": self.product_id,
            }
        )
        return test_case

    def add_test_case_to_plan(self, case_id, plan_id):
        if not self.rpc.TestCase.filter({"pk": case_id, "plan": plan_id}):
            self.rpc.TestPlan.add_case(plan_id, case_id)

    def create_test_run(self, plan_id: int, build_id: int, summary: str) -> dict:
        # テスト計画を作った人間をマネージャーとみなす
        manager_id = self.rpc.TestPlan.filter({"pk": plan_id})[0]["author"]
        data = {
            "summary": summary,
            "manager": manager_id,
            "plan": plan_id,
            "build": build_id,
            "start_date": self._current_date(),
        }
        # https://kiwitcms.readthedocs.io/en/latest/modules/tcms.rpc.api.testrun.html#tcms.rpc.api.testrun.create
        new_run = self.rpc.TestRun.create(data)
        return new_run

    def add_test_case_to_run(self, case_id: int, run_id: int) -> dict:
        result = self.rpc.TestRun.add_case(run_id, case_id)
        if isinstance(result, list):
            return result[0]
        else:
            return result

    def _current_date(self) -> str:
        return datetime.now().isoformat().replace("T", " ")[:19]

    def update_test_execution(self, test_execution_id: int, status_id: int, comment: str):
        args = {
            "status": status_id,
            "start_date": self._current_date(),
            "stop_date": self._current_date(),
        }
        self.rpc.TestExecution.update(test_execution_id, args)
        if comment:
            self.rpc.TestExecution.add_comment(test_execution_id, comment)

    def finish_test_run(self, run_id: int):
        self.rpc.TestRun.update(
            run_id,
            {
                "stop_date": self._current_date(),
            },
        )
