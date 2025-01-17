import concurrent.futures

from src.services import ExtractInfoFromStock
from tests.test_base import BaseTestClass


class TestExtractInfoStock(BaseTestClass):
    def test_get_info_active(self):
        result_actives = []

        with concurrent.futures.ThreadPoolExecutor() as executor:
            futures = [executor.submit(ExtractInfoFromStock().get_info_active, active) for active in self.stock_list]

            for future in concurrent.futures.as_completed(futures):
                try:
                    active = future.result()

                    if isinstance(active, str):
                        active = ExtractInfoFromStock().get_active_keys_indicators(active)

                    result_actives.append(active)

                except Exception:
                    assert False

                finally:
                    assert True
